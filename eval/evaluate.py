#!/usr/bin/env python3
import argparse, os, json, csv, glob, math
from collections import defaultdict, OrderedDict
from utils import load_json, load_jsonl, write_csv, get_doc_id

# def normalize_doc_id(doc_id: str, normalize_sections=True) -> str:
#     if doc_id is None:
#         return ""
#     s = doc_id.strip().lower()
#     if normalize_sections and "#" in s:
#         s = s.split("#", 1)[0]
#     return s

def load_qrels(path: str, normalize_sections=True, key_name="rel"):
    """
    Load ground truth relevance judgments from a jsonl file with schema like:
        {"qid": "Q1", "doc_id": "doc_1", "rel": 1}
        {"qid": "Q1", "doc_id": "doc_2", "rel": 0}
        {"qid": "Q2", "doc_id": "doc_3", "rel": 1}
    """
    qrels = defaultdict(dict)  # qid -> doc_id -> rel
    ext = os.path.splitext(path)[1].lower()
    if ext == ".jsonl":
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                obj = json.loads(line)
                qid = str(obj.get("qid", "")).strip()
                # doc_id = normalize_doc_id(str(obj.get("doc_id", "")), normalize_sections)
                filter = obj.get("filters", {})
                doc_id = get_doc_id(filter)
                # deal with list of doc_ids
                if isinstance(doc_id, list):
                    for d in doc_id:
                        qrels[qid][d] = 1
                    continue

                # rel = int(obj.get("rel", 0))
                rel = 1     # assume relevance if present
                if qid and doc_id:
                    qrels[qid][doc_id] = rel
    elif ext == ".csv":
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                qid = str(row.get("qid", "")).strip()
                # TODO: deal with csv format
                # doc_id = normalize_doc_id(str(row.get("doc_id", "")), normalize_sections)
                doc_id = get_doc_id(row)
                rel_str = row.get("rel", "0").strip()
                if not rel_str:
                    continue
                rel = int(rel_str)
                if qid and doc_id:
                    qrels[qid][doc_id] = rel
    else:
        raise ValueError(f"Unsupported qrels extension: {ext}")
    return qrels

def load_runs(runs_dir: str, normalize_sections=True):
    """
    Load retrieved docs per query for all systems from a directory.
    Expects files like runs/<system>/*.json with schema:
        {"qid": "Q1", "hits": [{"rank": 1, "doc_id": "...", "score": 27.1, "corpus": "hf_models"}, ...]}
    """
    systems = {}
    if not os.path.isdir(runs_dir):
        return systems
    # get sub-directories
    for sys_dir in sorted([d for d in glob.glob(os.path.join(runs_dir, "*")) if os.path.isdir(d)]):
        system = os.path.basename(sys_dir)
        systems[system] = {}
        # get per-query files
        for path in sorted(glob.glob(os.path.join(sys_dir, "*.json"))):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                # data consists of multiple queries, so need iteration
                for key in data:
                    obj = data[key]
                    
                    qid = obj.get("qid")
                    # Fallback: infer qid from filename like Q1.json
                    if not qid:
                        qid = os.path.splitext(os.path.basename(path))[0]
                    hits = obj.get("hits", [])
                    # Normalize and sort by provided rank or score
                    def sort_key(h):
                        if "rank" in h and isinstance(h["rank"], int):
                            return h["rank"]
                        return -float(h.get("score", 0.0))
                    hits_sorted = sorted(hits, key=sort_key)
                    docs = []
                    for h in hits_sorted:
                        # doc_id = normalize_doc_id(h.get("doc_id", ""), normalize_sections)
                        doc_id = get_doc_id(h)
                        if isinstance(doc_id, list):
                            docs.extend(doc_id)
                        elif doc_id:
                            docs.append(doc_id)
                    systems[system][qid] = docs
            except Exception as e:
                print(f"Warning: failed to parse {path}: {e}")
    return systems

# discounted cumulative gain
def dcg_at_k(gains, k):
    dcg = 0.0
    for i, g in enumerate(gains[:k], start=1):
        dcg += (2**g - 1) / math.log2(i + 1)
    return dcg

def ndcg_at_k(ranked_doc_ids, qrels_for_q, k):
    gains = [qrels_for_q.get(doc_id, 0) for doc_id in ranked_doc_ids]
    ideal = sorted(qrels_for_q.values(), reverse=True)
    if not ideal:
        return None  # undefined if no judged relevant
    return dcg_at_k(gains, k) / max(dcg_at_k(ideal, k), 1e-9)

def recall_at_k(ranked_doc_ids, qrels_for_q, k, primary_only=False):
    if primary_only:
        relevant = {d for d, r in qrels_for_q.items() if r >= 2}
    else:
        relevant = {d for d, r in qrels_for_q.items() if r > 0}
    if not relevant:
        return None
    retrieved = set(ranked_doc_ids[:k]) & relevant
    return len(retrieved) / len(relevant)

