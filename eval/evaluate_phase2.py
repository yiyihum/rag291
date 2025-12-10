#!/usr/bin/env python3
"""
Evaluation script for retrieve_enhanced methods.
Computes traditional IR metrics (NDCG, MAP, MRR, Recall) for the enhanced RAG system outputs.

The retrieve_enhanced methods produce JSONL outputs with structure:
{
    "qid": "Q1",
    "query": "...",
    "llm_response": "...",
    "retrieve_results": [{"doc_id": "...", "chunk": "..."}, ...]
}
"""

import argparse
import os
import json
import csv
import math
from collections import defaultdict, OrderedDict


def load_jsonl(file_path):
    """Load data from JSONL file."""
    with open(file_path, 'r') as f:
        lines = f.readlines()
        data = [json.loads(line) for line in lines]
    return data


def write_csv(path, rows, fieldnames):
    """Write rows to CSV file."""
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in rows:
            writer.writerow({k: r.get(k, None) for k in fieldnames})


def get_doc_id(obj: dict) -> str:
    """Get doc_id from various possible fields in the object."""
    candidates = [
        "doc_id",
        "dataset_id",
        "model_id",
        "arxiv_id",
        "hf_id",
        "repo",
        "dataset_ids",
    ]
    
    for key in candidates:
        if key not in obj:
            continue
        val = obj[key]
        if val is None:
            continue
        
        if isinstance(val, (list, tuple)):
            return val
        
        if isinstance(val, str):
            s = val.strip()
            if s:
                return s
    
    return ""


def normalize_doc_id(doc_id: str) -> str:
    """
    Normalize doc_id to a canonical form for comparison.
    
    Handles conversions like:
    - 'data/github_readmes/DAMO-NLP-SG/multimodal_textbook/README.md' -> 'DAMO-NLP-SG/multimodal_textbook'
    - 'data/hf_cards_2025/datasets/nvidia__Nemotron-Personas.md' -> 'nvidia/Nemotron-Personas'
    - 'data/arxiv_llm_2025/arxiv_llm_2025.jsonl' with arxiv_id '2501.00697' -> '2501.00697'
    """
    if not doc_id:
        return ""
    
    doc_id = doc_id.strip()
    
    # Handle GitHub README paths
    if 'github_readmes/' in doc_id:
        # Extract 'org/repo' from 'data/github_readmes/org/repo/README.md'
        parts = doc_id.split('github_readmes/')
        if len(parts) > 1:
            path_parts = parts[1].split('/')
            if len(path_parts) >= 2:
                return f"{path_parts[0]}/{path_parts[1]}"
    
    # Handle HuggingFace dataset/model card paths
    if 'hf_cards' in doc_id:
        # Extract from patterns like 'data/hf_cards_2025/datasets/nvidia__Nemotron-Personas.md'
        if '__' in doc_id:
            filename = doc_id.split('/')[-1]
            filename = filename.replace('.md', '')
            # Convert 'nvidia__Nemotron-Personas' to 'nvidia/Nemotron-Personas'
            return filename.replace('__', '/')
    
    # Handle arxiv paths - keep as is if it's an arxiv ID
    if doc_id.startswith('250') or doc_id.startswith('240'):  # arxiv IDs like 2501.xxxxx
        return doc_id
    
    return doc_id


def extract_id_from_retrieved_doc(doc_id: str) -> list:
    """
    Extract possible matching IDs from a retrieved document path.
    Returns a list of possible IDs that could match ground truth.
    """
    ids = [doc_id]  # Original
    normalized = normalize_doc_id(doc_id)
    if normalized and normalized != doc_id:
        ids.append(normalized)
    
    # Also try extracting just the filename without extension
    if '/' in doc_id:
        filename = doc_id.split('/')[-1]
        basename = filename.rsplit('.', 1)[0] if '.' in filename else filename
        if basename and basename not in ids:
            ids.append(basename)
    
    return ids


def load_qrels(path: str, key_name="rel"):
    """
    Load ground truth relevance judgments from a jsonl file.
    Uses the same format as requests.jsonl with filters containing the relevant doc_id.
    """
    qrels = defaultdict(dict)
    data = load_jsonl(path)
    
    for obj in data:
        qid = str(obj.get("qid", "")).strip()
        filters = obj.get("filters", {})
        doc_id = get_doc_id(filters)
        
        # Deal with list of doc_ids
        if isinstance(doc_id, list):
            for d in doc_id:
                qrels[qid][d] = 1
            continue
        
        rel = 1  # Assume relevance if present
        if qid and doc_id:
            qrels[qid][doc_id] = rel
    
    return qrels


