#!/usr/bin/env python3
"""Download README files for GitHub repositories referenced in a JSONL file.

The script scans each JSON object in the input file, extracts any GitHub repository
URLs, deduplicates them, and then attempts to download their README files using the
raw content endpoint. The downloaded READMEs are stored under the provided output
directory, organized by owner and repository name.
"""

from __future__ import annotations

import argparse
import json
import logging
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Iterable, Iterator, Optional, Sequence, Tuple
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

LOG = logging.getLogger(__name__)
DEFAULT_CANDIDATES: tuple[str, ...] = (
    "README.md",
    "README.MD",
    "Readme.md",
    "readme.md",
    "README.rst",
    "README.txt",
    "README",
)
USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
)


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        default="arxiv_llm_2025.jsonl",
        help="Path to the JSONL file containing arXiv metadata.",
    )
    parser.add_argument(
        "--output-dir",
        default="github_readmes",
        help="Directory where README files will be stored.",
    )
    parser.add_argument(
        "--max-workers",
        type=int,
        default=8,
        help="Maximum number of concurrent downloads.",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=20.0,
        help="Timeout (seconds) for each HTTP request.",
    )
    parser.add_argument(
        "--readme-candidates",
        nargs="*",
        default=DEFAULT_CANDIDATES,
        help=(
            "Candidate README filenames to attempt for each repository. "
            "If omitted, a sensible default list is used."
        ),
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Only list the repositories discovered without downloading READMEs.",
    )
    return parser.parse_args(argv)


def iter_strings(obj: object) -> Iterator[str]:
    """Yield all string values from a JSON-like structure."""

    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for value in obj.values():
            yield from iter_strings(value)
    elif isinstance(obj, list):
        for item in obj:
            yield from iter_strings(item)


def extract_repo(slug: str) -> Optional[Tuple[str, str]]:
    """Convert a GitHub URL into an (owner, repo) tuple if possible."""

    parsed = urlparse(slug)
    netloc = parsed.netloc.lower()
    if netloc.startswith("www."):
        netloc = netloc[4:]
    if netloc != "github.com":
        return None

    path = parsed.path.strip("/")
    if not path:
        return None
    segments = path.split("/")
    if len(segments) < 2:
        return None

    owner, repo = segments[0], segments[1]
    if not owner or not repo:
        return None
    if repo.endswith(".git"):
        repo = repo[:-4]

    return owner, repo


def discover_repositories(jsonl_path: Path) -> set[Tuple[str, str]]:
    """Scan the JSONL file and return unique GitHub repositories found."""

    repos: set[Tuple[str, str]] = set()
    total_lines = 0

    with jsonl_path.open("r", encoding="utf-8") as handle:
        for line in handle:
            total_lines += 1
            line = line.strip()
            if not line:
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                LOG.warning("Skipping invalid JSON on line %d: %s", total_lines, exc)
                continue

            for text in iter_strings(record):
                if "github.com" not in text.lower():
                    continue
                for token in text.split():
                    if "github.com" not in token.lower():
                        continue
                    cleaned = token.strip('"\'(),>.,;')
                    repo = extract_repo(cleaned)
                    if repo:
                        repos.add(repo)

    LOG.info("Scanned %d lines and discovered %d unique GitHub repositories.", total_lines, len(repos))
    return repos


def fetch_readme(
    owner: str,
    repo: str,
    output_dir: Path,
    candidates: Iterable[str],
    timeout: float,
) -> Tuple[bool, str, Optional[Path]]:
    """Attempt to download a README for the given repository."""

    for candidate in candidates:
        raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/HEAD/{candidate}"
        request = Request(raw_url, headers={"User-Agent": USER_AGENT})
        try:
            with urlopen(request, timeout=timeout) as response:
                content = response.read()
        except HTTPError as exc:
            if exc.code == 404:
                continue
            return False, f"HTTP {exc.code} for {raw_url}", None
        except URLError as exc:
            return False, f"URL error for {raw_url}: {exc}", None

        if not content:
            continue

        destination = output_dir / owner / repo
        destination.mkdir(parents=True, exist_ok=True)
        target_path = destination / candidate
        target_path.write_bytes(content)
        return True, f"Downloaded {candidate}", target_path

    return False, "No README candidate found", None


def configure_logging() -> None:
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter("%(levelname)s: %(message)s")
    handler.setFormatter(formatter)
    LOG.addHandler(handler)
    LOG.setLevel(logging.INFO)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    configure_logging()

    jsonl_path = Path(args.input).expanduser().resolve()
    if not jsonl_path.exists():
        LOG.error("Input file not found: %s", jsonl_path)
        return 1

    output_dir = Path(args.output_dir).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    candidates = tuple(args.readme_candidates) if args.readme_candidates else DEFAULT_CANDIDATES

    repos = discover_repositories(jsonl_path)
    if not repos:
        LOG.warning("No GitHub repositories found in %s", jsonl_path)
        return 0

    LOG.info("Processing %d repositories.", len(repos))

    if args.dry_run:
        for owner, repo in sorted(repos):
            print(f"{owner}/{repo}")
        LOG.info("Dry run complete. No files downloaded.")
        return 0

    successes = 0
    failures: list[tuple[str, str, str]] = []

    with ThreadPoolExecutor(max_workers=args.max_workers) as executor:
        future_map = {
            executor.submit(
                fetch_readme,
                owner,
                repo,
                output_dir,
                candidates,
                args.timeout,
            ): (owner, repo)
            for owner, repo in repos
        }

        for future in as_completed(future_map):
            owner, repo = future_map[future]
            try:
                ok, message, path = future.result()
            except Exception as exc:  # noqa: BLE001
                LOG.error("Unexpected error fetching %s/%s: %s", owner, repo, exc)
                failures.append((owner, repo, f"Unhandled exception: {exc}"))
                continue

            if ok:
                successes += 1
                LOG.info("%s/%s: %s (%s)", owner, repo, message, path)
            else:
                failures.append((owner, repo, message))
                LOG.warning("%s/%s: %s", owner, repo, message)

    LOG.info("Downloaded READMEs for %d repositories.", successes)
    if failures:
        LOG.warning("Failed to fetch %d repositories.", len(failures))
        for owner, repo, reason in sorted(failures):
            LOG.warning("  %s/%s -> %s", owner, repo, reason)

    return 0 if successes else 1


if __name__ == "__main__":
    sys.exit(main())
