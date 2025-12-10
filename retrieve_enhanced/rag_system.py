import json
from typing import List, Dict, Any, Optional
from retrieval_system import RetrievalSystem
from llm_client import LLMClient, get_llm_client

class RAGSystem:
    def __init__(self, retriever: RetrievalSystem, llm_client: LLMClient):
        self.retriever = retriever
        self.llm = llm_client

    def _format_context(self, docs: List[Dict[str, Any]]) -> str:
        context = ""
        for i, doc in enumerate(docs, 1):
            context += f"{doc['content']}\n\n"
        return context

    # 3.1 Simple Mode
    def answer_simple(self, question: str, top_n: int = 3) -> tuple[str, List[Dict[str, Any]]]:
        print(f"[Simple] Retrieving for: {question}")
        docs = self.retriever.retrieve(question, top_k=top_n)
        
        context = self._format_context(docs)
        prompt = f"""Answer the question using ONLY the context below. Provide a brief explanation, followed by a concise final answer starting with 'Answer:'.
        
        Context:
        {context}
        
        Question: {question}
        """
        answer = self.llm.generate(prompt, system_prompt="You are a helpful RAG assistant.")
        return answer, docs

    # 3.2 Agent Single-turn
    def answer_agent_single(self, question: str, top_n: int = 3) -> tuple[str, List[Dict[str, Any]]]:
        # Generate Query
        prompt_q = f"""Given the user question, generate a better search query for a retrieval system.
        Return ONLY the query text.
        
        User Question: {question}
        """
        query = self.llm.generate(prompt_q, system_prompt="You are a query optimization assistant.").strip()
        print(f"[Agent Single] Generated Query: {query}")
        
        docs = self.retriever.retrieve(query, top_k=top_n)
        
        context = self._format_context(docs)
        prompt_a = f"""Answer the question using ONLY the context below. Provide a brief explanation, followed by a concise final answer starting with 'Answer:'.
        
        Context:
        {context}
        
        Question: {question}
        """
        answer = self.llm.generate(prompt_a, system_prompt="You are a helpful RAG assistant.")
        return answer, docs

    # 3.4 Agent Multi-turn
    def answer_agent_loop(self, question: str, max_turns: int = 3, top_n: int = 3) -> tuple[str, List[Dict[str, Any]]]:
        current_query = question
        collected_docs = []
        
        for turn in range(max_turns):
            print(f"[Agent Loop] Turn {turn+1}: Querying '{current_query}'")
            docs = self.retriever.retrieve(current_query, top_k=top_n)
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
        # Deduplicate and sort
        seen = set()
        unique_docs = []
        for d in collected_docs:
            if d['content'] not in seen:
                seen.add(d['content'])
                unique_docs.append(d)
                
        unique_docs.sort(key=lambda x: x['score'], reverse=True)
        final_docs = unique_docs[:top_n]
        context = self._format_context(final_docs)
        
        prompt_a = f"""Answer the question using ONLY the context below. Provide a brief explanation, followed by a concise final answer starting with 'Answer:'.
        
        Context:
        {context}
        
        Question: {question}
        """
        answer = self.llm.generate(prompt_a, system_prompt="You are a helpful RAG assistant.")
        return answer, final_docs