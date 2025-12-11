# pip install ragas

from ragas import evaluate, EvaluationDataset
from ragas.metrics import LLMContextRecall, ContextEntityRecall, Faithfulness, FactualCorrectness, AnswerCorrectness, ContextPrecision
from ragas.llms import LangchainLLMWrapper

from openai import OpenAI
from langchain_openai import ChatOpenAI

import os, argparse
from utils import load_jsonl, load_json, write_jsonl, get_doc_content   #, call_openai

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

def make_eval_llm(model_name="gpt-4.1-mini"):
    eval_llm = LangchainLLMWrapper(ChatOpenAI(model=model_name, openai_api_key=os.getenv("OPENAI_API_KEY")))
    return eval_llm

def ragas_eval(dataset, eval_llm):
    results = evaluate(
        dataset=dataset,
        metrics=[
            ContextEntityRecall(), # 上下文实体召回率
            ContextPrecision(),    # 上下文精确度
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

    ap = argparse.ArgumentParser(description="Evaluate retrieval runs against qrels with RAGAS.")
    ap.add_argument("--example", action="store_true", help="Run with example data")
    ap.add_argument("--run_name", required=True, help="Help to name output files")
    ap.add_argument("--qrels", required=True, help="Path to qrels.jsonl or qrels.csv")  # same as ground truth
    ap.add_argument("--runs_path", default="runs", help="Directory containing system subfolders with per-Q JSON files")  # same as retrieved contexts
    ap.add_argument("--responses_dir", default=None, help="Directory containing system subfolders with per-Q generated answers")   # generated answers
    ap.add_argument("--out_dir", default="eval_results", help="Where to write leaderboard and breakdowns")
    ap.add_argument("--model_name", default="gpt-4.1-mini", help="LLM model name for evaluation")
    args = ap.parse_args()

    os.makedirs(args.out_dir, exist_ok=True)

    # -------------------------------
    # 1️⃣ construct example RAG QA data
    # -------------------------------
    if args.example:
        # retrieved docs
        sample_docs = [
            "Albert Einstein proposed the theory of relativity, which transformed our understanding of time, space, and gravity.",
            "Marie Curie was a physicist and chemist who conducted pioneering research on radioactivity and won two Nobel Prizes.",
            "Isaac Newton formulated the laws of motion and universal gravitation, laying the foundation for classical mechanics.",
            "Charles Darwin introduced the theory of evolution by natural selection in his book 'On the Origin of Species'.",
            "Ada Lovelace is regarded as the first computer programmer for her work on Charles Babbage's early mechanical computer, the Analytical Engine."
        ]
        # human query
        questions = [
            "Who developed the theory of relativity?",
            "Who was the first computer programmer?",
            "Who proposed the theory of evolution by natural selection?"
        ]
        # simulate LLM generated response
        generated_answers = [
            "The theory of relativity was proposed by Albert Einstein.",
            "Ada Lovelace is considered the first computer programmer.",
            "Charles Darwin introduced the theory of evolution by natural selection."
        ]
        # Ground truth for each question
        ground_truths = [
            "Albert Einstein",
            "Ada Lovelace",
            "Charles Darwin"
        ]
        # simulate retrieved docs (contexts)，comes from retriever top-k
        contexts = [
            [sample_docs[0], sample_docs[1]],      # Einstein
            [sample_docs[4]],      # Lovelace
            [sample_docs[3]]       # Darwin
        ]
    else:
        # Normal processing pipeline

        contexts = []
        generated_answers = []        
        arxiv_corpus = load_jsonl("../data/arxiv_llm_2025/arxiv_llm_2025.jsonl")

        retrieved_result = load_json(args.runs_path)
        for key in retrieved_result:
            # print(f"Processing query: {key}")
            obj = retrieved_result[key]

            hits = obj.get("hits", [])
            # Normalize and sort by provided rank or score
            def sort_key(h):
                if "rank" in h and isinstance(h["rank"], int):
                    return h["rank"]
                return -float(h.get("score", 0.0))
            hits_sorted = sorted(hits, key=sort_key)
            docs = [get_doc_content(h) for h in hits_sorted]
            contexts.append(docs)
            
            if args.responses_dir is None:
                # generated_answers.append(hits_sorted[0]["context"])
                # generated_answers.append(hits_sorted[0]["preview"])
                tmp_query = obj.get("query", "")
                prompt = tmp_query + "\nPlease answer the question in one or two sentences.\nHere is retrieved docs for reference.\n"
                for d in docs:
                    prompt += d + '\n'
                print("Use LLM generated code!")
                # generated_answers.append(call_openai(prompt))

        requests = load_jsonl(args.qrels)
        questions = [req["query"] for req in requests]
        # need to fill with fluent generated answers, rather than id/instruction
        ground_truths = [req["ground_truth"] for req in requests]
        if args.responses_dir is None:
            write_jsonl(generated_answers, f"../LLM_answer_for_{args.run_name}.txt")
        else:
            generated_answers = load_jsonl(args.responses_dir)
        
            # update with response data
            # generated_answers = load_json(args.responses_dir)
            # generated_answers = [req["llm_response"] for req in requests]

        # print("questions:", questions[-1])
        # print("ground_truths:", ground_truths[-1])
        # print("contexts:", contexts[-1])

    # -------------------------------
    # 2️⃣ construct RAGAS EvaluationDataset
    # -------------------------------

    eval_dataset = make_eval_dataset(questions, contexts, generated_answers, ground_truths)

    # -------------------------------
    # 3️⃣ define LLM interface for evaluation
    # -------------------------------
    # client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    # def llm(prompt: str) -> str:
    #     completion = client.chat.completions.create(
    #         model="gpt-4o",
    #         messages=[{"role": "user", "content": prompt}],
    #     )
    #     return completion.choices[0].message.content

    # evaluator_llm = instructor_llm_factory("openai", model="gpt-4o", client=client)

    evaluator_llm = make_eval_llm(model_name=args.model_name)

    # -------------------------------
    # 4️⃣ evaluate
    # -------------------------------

    results = ragas_eval(eval_dataset, evaluator_llm)

    # -------------------------------
    # 5️⃣ print results
    # -------------------------------
    print("RAG Evaluation Results:")
    print(results)
    final_output_dir = os.path.join(args.out_dir, f"{args.run_name}_ragas_evaluation_results.txt")
    print(f"Save result to {final_output_dir}")
    with open(final_output_dir, "w", encoding="utf-8") as f:
        print(results, file=f)