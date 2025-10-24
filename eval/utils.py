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