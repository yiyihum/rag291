import os
import faiss
import numpy as np
from openai import OpenAI
import tiktoken

# 初始化
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# -------- 1. 读取数据 --------
def load_texts(data_dir):
    texts = []
    for root, _, files in os.walk(data_dir):
        for f in files:
            if f.endswith((".txt", ".md")):
                with open(os.path.join(root, f), "r", encoding="utf-8") as fin:
                    texts.append(fin.read())
    return texts


# -------- 2. 拆分文本为小块 --------
def chunk_text(text, chunk_size=500, overlap=100):
    enc = tiktoken.get_encoding("cl100k_base")
    # Allow special token <|endoftext|> during encoding
    tokens = enc.encode(text, allowed_special={'<|endoftext|>'})
    chunks = []
    for i in range(0, len(tokens), chunk_size - overlap):
        chunk = enc.decode(tokens[i:i + chunk_size])
        chunks.append(chunk)
    return chunks


# -------- 3. 获取文本embedding --------
def get_embeddings(texts, model="text-embedding-3-small"):
    embeddings = []
    for i in range(0, len(texts), 100):  # 批处理防止过多请求
        batch = texts[i:i+100]
        resp = client.embeddings.create(model=model, input=batch)
        batch_emb = [d.embedding for d in resp.data]
        embeddings.extend(batch_emb)
    return np.array(embeddings).astype("float32")


# -------- 4. 构建Faiss索引 --------
def build_faiss_index(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index


# -------- 5. 检索 --------
def retrieve(query, index, chunks, top_k=3):
    q_emb = client.embeddings.create(model="text-embedding-3-small", input=query).data[0].embedding
    q_emb = np.array(q_emb).astype("float32").reshape(1, -1)
    D, I = index.search(q_emb, top_k)
    retrieved = []
    retrieve_results_llm = []
    for i in I[0]:
        chunk = chunks[i]
        doc_id = f"doc_{i}"  # Placeholder: Use real doc_id if available
        retrieved.append(chunk)
        retrieve_results_llm.append({"doc_id": doc_id, "chunk": chunk})
    return retrieved, retrieve_results_llm


# -------- 6. 生成回答 --------
def generate_answer(query, retrieved_chunks):
    context = "\n\n---\n\n".join(retrieved_chunks)
    prompt = f"""You are a helpful assistant. 
Use the following context to answer the question. If the question is not related to the context, say "I don't know". Do not make up information.
If the question is related to the context, answer the question briefly in detail.
Answer in less than 2-3 sentences.

Context:
{context}

Question:
{query}

Answer in detail:"""
    resp = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return resp.choices[0].message.content


# -------- 7. 主函数 --------
def rag_query(data_path, query):
    print("Loading data...")
    raw_texts = load_texts(data_path)
    chunks = []
    for t in raw_texts:
        chunks.extend(chunk_text(t))

    print(f"Total chunks: {len(chunks)}")

    print("Building embeddings and index...")
    embeddings = get_embeddings(chunks)
    index = build_faiss_index(embeddings)

    print("Retrieving relevant chunks...")
    retrieved, retrieve_results_llm = retrieve(query, index, chunks)

    print("Generating answer with GPT-4o...")
    answer = generate_answer(query, retrieved)
    print("\n=== Final Answer ===\n")
    print(answer)
    return answer, retrieve_results_llm


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_path", type=str, required=True, help="Path to data folder")
    parser.add_argument("--query", type=str, required=True, help="User query")
    args = parser.parse_args()

    rag_query(args.data_path, args.query)
