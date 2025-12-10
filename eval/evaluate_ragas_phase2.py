#!/usr/bin/env python3
"""
RAGAS Evaluation script for retrieve_enhanced methods.

The retrieve_enhanced methods produce JSONL outputs with structure:
{
    "qid": "Q1",
    "query": "...",
    "ground_truth": "...",
    "llm_response": "...",
    # "retrieve_results": [{"doc_id": "...", "chunk": "..."}, ...]
    "retrieve_results": [{'score', 'content', 'metadata', 'raw_content'}, ...], for the metadata: {'source', 'title', 'path', 'id'}, and the id can be read as doc_id after the get_doc_id()
}

This script computes RAGAS metrics including:
- Context Entity Recall
- Context Precision
- LLM Context Recall
- Faithfulness
- Answer Correctness
"""

from ragas import evaluate, EvaluationDataset
from ragas.metrics import (
    LLMContextRecall,
    ContextEntityRecall,
    Faithfulness,
    AnswerCorrectness,
    ContextPrecision
)
from ragas.llms import LangchainLLMWrapper
from langchain_openai import ChatOpenAI

from utils import get_doc_id

import os
import json
import argparse


def load_jsonl(file_path):
    """Load data from JSONL file."""
    with open(file_path, 'r') as f:
        lines = f.readlines()
        data = [json.loads(line) for line in lines]
    return data


