# Retrieval Evaluator

We evaluate retrieved results from **two complementary perspectives** — traditional **information retrieval metrics** (ID-based) and **LLM-based RAG quality metrics** (content-based).

---

## 🔹 Traditional Information Retrieval Metrics

These metrics are computed **only from document IDs**, using the ground-truth relevance annotations (`qrels`) and the ranked retrieval results in `runs/`.  
They **do not require document content** or an LLM.  
The `get_doc_id()` function in `utils.py` is used to normalize or extract document identifiers.

Evaluation is implemented in `evaluate.py`, which loads the `qrels` and system runs, computes per-query scores, and then aggregates them by macro-averaging (averaging over all queries).

### **Recall@k**

> Measures how many relevant documents are successfully retrieved within the top-k results.

$$
Recall@k = \frac{|\text{Relevant} \cap \text{Retrieved@k}|}{|\text{Relevant}|}
$$

- High recall → good coverage (few relevant documents missed).  
- Computed per query, then averaged.

---

### **MRR (Mean Reciprocal Rank)**

> Focuses on how early the first relevant document appears in the ranked list.

$$
MRR = \frac{1}{|Q|}\sum_{q}\frac{1}{rank_{first\ relevant}(q)}
$$

- A high MRR means relevant documents are ranked near the top.  
- This script reports `mrr@10` by default.

---

### **nDCG (Normalized Discounted Cumulative Gain)**

> Measures how well the ranking order reflects the graded relevance of documents, giving higher weight to top-ranked hits.

$$
DCG@k = \sum_{i=1}^{k} \frac{2^{rel_i}-1}{\log_2(i+1)},\quad
nDCG@k = \frac{DCG@k}{IDCG@k}
$$

- Supports graded relevance (e.g., rel = 0, 1, 2).  
- A value close to 1 means the most relevant docs appear near the top.

---

### **MAP (Mean Average Precision)**

> Evaluates both precision and recall, considering the ranks of all relevant documents.

$$
AP = \frac{1}{|\text{Relevant}|}\sum_{r_i \in \text{Relevant}}Precision@r_i,\quad
MAP = \text{mean of }AP\text{ across all queries}
$$

- Sensitive to the ordering of multiple relevant documents.  
- Commonly used for overall ranking quality.

---

### ⚙️ Implementation Notes
- Metrics are computed **per query**, then averaged across queries (macro average).  
- The script also reports optional `primary_recall@k` where `rel ≥ 2`.  
- No LLM or document text is required.

---

## 🔹 LLM-based RAG Metrics

To evaluate the **semantic and factual quality** of RAG (Retrieval-Augmented Generation) outputs, we use the [**RAGAS**](https://docs.ragas.io/en/stable/) library.  
These metrics are **content-based** and require:
- `question`
- `contexts` → retrieved document texts (typically Top-k passages, *not* the whole corpus)
- `answers` → model-generated responses
- `ground_truths` → reference answers

All evaluations are powered by an LLM judge; here we use **`gpt-4.1-mini`**.

---

### **ContextEntityRecall()**
> Measures whether key entities in the ground-truth answer are present in the retrieved contexts.  
Higher values mean the retrieval step covers the essential entities.

---

### **ContextPrecision()**
> Measures how much of the retrieved context is actually relevant to the ground truth.  
High precision → less irrelevant or noisy context.

---

### **LLMContextRecall()**
> Uses an LLM to assess if the **retrieved contexts** contain enough information to support the correct answer.  
Focuses on **coverage** of supporting evidence.

---

### **Faithfulness()**
> Evaluates whether the **generated answer** is faithful to the retrieved contexts (i.e., free of hallucination).  
The answer should not include unsupported statements.

---

### **AnswerCorrectness()**
> Compares the generated answer with the reference answer (ground truth) for factual and semantic equivalence.  
Checks if the model’s output correctly answers the question.

---

### ⚙️ Practical Notes
- Only **retrieved Top-k documents** are used (to avoid exceeding LLM context limits).  
- Each document can be truncated (e.g., first 512–1024 tokens).  
- Metrics such as `Faithfulness`, `FactualCorrectness`, and `AnswerCorrectness` internally call the LLM for evaluation, while `ContextEntityRecall` and `ContextPrecision` can be computed more directly.  

---

## 🧾 Summary Comparison

| Category | Based on | Needs LLM? | Uses doc text? | Measures |
|:--|:--|:--:|:--:|:--|
| **Traditional IR** | Document IDs + relevance labels | ❌ | ❌ | Retrieval ranking quality |
| **RAGAS (LLM-based)** | Question + retrieved contexts + generated/ground truth answers | ✅ | ✅ | Context coverage, faithfulness, factual correctness |

---

**In short:**  
- `evaluate.py` measures how well your retriever ranks documents.  
- `ragas` metrics measure whether those retrieved documents truly help the generator produce correct and faithful answers.
