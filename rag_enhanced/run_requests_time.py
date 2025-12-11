import json
import argparse
import time  # [Added] 用于计时
from pathlib import Path
from tqdm import tqdm
from llm_client import get_llm_client
from retrieval_system import RetrievalSystem
from rag_system import RAGSystem

# [Added] 简单的 Token 估算函数
# 如果需要非常精确，建议安装 tiktoken 并替换此函数
def estimate_tokens(text: str) -> int:
    if not text:
        return 0
    # 粗略估算：英文平均 4 字符 1 token，中文通常 0.7 字符 1 token
    # 这里使用通用的 len(text) / 4 进行估算，或者你可以简单地使用 len(text)
    return int(len(text) / 4)

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
    # Embedding 和 Index 构建在这里进行，不会计入后面的 query time
    retriever = RetrievalSystem(data_root, processed_file=processed_file, embedding_type=embedding_type, chunk_size=1000, use_faiss=True)
    llm = get_llm_client() 
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
        
        # [Added] 开始计时
        start_time = time.perf_counter()
        
        if method == "simple":
            response, docs = rag.answer_simple(query, top_n=5)
        elif method == "agent-single":
            response, docs = rag.answer_agent_single(query, top_n=5)
        elif method == "agent-loop":
            response, docs = rag.answer_agent_loop(query, top_n=5)
        else:
            raise ValueError(f"Unknown method: {method}")
            
        # [Added] 结束计时 (计算秒数)
        end_time = time.perf_counter()
        query_time = end_time - start_time
        
        # [Added] 计算 Token 数
        # 1. 计算 Response 的 token
        resp_tokens = estimate_tokens(response)
        
        # 2. 计算 Retrieve Docs 的总 token
        # 注意：这里假设 docs 是字符串列表或包含 'content'/'text' 字段的字典列表
        doc_tokens = 0
        if isinstance(docs, list):
            for doc in docs:
                if isinstance(doc, str):
                    doc_tokens += estimate_tokens(doc)
                elif isinstance(doc, dict):
                    # 尝试获取常见的内容字段，如果你的 doc 结构不同，请在此调整
                    content = doc.get('content') or doc.get('text') or str(doc)
                    doc_tokens += estimate_tokens(content)
        
        total_tokens = resp_tokens + doc_tokens
        
        print(f"[INFO] Time: {query_time:.4f}s | Tokens: {total_tokens} (Resp: {resp_tokens}, Docs: {doc_tokens})")

        result = {
            "qid": qid,
            "query": query,
            "intent": req.get('intent'),
            "required_corpora": required_corpora,
            "filters": filters,
            "notes_for_judges": req.get('notes_for_judges'),
            "ground_truth": req.get('ground_truth'),
            "llm_response": response,
            "retrieve_results": docs,
            "metrics": {  # [Added] 将性能指标保存到结果中
                "latency_seconds": query_time,
                "total_tokens": total_tokens,
                "response_tokens": resp_tokens,
                "context_tokens": doc_tokens
            }
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