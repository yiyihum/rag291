# fetch_arxiv_llm_2025_api.py
import time, re, csv, json, math, urllib.parse, feedparser
from datetime import datetime
from dateutil import parser as dtp

BASE = "https://export.arxiv.org/api/query"
# 人类可读版转成 URL 查询字符串（要做百分号转义）
QUERY_HUMAN = (
    '((ti:"large language model" OR all:LLM OR all:"large language models" '
    'OR all:"retrieval-augmented generation" OR all:RAG '
    'OR all:"in-context learning" OR all:"instruction tuning") '
    'AND (cat:cs.CL OR cat:cs.LG OR cat:cs.AI OR cat:cs.IR OR cat:stat.ML) '
    'AND submittedDate:[202501010000 TO 202512312359])'
)

params_common = {
    "search_query": QUERY_HUMAN,
    "sortBy": "submittedDate",
    "sortOrder": "ascending",
    "max_results": 2000,
}

def strip_version(arxiv_id):
    # 2301.01234v2 -> 2301.01234
    m = re.match(r"(.+?)v\d+$", arxiv_id)
    return m.group(1) if m else arxiv_id

def entry_to_record(e):
    # 解析作者
    authors = [a.name for a in getattr(e, "authors", [])]
    # 类别
    cats = [t["term"] for t in getattr(e, "tags", []) if "term" in t]
    primary_cat = getattr(e, "arxiv_primary_category", {}).get("term") if hasattr(e, "arxiv_primary_category") else (cats[0] if cats else None)
    # 链接（取 PDF）
    pdf_url = None
    for l in getattr(e, "links", []):
        if l.get("type") == "application/pdf" or l.get("title") == "pdf":
            pdf_url = l.get("href")
            break
    # arXiv id 与版本
    abs_id = e.id.split("/abs/")[-1]
    return {
        "id": strip_version(abs_id),              # 去掉 vN 版本号
        "version": abs_id.split("v")[-1] if "v" in abs_id else "1",
        "title": e.title,
        "abstract": re.sub(r"\s+", " ", e.summary),
        "authors": authors,
        "categories": cats,
        "primary_category": primary_cat,
        "published": e.published,                # 首次提交时间
        "updated": e.updated,                    # 最近更新
        "doi": getattr(e, "arxiv_doi", None),
        "journal_ref": getattr(e, "arxiv_journal_ref", None),
        "comment": getattr(e, "arxiv_comment", None),
        "pdf_url": pdf_url,
        "link": e.link,                          # 摘要页
        "year": dtp.parse(e.published).year if hasattr(e, "published") else None,
        "source": "arxiv_api"
    }

def fetch_total_results():
    # 用一次小结果查看 totalResults，便于估算分页次数
    q = params_common.copy()
    q["max_results"] = 1
    feed = feedparser.parse(BASE + "?" + urllib.parse.urlencode(q))
    tr = getattr(feed, "feed", {}).get("opensearch_totalresults")
    return int(tr) if tr else None  # 可能为空

def main():
    total = fetch_total_results()
    # 如果 total 为空，按经验先跑 30,000 的上限（也可改小）
    total = total or 30000
    page = 0
    seen = set()
    jsonl = open("arxiv_llm_2025.jsonl", "w", encoding="utf-8")
    csvf  = open("arxiv_llm_2025.csv",  "w", newline="", encoding="utf-8")
    writer = csv.DictWriter(csvf, fieldnames=[
        "id","version","title","abstract","authors","categories","primary_category",
        "published","updated","doi","journal_ref","comment","pdf_url","link","year","source"
    ])
    writer.writeheader()

    per = params_common["max_results"]
    pages = math.ceil(total / per)
    for i in range(pages):
        start = i * per
        q = params_common.copy()
        q["start"] = start
        url = BASE + "?" + urllib.parse.urlencode(q, quote_via=urllib.parse.quote)
        feed = feedparser.parse(url)
        entries = getattr(feed, "entries", [])
        if not entries:
            break
        for e in entries:
            rec = entry_to_record(e)
            if rec["id"] in seen:  # 去重（以去版本号后的 id 为准）
                continue
            seen.add(rec["id"])
            jsonl.write(json.dumps(rec, ensure_ascii=False) + "\n")
            row = rec.copy()
            row["authors"] = "; ".join(rec["authors"])
            row["categories"] = "; ".join(rec["categories"] or [])
            writer.writerow(row)
        time.sleep(3)  # 遵守 arXiv 速率限制

    jsonl.close(); csvf.close()
    print(f"done. wrote {len(seen)} unique records.")

if __name__ == "__main__":
    main()