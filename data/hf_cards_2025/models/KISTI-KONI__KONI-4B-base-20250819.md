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

# KISTI-KONI/KONI-4B-base-20250819

## Model Description

**KONI (KISTI Open Neural Intelligence)** is a large language model developed by the Korea Institute of Science and Technology Information (KISTI). Designed specifically for the scientific and technological domains, KONI excels in both Korean and English, making it an ideal tool for tasks requiring specialized knowledge in these areas.

---

## Key Features

- **Bilingual Model**: Supports both Korean and English, with a focus on scientific and technical texts.
- **Continual Pretraining**: The model is continual pretrained on a filtered, high-quality bilingual corpus that includes scientific data and publicly available resources. This ensures adaptability to evolving scientific and technological content.
- **Base Model**: Built upon *google/gemma-3-4b-pt*, KONI-4B-base undergoes continual pretraining for superior performance on both general LLM benchmark and scientific benchmarks.
- **Training Environment**: Trained on *24* H200 GPUs at the KISTI supercomputer, optimizing both speed and quality during development.
- **Corpus**: Utilizes a high-quality, filtered corpus of **OOO B tokens**, comprising scientific texts as well as publicly available bilingual data.
- **Data Optimization**: The continual pretraining process involved testing a variety of data distributions (balanced, reasoning-enhanced, knowledge-enhanced, minimal Korean settings, etc.), followed by selection of the optimal combination for training.
- **Enhanced Performance**: KONI-4B-base delivers excellent performance, especially compared to other 4B-sized pretrained models, even though it is not instruction-tuned. An instruction-tuned version is expected soon, which will further improve its performance.

---

## Model Performance

KONI-4B-base has demonstrated strong performance on a variety of scientific benchmarks, outperforming several other 4B-sized pretrained models. Here is a comparison of KONI-4B-base’s performance across various benchmarks including scientific and technological benchmarks:

