# run_path="../retrieve_results/faiss/retrieval_results_faiss.json"
# run_path="../retrieve_results/faiss_chunk/retrieval_results_chunk_faiss.json"
# run_path="../retrieve_results/qdrant/retrieval_results_qdrant.json"
run_path="../retrieve_results/qdrant_chunk/retrieval_results_chunk_qdrant.json"

# evaluate based on doc_id
# once for all subsets
# python evaluate.py \
#     --runs_dir ../retrieve_results \
#     --qrels ../requests.jsonl \
#     --ks 5 \
#     --ndcg_k 5 \
    # --out_dir tmp_results

# evaluate based on doc content with LLM
python evaluate_ragas.py \
    --runs_path $run_path \
    --qrels ../requests.jsonl \
    --model_name gpt-4.1-mini