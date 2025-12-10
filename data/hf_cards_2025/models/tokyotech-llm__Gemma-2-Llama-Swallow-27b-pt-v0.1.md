---
language:
- en
- ja
library_name: transformers
pipeline_tag: text-generation
license:
- gemma
- llama3.3
---

# Gemma-2-Llama-Swallow

Gemma-2-Llama-Swallow series was built by continual pre-training on the [gemma-2](https://huggingface.co/collections/google/gemma-2-release-667d6600fd5220e7b967f315) models.
Gemma 2 Swallow enhanced the Japanese language capabilities of the original Gemma 2 while retaining the English language capabilities.
We use approximately 200 billion tokens that were sampled from a large Japanese web corpus (Swallow Corpus Version 2), Japanese and English Wikipedia articles, and mathematical and coding contents, etc (see the Training Datasets section of the base model) for continual pre-training.
The instruction-tuned models (it) were built by supervised fine-tuning (SFT) on the synthetic data specially built for Japanese.
See the Swallow Model Index section to find other model variants. Built with Gemma. Built with Llama.

# Release History

- **May 19, 2025**: Released [Gemma-2-Llama-Swallow-2b-pt-v0.1](https://huggingface.co/tokyotech-llm/Gemma-2-Llama-Swallow-2b-pt-v0.1),
  [Gemma-2-Llama-Swallow-9b-pt-v0.1](https://huggingface.co/tokyotech-llm/Gemma-2-Llama-Swallow-9b-pt-v0.1),
  [Gemma-2-Llama-Swallow-27b-pt-v0.1](https://huggingface.co/tokyotech-llm/Gemma-2-Llama-Swallow-27b-pt-v0.1),
  [Gemma-2-Llama-Swallow-2b-it-v0.1](https://huggingface.co/tokyotech-llm/Gemma-2-Llama-Swallow-2b-it-v0.1),
  [Gemma-2-Llama-Swallow-9b-it-v0.1](https://huggingface.co/tokyotech-llm/Gemma-2-Llama-Swallow-9b-it-v0.1),
  and [Gemma-2-Llama-Swallow-27b-it-v0.1](https://huggingface.co/tokyotech-llm/Gemma-2-Llama-Swallow-27b-it-v0.1).

## Swallow Model Index

| Model | gemma-2-swallow v0.1                                                                     | gemma-2-swallow-it v0.1                                                                  |
| ----- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| 2B    | [🤗 HuggingFace](https://huggingface.co/tokyotech-llm/Gemma-2-Llama-Swallow-2b-pt-v0.1)  | [🤗 HuggingFace](https://huggingface.co/tokyotech-llm/Gemma-2-Llama-Swallow-2b-it-v0.1)  |
| 9B    | [🤗 HuggingFace](https://huggingface.co/tokyotech-llm/Gemma-2-Llama-Swallow-9b-pt-v0.1)  | [🤗 HuggingFace](https://huggingface.co/tokyotech-llm/Gemma-2-Llama-Swallow-9b-it-v0.1)  |
| 27B   | [🤗 HuggingFace](https://huggingface.co/tokyotech-llm/Gemma-2-Llama-Swallow-27b-pt-v0.1) | [🤗 HuggingFace](https://huggingface.co/tokyotech-llm/Gemma-2-Llama-Swallow-27b-it-v0.1) |

![logo](./logo.png)

The website [https://swallow-llm.github.io/](https://swallow-llm.github.io/index.en.html) provides large language models developed by the Swallow team.

## Model Details

- **Model type**: Please refer to [Gemma 2 paper](https://arxiv.org/abs/2408.00118) for details on the model architecture.
- **Language(s)**: Japanese English
- **Library**: [maxtext](https://github.com/AI-Hypercomputer/maxtext)
- **Tokenizer**: Please refer to [Gemma 2 paper](https://arxiv.org/abs/2408.00118) for details on the tokenizer.
- **Contact**: swallow[at]nlp.c.titech.ac.jp

## Model Performance

### Japanese tasks

| Model                                               | JCom.  | JEMHopQA | NIILC   | JSQuAD  | XL-Sum  | MGSM   | WMT20-en-ja | WMT20-ja-en | JMMLU  | JHumanEval | Ja Avg |
| --------------------------------------------------- | ------ | -------- | ------- | ------- | ------- | ------ | ----------- | ----------- | ------ | ---------- | ------ |
|                                                     | 4-shot | 4-shot   | 4-shot  | 4-shot  | 1-shot  | 4-shot | 4-shot      | 4-shot      | 5-shot | 0-shot     |        |
|                                                     | EM acc | Char-F1  | Char-F1 | Char-F1 | ROUGE-2 | EM acc | BLEU        | BLEU        | EM acc | pass@1     |        |
| google/gemma-3-1b-pt                                | 0.237  | 0.410    | 0.252   | 0.631   | 0.079   | 0.024  | 0.150       | 0.136       | 0.239  | 0.073      | 0.223  |
| Qwen/Qwen2.5-1.5B                                   | 0.800  | 0.383    | 0.241   | 0.849   | 0.143   | 0.292  | 0.132       | 0.134       | 0.438  | 0.308      | 0.372  |
| google/gemma-2-2b                                   | 0.721  | 0.472    | 0.316   | 0.810   | 0.083   | 0.124  | 0.203       | 0.190       | 0.388  | 0.177      | 0.348  |
| rinna/gemma-2-baku-2b                               | 0.760  | 0.475    | 0.443   | 0.843   | 0.121   | 0.124  | 0.255       | 0.187       | 0.376  | 0.137      | 0.372  |
| **tokyotech-llm/Gemma-2-Llama-Swallow-2b-pt-v0.1**  | 0.830  | 0.509    | 0.549   | 0.863   | 0.119   | 0.172  | 0.261       | 0.195       | 0.461  | 0.251      | 0.421  |
| Qwen/Qwen2.5-3B                                     | 0.847  | 0.475    | 0.306   | 0.878   | 0.176   | 0.460  | 0.180       | 0.167       | 0.529  | 0.404      | 0.442  |
| google/gemma-3-4b-pt                                | 0.851  | 0.432    | 0.410   | 0.887   | 0.139   | 0.248  | 0.230       | 0.205       | 0.499  | 0.273      | 0.417  |
| Qwen/Qwen2.5-7B                                     | 0.924  | 0.459    | 0.426   | 0.907   | 0.216   | 0.616  | 0.229       | 0.199       | 0.634  | 0.507      | 0.512  |
| tokyotech-llm/Llama-3.1-Swallow-8B-v0.2             | 0.911  | 0.510    | 0.627   | 0.892   | 0.198   | 0.464  | 0.296       | 0.233       | 0.525  | 0.336      | 0.499  |
| google/gemma-2-9b                                   | 0.904  | 0.573    | 0.524   | 0.898   | 0.168   | 0.456  | 0.269       | 0.236       | 0.623  | 0.345      | 0.500  |
| **tokyotech-llm/Gemma-2-Llama-Swallow-9b-pt-v0.1**  | 0.950  | 0.643    | 0.677   | 0.897   | 0.187   | 0.560  | 0.304       | 0.247       | 0.650  | 0.462      | 0.558  |
| google/gemma-3-12b-pt                               | 0.787  | 0.563    | 0.569   | 0.911   | 0.194   | 0.584  | 0.288       | 0.244       | 0.659  | 0.385      | 0.518  |
| google/gemma-2-27b                                  | 0.936  | 0.553    | 0.573   | 0.916   | 0.194   | 0.596  | 0.295       | 0.251       | 0.659  | 0.490      | 0.546  |
| **tokyotech-llm/Gemma-2-Llama-Swallow-27b-pt-v0.1** | 0.958  | 0.660    | 0.671   | 0.924   | 0.200   | 0.644  | 0.321       | 0.255       | 0.679  | 0.629      | 0.594  |
| google/gemma-3-27b-pt                               | 0.944  | 0.582    | 0.627   | 0.915   | 0.210   | 0.704  | 0.301       | 0.255       | 0.724  | 0.473      | 0.574  |
| Qwen/Qwen2.5-32B                                    | 0.961  | 0.561    | 0.538   | 0.925   | 0.228   | 0.808  | 0.271       | 0.233       | 0.751  | 0.637      | 0.591  |

### English tasks

| Model                                               | OpenBookQA | TriviaQA | HellaSWAG | SQuAD2.0 | XWINO  | MMLU   | GSM8K  | MATH       | BBH        | HumanEval | En Avg |
| --------------------------------------------------- | ---------- | -------- | --------- | -------- | ------ | ------ | ------ | ---------- | ---------- | --------- | ------ |
|                                                     | 4-shot     | 4-shot   | 4-shot    | 4-shot   | 4-shot | 5-shot | 4-shot | 4-shot     | 3-shot     | 0-shot    |        |
|                                                     | Acc        | EM acc   | Acc       | EM acc   | Acc    | Acc    | EM acc | CoT EM Acc | CoT EM Acc | pass@1    |        |
| google/gemma-3-1b-pt                                | 0.304      | 0.358    | 0.471     | 0.501    | 0.832  | 0.262  | 0.016  | 0.008      | 0.276      | 0.070     | 0.310  |
| Qwen/Qwen2.5-1.5B                                   | 0.342      | 0.397    | 0.499     | 0.506    | 0.851  | 0.610  | 0.611  | 0.314      | 0.413      | 0.356     | 0.490  |
| google/gemma-2-2b                                   | 0.342      | 0.552    | 0.552     | 0.501    | 0.890  | 0.530  | 0.249  | 0.176      | 0.415      | 0.188     | 0.439  |
| rinna/gemma-2-baku-2b                               | 0.314      | 0.475    | 0.533     | 0.501    | 0.881  | 0.493  | 0.168  | 0.110      | 0.376      | 0.150     | 0.400  |
| **tokyotech-llm/Gemma-2-Llama-Swallow-2b-pt-v0.1**  | 0.312      | 0.435    | 0.516     | 0.501    | 0.871  | 0.538  | 0.275  | 0.144      | 0.384      | 0.286     | 0.426  |
| Qwen/Qwen2.5-3B                                     | 0.360      | 0.504    | 0.553     | 0.541    | 0.872  | 0.657  | 0.580  | 0.440      | 0.442      | 0.387     | 0.534  |
| google/gemma-3-4b-pt                                | 0.360      | 0.603    | 0.576     | 0.502    | 0.895  | 0.596  | 0.376  | 0.258      | 0.495      | 0.351     | 0.501  |
| Qwen/Qwen2.5-7B                                     | 0.392      | 0.601    | 0.600     | 0.618    | 0.888  | 0.742  | 0.832  | 0.510      | 0.562      | 0.554     | 0.630  |
| tokyotech-llm/Llama-3.1-Swallow-8B-v0.2             | 0.382      | 0.651    | 0.596     | 0.513    | 0.904  | 0.622  | 0.521  | 0.228      | 0.605      | 0.366     | 0.539  |
| google/gemma-2-9b                                   | 0.382      | 0.718    | 0.626     | 0.506    | 0.907  | 0.706  | 0.688  | 0.338      | 0.704      | 0.390     | 0.597  |
| **tokyotech-llm/Gemma-2-Llama-Swallow-9b-pt-v0.1**  | 0.362      | 0.659    | 0.602     | 0.532    | 0.906  | 0.687  | 0.678  | 0.330      | 0.664      | 0.529     | 0.595  |
| google/gemma-3-12b-pt                               | 0.398      | 0.747    | 0.637     | 0.524    | 0.917  | 0.737  | 0.703  | 0.398      | 0.683      | 0.445     | 0.619  |
| google/gemma-2-27b                                  | 0.412      | 0.780    | 0.675     | 0.549    | 0.921  | 0.754  | 0.757  | 0.438      | 0.760      | 0.508     | 0.655  |
| **tokyotech-llm/Gemma-2-Llama-Swallow-27b-pt-v0.1** | 0.414      | 0.756    | 0.652     | 0.597    | 0.915  | 0.749  | 0.732  | 0.416      | 0.765      | 0.658     | 0.665  |
| google/gemma-3-27b-pt                               | 0.414      | 0.809    | 0.667     | 0.618    | 0.923  | 0.780  | 0.801  | 0.520      | 0.732      | 0.507     | 0.677  |
| Qwen/Qwen2.5-32B                                    | 0.406      | 0.664    | 0.656     | 0.668    | 0.913  | 0.832  | 0.718  | 0.600      | 0.717      | 0.523     | 0.670  |

## Evaluation Benchmarks

The evaluation script can be found at [swallow-llm/swallow-evaluation](https://github.com/swallow-llm/swallow-evaluation), tagged as `v202411`.

### Japanese evaluation benchmarks

We used llm-jp-eval(v1.3.0), JP Language Model Evaluation Harness(commit #9b42d41) and Code Generation LM Evaluation Harness(commit #0261c52). The details are as follows:

- Multiple-choice question answering (JCommonsenseQA [Kurihara et al., 2022])
- Open-ended question answering (JEMHopQA [Ishii et al., 2024])
- Open-ended question answering (NIILC [関根, 2003])
- Machine reading comprehension (JSQuAD [Kurihara et al., 2022])
- Automatic summarization (XL-Sum [Hasan et al., 2021])
- Machine translation (WMT2020 ja-en [Barrault et al., 2020])
- Machine translation (WMT2020 en-ja [Barrault et al., 2020])
- Mathematical reasoning (MGSM [Shi et al., 2023])
- Academic exams (JMMLU [尹ら, 2024])
- Code generation (JHumanEval [佐藤ら, 2024])

### English evaluation benchmarks

We used the Language Model Evaluation Harness(v.0.4.2) and Code Generation LM Evaluation Harness(commit #0261c52). The details are as follows:

- Multiple-choice question answering (OpenBookQA [Mihaylov et al., 2018])
- Open-ended question answering (TriviaQA [Joshi et al., 2017])
- Machine reading comprehension (SQuAD2 [Rajpurkar et al., 2018])
- Commonsense reasoning (XWINO [Tikhonov and Ryabinin, 2021])
- Natural language inference (HellaSwag [Zellers et al., 2019])
- Mathematical reasoning (GSM8K [Cobbe et al., 2021])
- Mathematical reasoning (MATH [Hendrycks et al., 2022][Lightman et al., 2024])
- Reasoning (BBH (BIG-Bench-Hard) [Suzgun et al., 2023])
- Academic exams (MMLU [Hendrycks et al., 2021])
- Code generation (HumanEval [Chen et al., 2021])

## Training Datasets

### Continual Pre-Training

The following datasets were used for continual pre-training.

- [Cosmopedia](https://huggingface.co/datasets/HuggingFaceTB/cosmopedia)
- [Dclm-baseline-1.0](https://huggingface.co/datasets/mlfoundations/dclm-baseline-1.0)
- [English Wikipedia](https://dumps.wikimedia.org/other/cirrussearch)
- [FineMath-4+](https://huggingface.co/datasets/HuggingFaceTB/finemath)
- [Japanese Wikipedia](https://dumps.wikimedia.org/other/cirrussearch)
- [Filtered Laboro ParaCorpus](https://github.com/laboroai/Laboro-ParaCorpus)
- [Swallow Corpus Version 2](https://arxiv.org/abs/2404.17733) (filtered using [Swallow Education Classifier(Wiki-based)](https://huggingface.co/tokyotech-llm/edu-classifier))
- [Swallow Corpus Version 2](https://arxiv.org/abs/2404.17733) (filtered using [Swallow Education Classifier](https://huggingface.co/tokyotech-llm/edu-classifier))
- [Swallow Corpus Version 2](https://arxiv.org/abs/2404.17733) (synthetic QA-format)
- Swallow Code Version 0.3 (filtering from [The Stack v2 train smol ids](https://huggingface.co/datasets/bigcode/the-stack-v2-train-smol-ids) and then refactoring with Llama-3.3-70B-Instruct)

### Swallow Corpus Version 2

We built the Swallow Corpus by extracting high-quality Japanese texts from Common Crawl. In Version 2, we expanded the scope of the Common Crawl collection and modified the pipeline sequence to enable more flexible quality filtering.
For Llama 3.1 Swallow v0.2, we further refined our quality filtering and data sampling strategies, resulting in an even higher-quality selection of Japanese texts for pre-training.
For Gemma 2 Swallow v0.1, we generated synthetic QA-format text by using Gemma 2 27B IT to paraphrase educational web documents from our corpus

Further details of the methodology and analysis will be provided in a forthcoming paper.

### Swallow Code Version 0.3

We built the Swallow Code Version 0.3 by filtering from the stack v2 train smol ids and then refactoring with Llama-3.3-70B-Instruct.
In filtering, we removed the code texts with syntax errors or scored below seven by pylint. We have already released the filtered version as [Swallow Code Version 0.1](https://huggingface.co/datasets/tokyotech-llm/swallow-code-v0.1).
In refactoring, we gave a prompt to Llama-3.3-70B-Instruct to follow [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html) and coding best practices.

## Risks and Limitations

The models released here are still in the early stages of our research and development and have not been tuned to ensure outputs align with human intent and safety considerations.

## Acknowledgements

We thank Google DeepMind for releasing Gemma 2 under a generous open license.

We received various support, including:

- AIST project: "Research and Development of Foundation Models for Generative AI in the Physical Domain"
- NEDO project: "Development of Artificial Intelligence Application Technology to Support Judgment in Design Risk Assessment Work Based on the Perspective of Skilled Persons" (JPNP18002) of "Development of Integration Technology as the Core of Next Generation Artificial Intelligence and Robotics"
- MEXT project: "Formation of R&D center to ensure transparency and reliability of generative AI models"
- AIST program: [Large Generative AI Development Support Program](https://abci.ai/en/link/lfm_support_program.html)
- TPU Research Cloud

## License

[Gemma Terms of Use](https://ai.google.dev/gemma/terms) and [META LLAMA 3.3 COMMUNITY LICENSE](https://www.llama.com/llama3_3/license/)

## Authors

Team members:

- From [Institute of Science Tokyo Okazaki Laboratory](https://www.nlp.c.titech.ac.jp/index.en.html), the following members:
  - [Naoaki Okazaki](https://www.chokkan.org/index.ja.html)
  - [Sakae Mizuki](https://s-mizuki-nlp.github.io/)
  - [Youmi Ma](https://www.nlp.c.titech.ac.jp/member/youmi.en.html)
  - [Koki Maeda](https://sites.google.com/view/silviase)
  - [Kakeru Hattori](https://aya-se.vercel.app/)
  - [Masanari Ohi](https://sites.google.com/view/masanariohi)
  - [Hinari Shimada](https://hinarishimada.github.io/portfolio)
  - [Taihei Shiotani](https://github.com/inatoihs)
  - [Koshiro Saito](https://sites.google.com/view/koshiro-saito)
- From [Institute of Science Tokyo YOKOTA Laboratory](https://www.rio.gsic.titech.ac.jp/en/index.html), the following members:
  - [Rio Yokota](https://twitter.com/rioyokota)
  - [Kazuki Fujii](https://twitter.com/okoge_kaz)
  - [Taishi Nakamura](https://twitter.com/Setuna7777_2)
  - [Takumi Okamoto](https://www.linkedin.com/in/takumi-okamoto)
  - [Ishida Shigeki](https://www.wantedly.com/id/reborn27)
  - [Yukito Tajima](https://www.linkedin.com/in/yukito-tajima-51bbb2299)
  - [Masaki Kawamura](https://x.com/Masakichi333210)
- From [Artificial Intelligence Research Center, AIST, Japan](https://www.airc.aist.go.jp/en/teams/), the following members:
  - [Hiroya Takamura](https://sites.google.com/view/hjtakamura)

## How to cite

If you find our work is helpful, please feel free to cite these papers.

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
```

### References

```tex
@misc{gemmateam2024gemma2improvingopen,
      title={Gemma 2: Improving Open Language Models at a Practical Size},
      author={Gemma Team},
      year={2024},
      eprint={2408.00118},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2408.00118},
}
```
