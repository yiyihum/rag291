---
library_name: transformers
license: apache-2.0
---

# II-Medical-8B-1706

<div style="display: flex; justify-content: center;">
    <img src="https://cdn-uploads.huggingface.co/production/uploads/6389496ff7d3b0df092095ed/73Y-oDmehp0eJ2HWrfn3V.jpeg" width="800">
</div>

## I. Model Overview

II-Medical-8B-1706 is the newest advanced large language model developed by Intelligent Internet, specifically engineered to enhance AI-driven medical reasoning. Following the positive reception of our previous [II-Medical-8B](https://huggingface.co/Intelligent-Internet/II-Medical-8B), this new iteration significantly advances the capabilities of medical question answering, 

We also provide the static quants versions of II-Medical-8B-1706 [here](https://huggingface.co/Intelligent-Internet/II-Medical-8B-1706-GGUF)

## II. Training Methodology

We collected and generated a comprehensive set of reasoning datasets for the medical domain and performed SFT fine-tuning on the **Qwen/Qwen3-8B** model. Following this, we further optimized the SFT model by training DAPO on a hard-reasoning dataset to boost performance.

For SFT stage we using the hyperparameters: 

- Max Length: 16378.
- Batch Size: 128.
- Learning-Rate: 5e-5.
- Number Of Epoch: 6.

For the Reinforcement Learning (RL) stage, we designed a two-stage training process. The first stage focuses on enhancing the model's reasoning capabilities for complex medical questions. The second stage ensures that the model's responses prioritize safety and helpfulness. Both stages utilize the following configuration:

- Max prompt length: 2048 tokens.
- Max response length: 12288 tokens.
- Overlong buffer: Enabled, 4096 tokens, penalty factor 1.0.
- Clip ratios: Low 0.2, High 0.28.
- Batch sizes: Train prompt 512, Generation prompt 1536, Mini-batch 32.
- Responses per prompt: 16.
- Temperature: 1.0, Top-p: 1.0, Top-k: -1 (vLLM rollout).
- Learning rate: 1e-6, Warmup steps: 10, Weight decay: 0.1.
- Loss aggregation: Token-mean.
- Gradient clipping: 1.0.
- Entropy coefficient: 0.

## III. Evaluation Results

![image/png](https://cdn-uploads.huggingface.co/production/uploads/63466107f7bd6326925fc770/kAyJOqZDuWRYkN3f1YWcS.png)

![image/png](https://cdn-uploads.huggingface.co/production/uploads/63466107f7bd6326925fc770/Sbgmwsefab7uDx5obvy18.png)

Our II-Medical-8B-1706 model achieved a 46.8% score on [HealthBench](https://openai.com/index/healthbench/), a comprehensive open-source benchmark evaluating the performance and safety of large language models in healthcare. This performance is comparable to MedGemma-27B from Google. We provide a comparison to models available in ChatGPT below.

<!-- ![image/jpeg](https://cdn-uploads.huggingface.co/production/uploads/61f2636488b9b5abbe184a8e/5r2O4MtzffVYfuUZJe5FO.jpeg) -->
Detailed result for HealthBench can be found [here](https://huggingface.co/datasets/Intelligent-Internet/OpenAI-HealthBench-II-Medical-8B-1706-GPT-4.1).

<!-- ![Model Benchmark](https://cdn-uploads.huggingface.co/production/uploads/6389496ff7d3b0df092095ed/uvporIhY4_WN5cGaGF1Cm.png) -->

We also evaluate on nine other medical QA benchmarks include MedMCQA, MedQA, PubMedQA, HealthBench, medical related questions from MMLU-Pro, small QA sets from Lancet and the New England
Journal of Medicine,  4 Options  and 5 Options splits from the MedBullets platform and MedXpertQA.

| Model                   | MedMC | MedQA | PubMed | MMLU-P | HealthBench | Lancet | MedB-4 | MedB-5 | MedX  | NEJM  | Avg   |
|--------------------------|-------|-------|--------|--------|------|--------|--------|--------|------|-------|-------|
| [HuatuoGPT-o1-72B](https://huggingface.co/FreedomIntelligence/HuatuoGPT-o1-72B)         | **76.76** | 88.85 | **79.90**   | 80.46  | 22.73 | 70.87   | 77.27  | 73.05  |23.53 |76.29  | 66.97 |
| [M1](https://huggingface.co/UCSC-VLAA/m1-7B-23K)                     | 62.54 | 75.81 | 75.80  | 65.86  | 15.51 | 62.62  | 63.64  | 59.74  |19.59 |64.34  | 56.55  |
| [Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B)                  | 66.53 | 81.38 | 73.9   | 77.85  | 42.27 | 66.26   | 68.83  | 62.66  |19.59 |69.65  | 62.89 |
| [Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B)                  | 74.18 | 88.92 | 76.1   | 80.7  | **47.08** | 72.33   | 72.27  | 71.42  |28.04 |76.94  | 68.80 |
| [MedGemma-27B-IT](https://huggingface.co/google/medgemma-27b-text-it)                  | 73.24 | 87.27 | 70.9   | 80.13  | 46.54| 70.14   | 75.32  | 73.37  |25.55 |76.28  | 67.87 |
| [II-Medical-8B](https://huggingface.co/Intelligent-Internet/II-Medical-8B)        | 71.57 | 87.90 | 78.7   |**80.46**  | 40.02| 70.38  | 78.25  | 72.07  |25.26 |73.13  |67.77  |
| [II-Medical-8B-1706](https://huggingface.co/Intelligent-Internet/II-Medical-8B-1706)            | 74.44 | **88.61** | 79.8   | 81.04  | 46.8 | 71.60  | **80.84**  | **74.67**  |**29.63** |77.61  | **70.5**  |

## IV. Dataset Curation

The training dataset comprises 2,197,741 samples from the following sources:

### 1. Public Medical Reasoning Datasets
- [General Medical Reasoning](https://huggingface.co/datasets/GeneralReasoning/GeneralThought-430K)
- [Medical-R1-Distill-Data](https://huggingface.co/datasets/FreedomIntelligence/Medical-R1-Distill-Data)
- [Medical-R1-Distill-Data-Chinese](https://huggingface.co/datasets/FreedomIntelligence/Medical-R1-Distill-Data-Chinese)
- [UCSC-VLAA/m23k-tokenized](https://huggingface.co/datasets/UCSC-VLAA/m23k-tokenized)

### 2. Synthetic Medical QA Data with Qwen3-235B-A22B (873,497 samples)

Generated from established medical datasets:

- [MedMcQA](https://huggingface.co/datasets/openlifescienceai/medmcqa)
- [MedQA](https://huggingface.co/datasets/bigbio/med_qa)
- [PubmedQA](https://huggingface.co/datasets/qiaojin/PubMedQA/viewer/pqa_unlabeled)
- [MedReason](https://huggingface.co/datasets/UCSC-VLAA/MedReason)

For each prompt, we generated 6-10 sampled responses, resulting in the comprehensive dataset mentioned above, and keep only the correct one.

### 3. Curated Medical R1 Traces

First we gather all the public R1 traces from:

- [PrimeIntellect/SYNTHETIC-1](https://huggingface.co/collections/PrimeIntellect/synthetic-1-67a2c399cfdd6c9f7fae0c37)
- [GeneralReasoning/GeneralThought-430K](https://huggingface.co/datasets/GeneralReasoning/GeneralThought-430K)
- [a-m-team/AM-DeepSeek-R1-Distilled-1.4M](https://arxiv.org/abs/2503.19633v1)
- [open-thoughts/OpenThoughts2-1M](https://huggingface.co/datasets/open-thoughts/OpenThoughts2-1M)
- [nvidia/Llama-Nemotron-Post-Training-Dataset](https://huggingface.co/datasets/nvidia/Llama-Nemotron-Post-Training-Dataset): Science subset only
- Other resources: [cognitivecomputations/dolphin-r1](https://huggingface.co/datasets/cognitivecomputations/dolphin-r1), [ServiceNow-AI/R1-Distill-SFT](https://huggingface.co/datasets/ServiceNow-AI/R1-Distill-SFT),...

All R1 reasoning traces were processed through a domain-specific pipeline as follows:

1. Embedding Generation: Prompts are embedded using sentence-transformers/all-MiniLM-L6-v2.

2. Clustering: Perform K-means clustering with 50,000 clusters.

3. Domain Classification:

    - For each cluster, select the 10 prompts nearest to the cluster center.
    - Classify the domain of each selected prompt using Qwen2.5-32b-Instruct.
    - Assign the cluster's domain based on majority voting among the classified prompts.

4. Domain Filtering: Keep only clusters labeled as Medical or Biology for the final dataset.


### General Medical & Instruction Following Dataset (1,025,903 samples)

We generated general medical instruction-following data and evaluated it with GPT-4o as an automatic judge. Only the high-scoring (i.e >= 8/10) responses compared to ground-truth answers were retained.

- 229,433 prompts from [Text-Book-QA-subset](https://huggingface.co/datasets/FreedomIntelligence/ApolloCorpus) 
- 276,079 prompts from [Text-Patient-QA-subset](https://huggingface.co/datasets/FreedomIntelligence/ApolloCorpus)
- 142,927 prompts from [Text-GuildLine-QA-subset](https://huggingface.co/datasets/FreedomIntelligence/ApolloCorpus)
- 215,647 prompts from [Chat-Doctor-QA](https://huggingface.co/datasets/lavita/ChatDoctor-HealthCareMagic-100k)
- 74,190 prompts from our Evol-Instruct medical dataset.

We also using 87,627 prompts from Subset Instruction-following [a-m-team/AM-Qwen3-Distilled](https://huggingface.co/datasets/a-m-team/AM-Qwen3-Distilled)


### Deduplicate
  
Response Deduplicate
   - Ngram: 4
   - Jacard Threshold: 0.7

### Data Decontamination

We using two step decontamination:
1. Following [open-r1](https://github.com/huggingface/open-r1) project: We decontaminate a dataset using 8-grams with the evaluation datasets.
2. After that, we using the fuzzy decontamination from [`s1k`](https://arxiv.org/abs/2501.19393) method with threshold 80%. 

**Our pipeline is carefully decontaminated with the evaluation datasets.**

## VII. Limitations and Considerations

- Dataset may contain inherent biases from source materials
- Medical knowledge requires regular updates
- Please note that **It’s not suitable for medical use.**

## V. How To Use
Our model can be utilized in the same manner as Qwen or Deepseek-R1-Distill models.

For instance, you can easily start a service using [vLLM](https://github.com/vllm-project/vllm):

```bash
vllm serve Intelligent-Internet/II-Medical-8B-1706
```

You can also easily start a service using [SGLang](https://github.com/sgl-project/sglang):

```bash
python -m sglang.launch_server --model Intelligent-Internet/II-Medical-8B-1706
```

## VI. Usage Guidelines

- Recommended Sampling Parameters: temperature = 0.6, top_p = 0.9
- When using, explicitly request step-by-step reasoning and format the final answer within \boxed{} (e.g., "Please reason step-by-step, and put your final answer within \boxed{}.").
## VII. Limitations and Considerations

- Dataset may contain inherent biases from source materials
- Medical knowledge requires regular updates
- Please note that **It’s not suitable for medical use.**


## VIII. Citation

```bib
@misc{2025II-Medical-8B-1706,
      title={II-Medical-8B: Medical Reasoning Model}, 
      author={Intelligent Internet},
      year={2025}
}
```