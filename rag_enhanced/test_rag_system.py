import sys
from pathlib import Path
import json

# Add current directory to sys.path
THIS_DIR = Path(__file__).resolve().parent
if str(THIS_DIR) not in sys.path:
    sys.path.insert(0, str(THIS_DIR))

from retrieval_system import RetrievalSystem
from rag_system import RAGSystem
from llm_client import get_llm_client

def main():
    print("=== Testing RAG System Refactor ===")
    
    # 1. Initialize Retrieval System
    # We use the current directory as root for finding data folders like 'arxiv_llm_2025'
    # If data is missing, it will warn but proceed.
    root_dir = str(THIS_DIR.parent) # Assuming data is in parent or relative to it as per original code
    print(f"Initializing RetrievalSystem with root: {root_dir}")
    retriever = RetrievalSystem(root_dir=root_dir, embedding_type="tfidf") # Use TFIDF for faster test build
    
    # 2. Initialize RAG System with Default Client (OpenRouter)
    llm = get_llm_client()
    rag = RAGSystem(retriever, llm)
    
    question = "What is Retrieval-Augmented Generation?"
    
    # 3. Test Modes
    print("\n--- Testing Mode 3.1: Simple RAG ---")
    ans1 = rag.answer_simple(question)
    print(f"Answer: {ans1}")
    
    print("\n--- Testing Mode 3.2: Agent Single-turn ---")
    ans2 = rag.answer_agent_single(question)
    print(f"Answer: {ans2}")
    
    print("\n--- Testing Mode 3.3: Agent Single-turn Multi-query ---")
    ans3 = rag.answer_agent_multi_query(question)
    print(f"Answer: {ans3}")
    
    print("\n--- Testing Mode 3.4: Agent Multi-turn ---")
    ans4 = rag.answer_agent_loop(question)
    print(f"Answer: {ans4}")
    
    print("\n=== Test Complete ===")

if __name__ == "__main__":
    main()
