---
base_model:
- google/gemma-3-4b-pt
datasets:
- MBZUAI-Paris/Egyptian-SFT-Mixture
language:
- arz
library_name: transformers
license: gemma
pipeline_tag: text-generation
tags:
- conversational
extra_gated_button_content: Acknowledge license
---


# JAIS Initiative: Nile-Chat Models

## Model Overview
![overall benchmark scores](overall_benchmark_scores.png)
Nile-Chat is a family of open instruction-tuned models for Egyptian dialect, developed to handle both scripts commonly used in Egypt: Arabic script and Latin-based Arabizi. As part of the [Jais](https://arxiv.org/abs/2308.16149) project for standard Arabic and its extensions to dialectal Arabic, Nile-Chat is designed to support natural language generation in a way that reflects the script-diverse nature of Egyptian communication. These models are effective for a variety of tasks including question answering, translation and transliteration. Their range of sizes ensures accessibility, from lightweight personal deployments to more powerful setups, enabling broader use of AI technologies for Egyptian Arabic speakers. The family includes two versions:

* [Nile-Chat-4B](https://huggingface.co/MBZUAI-Paris/Nile-Chat-4B): A compact 4B parameter model that balances efficiency and fluency, well-suited for generating Egyptian Arabic in both Arabic and Latin scripts.
* [Nile-Chat-2x4B-A6B](https://huggingface.co/MBZUAI-Paris/Nile-Chat-2x4B-A6B): A 2x4B MoE parameter model with 6B Activated (soft-merging/1 Expert per script) that balances efficiency and fluency, well-suited for generating Egyptian Arabic in both Arabic and Latin scripts.
* [Nile-Chat-3x4B-A6B](https://huggingface.co/MBZUAI-Paris/Nile-Chat-3x4B-A6B): A 3x4B MoE parameter model with 6B Activated (2 experts activated) providing high-capacity generation in Egyptian Arabic in both Arabic and Latin scripts and English.
* [Nile-Chat-12B](https://huggingface.co/MBZUAI-Paris/Nile-Chat-12B): A dense 12B parameter model providing high-capacity generation capabilities, ideal for complex, multi-turn interactions and nuanced understanding in both Egyptian scripts.

**Paper:** [Nile-Chat: Egyptian Language Models for Arabic and Latin Scripts](https://huggingface.co/papers/2507.04569)

## 👥 Our Team

The model is developed by MBZUAI France Lab, an AI research center in Paris affiliated with the [Mohamed bin Zayed University of Artificial Intelligence (MBZUAI)](https://mbzuai.ac.ae/) headquartered in Abu Dhabi.


## Usage

Below we share some code snippets on how to get quickly started with running the model. First, install the Transformers library with:

```sh
pip install -U transformers sentencepiece
```

Then, copy the snippet from the section below.

#### Running with the `pipeline` API
```python
import torch
from transformers import pipeline

pipe = pipeline(
    "text-generation",
    model="MBZUAI-Paris/Nile-Chat-4B",
    model_kwargs={"torch_dtype": torch.bfloat16},
    device="cuda" # replace with "mps" to run on a Mac device
)

```
Q1:
```
messages = [
    {"role": "user", "content": 'اسمك ايه؟'},
]

outputs = pipe(messages, max_new_tokens=256)
assistant_response = outputs[0]["generated_text"][-1]["content"].strip()
print(assistant_response)
```
A1:

>اسمي نايل-شات، على اسم نهر النيل، اطول نهر في العالم، اللي من زمان كان عامل مهم في تطور مصر، وبيساعد في معيشة الناس وأثر على التراث والثقافة بتاعتنا. وعشان انا موديل لغة، الباحثين بتوع جامعة محمد بن زايد للذكاء الاصطناعي دربوني باستخدام مجموعة من المصادر المفتوحة، فدي حاجة خلتني مميز. 

Q2:
```python
messages = [
    {"role": "user", "content": 'Esmak eh?'},
]
outputs = pipe(messages, max_new_tokens=256)
assistant_response = outputs[0]["generated_text"][-1]["content"].strip()
print(assistant_response)
```
A2:

>Esmi Nile-Chat, 3ala esm nahr el-nil, atwal nahr fel 3alam, elli men zaman kan 3amel mohemm fi tatwor masr, w bir3a el nas, w tb3an el torath

## Training Data
Nile-Chat models were trained on diverse datasets focusing on Egyptian dialect consisting of approximately 3.3B tokens during continual pre-training phase, 1.9M instructions during instruction finetuning and 0.2M samples for DPO, with a maximum length of 2048 tokens, including:

* Web documents: A diverse collection of Egyptian web text ensures the model is exposed to a broad range of linguistic styles, topics, and vocabulary.
* Instruction samples created from publicly available Egyptian Arabic datasets including translation and transliteration.
* Translated English and multi-lingual pretraining and instruction-tuning datasets using Claude 3.5 Sonnet (v2).

The dataset covers both Egyptian Arabic and Latin scripts. Our instruction tuning dataset [Egyptian-SFT-Mixture](https://huggingface.co/datasets/MBZUAI-Paris/Egyptian-SFT-Mixture) is publicly available.


## Implementation Information
Nile-Chat models are based on Gemma 3 models. The Nile-Chat models were trained using 8 NVIDIA A100 80 GB GPUs in parallel using FSDP on AWS Sagemaker. The model is trained using HuggingFace transformers and parameter-efficient fine-tuning with LoRA rank of 256 for both continual pre-training and instruction finetuning, while performing full finetuning for DPO. The continual pre-training is divided into two phases: (i) general pre-training on 2.8B tokens from the Egyptian web and (ii) annealing phase with 0.5B high quality Egyptian text.

# Evaluation
Nile-Chat models were evaluated on a comprehensive suite of tasks using various datasets and benchmarks to assess their performance across multiple dimensions. These included tasks such as:

* **EgyptianMMLU:** An Egyptian version of ArabicMMLU and MMLU benchmarks.
* **EgyptianHellaSwag:** An Egyptian version of HellaSwag (In both scripts Arabic and Latin).
* **Belebele Arz_Arab:** Belebele is a multiple-choice machine reading comprehension dataset published by Facebook spanning 122 language variants. The Evaluation is done on the Arz_Arab part of Belebele that refers to Egyptian Arabic.
* **Translation:** Including four directions and three languages: Arabic script Egyptian, MSA and English.
* **Transliteration:** Transforming a sentence from Egyptian (written in Arabic script) to Arabizi (Written in Latin script) and vice-versa.
* **EgyptianPIQA:** An Egyptian version of PIQA benchmark (In both scripts Arabic and Latin).
* **EgyptianWinoGrande:** An Egyptian version of WinoGrande benchmark (In both scripts Arabic and Latin).
* **EgyptianRACE:** An Egyptian version of RACE benchmark (In both scripts Arabic and Latin).
* **EgyptianOpenBookQA:** An Egyptian version of OpenBookQA benchmark.
* **EgyptianAlpacaEval:** An Egyptian adaptation of AlpacaEval to assess LLM instruction-following and cultural alignment.

The models were compared against a collection of existing open-source Arabic models to gauge their effectiveness, with a particular focus on performance in Egyptian. All scores are based on zero-shot performance. The prompts are written mainly in Egyptian. We used [Language Model Evaluation Harness](https://github.com/MBZUAI-Paris/lm-evaluation-harness-nile-chat) to conduct these evaluations. All evaluations are done with applying chat template except for EgyptianWinoGrande.

## Benchmarks:
### Arabic Script Benchmarks
<table>
  <thead>
    <tr>
      <th><a href="#">Model</a></th>
      <th>Average</th>
      <th><a href="https://huggingface.co/datasets/MBZUAI-Paris/EgyptianMMLU_dev" target="_blank">EgyptianMMLU</a></th>
      <th><a href="https://huggingface.co/datasets/facebook/belebele/viewer/ary_Arab" target="_blank">Belebele Arz</a></th>
      <th><a href="https://huggingface.co/datasets/MBZUAI-Paris/EgyptianHellaSwag" target="_blank">EgyptianHellaSwag</a></th>
      <th><a href="https://huggingface.co/datasets/MBZUAI-Paris/EgyptianPIQA" target="_blank">EgyptianPIQA</a></th>
      <th><a href="https://huggingface.co/datasets/MBZUAI-Paris/EgyptianWinoGrande" target="_blank">EgyptianWinoGrande</a></th>
      <th><a href="https://huggingface.co/datasets/MBZUAI-Paris/EgyptianOpenBookQA" target="_blank">EgyptianOpenBookQA</a></th>
      <th><a href="https://huggingface.co/datasets/MBZUAI-Paris/EgyptianRACE" target="_blank">EgyptianRACE High</a></th>
      <th><a href="https://huggingface.co/datasets/MBZUAI-Paris/EgyptianRACE" target="_blank">EgyptianRACE Middle</a></th>
      <th><a href="https://huggingface.co/datasets/MBZUAI-Paris/EgyptianAlpacaEval" target="_blank">EgyptianAlpacaEval</a></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="https://huggingface.co/google/gemma-3-4b-it" target="_blank">gemma-3-4b-it</a></td>
      <td>48.76</td>
      <td>46.08</td><td>38.56</td><td>42.56</td><td>60.32</td><td>56.49</td><td>35.79</td><td>33.68</td><td>40.06</td><td>85.30</td>
    </tr>
    <tr>
      <td><a href="https://huggingface.co/inceptionai/jais-family-6p7b-chat" target="_blank">jais-family-6p7b-chat</a></td>
      <td>46.64</td>
      <td>42.60</td><td>57.33</td><td>49.18</td><td>62.23</td><td>57.04</td><td>33.33</td><td>34.72</td><td>37.50</td><td>45.86</td>
    </tr>
    <tr>
      <td><a href="https://huggingface.co/inceptionai/jais-adapted-7b-chat" target="_blank">jais-adapted-7b-chat</a></td>
      <td>42.18</td>
      <td>40.96</td><td>55.67</td><td>40.85</td><td>56.50</td><td>54.35</td><td>32.89</td><td>34.62</td><td>42.33</td><td>21.45</td>
    </tr>
    <tr>
      <td><a href="https://huggingface.co/Qwen/Qwen2.5-7B-Instruct" target="_blank">Qwen2.5-7B-Instruct</a></td>
      <td>49.40</td>
      <td>45.74</td><td>64.22</td><td>45.47</td><td>58.02</td><td>56.41</td><td>38.70</td><td>35.45</td><td>41.76</td><td>58.80</td>
    </tr>
    <tr>
      <td><a href="https://huggingface.co/ALLaM-AI/ALLaM-7B-Instruct-preview" target="_blank">ALLaM-7B-Instruct-preview</a></td>
      <td>56.40</td>
      <td>60.08</td><td>67.67</td><td>57.29</td><td>66.10</td><td>62.18</td><td>40.04</td><td>39.50</td><td>45.17</td><td>69.55</td>
    </tr>
    <tr>
      <td><a href="https://huggingface.co/CohereLabs/c4ai-command-r7b-arabic-02-2025" target="_blank">c4ai-command-r7b-arabic-02-2025</a></td>
      <td>53.36</td>
      <td>50.97</td><td>70.67</td><td>50.39</td><td>61.84</td><td>57.20</td><td>36.91</td><td>41.89</td><td>46.02</td><td>73.36</td>
    </tr>
    <tr>
      <td><a href="https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct" target="_blank">Llama-3.1-8B-Instruct</a></td>
      <td>46.31</td>
      <td>42.88</td><td>55.89</td><td>43.10</td><td>57.97</td><td>54.27</td><td>35.57</td><td>34.41</td><td>40.34</td><td>52.35</td>
    </tr>
    <tr>
      <td><a href="https://huggingface.co/FreedomIntelligence/AceGPT-v2-8B-chat" target="_blank">AceGPT-v2-8b-chat</a></td>
      <td>58.33</td>
      <td>55.25</td><td>73.33</td><td>53.14</td><td>62.50</td><td>58.39</td><td>39.82</td><td>41.06</td><td>47.16</td><td>93.33</td>
    </tr>
    <tr>
      <td><a href="https://huggingface.co/google/gemma-2-9b-it" target="_blank">gemma-2-9b-it</a></td>
      <td>53.17</td>
      <td>50.72</td><td>49.44</td><td>49.53</td><td>61.35</td><td>61.79</td><td>35.79</td><td>40.23</td><td>48.01</td><td>81.66</td>
    </tr>
    <tr>
      <td><a href="https://huggingface.co/google/gemma-3-12b-it" target="_blank">gemma-3-12b-it</a></td>
      <td>59.70</td>
      <td>61.55</td><td>77.00</td><td>49.49</td><td>64.96</td><td>63.53</td><td>38.03</td><td>41.27</td><td>48.86</td><td>92.61</td>
    </tr>
    <tr>
      <td><a href="https://huggingface.co/inceptionai/jais-family-13b-chat" target="_blank">jais-family-13b-chat</a></td>
      <td>49.81</td>
      <td>44.85</td><td>66.33</td><td>52.99</td><td>64.85</td><td>57.91</td><td>36.91</td><td>33.26</td><td>38.64</td><td>52.52</td>
    </tr>
    <tr>
      <td><a href="https://huggingface.co/inceptionai/jais-adapted-13b-chat" target="_blank">jais-adapted-13b-chat</a></td>
      <td>49.80</td>
      <td>50.03</td><td>65.33</td><td>47.53</td><td>61.30</td><td>56.72</td><td>37.14</td><td>35.45</td><td>41.76</td><td>52.91</td>
    </tr>
    <tr>
      <td><a href="https://huggingface.co/Qwen/Qwen2.5-14B-Instruct" target="_blank">Qwen2.5-14B-Instruct</a></td>
      <td>57.34</td>
      <td>60.81</td><td>72.33</td><td>55.84</td><td>63.97</td><td>59.97</td><td>38.26</td><td>43.25</td><td>50.28</td><td>71.35</td>
    </tr>
    <tr style="border-top: 4px solid;"></tr>
    <tr>
      <td><a href="https://huggingface.co/MBZUAI-Paris/Nile-Chat-4B" target="_blank"><strong>Nile-Chat-4B</strong></a></td>
      <td>57.85</td>
      <td>50.25</td><td>68.56</td><td>55.92</td><td>67.30</td><td>61.87</td><td>40.94</td><td>42.10</td><td>46.02</td><td>86.95</td>
    </tr>
    <tr>
      <td><a href="https://huggingface.co/MBZUAI-Paris/Nile-Chat-2x4B-A6B" target="_blank"><strong>Nile-Chat-2x4B-A6B</strong></a></td>
      <td>60.89</td>
      <td>52.05</td><td>73.89</td><td>59.69</td><td>68.67</td><td>62.26</td><td>41.61</td><td>44.07</td><td>51.14</td><td>94.58</td>
    </tr>
    <tr>
      <td><a href="https://huggingface.co/MBZUAI-Paris/Nile-Chat-3x4B-A6B" target="_blank"><strong>Nile-Chat-3x4B-A6B</strong></a></td>
      <td>60.25</td>
      <td>52.13</td><td>75.44</td><td>59.3</td><td>69.27</td><td>57.91</td><td>41.16</td><td>44.59</td><td>48.3</td><td>94.18</td>
    </tr>
    <tr>
      <td><a href="https://huggingface.co/MBZUAI-Paris/Nile-Chat-12B" target="_blank"><strong>Nile-Chat-12B</strong></a></td>
      <td>64.34</td>
      <td>62.59</td><td>79.44</td><td>64.04</td><td>70.69</td><td>63.53</td><td>42.06</td><td>48.02</td><td>53.13</td><td>95.56</td>
    </tr>
  </tbody>
</table>

### Latin Script Benchmarks
<table>
  <thead>
    <tr>
      <th><a href="#">Model</a></th>
      <th>Average</th>
      <th><a href="https://huggingface.co/datasets/MBZUAI-Paris/EgyptianHellaSwag" target="_blank">EgyptianHellaSwag</a></th>
      <th><a href="https://huggingface.co/datasets/MBZUAI-Paris/EgyptianPIQA" target="_blank">EgyptianPIQA</a></th>
      <th><a href="https://huggingface.co/datasets/MBZUAI-Paris/EgyptianWinoGrande" target="_blank">EgyptianWinoGrande</a></th>
      <th><a href="https://huggingface.co/datasets/MBZUAI-Paris/EgyptianRACE" target="_blank">EgyptianRACE High</a></th>
      <th><a href="https://huggingface.co/datasets/MBZUAI-Paris/EgyptianRACE" target="_blank">EgyptianRACE Middle</a></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="https://huggingface.co/google/gemma-3-4b-it" target="_blank">gemma-3-4b-it</a></td>
      <td>36.93</td>
      <td>30.90</td><td>52.76</td><td>48.57</td><td>25.47</td><td>26.94</td>
    </tr>
    <tr>
      <td><a href="https://huggingface.co/inceptionai/jais-family-6p7b-chat" target="_blank">jais-family-6p7b-chat</a></td>
      <td>37.58</td>
      <td>30.27</td><td>53.25</td><td>52.14</td><td>24.18</td><td>28.06</td>
    </tr>
    <tr>
      <td><a href="https://huggingface.co/inceptionai/jais-adapted-7b-chat" target="_blank">jais-adapted-7b-chat</a></td>
      <td>37.06</td>
      <td>30.81</td><td>51.67</td><td>50.40</td><td>24.38</td><td>28.06</td>
    </tr>
    <tr>
      <td><a href="https://huggingface.co/Qwen/Qwen2.5-7B-Instruct" target="_blank">Qwen2.5-7B-Instruct</a></td>
      <td>36.87</td>
      <td>30.51</td><td>51.88</td><td>50.95</td><td>24.88</td><td>26.11</td>
    </tr>
    <tr>
      <td><a href="https://huggingface.co/ALLaM-AI/ALLaM-7B-Instruct-preview" target="_blank">ALLaM-7B-Instruct-preview</a></td>
      <td>38.58</td>
      <td>32.17</td><td>53.09</td><td>50.63</td><td>25.07</td><td>31.94</td>
    </tr>
    <tr>
      <td><a href="https://huggingface.co/CohereLabs/c4ai-command-r7b-arabic-02-2025" target="_blank">c4ai-command-r7b-arabic-02-2025</a></td>
      <td>37.38</td>
      <td>30.88</td><td>52.32</td><td>51.43</td><td>25.07</td><td>27.22</td>
    </tr>
    <tr>
      <td><a href="https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct" target="_blank">Llama-3.1-8B-Instruct</a></td>
      <td>37.62</td>
      <td>31.77</td><td>53.30</td><td>50.24</td><td>24.48</td><td>28.33</td>
    </tr>
    <tr>
      <td><a href="https://huggingface.co/FreedomIntelligence/AceGPT-v2-8B-chat" target="_blank">AceGPT-v2-8b-chat</a></td>
      <td>38.77</td>
      <td>33.16</td><td>53.80</td><td>50.24</td><td>26.07</td><td>30.56</td>
    </tr>
    <tr>
      <td><a href="https://huggingface.co/google/gemma-2-9b-it" target="_blank">gemma-2-9b-it</a></td>
      <td>38.70</td>
      <td>33.75</td><td>53.69</td><td>50.79</td><td>26.66</td><td>28.61</td>
    </tr>
    <tr>
      <td><a href="https://huggingface.co/google/gemma-3-12b-it" target="_blank">gemma-3-12b-it</a></td>
      <td>41.63</td>
      <td>37.52</td><td>53.14</td><td>51.19</td><td>31.02</td><td>35.28</td>
    </tr>
    <tr>
      <td><a href="https://huggingface.co/inceptionai/jais-family-13b-chat" target="_blank">jais-family-13b-chat</a></td>
      <td>36.96</td>
      <td>30.46</td><td>53.09</td><td>48.18</td><td>25.28</td><td>27.78</td>
    </tr>
    <tr>
      <td><a href="https://huggingface.co/inceptionai/jais-adapted-13b-chat" target="_blank">jais-adapted-13b-chat</a></td>
      <td>36.98</td>
      <td>31.14</td><td>52.87</td><td>50.79</td><td>23.98</td><td>26.11</td>
    </tr>
    <tr>
      <td><a href="https://huggingface.co/Qwen/Qwen2.5-14B-Instruct" target="_blank">Qwen2.5-14B-Instruct</a></td>
      <td>39.48</td>
      <td>33.49</td><td>52.87</td><td>53.41</td><td>27.35</td><td>30.28</td>
    </tr>
    <tr style="border-top: 4px solid;"></tr>
    <tr>
      <td><a href="https://huggingface.co/MBZUAI-Paris/Nile-Chat-4B" target="_blank"><strong>Nile-Chat-4B</strong></a></td>
      <td>51.38</td>
      <td>50.55</td><td>65.32</td><td>60.62</td><td>37.36</td><td>43.06</td>
    </tr>
    <tr>
      <td><a href="https://huggingface.co/MBZUAI-Paris/Nile-Chat-2x4B-A6B" target="_blank"><strong>Nile-Chat-2x4B-A6B</strong></a></td>
      <td>54.12</td>
      <td>55.49</td><td>68</td><td>61.33</td><td>40.24</td><td>45.56</td>
    </tr>
    <tr>
      <td><a href="https://huggingface.co/MBZUAI-Paris/Nile-Chat-3x4B-A6B" target="_blank"><strong>Nile-Chat-3x4B-A6B</strong></a></td>
      <td>52.26</td>
      <td>55</td><td>66.68</td><td>56.42</td><td>40.44</td><td>42.78</td>
    </tr>
    <tr>
      <td><a href="https://huggingface.co/MBZUAI-Paris/Nile-Chat-12B" target="_blank"><strong>Nile-Chat-12B</strong></a></td>
      <td>53.88</td>
      <td>53.71</td><td>65.10</td><td>59.98</td><td>41.72</td><td>48.89</td>
    </tr>
  </tbody>
</table>

### Translation and Transliteration Tasks:
<table>
    <tr>
        <td rowspan="2">Model</td>
        <td colspan="3"><a href="https://huggingface.co/datasets/MBZUAI-Paris/EgyptianBench" target="_blank">Long Translation</a></td>
        <td colspan="3"><a href="https://huggingface.co/datasets/MBZUAI-Paris/EgyptianBench" target="_blank">Short Translation</a></td>
        <td colspan="3"><a href="https://huggingface.co/datasets/MBZUAI-Paris/EgyptianBench" target="_blank">Transliteration</a></td>
    </tr>
    <tr>
        <td>BLEU</td>
        <td>chrF</td>
        <td>BERTScore</td>
        <td>BLEU</td>
        <td>chrF</td>
        <td>BERTScore</td>
        <td>BLEU</td>
        <td>chrF</td>
        <td>BERTScore</td>
    </tr>
    <tr>
        <td><a href="https://huggingface.co/google/gemma-3-4b-it" target="_blank">gemma-3-4b-it</a></td>
        <td>20.67</td>
        <td>44.75</td>
        <td>73.03</td>
        <td>04.76</td>
        <td>31.15</td>
        <td>52.98</td>
        <td>01.44</td>
        <td>20.36</td>
        <td>47.54</td>
    </tr>
    <tr>
        <td><a href="https://huggingface.co/inceptionai/jais-family-6p7b-chat" target="_blank">jais-family-6p7b-chat</a></td>
        <td>12.71</td>
        <td>36.53</td>
        <td>68.07</td>
        <td>08.73</td>
        <td>31.52</td>
        <td>56.78</td>
        <td>00.70</td>
        <td>10.64</td>
        <td>42.51</td>
    </tr>
    <tr>
        <td><a href="https://huggingface.co/inceptionai/jais-adapted-7b-chat" target="_blank">jais-adapted-7b-chat</a></td>
        <td>10.61</td>
        <td>27.56</td>
        <td>63.48</td>
        <td>09.19</td>
        <td>24.85</td>
        <td>53.52</td>
        <td>01.11</td>
        <td>06.14</td>
        <td>40.45</td>
    </tr>
    <tr>
        <td><a href="https://huggingface.co/Qwen/Qwen2.5-7B-Instruct"  target="_blank">Qwen2.5-7B-Instruct</a></td>
        <td>19.89</td>
        <td>44.80</td>
        <td>73.64</td>
        <td>11.34</td>
        <td>36.31</td>
        <td>54.96</td>
        <td>02.74</td>
        <td>20.63</td>
        <td>49.32</td>
    </tr>
    <tr>
        <td><a href="https://huggingface.co/ALLaM-AI/ALLaM-7B-Instruct-preview" target="_blank">ALLaM-7B-Instruct-preview</a></td>
        <td>26.57</td>
        <td>52.59</td>
        <td>78.34</td>
        <td>25.20</td>
        <td>48.12</td>
        <td>65.97</td>
        <td>02.10</td>
        <td>18.92</td>
        <td>49.42</td>
    </tr>
    <tr>
        <td><a href="https://huggingface.co/CohereLabs/c4ai-command-r7b-arabic-02-2025" target="_blank">c4ai-command-r7b-arabic-02-2025</a></td>
        <td>25.18</td>
        <td>50.26</td>
        <td>77.97</td>
        <td>23.30</td>
        <td>45.34</td>
        <td>65.20</td>
        <td>03.52</td>
        <td>24.57</td>
        <td>50.49</td>
    </tr>
    <!-- <tr style="border-top: 4px solid;"></tr> -->
    <tr>
        <td><a href="https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct" target="_blank">Llama-3.1-8B-Instruct</a></td>
        <td>12.90</td>
        <td>32.58</td>
        <td>68.76</td>
        <td>09.06</td>
        <td>28.56</td>
        <td>54.19</td>
        <td>03.26</td>
        <td>17.55</td>
        <td>48.71</td>
    </tr>
    <tr>
        <td><a href="https://huggingface.co/FreedomIntelligence/AceGPT-v2-8B-chat" target="_blank">AceGPT-v2-8b-chat</a></td>
        <td>24.59</td>
        <td>49.39</td>
        <td>77.57</td>
        <td>22.47</td>
        <td>44.97</td>
        <td>66.30</td>
        <td>04.80</td>
        <td>23.52</td>
        <td>49.33</td>
    </tr>
    <tr>
        <td><a href="https://huggingface.co/google/gemma-2-9b-it" target="_blank">gemma-2-9b-it</a></td>
        <td>23.09</td>
        <td>46.98</td>
        <td>75.42</td>
        <td>11.73</td>
        <td>39.00</td>
        <td>60.42</td>
        <td>02.68</td>
        <td>24.28</td>
        <td>48.26</td>
    </tr>
    <tr>
        <td><a href="https://huggingface.co/google/gemma-3-12b-it" target="_blank">gemma-3-12b-it</a></td>
        <td>22.90</td>
        <td>45.97</td>
        <td>73.46</td>
        <td>05.24</td>
        <td>32.82</td>
        <td>54.34</td>
        <td>02.77</td>
        <td>26.16</td>
        <td>50.47</td>
    </tr>
    <tr>
        <td><a href="https://huggingface.co/inceptionai/jais-family-13b-chat" target="_blank">jais-family-13b-chat</a></td>
        <td>10.41</td>
        <td>31.98</td>
        <td>64.15</td>
        <td>08.64</td>
        <td>30.10</td>
        <td>57.00</td>
        <td>00.84</td>
        <td>11.35</td>
        <td>44.71</td>
    </tr>
    <tr>
        <td><a href="https://huggingface.co/inceptionai/jais-adapted-13b-chat" target="_blank">jais-adapted-13b-chat</a></td>
        <td>15.53</td>
        <td>41.48</td>
        <td>70.86</td>
        <td>15.96</td>
        <td>38.81</td>
        <td>63.52</td>
        <td>01.00</td>
        <td>13.33</td>
        <td>46.08</td>
    </tr>
    <tr>
        <td><a href="https://huggingface.co/Qwen/Qwen2.5-14B-Instruct"  target="_blank">Qwen2.5-14B-Instruct</a></td>
        <td>21.71</td>
        <td>45.55</td>
        <td>73.36</td>
        <td>09.26</td>
        <td>34.21</td>
        <td>53.89</td>
        <td>04.07</td>
        <td>25.83</td>
        <td>51.41</td>
    </tr>
    <tr style="border-top: 4px solid;"></tr>
    <tr>
        <td><strong><a href="https://huggingface.co/MBZUAI-Paris/Nile-Chat-4B" target="_blank">Nile-Chat-4B</a></td>
        <td>37.49</td>
        <td>58.40</td>
        <td>84.30</td>
        <td>30.35</td>
        <td>52.01</td>
        <td>74.07</td>
        <td>51.46</td>
        <td>80.44</td>
        <td>89.59</td>
    </tr>
    <tr>
        <td><strong><a href="https://huggingface.co/MBZUAI-Paris/Nile-Chat-2x4B-A6B" target="_blank">Nile-Chat-2x4B-A6B</a></td>
        <td>41.98</td>
        <td>61.59</td>
        <td>86.11</td>
        <td>33.4</td>
        <td>53.71</td>
        <td>76.78</td>
        <td>57.75</td>
        <td>83.89</td>
        <td>91.05</td>
    </tr>
    <tr>
        <td><strong><a href="https://huggingface.co/MBZUAI-Paris/Nile-Chat-3x4B-A6B" target="_blank">Nile-Chat-3x4B-A6B</a></td>
        <td>42.43</td>
        <td>61.9</td>
        <td>86.26</td>
        <td>34.56</td>
        <td>55.37</td>
        <td>76.97</td>
        <td>57.79</td>
        <td>83.97</td>
        <td>91.13</td>
    </tr>
    <tr>
        <td><strong><a href="https://huggingface.co/MBZUAI-Paris/Nile-Chat-12B" target="_blank">Nile-Chat-12B</a></td>
        <td>40.53</td>
        <td>60.61</td>
        <td>85.45</td>
        <td>32.2</td>
        <td>53.53</td>
        <td>74.72</td>
        <td>52.21</td>
        <td>80.97</td>
        <td>89.71</td>
    </tr>

    
</table>


## Usage and Limitations

These models have certain limitations that users should be aware of.
<details>
<summary>Intended Usage</summary>

Open Large Language Models (LLMs) have a wide range of applications across
various industries and domains. The following list of potential uses is not
comprehensive. The purpose of this list is to provide contextual information
about the possible use-cases that the model creators considered as part of model
training and development.

* Content Creation and Communication
  * Text Generation: These models can be used to generate creative text formats
    such as poems, scripts, code, marketing copy, and email drafts.
  * Chatbots and Conversational AI: Power conversational interfaces for customer
    service, virtual assistants, or interactive applications.
  * Text Summarization: Generate concise summaries of a text corpus, research
    papers, or reports.
* Research and Education
  * Natural Language Processing (NLP) Research: These models can serve as a
    foundation for researchers to experiment with NLP techniques, develop
    algorithms, and contribute to the advancement of the field.
  * Language Learning Tools: Support interactive language learning experiences,
    aiding in grammar correction or providing writing practice.
  * Knowledge Exploration: Assist researchers in exploring large bodies of text
    by generating summaries or answering questions about specific topics.
</details>
<details>
<summary>Limitations</summary>

* Training Data
  * The quality and diversity of the training data significantly influence the
    model's capabilities. Biases or gaps in the training data can lead to
    limitations in the model's responses.
  * The scope of the training dataset determines the subject areas the model can
    handle effectively.
* Context and Task Complexity
  * LLMs perform better on tasks framed with clear prompts and
    instructions. Open-ended or highly complex tasks might be challenging.
  * A model's performance can be influenced by the amount of context provided
    (longer context generally leads to better outputs, up to a certain point).
* Language Ambiguity and Nuance
  * Natural language is inherently complex. LLMs might struggle to grasp subtle
    nuances, sarcasm, or figurative language.
* Factual Accuracy
  * LLMs generate responses based on information they learned from their
    training datasets, but they are not knowledge bases. They may generate
    incorrect or outdated factual statements.
* Common Sense
  * LLMs rely on statistical patterns in language. They might lack the ability
    to apply common sense reasoning in certain situations.
</details>
<details>
<summary> Ethical Considerations and Risks</summary>

The development of large language models (LLMs) raises several ethical concerns.
In creating an open model, we have carefully considered the following:

* Bias and Fairness
  * LLMs trained on large-scale, real-world text data can reflect socio-cultural
    biases embedded in the training material.
* Misinformation and Misuse
  * LLMs can be misused to generate text that is false, misleading, or harmful.
  * Guidelines are provided for responsible use with the model, see the
    [Responsible Generative AI Toolkit][rai-toolkit].
* Transparency and Accountability:
  * This model card summarizes details on the models' architecture,
    capabilities, limitations, and evaluation processes.
  * A responsibly developed open model offers the opportunity to share
    innovation by making LLM technology accessible to developers and researchers
    across the AI ecosystem.

Risks identified and mitigations:

* Perpetuation of biases: It's encouraged to perform continuous monitoring
  (using evaluation metrics, human review) and the exploration of de-biasing
  techniques during model training, fine-tuning, and other use cases.
* Generation of harmful content: Mechanisms and guidelines for content safety
  are essential. Developers are encouraged to exercise caution and implement
  appropriate content safety safeguards based on their specific product policies
  and application use cases.
* Privacy violations: Models were trained on data filtered for removal of PII
  (Personally Identifiable Information). Developers are encouraged to adhere to
  privacy regulations with privacy-preserving techniques.

</details>