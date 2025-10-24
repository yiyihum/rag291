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

def write_csv(data, file_path):
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)