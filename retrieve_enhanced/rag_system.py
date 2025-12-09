import json
from typing import List, Dict, Any, Optional
from retrieval_system import RetrievalSystem
from llm_client import LLMClient, get_llm_client

class RAGSystem:
    def __init__(self, retriever: RetrievalSystem, llm_client: LLMClient, rerank_model_name: str = "cross-encoder/ms-marco-MiniLM-L-6-v2"):
        self.retriever = retriever
        self.llm = llm_client
        self.reranker = None
        
        try:
            from sentence_transformers import CrossEncoder
            self.reranker = CrossEncoder(rerank_model_name)
            print(f"[INFO] Loaded Reranker: {rerank_model_name}")
        except ImportError:
            print("[WARN] sentence-transformers not found or CrossEncoder failed. Reranking disabled.")
        except Exception as e:
            print(f"[WARN] Failed to load Reranker: {e}. Reranking disabled.")

    def rerank(self, query: str, docs: List[Dict[str, Any]], top_n: int = 5) -> List[Dict[str, Any]]:
        """Rerank retrieved documents using CrossEncoder."""
        if not self.reranker or not docs:
            return docs[:top_n]
        
        # Prepare pairs for cross-encoder
        pairs = [[query, doc['content']] for doc in docs]
        scores = self.reranker.predict(pairs)
        
        # Update scores and sort
        for doc, score in zip(docs, scores):
            doc['score'] = float(score)
            
        ranked_docs = sorted(docs, key=lambda x: x['score'], reverse=True)
        return ranked_docs[:top_n]

    def _format_context(self, docs: List[Dict[str, Any]]) -> str:
        context = ""
        for i, doc in enumerate(docs, 1):
            meta = doc.get('metadata', {})
            source = meta.get('source', 'unknown')
            title = meta.get('title', 'Untitled')
            context += f"Source {i} ({source} - {title}):\n{doc['content']}\n\n"
        return context

    # 3.1 Simple Mode
    def answer_simple(self, question: str, top_n: int = 3, retrieval_kwargs: Dict[str, Any] = None) -> tuple[str, List[Dict[str, Any]]]:
        print(f"[Simple] Retrieving for: {question}")
        kwargs = retrieval_kwargs or {}
        docs = self.retriever.retrieve(question, top_k=top_n*2, **kwargs) # Retrieve more for reranking
        docs = self.rerank(question, docs, top_n=top_n)
        
        context = self._format_context(docs)
        prompt = f"""Answer the question based on the context below.
        
        Context:
        {context}
        
        Question: {question}
        """
        answer = self.llm.generate(prompt, system_prompt="You are a helpful RAG assistant.")
        return answer, docs

    # 3.2 Agent Single-turn
    def answer_agent_single(self, question: str, top_n: int = 3, retrieval_kwargs: Dict[str, Any] = None) -> tuple[str, List[Dict[str, Any]]]:
        # Generate Query
        prompt_q = f"""Given the user question, generate a better search query for a retrieval system.
        Return ONLY the query text.
        
        User Question: {question}
        """
        query = self.llm.generate(prompt_q, system_prompt="You are a query optimization assistant.").strip()
        print(f"[Agent Single] Generated Query: {query}")
        
        kwargs = retrieval_kwargs or {}
        docs = self.retriever.retrieve(query, top_k=top_n*2, **kwargs)
        docs = self.rerank(query, docs, top_n=top_n)
        
        context = self._format_context(docs)
        prompt_a = f"""Answer the question based on the context below.
        
        Context:
        {context}
        
        Question: {question}
        """
        answer = self.llm.generate(prompt_a, system_prompt="You are a helpful RAG assistant.")
        return answer, docs

    # 3.3 Agent Single-turn Multi-query
    def answer_agent_multi_query(self, question: str, top_n: int = 3, retrieval_kwargs: Dict[str, Any] = None) -> tuple[str, List[Dict[str, Any]]]:
        # Generate Queries
        prompt_q = f"""Given the user question, generate 3 search queries to cover different aspects or sources (Arxiv, GitHub, HuggingFace).
        Format the output as a JSON list of strings.
        
        User Question: {question}
        """
        response = self.llm.generate(prompt_q, system_prompt="You are a query optimization assistant.")
        try:
            queries = json.loads(response)
            if not isinstance(queries, list):
                queries = [question]
        except:
            queries = [question]
            
        print(f"[Agent Multi-Query] Generated Queries: {queries}")
        
        all_docs = []
        kwargs = retrieval_kwargs or {}
        
        for q in queries:
            # Retrieve for each query
            docs = self.retriever.retrieve(q, top_k=top_n, **kwargs)
            all_docs.extend(docs)
            
        # Deduplicate by content or some ID if available. Here simple content check.
        seen = set()
        unique_docs = []
        for d in all_docs:
            if d['content'] not in seen:
                seen.add(d['content'])
                unique_docs.append(d)
        
        # Rerank all unique docs against original question
        ranked_docs = self.rerank(question, unique_docs, top_n=top_n)
        
        context = self._format_context(ranked_docs)
        prompt_a = f"""Answer the question based on the context below.
        
        Context:
        {context}
        
        Question: {question}
        """
        answer = self.llm.generate(prompt_a, system_prompt="You are a helpful RAG assistant.")
        return answer, ranked_docs

    # 3.4 Agent Multi-turn
    def answer_agent_loop(self, question: str, max_turns: int = 3, top_n: int = 3, retrieval_kwargs: Dict[str, Any] = None) -> tuple[str, List[Dict[str, Any]]]:
        current_query = question
        collected_docs = []
        kwargs = retrieval_kwargs or {}
        
        for turn in range(max_turns):
            print(f"[Agent Loop] Turn {turn+1}: Querying '{current_query}'")
            docs = self.retriever.retrieve(current_query, top_k=top_n, **kwargs)
            collected_docs.extend(docs)
            
            # Evaluate if we have enough info
            context = self._format_context(collected_docs[-top_n:]) # Check latest
            prompt_eval = f"""We are trying to answer: "{question}"
            
            Based on the retrieved context below, do we have enough information to answer?
            If YES, return "YES".
            If NO, suggest a new search query to find missing information. Return ONLY the new query.
            
            Context:
            {context[:1000]}...
            """
            response = self.llm.generate(prompt_eval, system_prompt="You are a retrieval evaluator.").strip()
            
            if "YES" in response.upper():
                print("[Agent Loop] Sufficient information found.")
                break
            else:
                current_query = response
                print(f"[Agent Loop] New Query Suggested: {current_query}")
        
        # Final Answer
        # Rerank all collected docs
        seen = set()
        unique_docs = []
        for d in collected_docs:
            if d['content'] not in seen:
                seen.add(d['content'])
                unique_docs.append(d)
                
        ranked_docs = self.rerank(question, unique_docs, top_n=top_n)
        context = self._format_context(ranked_docs)
        
        prompt_a = f"""Answer the question based on the context below.
        
        Context:
        {context}
        
        Question: {question}
        """
        answer = self.llm.generate(prompt_a, system_prompt="You are a helpful RAG assistant.")
        return answer, ranked_docs
