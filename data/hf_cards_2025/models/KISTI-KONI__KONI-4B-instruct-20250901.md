---
license: gemma
language:
- ko
- en
tags:
- text-generation
- pytorch
- causal-lm
- gemma3
- 4b
library_name: transformers
base_model:
- google/gemma-3-4b-pt
---

# KISTI-KONI/KONI-4B-instruct-20250901

## Model Description

**KONI (KISTI Open Neural Intelligence)** is a large language model developed by the Korea Institute of Science and Technology Information (KISTI). Designed specifically for the scientific and technological domains, KONI excels in both Korean and English, making it an ideal tool for tasks requiring specialized knowledge in these areas.

---

## Key Features

- **Bilingual Model**: Supports both Korean and English, with a focus on scientific and technical texts.
- **Post-training**: The model undergoes post-training via instruction tuning (IT) and direct preference optimization (DPO) using a filtered, high-quality bilingual dataset that includes scientific data and publicly available resources. This ensures adaptability to evolving scientific and technological content.
- **Base Model**: Built upon *KISTI-KONI/KONI-4B-base-20250819*, KONI-4B-instruct undergoes post-training for superior performance on both general and scientific benchmarks.
- **Training Environment**: Trained on *24* H200 GPUs at the KISTI supercomputer, optimizing both speed and quality during development.
- **Dataset**: Utilizes a high-quality and balanced dataset of 9 billion instruction-following pairs, comprising scientific texts as well as publicly available bilingual data.
- **Data Optimization**: The post-training process involved testing a variety of data distributions (balanced, reasoning-enhanced, knowledge-enhanced, minimal Korean settings, etc.) and selecting the optimal combination for training.
- **Enhanced Performance**: KONI-4B-instruct, developed through instruction tuning of the KONI-4B-base model, delivers superior performance compared to other similarly-sized models.

---

## Model Performance

KONI-4B-instruct has demonstrated strong performance on a variety of scientific benchmarks, outperforming several other 4B-sized pretrained models. Here is a comparison of KONI-4B-instruct’s performance across various benchmarks including scientific and technological benchmarks:

| Rank | Model                                                        | KMMLU | KMMLU-Hard | KMMLU-Direct | KoBEST | HAERAE | kormedmcqa | MMLU  | ARC_easy | ARC_challenge | Hellaswag | ScholarBench-MC | AidaBench-MC | average |
|------|--------------------------------------------------------------|-------|------------|------------|--------|--------|------------|-------|----------|---------------|-----------|-----------------|--------------|---------|
| 1    | Qwen/Qwen3-8B                                                | 0.5500 | 0.2900     | 0.5558     | 0.7800 | 0.6700 | 0.3750     | 0.7400 | 0.8700   | 0.6400        | 0.5700    | 0.7094          | 0.7314       | 0.623462  |
| 2    | kakaocorp/kanana-1.5-8b-base                                 | 0.4800 | 0.2500     | 0.4872     | 0.6200 | 0.8200 | 0.5910     | 0.6300 | 0.8300   | 0.5600        | 0.6000    | 0.6800          | 0.7548       | 0.608580  |
| 3    | LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct                         | 0.4700 | 0.2300     | 0.4532     | 0.5900 | 0.7800 | 0.5310     | 0.6500 | 0.8300   | 0.5900        | 0.6200    | 0.6900          | 0.7057       | 0.594986  |
| 4    | **KISTI-KONI/KONI-4B-instruct-20250901**                     | **0.4188** | **0.2110** | **0.4194** | **0.7393** | **0.7333** | **0.4719** | **0.5823** | **0.8342** | **0.5452** | **0.5783** | **0.6980** | **0.6274** | **0.571603** |
| 5    | kakaocorp/kanana-1.5-2.1b-instruct-2505                      | 0.4200 | 0.2100     | 0.4247     | 0.7700 | 0.7900 | 0.5224     | 0.5500 | 0.8000   | 0.5300        | 0.5100    | 0.6630          | 0.6688       | 0.571577  |
| 6    | **KISTI-KONI/KONI-4B-base-20250819**                         | **0.4300** | **0.2100** | **0.4349** | **0.7300** | 0.6600 | **0.4800** | **0.5800** | **0.8200** | **0.5200** | **0.5700** | **0.6800** | **0.6147** | **0.560803** |
| 7    | LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct                         | 0.4300 | 0.2100     | 0.4379     | 0.7400 | 0.6600 | 0.4842     | 0.5900 | 0.7700   | 0.5000        | 0.5400    | 0.6900          | 0.6511       | 0.558603  |
| 8    | KISTI-KONI/KONI-Llama3.1-8B-Instruct-20241024                | 0.4000 | 0.2000     | 0.4100     | 0.5600 | 0.6400 | 0.4905     | 0.6300 | 0.8300   | 0.5400        | 0.6100    | 0.6980          | 0.6722       | 0.556725  |
| 9    | meta-llama/Llama-3.1-8B-Instruct                             | 0.4000 | 0.2000     | 0.4119     | 0.7000 | 0.4400 | 0.4789     | 0.6500 | 0.8400   | 0.5400        | 0.6100    | 0.6960          | 0.6709       | 0.553135  |
| 10    | google/gemma-3-4b-pt                                         | 0.3980 | 0.1998     | 0.3966     | 0.6990 | 0.6672 | 0.4726     | 0.5964 | 0.8300   | 0.5435        | 0.5763    | 0.6670          | 0.5886       | 0.552906  |
| 11   | google/gemma-3-4b-it                                         | 0.3900 | 0.2100     | 0.3904     | 0.7200 | 0.5900 | 0.4400     | 0.5800 | 0.8400   | 0.5600        | 0.5600    | 0.6990          | 0.6013       | 0.548388  |
| 12   | saltlux/Ko-Llama3-Luxia-8B                                   | 0.3800 | 0.2100     | 0.3935     | 0.7100 | 0.6800 | 0.4320     | 0.5500 | 0.8000   | 0.4800        | 0.5600    | 0.6650          | 0.6109       | 0.539283  |
| 13   | MLP-KTLim/llama-3-Korean-Bllossom-8B                         | 0.3700 | 0.2200     | 0.3738     | 0.5500 | 0.4700 | 0.4163     | 0.6400 | 0.8400   | 0.5700        | 0.5900    | 0.6525          | 0.5862       | 0.523239  |
| 14   | kakaocorp/kanana-1.5-2.1b-base                               | 0.3900 | 0.2400     | 0.4502     | 0.6200 | 0.5700 | 0.5138     | 0.4700 | 0.7300   | 0.4400        | 0.4500    | 0.6500          | 0.6478       | 0.514315  |
| 15   | naver-hyperclovax/HyperCLOVAX-SEED-Text-Instruct-1.5B        | 0.3900 | 0.2400     | 0.3524     | 0.6400 | 0.5700 | 0.3550     | 0.4700 | 0.7300   | 0.4400        | 0.4500    | 0.5950          | 0.5450       | 0.481447  |
| 16   | naver-hyperclovax/HyperCLOVAX-SEED-Text-Instruct-0.5B        | 0.3700 | 0.2200     | 0.3798     | 0.6200 | 0.5600 | 0.3383     | 0.4400 | 0.7200   | 0.3900        | 0.4100    | 0.5600          | 0.5173       | 0.460449  |
| 17   | mistralai/Mistral-7B-v0.3                                    | 0.3700 | 0.2200     | 0.3739     | 0.6300 | 0.3700 | 0.3735     | 0.6200 | 0.8300   | 0.5500        | 0.6200    | 0.5440          | 0.4257       | 0.413117  |
| 18   | google/gemma-3-1b-it                                         | 0.3069 | 0.2400     | 0.2935     | 0.3556 | 0.5987 | 0.2761     | 0.3970 | 0.6620   | 0.3430        | 0.4204    | 0.5720          | 0.3972       | 0.390038  |
| 19   | google/gemma-3-1b-pt                                         | 0.2582 | 0.2456     | 0.2556     | 0.5569 | 0.1952 | 0.1964     | 0.2641 | 0.7146   | 0.3541        | 0.4703    | 0.2192          | 0.1980       | 0.327362  |
| 20   | etri-lirs/eagle-3b-preview                                   | 0.1600 | 0.2100     | 0.1617     | 0.5100 | 0.1900 | 0.1804     | 0.2500 | 0.5700   | 0.2400        | 0.3700    | 0.2678          | 0.2224       | 0.236846  |