def load_enhanced_runs(responses_path: str):
    """
    Load retrieved docs from retrieve_enhanced output (JSONL format).
    
    Expected format per line:
    {
        "qid": "Q1",
        "query": "...",
        "llm_response": "...",
        "retrieve_results": [{"doc_id": "...", "chunk": "..."}, ...]
    }
    
    Returns:
        runs: dict mapping qid -> list of (normalized_id, all_possible_ids) tuples
    """
    runs = {}
    data = load_jsonl(responses_path)
    
    for obj in data:
        qid = str(obj.get("qid", "")).strip()
        retrieve_results = obj.get("retrieve_results", [])
        
        # Extract doc_ids in order (ranked by retrieval system)
        doc_entries = []
        for item in retrieve_results:
            doc_id = item.get("doc_id", "")
            if doc_id and doc_id != "unknown":
                # Store tuple of (normalized_id, all_possible_ids)
                possible_ids = extract_id_from_retrieved_doc(doc_id)
                doc_entries.append((normalize_doc_id(doc_id), set(possible_ids)))
        
        runs[qid] = doc_entries
    
    return runs


def check_doc_match(doc_entry, qrels_for_q):
    """
    Check if a retrieved document matches any ground truth document.
    
    Args:
        doc_entry: Tuple of (normalized_id, set of all_possible_ids)
        qrels_for_q: Dict of ground_truth_id -> relevance
    
    Returns:
        Relevance score if matched, 0 otherwise
    """
    normalized_id, possible_ids = doc_entry
    
    # Check if normalized form matches
    if normalized_id in qrels_for_q:
        return qrels_for_q[normalized_id]
    
    # Check if any possible ID matches
    for pid in possible_ids:
        if pid in qrels_for_q:
            return qrels_for_q[pid]
        # Also try partial matching (e.g., 'org/repo' in 'org/repo/README.md')
        for gt_id in qrels_for_q.keys():
            if gt_id in pid or pid in gt_id:
                return qrels_for_q[gt_id]
    
    return 0


# Evaluation metrics
def dcg_at_k(gains, k):
    """Discounted Cumulative Gain at k."""
    dcg = 0.0
    for i, g in enumerate(gains[:k], start=1):
        dcg += (2**g - 1) / math.log2(i + 1)
    return dcg


def ndcg_at_k(ranked_doc_entries, qrels_for_q, k):
    """
    Normalized Discounted Cumulative Gain at k.
    
    Args:
        ranked_doc_entries: List of (normalized_id, possible_ids) tuples
        qrels_for_q: Dict of ground_truth_id -> relevance
        k: Cutoff
    """
    gains = []
    seen_relevant = set()
    
    for doc_entry in ranked_doc_entries[:k]:
        normalized_id, possible_ids = doc_entry
        rel = check_doc_match(doc_entry, qrels_for_q)
        
        # Avoid double-counting same document
        match_key = normalized_id or next(iter(possible_ids), "")
        if rel > 0 and match_key not in seen_relevant:
            gains.append(rel)
            seen_relevant.add(match_key)
        else:
            gains.append(0)
    
    ideal = sorted(qrels_for_q.values(), reverse=True)
    if not ideal:
        return None
    return dcg_at_k(gains, k) / max(dcg_at_k(ideal, k), 1e-9)


def recall_at_k(ranked_doc_entries, qrels_for_q, k, primary_only=False):
    """Recall at k."""
    if primary_only:
        relevant = {d for d, r in qrels_for_q.items() if r >= 2}
    else:
        relevant = {d for d, r in qrels_for_q.items() if r > 0}
    if not relevant:
        return None
    
    # Track which ground truth docs have been matched to avoid double-counting
    matched_gt_docs = set()
    for doc_entry in ranked_doc_entries[:k]:
        normalized_id, possible_ids = doc_entry
        
        # Find which ground truth doc this matches
        for gt_id in qrels_for_q.keys():
            if qrels_for_q[gt_id] > 0:
                if primary_only and qrels_for_q[gt_id] < 2:
                    continue
                # Check if this retrieved doc matches this ground truth
                if gt_id in possible_ids or normalized_id == gt_id:
                    matched_gt_docs.add(gt_id)
                    break
                # Partial matching
                for pid in possible_ids:
                    if gt_id in pid or pid in gt_id:
                        matched_gt_docs.add(gt_id)
                        break
    
    return len(matched_gt_docs) / len(relevant)


def average_precision(ranked_doc_entries, qrels_for_q):
    """Average Precision."""
    relevant = {d for d, r in qrels_for_q.items() if r > 0}
    if not relevant:
        return None
    
    hits = 0
    precisions = []
    seen_relevant = set()
    
    for i, doc_entry in enumerate(ranked_doc_entries, start=1):
        normalized_id, possible_ids = doc_entry
        rel = check_doc_match(doc_entry, qrels_for_q)
        match_key = normalized_id or next(iter(possible_ids), "")
        
        if rel > 0 and match_key not in seen_relevant:
            hits += 1
            precisions.append(hits / i)
            seen_relevant.add(match_key)
    
    if not precisions:
        return 0.0
    return sum(precisions) / len(relevant)


def mrr_at_k(ranked_doc_entries, qrels_for_q, k):
    """Mean Reciprocal Rank at k."""
    relevant = {d for d, r in qrels_for_q.items() if r > 0}
    if not relevant:
        return None
    
    for i, doc_entry in enumerate(ranked_doc_entries[:k], start=1):
        rel = check_doc_match(doc_entry, qrels_for_q)
        if rel > 0:
            return 1.0 / i
    return 0.0


