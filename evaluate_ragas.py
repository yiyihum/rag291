# pip install ragas

from ragas import evaluate, EvaluationDataset
from ragas.metrics import LLMContextRecall, ContextEntityRecall, Faithfulness, FactualCorrectness, AnswerCorrectness, ContextPrecision
from ragas.llms import instructor_llm_factory, LangchainLLMWrapper

from openai import OpenAI
from langchain_openai import ChatOpenAI

import os

def make_eval_dataset(questions, contexts, generated_answers, ground_truths):
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

def make_eval_llm(model_name="gpt-4o"):
    eval_llm = LangchainLLMWrapper(ChatOpenAI(model=model_name, openai_api_key=os.getenv("OPENAI_API_KEY")))
    return eval_llm

def ragas_eval(dataset, eval_llm):
    results = evaluate(
        dataset=dataset,
        metrics=[
            ContextEntityRecall(), # 上下文实体召回率
            ContextPrecision(),   # 上下文精确度
            # FactualCorrectness()  # 答案是否事实正确 (based on retrieved context)
            LLMContextRecall(),   # 检索的上下文是否包含正确信息
            Faithfulness(),       # 答案是否忠实于上下文
            AnswerCorrectness(),  # 答案是否正确 (based on ground truth)
        ],
        llm=eval_llm
    )
    return results

if __name__ == "__main__":
    # A complete example of RAG evaluation using RAGAS
    # -------------------------------
    # 1️⃣ 构造模拟RAG QA样例数据
    # -------------------------------

    sample_docs = [
        "Albert Einstein proposed the theory of relativity, which transformed our understanding of time, space, and gravity.",
        "Marie Curie was a physicist and chemist who conducted pioneering research on radioactivity and won two Nobel Prizes.",
        "Isaac Newton formulated the laws of motion and universal gravitation, laying the foundation for classical mechanics.",
        "Charles Darwin introduced the theory of evolution by natural selection in his book 'On the Origin of Species'.",
        "Ada Lovelace is regarded as the first computer programmer for her work on Charles Babbage's early mechanical computer, the Analytical Engine."
    ]

    questions = [
        "Who developed the theory of relativity?",
        "Who was the first computer programmer?",
        "Who proposed the theory of evolution by natural selection?"
    ]

    # 模拟从 RAG 系统生成的答案
    generated_answers = [
        "The theory of relativity was proposed by Albert Einstein.",
        "Ada Lovelace is considered the first computer programmer.",
        "Charles Darwin introduced the theory of evolution by natural selection."
    ]

    # 参考答案（Ground truth）
    ground_truths = [
        "Albert Einstein",
        "Ada Lovelace",
        "Charles Darwin"
    ]

    # 模拟检索结果 (contexts)，通常来自retriever top-k
    contexts = [
        [sample_docs[0]],      # 对应Einstein
        [sample_docs[4]],      # 对应Lovelace
        [sample_docs[3]]       # 对应Darwin
    ]

    # from utils import load_jsonl, load_csv, convert_json_to_string
    # arxiv_data = load_jsonl("data/arxiv_llm_2025/arxiv_llm_2025.jsonl")
    # corpus_abs = [item["abstract"] for item in arxiv_data]
    # corpus_1 = [convert_json_to_string(item) for item in arxiv_data]

    # contexts = corpus_1

    # requests = load_jsonl("requests.jsonl")
    # questions = [req["query"] for req in requests]
    # ground_truths = [req["notes_for_judges"] for req in requests]

    # -------------------------------
    # 2️⃣ 构造 RAGAS 的 EvaluationDataset
    # -------------------------------

    eval_dataset = make_eval_dataset(questions, contexts, generated_answers, ground_truths)

    # -------------------------------
    # 3️⃣ 定义用于评估的 LLM 接口
    # -------------------------------
    # RAGAS支持OpenAI-compatible接口；也可用本地模型
    # client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # 定义一个简单的LLM调用封装
    # def llm(prompt: str) -> str:
    #     completion = client.chat.completions.create(
    #         model="gpt-4o",
    #         messages=[{"role": "user", "content": prompt}],
    #     )
    #     return completion.choices[0].message.content

    # evaluator_llm = instructor_llm_factory("openai", model="gpt-4o", client=client)

    evaluator_llm = make_eval_llm(model_name="gpt-4o")

    # -------------------------------
    # 4️⃣ 执行评估
    # -------------------------------

    results = ragas_eval(eval_dataset, evaluator_llm)

    # -------------------------------
    # 5️⃣ 打印结果
    # -------------------------------
    print("RAG Evaluation Results:")
    print(results)