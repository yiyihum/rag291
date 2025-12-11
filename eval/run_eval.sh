run_name=faiss

run_path="../results_baseline/retrieve_results/faiss/retrieval_results_faiss.json"
# run_path="../results_baseline/retrieve_results/faiss_chunk/retrieval_results_chunk_faiss.json"
# run_path="../results_baseline/retrieve_results/qdrant/retrieval_results_qdrant.json"
# run_path="../results_baseline/retrieve_results/qdrant_chunk/retrieval_results_chunk_qdrant.json"

OUTPUT_PATH="eval_results_baseline"

# evaluate based on doc_id
# once for all subsets
# python evaluate.py \
#     --runs_dir ../results_baseline/retrieve_results \
#     --qrels ../requests.jsonl \
#     --ks 5 \
#     --ndcg_k 5 \
#     --out_dir $OUTPUT_PATH

# evaluate based on doc content with LLM
python evaluate_ragas.py \
    --run_name $run_name \
    --runs_path $run_path \
    --qrels ../requests.jsonl \
    --model_name gpt-4.1-mini \
    --responses_dir ../results_baseline/LLM_answer_for_$run_name.txt \
    --out_dir $OUTPUT_PATH