# mean average precision
def average_precision(ranked_doc_ids, qrels_for_q):
    relevant = {d for d, r in qrels_for_q.items() if r > 0}
    if not relevant:
        return None
    hits = 0
    precisions = []
    for i, d in enumerate(ranked_doc_ids, start=1):
        if d in relevant:
            hits += 1
            precisions.append(hits / i)
    if not precisions:
        return 0.0
    return sum(precisions) / len(relevant)

# mean reciprocal rank
def mrr_at_k(ranked_doc_ids, qrels_for_q, k):
    relevant = {d for d, r in qrels_for_q.items() if r > 0}
    if not relevant:
        return None
    for i, d in enumerate(ranked_doc_ids[:k], start=1):
        if d in relevant:
            return 1.0 / i
    return 0.0

def evaluate_system(runs_for_system, qrels, ks=(10,20,50), ndcg_k=10):
    per_query = {}
    agg = {
        "ndcg@{}".format(ndcg_k): [],
        "map": [],
        "mrr@10": [],
    }
    for k in ks:
        agg[f"recall@{k}"] = []
        agg[f"primary_recall@{k}"] = []

    qids = sorted(qrels.keys())
    for qid in qids:
        ranked = runs_for_system.get(qid, [])
        qrels_q = qrels[qid]
        row = {"qid": qid}

        ndcg = ndcg_at_k(ranked, qrels_q, ndcg_k)
        ap = average_precision(ranked, qrels_q)
        mrr10 = mrr_at_k(ranked, qrels_q, 10)

        row[f"ndcg@{ndcg_k}"] = ndcg
        row["ap"] = ap
        row["mrr@10"] = mrr10

        if ndcg is not None: agg[f"ndcg@{ndcg_k}"].append(ndcg)
        if ap is not None: agg["map"].append(ap)
        if mrr10 is not None: agg["mrr@10"].append(mrr10)

        for k in ks:
            r = recall_at_k(ranked, qrels_q, k, primary_only=False)
            pr = recall_at_k(ranked, qrels_q, k, primary_only=True)
            row[f"recall@{k}"] = r
            row[f"primary_recall@{k}"] = pr
            if r is not None: agg[f"recall@{k}"].append(r)
            if pr is not None: agg[f"primary_recall@{k}"].append(pr)

        per_query[qid] = row

    # Macro-average over defined values
    summary = OrderedDict()
    summary["queries_judged"] = len(qrels)
    for k, arr in agg.items():
        vals = [v for v in arr if v is not None]
        summary[k] = sum(vals)/len(vals) if vals else None

    return summary, per_query

def main():
    ap = argparse.ArgumentParser(description="Evaluate retrieval runs against qrels and emit a leaderboard.")
    ap.add_argument("--qrels", required=True, help="Path to qrels.jsonl or qrels.csv")
    ap.add_argument("--runs_dir", default="runs", help="Directory containing system subfolders with per-Q JSON files")
    ap.add_argument("--out_dir", default="eval_results", help="Where to write leaderboard and breakdowns")
    ap.add_argument("--ks", nargs="+", type=int, default=[10,20,50], help="Recall@K values to compute")
    ap.add_argument("--ndcg_k", type=int, default=10, help="Compute nDCG at this cutoff")
    ap.add_argument("--no_section_normalize", action="store_true", help="Do not strip section anchors after '#' in doc IDs")
    args = ap.parse_args()

    os.makedirs(args.out_dir, exist_ok=True)

    qrels = load_qrels(args.qrels, normalize_sections=not args.no_section_normalize)
    assert qrels, "No qrels loaded"
    systems = load_runs(args.runs_dir, normalize_sections=not args.no_section_normalize)
    assert systems, "No runs loaded"

    print("query and ground truth:\n", qrels, "\n")
    print("retrieved results:\n", systems)

    # Evaluate each system
    leaderboard_rows = []
    for system, runs_for_system in sorted(systems.items()):
        summary, per_query = evaluate_system(runs_for_system, qrels, ks=args.ks, ndcg_k=args.ndcg_k)

        # Write per-system breakdown
        pq_path = os.path.join(args.out_dir, f"{system}_per_query.csv")
        pq_fields = ["qid", f"ndcg@{args.ndcg_k}", "ap", "mrr@10"] + \
                    [f"recall@{k}" for k in args.ks] + [f"primary_recall@{k}" for k in args.ks]
        rows = [dict({"qid": qid}, **per_query[qid]) for qid in sorted(per_query.keys())]
        write_csv(pq_path, rows, pq_fields)

        # Write summary JSON
        with open(os.path.join(args.out_dir, f"{system}_summary.json"), "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2)

        # One row for leaderboard
        row = {"system": system, "queries_judged": summary.get("queries_judged")}
        row.update(summary)
        leaderboard_rows.append(row)

    # Leaderboard CSV
    if leaderboard_rows:
        # Determine columns
        metric_keys = set()
        for r in leaderboard_rows:
            metric_keys.update(k for k in r.keys() if k not in {"system"})
        fieldnames = ["system"] + sorted(metric_keys)
        write_csv(os.path.join(args.out_dir, "leaderboard.csv"), leaderboard_rows, fieldnames)

    print(f"Done. Wrote outputs to: {args.out_dir}")

if __name__ == "__main__":
    main()