| Rank | Model                                                        | KMMLU | KMMLU-Hard | KoBEST | kormedmcqa | MMLU  | ARC_easy | ARC_challenge | Hellaswag | ScholarBench-MC | AidaBench-MC | average |
|------|--------------------------------------------------------------|-------|------------|--------|------------|-------|----------|---------------|-----------|-----------------|--------------|---------|
| 1    | Qwen/Qwen3-8B                                                | 0.5500 | 0.2900     | 0.7800 | 0.3750     | 0.7400 | 0.8700   | 0.6400        | 0.5700    | 0.7094          | 0.7314       | 0.6256  |
| 2    | kakaocorp/kanana-1.5-8b-base                                 | 0.4800 | 0.2500     | 0.6200 | 0.5910     | 0.6300 | 0.8300   | 0.5600        | 0.6000    | 0.6800          | 0.7548       | 0.5996  |
| 3    | LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct                         | 0.4700 | 0.2300     | 0.5900 | 0.5310     | 0.6500 | 0.8300   | 0.5900        | 0.6200    | 0.6900          | 0.7057       | 0.5907  |
| 4    | kakaocorp/kanana-1.5-2.1b-instruct-2505                      | 0.4200 | 0.2100     | 0.7700 | 0.5224     | 0.5500 | 0.8000   | 0.5300        | 0.5100    | 0.6630          | 0.6688       | 0.5644  |
| 5    | **KISTI-KONI/KONI-4B-base-20250819**                            | **0.4300** | **0.2100** | **0.7300** | **0.4800** | **0.5800** | **0.8200** | **0.5200** | **0.5700** | **0.6800** | **0.6147** | **0.5635** |
| 6    | KISTI-KONI/KONI-Llama3.1-8B-Instruct-20241024                | 0.4000 | 0.2000     | 0.5600 | 0.4905     | 0.6300 | 0.8300   | 0.5400        | 0.6100    | 0.6980          | 0.6722       | 0.5631  |
| 7    | LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct                         | 0.4300 | 0.2100     | 0.7400 | 0.4842     | 0.5900 | 0.7700   | 0.5000        | 0.5400    | 0.6900          | 0.6511       | 0.5605  |
| 8    | google/gemma-3-4b-pt                                         | 0.3980 | 0.1998     | 0.6990 | 0.4726     | 0.5964 | 0.8300   | 0.5435        | 0.5763    | 0.6670          | 0.5886       | 0.5571  |
| 9    | meta-llama/Llama-3.1-8B-Instruct                             | 0.4000 | 0.2000     | 0.7000 | 0.4789     | 0.6500 | 0.8400   | 0.5400        | 0.6100    | 0.6960          | 0.6709       | 0.5786  |
| 10   | google/gemma-3-4b-it                                         | 0.3900 | 0.2100     | 0.7200 | 0.4400     | 0.5800 | 0.8400   | 0.5600        | 0.5600    | 0.6990          | 0.6013       | 0.5600  |
| 11   | saltlux/Ko-Llama3-Luxia-8B                                   | 0.3800 | 0.2100     | 0.7100 | 0.4320     | 0.5500 | 0.8000   | 0.4800        | 0.5600    | 0.6650          | 0.6109       | 0.5398  |
| 12   | MLP-KTLim/llama-3-Korean-Bllossom-8B                         | 0.3700 | 0.2200     | 0.5500 | 0.4163     | 0.6400 | 0.8400   | 0.5700        | 0.5900    | 0.6525          | 0.5862       | 0.5435  |
| 13   | kakaocorp/kanana-1.5-2.1b-base                               | 0.3900 | 0.2400     | 0.6200 | 0.5138     | 0.4700 | 0.7300   | 0.4400        | 0.4500    | 0.6500          | 0.6478       | 0.5152  |
| 14   | mistralai/Mistral-7B-v0.3                                    | 0.3700 | 0.2200     | 0.6300 | 0.3735     | 0.6200 | 0.8300   | 0.5500        | 0.6200    | 0.5440          | 0.4257       | 0.5183  |
| 15   | naver-hyperclovax/HyperCLOVAX-SEED-Text-Instruct-1.5B        | 0.3900 | 0.2400     | 0.6400 | 0.3550     | 0.4700 | 0.7300   | 0.4400        | 0.4500    | 0.5950          | 0.5450       | 0.4855  |
| 16   | naver-hyperclovax/HyperCLOVAX-SEED-Text-Instruct-0.5B        | 0.3700 | 0.2200     | 0.6200 | 0.3383     | 0.4400 | 0.7200   | 0.3900        | 0.4100    | 0.5600          | 0.5173       | 0.4586  |
| 17   | google/gemma-3-1b-it                                         | 0.3069 | 0.2400     | 0.3556 | 0.2761     | 0.3970 | 0.6620   | 0.3430        | 0.4204    | 0.5720          | 0.3972       | 0.3776  |
| 18   | google/gemma-3-1b-pt                                         | 0.2582 | 0.2456     | 0.5569 | 0.1964     | 0.2641 | 0.7146   | 0.3541        | 0.4703    | 0.2192          | 0.1980       | 0.3477  |
| 19   | etri-lirs/eagle-3b-preview                                   | 0.1600 | 0.2100     | 0.5100 | 0.1804     | 0.2500 | 0.5700   | 0.2400        | 0.3700    | 0.2678          | 0.2224       | 0.2981  |


As shown, **KISTI-KONI/KONI-4B-base-20250819** is the top-performing model in the 4B-size pretrained model category, outstanding *google/gemma-3-4b-pt* and *KISTI-KONI/KONI-Llama3.1-8B-Instruct*. While this version is not instruction-tuned, it offers exceptional results in scientific and technological domains. An upcoming instruction-tuned version is expected to further enhance its performance. 
**Stay tuned for updates!**

---

## Strengths & Use Cases

- **Domain-Specific Excellence**: KONI-4B-base excels at tasks involving scientific literature, technological content, and complex reasoning. It is ideal for research, academic analysis, and specialized problem-solving.
- **Bilingual Advantage**: The model’s bilingual nature enables handling diverse datasets and generating high-quality responses in both English and Korean, especially in bilingual scientific collaborations.
- **Benchmark Performance**: KONI-4B-base has shown superior performance in benchmarks such as *KMMLU*, *kormedmcqa*, and *ScholarBench-MC*, proving its robustness in knowledge-intensive tasks.

---

## Citation

If you use this model in your work, please cite it as follows:

```bibtex
@article{KISTI-KONI/KONI-4B-base-20250819,
  title={KISTI-KONI/KONI-4B-base-20250819},
  author={KISTI},
  year={2025},
  url={https://huggingface.co/KISTI-KONI/KONI-4B-base-20250819}
}
```

---

## Acknowledgements
- This research was supported by the Korea Institute of Science and Technology Information (KISTI) in 2025 (No. (KISTI) K25L1M1C1), aimed at developing KONI (KISTI Open Neural Intelligence), a large language model specialized in science and technology.
- This work also benefited from the resources and technical support provided by the National Supercomputing Center (KISTI).

---

## References
- https://huggingface.co/google/gemma-3-4b-pt