def read_text(file_path):
    """Read text content from a file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


def convert_json_to_string(json_obj):
    """Convert JSON object to formatted string."""
    return json.dumps(json_obj, indent=4, ensure_ascii=False)


# Load arxiv corpus once at module level
ARXIV_CORPUS = None

def get_arxiv_corpus():
    """Lazy load arxiv corpus."""
    global ARXIV_CORPUS
    if ARXIV_CORPUS is None:
        arxiv_path = "../data/arxiv_llm_2025/arxiv_llm_2025.jsonl"
        if os.path.exists(arxiv_path):
            ARXIV_CORPUS = load_jsonl(arxiv_path)
        else:
            ARXIV_CORPUS = []
    return ARXIV_CORPUS


def get_full_doc_content(doc_id: str) -> str:
    """
    Read full document content from doc_id path.
    
    Handles different document types:
    - GitHub READMEs: data/github_readmes/org/repo/README.md
    - HuggingFace cards: data/hf_cards_2025/datasets/xxx.md or models/xxx.md
    - Arxiv papers: arxiv ID like '2501.00697'
    """
    if not doc_id:
        return ""
    
    # Handle arxiv IDs (e.g., '2501.00697')
    if doc_id.startswith('250') or doc_id.startswith('240'):
        arxiv_corpus = get_arxiv_corpus()
        for item in arxiv_corpus:
            if item.get("id") == doc_id:
                return convert_json_to_string(item)
        return f"Arxiv paper {doc_id} not found in corpus."
    
    # Handle file paths
    # Construct full path (relative to eval directory)
    if doc_id.startswith('data/'):
        file_path = "../" + doc_id
    else:
        file_path = doc_id
    
    # Read the file
    if os.path.exists(file_path):
        ext = os.path.splitext(file_path)[1].lower()
        if ext == '.md':
            return read_text(file_path)
        elif ext == '.jsonl':
            # For jsonl files, return first few items as context
            data = load_jsonl(file_path)
            return convert_json_to_string(data[:3]) if data else ""
        else:
            return read_text(file_path)
    else:
        return f"Document not found: {doc_id}"


def make_eval_dataset(questions, contexts, generated_answers, ground_truths):
    """Create RAGAS EvaluationDataset from lists of data."""
    data_list = []
    for question, context, answer, truth in zip(questions, contexts, generated_answers, ground_truths):
        assert isinstance(context, list), "context should be a list of retrieved documents"
        data_list.append({
            "user_input": question,
            "retrieved_contexts": context,
            "response": answer,
            "reference": truth,
        })
    eval_dataset = EvaluationDataset.from_list(data_list)
    return eval_dataset


def make_eval_llm(model_name="gpt-4.1-mini"):
    """Create LangChain LLM wrapper for RAGAS evaluation."""
    eval_llm = LangchainLLMWrapper(
        ChatOpenAI(model=model_name, openai_api_key=os.getenv("OPENAI_API_KEY"))
    )
    return eval_llm


def ragas_eval(dataset, eval_llm):
    """Run RAGAS evaluation with standard metrics."""
    results = evaluate(
        dataset=dataset,
        metrics=[
            ContextEntityRecall(),   # Context entity recall rate
            ContextPrecision(),      # Context precision
            LLMContextRecall(),      # Whether retrieved context contains correct info
            Faithfulness(),          # Whether answer is faithful to context
            AnswerCorrectness(),     # Whether answer is correct (based on ground truth)
        ],
        llm=eval_llm
    )
    return results


def load_enhanced_responses(responses_path: str, use_full_docs: bool = True):
    """
    Load responses from retrieve_enhanced output (JSONL format).
    
    Args:
        responses_path: Path to the responses JSONL file
        use_full_docs: If True, read full document content from doc_id paths.
                       If False, use the chunk field as-is.
    
    Returns:
        questions: List of query strings
        contexts: List of lists of context strings (from retrieve_results)
        generated_answers: List of LLM response strings
        ground_truths: List of ground truth strings
    """
    data = load_jsonl(responses_path)
    
    questions = []
    contexts = []
    generated_answers = []
    ground_truths = []
    
    for obj in data:
        # Extract query
        query = obj.get("query", "")
        questions.append(query)
        
        # Extract contexts from retrieve_results
        retrieve_results = obj.get("retrieve_results", [])
        doc_contexts = []
        seen_docs = set()  # Avoid duplicate full docs
        
        for item in retrieve_results:
            # since we have raw_content, we don't need to find each document by id again
            # doc_id = item.get("doc_id", "")
            doc_id = get_doc_id(item.get("metadata"))
            # print(doc_id)
            
            if use_full_docs and doc_id:
                # Read full document content (deduplicate by doc_id)
                if doc_id not in seen_docs:
                    # full_content = get_full_doc_content(doc_id)
                    full_content = item.get("raw_content", "Document not found!")
                    if full_content and not full_content.startswith("Document not found"):
                        doc_contexts.append(full_content)
                        seen_docs.add(doc_id)                
            else:
                # Use chunk as-is
                chunk = item.get("chunk", "")
                if chunk:
                    doc_contexts.append(chunk)
        
        assert doc_contexts, "No context retrieved!"
        contexts.append(doc_contexts if doc_contexts else ["No context retrieved."])
        
        # Extract LLM response (already generated by retrieve_enhanced)
        llm_response = obj.get("llm_response", "")
        generated_answers.append(llm_response if llm_response else "No response generated.")
        
        # Extract ground truth
        ground_truth = obj.get("ground_truth", "")
        ground_truths.append(ground_truth if ground_truth else "No ground truth available.")
    
    return questions, contexts, generated_answers, ground_truths


def main():
    ap = argparse.ArgumentParser(
        description="Evaluate retrieve_enhanced runs using RAGAS metrics."
    )
    ap.add_argument("--run_name", required=True, 
                    help="Name for this evaluation run (e.g., 'agent-multi')")
    ap.add_argument("--responses_path", required=True, 
                    help="Path to retrieve_enhanced responses JSONL file")
    ap.add_argument("--out_dir", default="eval_results", 
                    help="Directory to write evaluation results")
    ap.add_argument("--model_name", default="gpt-4.1-mini", 
                    help="LLM model name for RAGAS evaluation")
    ap.add_argument("--use_chunks", action="store_true",
                    help="Use chunk content instead of full documents (default: use full docs)")
    args = ap.parse_args()
    
    os.makedirs(args.out_dir, exist_ok=True)
    
    use_full_docs = not args.use_chunks
    

    # 1 Load retrieve_enhanced responses
    print(f"Loading responses from {args.responses_path}...")
    print(f"Context mode: {'CHUNKS' if args.use_chunks else 'FULL DOCUMENTS'}")
    questions, contexts, generated_answers, ground_truths = load_enhanced_responses(
        args.responses_path, use_full_docs=use_full_docs
    )
    
    print(f"Loaded {len(questions)} queries for evaluation")
    print(f"Sample query: {questions[0][:100]}...")
    print(f"Sample context count: {len(contexts[0])}")
    # print(contexts[0])
    if contexts[0]:
        print(f"Sample context length: {len(contexts[0][0])} chars")
    print(f"Sample response: {generated_answers[0][:100]}...")
    
    # 2 Construct RAGAS EvaluationDataset
    print("\nConstructing RAGAS evaluation dataset...")
    eval_dataset = make_eval_dataset(questions, contexts, generated_answers, ground_truths)
    
    # 3 Define LLM interface for evaluation
    print(f"Initializing evaluation LLM ({args.model_name})...")
    evaluator_llm = make_eval_llm(model_name=args.model_name)
    
    # 4 Run RAGAS evaluation
    print("\nRunning RAGAS evaluation (this may take a while)...")
    results = ragas_eval(eval_dataset, evaluator_llm)
    
    # 5 Save and print results
    print("\n" + "=" * 60)
    print(f"RAGAS Evaluation Results for {args.run_name}")
    print("=" * 60)
    print(results)
    
    # Save results to file
    output_path = os.path.join(args.out_dir, f"enhanced_{args.run_name}_ragas_results.txt")
    print(f"\nSaving results to {output_path}")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"RAGAS Evaluation Results for {args.run_name}\n")
        f.write("=" * 60 + "\n")
        f.write(str(results) + "\n")
    
    # Also save as JSON if possible
    try:
        json_output_path = os.path.join(args.out_dir, f"enhanced_{args.run_name}_ragas_results.json")
        results_df = results.to_pandas()
        results_df.to_json(json_output_path, orient="records", indent=2)
        print(f"Saved detailed results to {json_output_path}")
    except Exception as e:
        print(f"Note: Could not save JSON results: {e}")
    
    print("\nDone!")


if __name__ == "__main__":
    main()