![image/png](https://cdn-uploads.huggingface.co/production/uploads/67a07b7b89e01818543f9ec8/YARkt9n6sTa9fZdXUA2lV.png)

As shown, **KISTI-KONI/KONI-4B-instruct-20250901** is the top-performing model in the 4B-size instruction-tuned model category, outperforming *google/gemma-3-4b-it* and *KISTI-KONI/KONI-4B-base-20250819*.

---

## Strengths & Use Cases

- **Domain-Specific Excellence**: KONI-4B-instruct excels at tasks involving scientific literature, technological content, and complex reasoning. It is ideal for research, academic analysis, and specialized problem-solving.
- **Bilingual Advantage**: The model’s bilingual nature enables handling diverse datasets and generating high-quality responses in both English and Korean, especially in bilingual scientific collaborations.
- **Benchmark Performance**: KONI-4B-instruct has shown superior performance in benchmarks such as *KMMLU*, *kormedmcqa*, and *ScholarBench-MC*, proving its robustness in knowledge-intensive tasks.

---

## Usage

```sh
$ pip install -U transformers
```

```python
from transformers import pipeline
import torch

pipe = pipeline("text-generation", model="KISTI-KONI/KONI-4B-instruct-20250901", device="cuda", torch_dtype=torch.bfloat16)

messages = [
    [
        {
            "role": "system",
            "content": [{"type": "text", "text": "You are a helpful assistant."},]
        },
        {
            "role": "user",
            "content": [{"type": "text", "text": "슈퍼컴퓨터에 대해서 설명해줘."},]
        },
    ],
]

output = pipe(
    messages,
    max_new_tokens=512,
    eos_token_id=[pipe.tokenizer.eos_token_id, pipe.tokenizer.convert_tokens_to_ids("<end_of_turn>")]
)
```


## Citation

If you use this model in your work, please cite it as follows:

```bibtex
@article{KISTI-KONI/KONI-4B-instruct-20250901,
  title={KISTI-KONI/KONI-4B-instruct-20250901},
  author={KISTI},
  year={2025},
  url={https://huggingface.co/KISTI-KONI/KONI-4B-instruct-20250901}
}
```

---

## Acknowledgements
- This research was supported by the Korea Institute of Science and Technology Information (KISTI) in 2025 (No. (KISTI) K25L1M1C1), aimed at developing KONI (KISTI Open Neural Intelligence), a large language model specialized in science and technology.
- This work also benefited from the resources and technical support provided by the National Supercomputing Center (KISTI).

---

## References
- https://huggingface.co/KISTI-KONI/KONI-4B-base-20250819
