import json
import csv

def load_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def load_jsonl(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        data = [json.loads(line) for line in lines]
    return data

def load_csv(file_path):
    data = []
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    return data

def read_text(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    return content

def convert_json_to_string(json_obj):
    return json.dumps(json_obj, indent=4, ensure_ascii=False)

# ===========================================================================================

def write_json(data, file_path):    
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def write_jsonl(data, file_path):
    with open(file_path, 'w') as f:
        for item in data:
            f.write(json.dumps(item) + '\n')

def write_csv(path, rows, fieldnames):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in rows:
            writer.writerow({k: r.get(k, None) for k in fieldnames})

def write_text(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)

# ===========================================================================================

# formatting, get correct doc_id from various possible fields
def get_doc_id(obj: dict) -> str:
    candidates = [
        "doc_id",
        "dataset_id",
        "model_id",
        "arxiv_id",
        "hf_id",
        "repo",
        "dataset_ids",
    ]
    if 'source' in obj:
        if obj['source'] == 'github' and 'repo' in obj:
            return obj['source'] + '|' + obj['repo']
        elif obj['source'] == 'hf_datasets' and 'dataset_id' in obj:
            return obj['source'] + '|' + obj['dataset_id']
        elif obj['source'] == 'hf_models' and 'model_id' in obj:
            return obj['source'] + '|' + obj['model_id']

    for key in candidates:
        if key not in obj:
            continue
        val = obj[key]
        if val is None:
            continue

        if isinstance(val, (list, tuple)):
            # return first non-empty item
            # for item in val:
            #     if item not in (None, ""):
            #         return str(item)
            return val
        
        if isinstance(val, str):
            s = val.strip()
            if s:
                return s
            else:
                continue

    raise ValueError(f"Unknown doc_id field in objecy: {obj.keys()}")

arxiv_corpus = load_jsonl("../data/arxiv_llm_2025/arxiv_llm_2025.jsonl")

def get_doc_content(hit):
    path = "../" + hit.get("path", "")
    ext = os.path.splitext(path)[1].lower()
    # find actual arxiv document item           
    if ext == ".jsonl" and hit.get("source") == "arxiv":
        for item in arxiv_corpus:
            if item["id"] == hit.get("arxiv_id"):
                return convert_json_to_string(item)
    # normal text
    elif ext == ".md":
        return read_text(path)
    else:
        raise ValueError(f"Unsupported document format: {ext} for path: {path}")

from tenacity import retry, stop_after_attempt, wait_exponential
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, min=1, max=30), reraise=True)
def call_openai(content: str, model: str = "gpt-4.1-mini", temperature: float = 0.0, max_tokens: int = 512) -> str:
    messages = [{"role": "user", "content": content}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=1.0,
    )

    try:
        return response.choices[0].message.content
    except Exception:
        print("Wrong structure for response, ", Exception)
        return str(response)
    

if __name__ == "__main__":
    # print(call_openai("Hello world"))

    # get LLM response with query + retrieved docs

    faiss = load_json("../retrieve_results/faiss/retrieval_results_faiss.json")
    faiss_chunk = load_json("../retrieve_results/faiss_chunk/retrieval_results_chunk_faiss.json")
    qdrant = load_json("../retrieve_results/qdrant/retrieval_results_qdrant.json")
    qdrant_chunk = load_json("../retrieve_results/qdrant_chunk/retrieval_results_chunk_qdrant.json")

    requests = load_jsonl("../requests.jsonl")
    

    # questions = [req["query"] for req in requests]    
    outputs = []
    idx = 0
    for key in faiss:
        print(idx)
        obj = faiss[key]

        hits = obj.get("hits", [])
        query = obj.get("query", "")
        assert query, "Empty query!!!!"

        def sort_key(h):
            if "rank" in h and isinstance(h["rank"], int):
                return h["rank"]
            return -float(h.get("score", 0.0))
        hits_sorted = sorted(hits, key=sort_key)
        # get all retrieved docs:
        docs = [get_doc_content(h) for h in hits_sorted]

        prompt = query + "\nPlease answer the question in one or two sentences.\nHere is retrieved docs for reference.\n"
        for d in docs:
            prompt += d + '\n'
        
        # obj["llm_response"] = "call_openai(prompt)"
        requests[idx]["llm_response"] = call_openai(prompt)
        # break
        idx += 1

    write_jsonl(requests, "../new_request.jsonl")


    li = ["asd", "asd", "asd"]
    write_jsonl(li, "../test.jsonl")
