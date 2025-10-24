# evaluate based on doc_id
python evaluate.py --runs_dir ../retrieve_results --qrels ../requests.jsonl
# evaluate based on doc content with LLM
python evaluate_ragas.py --runs_path ../retrieve_results/retrieval_results_faiss.json --qrels ../requests.jsonl --model_name gpt-4.1-mini