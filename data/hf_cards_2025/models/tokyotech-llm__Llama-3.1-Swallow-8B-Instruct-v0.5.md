---
language:
- en
- ja
library_name: transformers
pipeline_tag: text-generation
license:
- llama3.3
- gemma
model_type: llama
datasets:
- tokyotech-llm/lmsys-chat-1m-synth
- lmsys/lmsys-chat-1m
base_model:
- tokyotech-llm/Llama-3.1-Swallow-8B-v0.5
---

# Llama 3.1 Swallow - Built with Llama

Llama 3.1 Swallow is a series of large language models (8B, 70B) that were built by continual pre-training on the [Meta Llama 3.1](https://huggingface.co/collections/meta-llama/llama-31-669fc079a0c406a149a5738f) models.
Llama 3.1 Swallow enhanced the Japanese language capabilities of the original Llama 3.1 while retaining the English language capabilities.
We use approximately 200 billion tokens that were sampled from a large Japanese web corpus (Swallow Corpus Version 2), Japanese and English Wikipedia articles, and mathematical and
coding contents, etc (see the Training Datasets section of the base model) for continual pre-training.
The instruction-tuned models (Instruct) were built by supervised fine-tuning (SFT) on the synthetic data specially built for Japanese.
See the Swallow Model Index section to find other model variants.

**Note**: [Llama-3.1-Swallow-8B-Instruct-v0.5](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.5) model was continually pre-trained from the [meta-llama/Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct) and then instruction-tuned with our instruction datasets.

# Release History

- **June 25, 2025**: Released [Llama-3.1-Swallow-8B-Instruct-v0.5](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.5) and [Llama-3.1-Swallow-8B-v0.5](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-v0.5).
- **March 10, 2025**: Released [Llama-3.3-Swallow-70B-Instruct-v0.4](https://huggingface.co/tokyotech-llm/Llama-3.3-Swallow-70B-Instruct-v0.4) and [Llama-3.3-Swallow-70B-v0.4](https://huggingface.co/tokyotech-llm/Llama-3.3-Swallow-70B-v0.4).
- **December 30, 2024**: Released [Llama-3.1-Swallow-70B-Instruct-v0.3](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-70B-Instruct-v0.3).
- **December 23, 2024**: Released [Llama-3.1-Swallow-8B-Instruct-v0.3](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3).
- **November 11, 2024**: Released [Llama-3.1-Swallow-8B-v0.2](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-v0.2) and [Llama-3.1-Swallow-8B-Instruct-v0.2](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.2).
- **October 08, 2024**: Released [Llama-3.1-Swallow-8B-v0.1](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-v0.1), [Llama-3.1-Swallow-8B-Instruct-v0.1](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.1), [Llama-3.1-Swallow-70B-v0.1](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-70B-v0.1), and [Llama-3.1-Swallow-70B-Instruct-v0.1](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-70B-Instruct-v0.1).

# Major Updates
This release enhances the conversation capability of Llama 3.1 Swallow. The model is trained to imitate the behavior of [gemma-3-27b-it](https://huggingface.co/google/gemma-3-27b-it).
Among all open-source LLMs with <= 8 billion parameters, Llama-3.1-Swallow-8B-Instruct-v0.5 exhibits **state-of-the-art performance on Japanese MT-Bench**, outperforming its predecessor, [Llama-3.1-Swallow-8B-Instruct-v0.3](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.2), by 1.5 points.

## Swallow Model Index
|Model|Llama-3.1-Swallow-Instruct v0.5|Llama-3.1-Swallow v0.5|Llama-3.3-Swallow v0.4|Llama-3.3-Swallow-Instruct v0.4|Llama-3.1-Swallow-Instruct v0.3|Llama-3.1-Swallow-Instruct v0.2|Llama-3.1-Swallow v0.2|Llama-3.1-Swallow-Instruct v0.1|Llama-3.1-Swallow v0.1|
|---|---|---|---|---|---|---|---|---|---|
|8B|[🤗 HuggingFace](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.5)|[🤗 HuggingFace](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-v0.5) |||[🤗 HuggingFace](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3)|[🤗 HuggingFace](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.2)|[🤗 HuggingFace](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-v0.2)|[🤗 HuggingFace](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.1)|[🤗 HuggingFace](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-v0.1)|
|70B|||[🤗 HuggingFace](https://huggingface.co/tokyotech-llm/Llama-3.3-Swallow-70B-v0.4)|[🤗 HuggingFace](https://huggingface.co/tokyotech-llm/Llama-3.3-Swallow-70B-Instruct-v0.4)|[🤗 HuggingFace](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-70B-Instruct-v0.3)| | |[🤗 HuggingFace](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-70B-Instruct-v0.1)| [🤗 HuggingFace](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-70B-v0.1)|

![logo](./logo_v0.5.png)

The website [https://swallow-llm.github.io/](https://swallow-llm.github.io/index.en.html) provides large language models developed by the Swallow team.

## Model Details

* **Model type**: Please refer to [Llama 3.1 MODEL_CARD](https://github.com/meta-llama/llama3/blob/main/MODEL_CARD.md) for details on the model architecture.
* **Language(s)**: Japanese English
* **Library**: [Megatron-LM](https://github.com/NVIDIA/Megatron-LM), [transformers](https://github.com/huggingface/transformers)
* **Tokenizer**: Please refer to [Llama 3.1 blog](https://ai.meta.com/blog/meta-llama-3-1) for details on the tokenizer.
* **Contact**: swallow[at]nlp.c.titech.ac.jp 

## Model Performance

## Japanese MT-Bench

* We report evaluation results judged by **gpt-4o-2024-08-06** as below.
  * In our releases earlier than January 1, 2025, we reported scores judged by gpt-4-1106-preview. Scores reported below are thus not directly comparable with those reported in those earlier releases.
  
|Model|coding|extraction|humanities|math|reasoning|roleplay|stem|writing|JMTAvg|
|---|---|---|---|---|---|---|---|---|---|
| llm-jp-3-7.2b-instruct3                   | 0.358 | 0.597 | 0.812 | 0.386 | 0.438 | 0.766 | 0.622 | 0.721  | 0.588 |
| Qwen2.5-7B-Instruct                       | 0.599 | 0.741 | 0.719 | 0.637 | 0.541 | 0.744 | 0.624 | 0.713  | 0.665 |
| Tanuki-8B-dpo-v1.0                        | 0.461 | 0.597 | 0.562 | 0.495 | 0.377 | 0.589 | 0.509 | 0.643  | 0.529 |
| Llama 3 8B Instruct                       | 0.467 | 0.706 | 0.692 | 0.310 | 0.433 | 0.542 | 0.532 | 0.546  | 0.529 |
| Llama 3.1 8B Instruct                     | 0.420 | **0.830** | 0.550 | 0.514 | 0.349 | 0.502 | 0.479 | 0.504  | 0.519 |
| Llama 3 Youko 8B Instruct                 | 0.464 | 0.757 | 0.769 | 0.414 | 0.487 | 0.695 | 0.583 | 0.753  | 0.616 |
| Llama-3-ELYZA-JP-8B                       | 0.389 | 0.706 | 0.647 | 0.426 | **0.613** | 0.684 | 0.533 | 0.697  | 0.587 |
| Llama 3 heron brain 8B v0.3              | 0.362 | 0.566 | 0.602 | 0.315 | 0.426 | 0.586 | 0.567 | 0.550  | 0.497 |
| Llama 3.1 Swallow 8B Instruct v0.1        | 0.427 | 0.738 | 0.675 | 0.527 | 0.453 | 0.615 | 0.593 | 0.624  | 0.581 |
| Llama 3.1 Swallow 8B Instruct v0.2        | 0.534 | 0.748 | 0.705 | 0.565 | 0.475 | 0.646 | 0.579 | 0.646  | 0.612 |
| Llama 3.1 Swallow 8B Instruct v0.3        | **0.562** | 0.756 | 0.869 | **0.610** | 0.512 | 0.783 | 0.748 | 0.803 | 0.705 |
| Llama 3.1 Swallow 8B Instruct v0.5        | 0.551 | 0.814 | **0.847** | 0.568 | 0.577 | **0.796** | **0.770** | **0.832** | **0.719** |

### Japanese tasks

|Model|JCom.|JEMHopQA|NIILC|JSQuAD|XL-Sum|MGSM|WMT20-en-ja|WMT20-ja-en|JMMLU|JHumanEval|Ja Avg|
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |4-shot|4-shot|4-shot|4-shot|1-shot|4-shot|4-shot|4-shot|5-shot|0-shot|   |
|   |EM acc|Char-F1|Char-F1|Char-F1|ROUGE-2|EM acc|BLEU|BLEU|EM acc|pass@1|   |
| llm-jp-3-7.2b-instruct3                   | 0.780 | 0.297 | 0.570 | 0.882 | 0.132 | 0.344 | 0.251 | 0.189 | 0.422 | 0.196 | 0.406 |
| Qwen2.5-7B-Instruct                       | 0.915 | 0.429 | 0.391 | 0.891 | 0.168 | 0.632 | 0.211 | 0.192 | 0.623 | 0.532 | 0.498 |
| Tanuki-8B-dpo-v1.0                        | 0.278 | 0.284 | 0.370 | 0.670 | 0.102 | 0.428 | 0.238 | 0.183 | 0.306 | 0.251 | 0.311 |
| Llama 3 8B Instruct                       | 0.880 | 0.417 | 0.385 | 0.891 | 0.126 | 0.424 | 0.214 | 0.202 | 0.468 | 0.296 | 0.430 |
| Llama 3.1 8B Instruct                     | 0.880 | 0.447 | 0.407 | 0.886 | 0.148 | 0.516 | 0.218 | 0.200 | 0.509 | 0.488 | 0.470 |
| Llama 3 Youko 8B Instruct                 | 0.921 | 0.481 | 0.517 | 0.899 | 0.209 | 0.472 | 0.256 | 0.191 | 0.469 | 0.262 | 0.468 |
| Llama-3-ELYZA-JP-8B                       | 0.897 | 0.498 | 0.496 | 0.906 | 0.168 | 0.436 | 0.250 | 0.185 | 0.487 | 0.388 | 0.471 |
| Llama 3 heron brain 8B v0.3              | 0.923 | 0.493 | 0.569 | 0.906 | **0.218** | 0.456 | 0.277 | 0.217 | 0.499 | 0.318 | 0.488 |
| Llama 3.1 Swallow 8B Instruct v0.1        | 0.924 | **0.587** | 0.574 | **0.917** | 0.138 | 0.508 | 0.282 | 0.228 | 0.530 | 0.366 | 0.505 |
| Llama 3.1 Swallow 8B Instruct v0.2        | 0.929 | 0.560 | 0.599 | 0.915 | 0.137 | 0.528 | 0.288 | 0.227 | 0.550 | 0.408 | 0.514 |
| Llama 3.1 Swallow 8B Instruct v0.3        | 0.924 | 0.528 | 0.583 | 0.896 | 0.191 | 0.532 | 0.281 | 0.229 | 0.544 | 0.394 | 0.510 |
| Llama 3.1 Swallow 8B Instruct v0.5        | **0.937** | 0.511 | **0.606** | 0.900 | 0.174 | **0.604** | **0.293** | **0.230** | **0.581** | **0.496** | **0.533** |


### English tasks

|Model|OpenBookQA|TriviaQA|HellaSWAG|SQuAD2.0|XWINO|MMLU|GSM8K|MATH|BBH|HumanEval|En Avg|
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |4-shot|4-shot|4-shot|4-shot|4-shot|5-shot|4-shot|4-shot | 3-shot|0-shot|   |
|   |Acc|EM acc|Acc|EM acc|Acc|Acc|EM acc|CoT EM Acc| CoT EM Acc| pass@1|   |
| llm-jp-3-7.2b-instruct3                   | 0.328 | 0.479 | 0.563 | 0.501 | 0.876 | 0.462 | 0.264 | 0.028 | 0.420 | 0.219 | 0.414 |
| Qwen2.5-7B-Instruct                       | 0.428 | 0.519 | 0.624 | 0.569 | 0.877 | 0.742 | 0.739 | 0.688 | 0.217 | 0.636 | 0.604 |
| Tanuki-8B-dpo-v1.0                        | 0.334 | 0.283 | 0.469 | 0.501 | 0.816 | 0.377 | 0.487 | 0.178 | 0.333 | 0.288 | 0.406 |
| Llama 3 8B Instruct                       | 0.388 | 0.670 | 0.583 | 0.611 | 0.892 | 0.657 | 0.745 | 0.306 | 0.646 | 0.554 | 0.605 |
| Llama 3.1 8B Instruct                     | 0.366 | 0.699 | 0.592 | 0.600 | 0.904 | 0.680 | 0.743 | 0.376 | 0.690 | 0.624 | 0.627 |
| Llama 3 Youko 8B Instruct                 | 0.406 | 0.613 | 0.599 | 0.559 | 0.897 | 0.596 | 0.563 | 0.152 | 0.401 | 0.287 | 0.507 |
| Llama-3-ELYZA-JP-8B                       | 0.318 | 0.551 | 0.523 | 0.600 | 0.882 | 0.587 | 0.558 | 0.164 | 0.321 | 0.449 | 0.495 |
| Llama 3 heron brain 8B v0.3              | 0.362 | 0.656 | 0.569 | 0.581 | 0.901 | 0.621 | 0.578 | 0.222 | 0.641 | 0.380 | 0.551 |
| Llama 3.1 Swallow 8B Instruct v0.1        | 0.388 | 0.649 | 0.615 | 0.598 | 0.891 | 0.624 | 0.605 | 0.236 | 0.642 | 0.379 | 0.563 |
| Llama 3.1 Swallow 8B Instruct v0.2        | 0.380 | 0.625 | 0.603 | 0.607 | 0.887 | 0.634 | 0.620 | 0.264 | 0.649 | 0.474 | 0.574 |
| Llama 3.1 Swallow 8B Instruct v0.3        | 0.396 | 0.629 | 0.593 | 0.570 | 0.884 | 0.629 | 0.622 | 0.266 | 0.626 | 0.445 | 0.566 |
| Llama 3.1 Swallow 8B Instruct v0.5        | 0.396 | 0.638 | 0.603 | 0.581 | 0.889 | 0.663 | 0.717 | 0.368 | 0.628 | 0.554 | 0.604 |


## Evaluation Benchmarks

### Japanese MT-Bench

We used [Japanese MT-Bench](https://wandb.ai/wandb-japan/llm-leaderboard/artifacts/dataset/mtbench_ja_question) to assess the capabilities of multi-turn dialogue with the following settings:

- Implementation: FastChat [Zheng+, 2023] (commit #e86e70d0)
- Question: [Nejumi LLM-Leaderboard NEO, mtbench_ja_question_v4](https://wandb.ai/wandb-japan/llm-leaderboard/artifacts/v4)
- Reference Answer: [swallow-evaluation, reference answer](https://github.com/swallow-llm/swallow-evaluation/tree/main/fastchat/fastchat/llm_judge/data/japanese_mt_bench/reference_answer)
- Prompt for Judge: [Nejumi LLM-Leaderboard NEO, mtbench_ja_prompt_v1](https://wandb.ai/wandb-japan/llm-leaderboard/artifacts/dataset/mtbench_ja_prompt/v1)
- Judge: `gpt-4o-2024-08-06`
- Scoring: Absolute scale normalized to a 0-1 range, averaged over five runs.

### Japanese evaluation benchmarks

We used llm-jp-eval(v1.3.0), JP Language Model Evaluation Harness(commit #9b42d41) and Code Generation LM Evaluation Harness(commit #0261c52). The details are as follows:

- Multiple-choice question answering (JCommonsenseQA [Kurihara et al., 2022])
- Open-ended question answering (JEMHopQA [Ishii et al., 2024])
- Open-ended question answering (NIILC [関根, 2003])
- Machine reading comprehension (JSQuAD [Kurihara et al., 2022])
- Automatic summarization (XL-Sum [Hasan et al., 2021])
- Machine translation (WMT2020 ja-en [Barrault et al., 2020])
- Machine translation (WMT2020 en-ja [Barrault et al., 2020])
- Arithmetic reasoning (MGSM [Shi et al., 2023])
- Academic exams (JMMLU [尹ら, 2024])
- Code generation (JHumanEval [佐藤ら, 2024])

### English evaluation benchmarks

We used the Language Model Evaluation Harness(v.0.4.2) and Code Generation LM Evaluation Harness(commit #0261c52). The details are as follows:

- Multiple-choice question answering (OpenBookQA [Mihaylov et al., 2018])
- Open-ended question answering (TriviaQA [Joshi et al., 2017])
- Machine reading comprehension (SQuAD2 [Rajpurkar et al., 2018])
- Commonsense reasoning (XWINO [Tikhonov and Ryabinin, 2021])
- Natural language inference (HellaSwag [Zellers et al., 2019])
- Arithmetic reasoning (GSM8K [Cobbe et al., 2021])
- Mathematical reasoning (MATH [Hendrycks et al., 2022][Lightman et al., 2024])
- Reasoning (BBH (BIG-Bench-Hard) [Suzgun et al., 2023])
- Academic exams (MMLU [Hendrycks et al., 2021])
- Code generation (HumanEval [Chen et al., 2021])

## Usage

```sh
pip install vllm
```

```python
from transformers import AutoTokenizer
from vllm import LLM, SamplingParams

model_name = "tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.5"

tokenizer = AutoTokenizer.from_pretrained(model_name)
llm = LLM(
    model=model_name,
    tensor_parallel_size=1,
)

sampling_params = SamplingParams(
    temperature=0.6, top_p=0.9, max_tokens=512, stop="<|eot_id|>"
)


message = [
    {
        "role": "user",
        "content": "東京の紅葉した公園で、東京タワーと高層ビルを背景に、空を舞うツバメと草地に佇むラマが出会う温かな物語を書いてください。",
    },
]
prompt = tokenizer.apply_chat_template(
    message, tokenize=False, add_generation_prompt=True
)

output = llm.generate(prompt, sampling_params)

print(output[0].outputs[0].text)

```

## Training Datasets

### Instruction Tuning

The following datasets were used for the instruction tuning.

- [Gemma-3-LMSYS-Chat-1M-Synth](https://huggingface.co/datasets/tokyotech-llm/lmsys-chat-1m-synth)
  - Single-turn Japanese instruction dataset synthesized and derived from [lmsys-chat-1m](https://huggingface.co/datasets/lmsys/lmsys-chat-1m) [\[Zhang+, ICLR24\]](https://openreview.net/forum?id=BOfDKxfwt0)).
  - First-turn user instructions were translated into Japanese via DeepL (machine translation), and assistant responses were generated using [gemma-3-27b-it](https://huggingface.co/google/gemma-3-27b-it). The same model, i.e., [gemma-3-27b-it](https://huggingface.co/google/gemma-3-27b-it) served as a judge for rejection sampling (n=10).
 Conversations containing personally identifiable information (PII) and template-based user instructions were removed. Duplicate instructions were removed.

## Risks and Limitations

The models released here are still in the early stages of our research and development and have not been tuned to ensure outputs align with human intent and safety considerations.

## Acknowledgements

We thank Meta Research for releasing Llama 3.1 under a generous open license.

We received various supports, including:

+ AIST project: "Research and Development of Foundation Models for Generative AI in the Physical Domain"
+ NEDO project: "Development of Artificial Intelligence Application Technology to Support Judgment in Design Risk Assessment Work Based on the Perspective of Skilled Persons" (JPNP18002) of "Development of Integration Technology as the Core of Next Generation Artificial Intelligence and Robotics"
+ MEXT project: "Formation of R&D center to ensure transparency and reliability of generative AI models"
+ AIST program: [Large Generative AI Development Support Program](https://abci.ai/en/link/lfm_support_program.html)

## License

[META LLAMA 3.1 COMMUNITY LICENSE](https://www.llama.com/llama3_1/license/) and [Gemma Terms of Use](https://ai.google.dev/gemma/terms)

## Authors

Here are the team members:
- From [Okazaki Laboratory, Institute of Science Tokyo](https://www.nlp.c.titech.ac.jp/index.en.html), the following members:
  - [Naoaki Okazaki](https://www.chokkan.org/index.ja.html)
  - [Sakae Mizuki](https://s-mizuki-nlp.github.io/)
  - [Youmi Ma](https://www.nlp.c.titech.ac.jp/member/youmi.en.html)
  - [Sangwhan Moon](https://www.sangwhan.com/)
  - [Koki Maeda](https://sites.google.com/view/silviase)
  - [Masanari Ohi](https://sites.google.com/view/masanariohi)
  - [Hinari Shimada](https://hinarishimada.github.io/portfolio)
  - [Taihei Shiotani](https://github.com/inatoihs)
  - [Koshiro Saito](https://sites.google.com/view/koshiro-saito)
  - [Tatsuya Ichinose](https://tatsuya736482.github.io/myprofile)
  - Naoya Matsushita
  - Sora Miyamoto
  - Nguyen Tien Dung
  - Yuta Katayama
- From [YOKOTA Laboratory, Institute of Science Tokyo](https://www.rio.gsic.titech.ac.jp/en/index.html), the following members:
  - [Rio Yokota](https://twitter.com/rioyokota)
  - [Kazuki Fujii](https://twitter.com/okoge_kaz)
  - [Taishi Nakamura](https://twitter.com/Setuna7777_2)
  - [Takumi Okamoto](https://www.linkedin.com/in/takumi-okamoto)
  - [Ishida Shigeki](https://www.wantedly.com/id/reborn27)
  - Masaki Kawamura
  - Yukito Tajima
- From [Artificial Intelligence Research Center, AIST, Japan](https://www.airc.aist.go.jp/en/teams/), the following members:
  - [Hiroya Takamura](https://sites.google.com/view/hjtakamura)

## How to cite

If you find our work helpful, please feel free to cite these papers.

```
@inproceedings{Fujii:COLM2024,
   title={Continual Pre-Training for Cross-Lingual LLM Adaptation:
Enhancing Japanese Language Capabilities},
   author={Kazuki Fujii and Taishi Nakamura and Mengsay Loem and Hiroki
Iida and Masanari Ohi and Kakeru Hattori and Hirai Shota and Sakae
Mizuki and Rio Yokota and Naoaki Okazaki},
   booktitle="Proceedings of the First Conference on Language Modeling",
   series={COLM},
   pages="(to appear)",
   year="2024",
   month=oct,
   address={University of Pennsylvania, USA},
}

@inproceedings{Okazaki:COLM2024,
   title={Building a Large Japanese Web Corpus for Large Language Models},
   author={Naoaki Okazaki and Kakeru Hattori and Hirai Shota and Hiroki
Iida and Masanari Ohi and Kazuki Fujii and Taishi Nakamura and Mengsay
Loem and Rio Yokota and Sakae Mizuki},
   booktitle="Proceedings of the First Conference on Language Modeling",
   series={COLM},
   pages="(to appear)",
   year="2024",
   month=oct,
   address={University of Pennsylvania, USA},
}

@misc{ma:arxiv2025,
      title={Building Instruction-Tuning Datasets from Human-Written Instructions with Open-Weight Large Language Models}, 
      author={Youmi Ma and Sakae Mizuki and Kazuki Fujii and Taishi Nakamura and Masanari Ohi and Hinari Shimada and Taihei Shiotani and Koshiro Saito and Koki Maeda and Kakeru Hattori and Takumi Okamoto and Shigeki Ishida and Rio Yokota and Hiroya Takamura and Naoaki Okazaki},
      year={2025},
      eprint={2503.23714},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2503.23714}, 
}
```

### References

```tex
@misc{dubey2024llama3herdmodels,
      title={The Llama 3 Herd of Models}, 
      author={Abhimanyu Dubey and Abhinav Jauhri and Abhinav Pandey and Abhishek Kadian and Ahmad Al-Dahle and Aiesha Letman and Akhil Mathur and Alan Schelten and Amy Yang and Angela Fan et al.},
      year={2024},
      eprint={2407.21783},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2407.21783}, 
}
```