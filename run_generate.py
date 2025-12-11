import json
import os
from generate_llm import rag_query

def update_requests_jsonl(requests_path):
    with open(requests_path, 'r', encoding='utf-8') as file:
        requests_data = [json.loads(line) for line in file]

    updated_data = []
    for entry in requests_data:
        query = entry['query']
        print(f"Processing: {query}")

        # Assuming rag_query is adjusted to return both the answer and retrieved results
        response, retrieve_results = rag_query('./data', query)

        # Update entry with new fields
        entry['llm_response'] = response
        entry['retrieve_results'] = retrieve_results

        updated_data.append(json.dumps(entry))

    with open(requests_path, 'w', encoding='utf-8') as file:
        file.write("\n".join(updated_data))

if __name__ == "__main__":
    update_requests_jsonl('/Users/jxchen/Documents/UCSD/cse291a/rag291/requests.jsonl')