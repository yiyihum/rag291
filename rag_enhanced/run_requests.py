import json
import argparse
from pathlib import Path
from tqdm import tqdm
from llm_client import get_llm_client
from retrieval_system import RetrievalSystem
from rag_system import RAGSystem

def process_requests(input_file: str, output_file: str, data_root: str, method: str, 
                    embedding_type: str, processed_file: str = None):
    print(f"[INFO] Loading requests from {input_file}")
    requests = []
    with open(input_file, 'r') as f:
        for line in f:
            if line.strip():
                requests.append(json.loads(line))
                
    print(f"[INFO] Loaded {len(requests)} requests.")
    
    # Initialize RAG System
    print("[INFO] Initializing RAG System...")
    retriever = RetrievalSystem(data_root, processed_file=processed_file, embedding_type=embedding_type,chunk_size=1000, use_faiss=True)
    llm = get_llm_client() # Defaults to OpenRouter
    rag = RAGSystem(retriever, llm)
    
    results = []
    
    for req in tqdm(requests, desc="Processing Requests"):
        qid = req.get('qid')
        query = req.get('query')
        required_corpora = req.get('required_corpora', [])
        filters = req.get('filters', {})
        
        
        print(f"\n[INFO] Processing QID: {qid}")
        print(f"Query: {query}")
        print(f"Method: {method}")
        
        if method == "simple":
            response, docs = rag.answer_simple(query, top_n=5)
        elif method == "agent-single":
            response, docs = rag.answer_agent_single(query, top_n=5)
        elif method == "agent-loop":
            response, docs = rag.answer_agent_loop(query, top_n=5)
        else:
            raise ValueError(f"Unknown method: {method}")
        
        result = {
            "qid": qid,
            "query": query,
            "intent": req.get('intent'),
            "required_corpora": required_corpora,
            "filters": filters,
            "notes_for_judges": req.get('notes_for_judges'),
            "ground_truth": req.get('ground_truth'),
            "llm_response": response,
            "retrieve_results": docs
        }
        results.append(result)
        
        # Save incrementally
        with open(output_file, 'w') as f:
            for r in results:
                f.write(json.dumps(r) + '\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Input requests.jsonl")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    parser.add_argument("--data-root", required=True, help="Data root directory")
    parser.add_argument("--processed-file", help="Optional pre-processed data file (jsonl)")
    parser.add_argument("--embedding_type", default="dense", choices=["dense", "hybrid"])
    parser.add_argument("--method", default="agent-single", choices=["simple", "agent-single", "agent-loop"], help="RAG method to use")
    
    args = parser.parse_args()
    
    # Construct filename based on parameters
    filename_parts = ["responses", args.method, args.embedding_type]
    if args.processed_file:
        filename_parts.append("processed")
    
    filename = "_".join(filename_parts) + ".jsonl"
    output_file = Path(args.output_dir) / filename
    
    # Ensure output directory exists
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    print(f"[INFO] Output file: {output_file}")
    
    process_requests(args.input, str(output_file), args.data_root, args.method, args.embedding_type, args.processed_file)