def evaluate_system(runs_for_system, qrels, ks=(5, 10, 20), ndcg_k=5):
    """
    Evaluate a single system's runs against qrels.
    
    Args:
        runs_for_system: dict mapping qid -> list of (normalized_id, possible_ids) tuples
        qrels: dict mapping qid -> {doc_id -> relevance}
        ks: Recall@K cutoffs
        ndcg_k: nDCG cutoff
    """
    per_query = {}
    agg = {
        f"ndcg@{ndcg_k}": [],
        "map": [],
        "mrr@10": [],
    }
    for k in ks:
        agg[f"recall@{k}"] = []
        agg[f"primary_recall@{k}"] = []
    
    qids = sorted(qrels.keys())
    for qid in qids:
        ranked_entries = runs_for_system.get(qid, [])
        qrels_q = qrels[qid]
        row = {"qid": qid}
        
        ndcg = ndcg_at_k(ranked_entries, qrels_q, ndcg_k)
        ap = average_precision(ranked_entries, qrels_q)
        mrr10 = mrr_at_k(ranked_entries, qrels_q, 10)
        
        row[f"ndcg@{ndcg_k}"] = ndcg
        row["ap"] = ap
        row["mrr@10"] = mrr10
        
        if ndcg is not None:
            agg[f"ndcg@{ndcg_k}"].append(ndcg)
        if ap is not None:
            agg["map"].append(ap)
        if mrr10 is not None:
            agg["mrr@10"].append(mrr10)
        
        for k in ks:
            r = recall_at_k(ranked_entries, qrels_q, k, primary_only=False)
            pr = recall_at_k(ranked_entries, qrels_q, k, primary_only=True)
            row[f"recall@{k}"] = r
            row[f"primary_recall@{k}"] = pr
            if r is not None:
                agg[f"recall@{k}"].append(r)
            if pr is not None:
                agg[f"primary_recall@{k}"].append(pr)
        
        per_query[qid] = row
    
    # Macro-average over defined values
    summary = OrderedDict()
    summary["queries_judged"] = len(qrels)
    for k, arr in agg.items():
        vals = [v for v in arr if v is not None]
        summary[k] = sum(vals) / len(vals) if vals else None
    
    return summary, per_query


def main():
    ap = argparse.ArgumentParser(
        description="Evaluate retrieve_enhanced runs against qrels using traditional IR metrics."
    )
    ap.add_argument("--qrels", required=True, 
                    help="Path to qrels.jsonl (same as requests.jsonl)")
    ap.add_argument("--responses_path", required=True, 
                    help="Path to retrieve_enhanced responses JSONL file")
    ap.add_argument("--run_name", required=True, 
                    help="Name for this evaluation run (e.g., 'agent-multi')")
    ap.add_argument("--out_dir", default="eval_results", 
                    help="Directory to write evaluation results")
    ap.add_argument("--ks", nargs="+", type=int, default=[5, 10, 20], 
                    help="Recall@K values to compute")
    ap.add_argument("--ndcg_k", type=int, default=5, 
                    help="Compute nDCG at this cutoff")
    args = ap.parse_args()
    
    os.makedirs(args.out_dir, exist_ok=True)
    
    # Load data
    print(f"Loading qrels from {args.qrels}...")
    qrels = load_qrels(args.qrels)
    assert qrels, "No qrels loaded"
    
    print(f"Loading enhanced runs from {args.responses_path}...")
    runs = load_enhanced_runs(args.responses_path)
    assert runs, "No runs loaded"
    
    print(f"Loaded {len(qrels)} queries with ground truth")
    print(f"Loaded {len(runs)} queries with retrieval results")
    
    # Evaluate
    summary, per_query = evaluate_system(runs, qrels, ks=args.ks, ndcg_k=args.ndcg_k)
    
    # Write per-query results
    pq_path = os.path.join(args.out_dir, f"enhanced_{args.run_name}_per_query.csv")
    pq_fields = ["qid", f"ndcg@{args.ndcg_k}", "ap", "mrr@10"] + \
                [f"recall@{k}" for k in args.ks] + [f"primary_recall@{k}" for k in args.ks]
    rows = [dict({"qid": qid}, **per_query[qid]) for qid in sorted(per_query.keys())]
    write_csv(pq_path, rows, pq_fields)
    print(f"Wrote per-query results to {pq_path}")
    
    # Write summary
    summary_path = os.path.join(args.out_dir, f"enhanced_{args.run_name}_summary.json")
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)
    print(f"Wrote summary to {summary_path}")
    
    # Print summary
    print("\n" + "=" * 50)
    print(f"Evaluation Summary for {args.run_name}")
    print("=" * 50)
    for metric, value in summary.items():
        if value is not None:
            if isinstance(value, float):
                print(f"  {metric}: {value:.4f}")
            else:
                print(f"  {metric}: {value}")
    print("=" * 50)


if __name__ == "__main__":
    main()

