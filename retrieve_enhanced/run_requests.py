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
    retriever = RetrievalSystem(data_root, processed_file=processed_file, embedding_type=embedding_type)
    llm = get_llm_client() # Defaults to OpenRouter
    rag = RAGSystem(retriever, llm)
    
    results = []
    
    for req in tqdm(requests, desc="Processing Requests"):
        qid = req.get('qid')
        query = req.get('query')
        required_corpora = req.get('required_corpora', [])
        filters = req.get('filters', {})
        
        # NOTE: User requested NOT to use required_corpora for filtering.
        # The agent/retriever should decide or search all.
        sources = None 
        
        print(f"\n[INFO] Processing QID: {qid}")
        print(f"Query: {query}")
        print(f"Method: {method}")
        
        retrieval_kwargs = {"sources": sources, "filters": filters}
        
        if method == "simple":
            response, docs = rag.answer_simple(query, retrieval_kwargs=retrieval_kwargs)
        elif method == "agent-single":
            response, docs = rag.answer_agent_single(query, retrieval_kwargs=retrieval_kwargs)
        elif method == "agent-multi":
            response, docs = rag.answer_agent_multi_query(query, retrieval_kwargs=retrieval_kwargs)
        elif method == "agent-loop":
            response, docs = rag.answer_agent_loop(query, retrieval_kwargs=retrieval_kwargs)
        else:
            raise ValueError(f"Unknown method: {method}")
        
        # Format retrieved results
        formatted_docs = []
        for d in docs:
            meta = d.get('metadata', {})
            # Use path or title as doc_id if id not present
            doc_id = meta.get('id') or meta.get('path') or meta.get('title') or "unknown"
            formatted_docs.append({
                "doc_id": doc_id,
                "chunk": d.get('content', '')
            })
        
        result = {
            "qid": qid,
            "query": query,
            "intent": req.get('intent'),
            "required_corpora": required_corpora,
            "filters": filters,
            "notes_for_judges": req.get('notes_for_judges'),
            "ground_truth": req.get('ground_truth'),
            "llm_response": response,
            "retrieve_results": formatted_docs
        }
        results.append(result)
        
        # Save incrementally
        with open(output_file, 'w') as f:
            for r in results:
                f.write(json.dumps(r) + '\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Input requests.jsonl")
    parser.add_argument("--output", required=True, help="Output responses.jsonl")
    parser.add_argument("--data-root", required=True, help="Data root directory")
    parser.add_argument("--processed-file", help="Optional pre-processed data file (jsonl)")
    parser.add_argument("--embedding_type", default="dense", choices=["dense", "hybrid"])
    parser.add_argument("--method", default="agent-multi", choices=["simple", "agent-single", "agent-multi", "agent-loop"], help="RAG method to use")
    
    args = parser.parse_args()
    output_file = args.output.replace(".jsonl", f"_{args.method}.jsonl")
    print(f"[INFO] Output file: {output_file}")
    
    process_requests(args.input, output_file, args.data_root, args.method, args.embedding_type, args.processed_file)
