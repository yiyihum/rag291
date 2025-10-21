#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
批量抓取 Hugging Face 上 2025 年（可自定义日期范围）“LLM 相关”的
Model/Dataset Card（README.md），并可选抓取官方指南页面（HTML）。

依赖:
  pip install --upgrade huggingface_hub tqdm requests
"""

import argparse
import json
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, List, Optional, Set, Tuple

from huggingface_hub import HfApi
from huggingface_hub.repocard import RepoCard
from tqdm import tqdm
import requests

# ---- 可根据需要扩展的判定规则 ----
LLM_MODEL_PIPELINES: Set[str] = {
    "text-generation",
    "text2text-generation",
    "conversational",
}
# 有些模型也会在 tags 中标注这些关键词（兜底）
LLM_MODEL_TAGS: Set[str] = {
    "llm",
    "large-language-model",
    "causal-lm",
    "seq2seq",
    "language-modeling",
    "chat",
    "instruct",
}

# 数据集以 task_categories 或通用标签识别 LLM 相关任务
LLM_DATASET_TAGS: Set[str] = {
    "task_categories:text-generation",
    "task_categories:conversational",
    "task_categories:language-modeling",
    "instruction-tuning",
    "rlhf",
    "sft",
    "pretraining",
    "chat",
}

# 指南（guide）页：可离线保存
GUIDE_PAGES: List[Tuple[str, str]] = [
    ("model_cards.html", "https://huggingface.co/docs/hub/en/model-cards"),
    ("dataset_cards.html", "https://huggingface.co/docs/hub/en/datasets-cards"),
    ("annotated_model_card.html", "https://huggingface.co/docs/hub/en/model-card-annotated"),
    ("repo_cards_and_data.html", "https://huggingface.co/docs/huggingface_hub/package_reference/cards"),
]

@dataclass
class RepoMeta:
    id: str
    author: Optional[str]
    created_at: Optional[str]
    last_modified: Optional[str]
    private: Optional[bool]
    gated: Optional[str]
    downloads: Optional[int]
    downloads_all_time: Optional[int]
    likes: Optional[int]
    library_name: Optional[str]
    pipeline_tag: Optional[str]
    tags: List[str]
    license: Optional[str] = None  # 可能在 card_data 里
    repo_type: str = "model"  # or "dataset"


def parse_date_range(s: str) -> Tuple[datetime, datetime]:
    # 例: "2025-01-01:2025-12-31"
    parts = s.split(":")
    if len(parts) != 2:
        raise ValueError("date-range 形如 YYYY-MM-DD:YYYY-MM-DD")
    start = datetime.fromisoformat(parts[0]).replace(tzinfo=timezone.utc)
    end = datetime.fromisoformat(parts[1]).replace(
        hour=23, minute=59, second=59, tzinfo=timezone.utc
    )
    if end < start:
        raise ValueError("date-range 结束日期应不早于开始日期")
    return start, end


def ensure_dir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)


def safe_name(repo_id: str) -> str:
    # "org/name" -> "org__name"
    return repo_id.replace("/", "__")


def created_in_range(info_dt: Optional[datetime], start: datetime, end: datetime) -> bool:
    if info_dt is None:
        return False
    # info_dt 已是 tz-aware（HF 返回带 tz）
    return start <= info_dt <= end


def is_llm_model(info) -> bool:
    # 依据 pipeline_tag 或 tags
    if getattr(info, "pipeline_tag", None) in LLM_MODEL_PIPELINES:
        return True
    tags = set(getattr(info, "tags", []) or [])
    if tags & LLM_MODEL_TAGS:
        return True
    return False


def is_llm_dataset(info) -> bool:
    tags = set(getattr(info, "tags", []) or [])
    # 既匹配 "task_categories:text-generation" 这类键值对，也匹配通用关键词
    for t in tags:
        if t in LLM_DATASET_TAGS:
            return True
        # 容错：有些站内会同时出现未带前缀的 'text-generation'
        if "text-generation" in t:
            return True
    return False


def collect_models(api: HfApi, start: datetime, end: datetime,
                   token: Optional[str], max_items: int) -> List[RepoMeta]:
    # 为避免 filter 的 "AND" 逻辑造成遗漏，我们分多次取并集
    filters_groups = [
        ["text-generation"],
        ["text2text-generation"],
        ["conversational"],
        # 兜底：有少量模型仅靠 tag 标识 LLM，不靠 pipeline_tag
        # 这里不直接传 "llm" 给 filter（平台未定义统一行为），改为本地二次判定
    ]

    seen: Set[str] = set()
    out: List[RepoMeta] = []

    for filt in filters_groups:
        for info in api.list_models(
            filter=filt,  # 多个字符串时通常是 AND，这里每组只放一个
            limit=max_items or None,  # None = 不限制，由生成器控制
        ):
            if info.id in seen:
                continue
            seen.add(info.id)
            if not is_llm_model(info):
                continue
            if not created_in_range(getattr(info, "created_at", None), start, end):
                continue

            # license 可能在 card_data 内（非必填）
            license_ = None
            try:
                if getattr(info, "card_data", None):
                    license_ = info.card_data.get("license")
            except Exception:
                pass

            out.append(
                RepoMeta(
                    id=info.id,
                    author=getattr(info, "author", None),
                    created_at=(getattr(info, "created_at", None) or None) and getattr(info, "created_at").isoformat(),
                    last_modified=(getattr(info, "last_modified", None) or None) and getattr(info, "last_modified").isoformat(),
                    private=getattr(info, "private", None),
                    gated=getattr(info, "gated", None),
                    downloads=getattr(info, "downloads", None),
                    downloads_all_time=getattr(info, "downloads_all_time", None),
                    likes=getattr(info, "likes", None),
                    library_name=getattr(info, "library_name", None),
                    pipeline_tag=getattr(info, "pipeline_tag", None),
                    tags=list(getattr(info, "tags", []) or []),
                    license=license_,
                    repo_type="model",
                )
            )
            if max_items and len(out) >= max_items:
                break
        if max_items and len(out) >= max_items:
            break

    return out


def collect_datasets(api: HfApi, start: datetime, end: datetime,
                     token: Optional[str], max_items: int) -> List[RepoMeta]:
    # 与模型类似，分多次取并集
    dataset_filters = [
        ["task_categories:text-generation"],
        ["task_categories:conversational"],
        ["task_categories:language-modeling"],
        ["instruction-tuning"],
        ["rlhf"],
        ["pretraining"],
        ["chat"],
    ]

    seen: Set[str] = set()
    out: List[RepoMeta] = []

    for filt in dataset_filters:
        for info in api.list_datasets(
            filter=filt,  # 每组单条件，避免 AND 过严
            limit=max_items or None,
        ):
            if info.id in seen:
                continue
            seen.add(info.id)
            if not is_llm_dataset(info):
                continue
            if not created_in_range(getattr(info, "created_at", None), start, end):
                continue

            license_ = None
            try:
                if getattr(info, "card_data", None):
                    license_ = info.card_data.get("license")
            except Exception:
                pass

            out.append(
                RepoMeta(
                    id=info.id,
                    author=getattr(info, "author", None),
                    created_at=(getattr(info, "created_at", None) or None) and getattr(info, "created_at").isoformat(),
                    last_modified=(getattr(info, "last_modified", None) or None) and getattr(info, "last_modified").isoformat(),
                    private=getattr(info, "private", None),
                    gated=getattr(info, "gated", None),
                    downloads=getattr(info, "downloads", None),
                    downloads_all_time=getattr(info, "downloads_all_time", None),
                    likes=getattr(info, "likes", None),
                    library_name=None,
                    pipeline_tag=None,
                    tags=list(getattr(info, "tags", []) or []),
                    license=license_,
                    repo_type="dataset",
                )
            )
            if max_items and len(out) >= max_items:
                break
        if max_items and len(out) >= max_items:
            break

    return out


def download_card(repo: RepoMeta, out_root: Path, token: Optional[str]) -> Tuple[str, bool, Optional[str]]:
    """
    返回: (repo_id, success, error_message)
    """
    save_dir = out_root / ("models" if repo.repo_type == "model" else "datasets")
    ensure_dir(save_dir)
    filename = save_dir / f"{safe_name(repo.id)}.md"
    if filename.exists():
        return repo.id, True, None

    try:
        card = RepoCard.load(repo.id, repo_type=repo.repo_type, token=token)
        filename.write_text(card.content, encoding="utf-8")
        return repo.id, True, None
    except Exception as e:
        return repo.id, False, f"{type(e).__name__}: {e}"


def save_manifest(items: List[RepoMeta], out_root: Path, which: str) -> None:
    manifest = out_root / f"manifest_{which}.jsonl"
    with manifest.open("w", encoding="utf-8") as f:
        for it in items:
            f.write(json.dumps(asdict(it), ensure_ascii=False) + "\n")


def download_guides(out_root: Path) -> None:
    guide_dir = out_root / "guides"
    ensure_dir(guide_dir)
    for fname, url in GUIDE_PAGES:
        try:
            r = requests.get(url, timeout=30)
            r.raise_for_status()
            (guide_dir / fname).write_text(r.text, encoding="utf-8")
        except Exception as e:
            print(f"[WARN] 指南页下载失败 {url}: {e}")


def main():
    parser = argparse.ArgumentParser(description="抓取 2025 年 LLM 相关的 HF Model/Dataset Cards")
    parser.add_argument("--out", required=True, help="输出目录")
    parser.add_argument("--token", default=None, help="可选：HF token（访问 gated/私有仓库时需提供）")
    parser.add_argument("--date-range", default="2025-01-01:2025-12-31",
                        help="时间范围，形如 2025-01-01:2025-12-31（含首尾）")
    parser.add_argument("--max-models", type=int, default=0, help="最多抓取模型数（0 表示不限制）")
    parser.add_argument("--max-datasets", type=int, default=0, help="最多抓取数据集数（0 表示不限制）")
    parser.add_argument("--workers", type=int, default=12, help="并发下载的线程数")
    parser.add_argument("--only", choices=["models", "datasets", "both"], default="both",
                        help="仅抓取模型 / 数据集 / 都抓")
    parser.add_argument("--include-docs", action="store_true",
                        help="同时抓取 Model/Dataset Card 的官方指南页面（HTML）")
    args = parser.parse_args()

    out_root = Path(args.out).resolve()
    ensure_dir(out_root)

    start, end = parse_date_range(args.date_range)
    api = HfApi()

    all_models: List[RepoMeta] = []
    all_datasets: List[RepoMeta] = []

    if args.only in ("models", "both"):
        print("[INFO] 搜索 LLM 模型（基于 pipeline_tag/tags），并筛选创建时间落在范围内…")
        all_models = collect_models(api, start, end, args.token, args.max_models)
        print(f"[INFO] 匹配到模型 {len(all_models)} 条")

    if args.only in ("datasets", "both"):
        print("[INFO] 搜索 LLM 相关数据集（基于 task_categories/tags），并筛选创建时间落在范围内…")
        all_datasets = collect_datasets(api, start, end, args.token, args.max_datasets)
        print(f"[INFO] 匹配到数据集 {len(all_datasets)} 条")

    # 保存 manifest
    if all_models:
        save_manifest(all_models, out_root, "models")
    if all_datasets:
        save_manifest(all_datasets, out_root, "datasets")

    # 下载 README（即卡片）
    to_download = all_models + all_datasets
    if to_download:
        print("[INFO] 开始下载 README.md（Model/Dataset Card）…")
        with ThreadPoolExecutor(max_workers=args.workers) as ex:
            futures = [ex.submit(download_card, repo, out_root, args.token) for repo in to_download]
            for _id, ok, err in tqdm(as_completed(futures), total=len(futures)):
                if not ok:
                    tqdm.write(f"[WARN] {_id} 下载失败：{err}")

    if args.include_docs:
        print("[INFO] 下载官方指南页面（HTML）以便离线查阅…")
        download_guides(out_root)

    print("[DONE] 全部完成。输出目录：", out_root)


if __name__ == "__main__":
    main()