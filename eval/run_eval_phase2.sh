#!/bin/bash
# Evaluation script for retrieve_enhanced methods
# 
# Usage examples:
#   ./run_eval_phase2.sh simple_dense
#   ./run_eval_phase2.sh simple_dense_processed
#   ./run_eval_phase2.sh simple_hybrid
#   ./run_eval_phase2.sh simple_hybrid_processed

#   ./run_eval_phase2.sh agent-single_dense
#   ./run_eval_phase2.sh agent-single_dense_processed
#   ./run_eval_phase2.sh agent-single_hybrid
#   ./run_eval_phase2.sh agent-single_hybrid_processed

#   ./run_eval_phase2.sh agent-loop_dense
#   ./run_eval_phase2.sh agent-loop_dense_processed
#   ./run_eval_phase2.sh agent-loop_hybrid
#   ./run_eval_phase2.sh agent-loop_hybrid_processed

# Load environment variables from .env file if it exists
if [ -f "../.env" ]; then
    export $(grep -v '^#' ../.env | xargs)
fi

# Default method if not specified
METHOD=${1:-agent-multi}

# Construct the responses file path
RESPONSES_PATH="../results_enhanced/responses_${METHOD}.jsonl"
# RESPONSES_PATH="../results_baseline/retrieve_results/retrieval_results_${METHOD}.jsonl"

OUTPUT_PATH="eval_results"

# Check if responses file exists
if [ ! -f "$RESPONSES_PATH" ]; then
    echo "Error: Responses file not found: $RESPONSES_PATH"
    echo "Please run retrieve_enhanced/run_requests.py first with --method $METHOD"
    exit 1
fi

echo "=============================================="
echo "Evaluating retrieve_enhanced method: $METHOD"
echo "Responses file: $RESPONSES_PATH"
echo "=============================================="

# Phase 2a: Traditional IR metrics (NDCG, MAP, MRR, Recall)
echo ""
echo ">>> Running Traditional IR Evaluation..."
python evaluate_phase2.py \
    --run_name $METHOD \
    --responses_path $RESPONSES_PATH \
    --qrels ../requests.jsonl \
    --ks 5 10 20 \
    --ndcg_k 5 \
    --out_dir $OUTPUT_PATH

# Phase 2b: RAGAS Evaluation
echo ""
echo ">>> Running RAGAS Evaluation..."
python evaluate_ragas_phase2.py \
    --run_name $METHOD \
    --responses_path $RESPONSES_PATH \
    --model_name gpt-4.1-mini \
    --out_dir $OUTPUT_PATH

echo ""
echo "=============================================="
echo "Evaluation complete for: $METHOD"
echo "Results saved in: eval_results/"
echo "=============================================="

