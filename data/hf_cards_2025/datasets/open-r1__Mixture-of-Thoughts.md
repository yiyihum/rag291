---
dataset_info:
- config_name: all
  features:
  - name: messages
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: num_tokens
    dtype: int64
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 7062819826.825458
    num_examples: 349317
  download_size: 3077653717
  dataset_size: 7062819826.825458
- config_name: code
  features:
  - name: messages
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: num_tokens
    dtype: int64
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 3872656251.3167396
    num_examples: 83070
  download_size: 1613338604
  dataset_size: 3872656251.3167396
- config_name: math
  features:
  - name: messages
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: num_tokens
    dtype: int64
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 1599028646
    num_examples: 93733
  download_size: 704448153
  dataset_size: 1599028646
- config_name: science
  features:
  - name: messages
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: num_tokens
    dtype: int64
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 1590765326
    num_examples: 172514
  download_size: 674333812
  dataset_size: 1590765326
configs:
- config_name: all
  data_files:
  - split: train
    path: all/train-*
- config_name: code
  data_files:
  - split: train
    path: code/train-*
- config_name: math
  data_files:
  - split: train
    path: math/train-*
- config_name: science
  data_files:
  - split: train
    path: science/train-*
task_categories:
- text-generation
language:
- en
pretty_name: Mixture of Thoughts
size_categories:
- 100K<n<1M
---

<img src="mot-thumbnail.png" alt="Centered Image" style="display: block; margin: 0 auto;" width="500">

# Dataset summary

Mixture-of-Thoughts is a curated dataset of 350k verified reasoning traces distilled from [DeepSeek-R1](https://huggingface.co/deepseek-ai/DeepSeek-R1). The dataset spans tasks in mathematics, coding, and science, and is designed to teach language models to reason step-by-step. It was used in the Open R1 project to train [OpenR1-Distill-7B](https://huggingface.co/open-r1/OpenR1-Distill-7B), an SFT model that replicates the reasoning capabilities of [deepseek-ai/DeepSeek-R1-Distill-Qwen-7B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B) from the same base model.

To load the dataset, run:

```python
from datasets import load_dataset

dataset = load_dataset("open-r1/Mixture-of-Thoughts", "all", split="train")

# Load a specific domain
dataset_math = load_dataset("open-r1/Mixture-of-Thoughts", "math", split="train")
```

## Dataset composition

Mixture-of-Thoughts is composed of three domains: math, code, and science. Each domain contains reasoning traces that are designed to teach language models to reason step-by-step. The dataset is structured as follows:

- **math**: 93.7k reasoning traces for mathematical problems, sourced from the `default` subset of [open-r1/OpenR1-Math-220k](https://huggingface.co/datasets/open-r1/OpenR1-Math-220k)
- **code**: 83.1k reasoning traces for competitive programming problems in Python and C++, sourced from the `solutions` and `solutions_w_editorials` subsets of [open-r1/codeforces-cots](https://huggingface.co/datasets/open-r1/codeforces-cots)
- **science**: 173k reasoning traces for scientific problems, sourced from the `science` subset of [nvidia/Llama-Nemotron-Post-Training-Dataset](https://huggingface.co/datasets/nvidia/Llama-Nemotron-Post-Training-Dataset)
- **all**: Contains all reasoning traces from the three domains, for a total of 350k traces.

## Curation methodology

To optimise the data mixture, we followed the same methodology described in the [Phi-4-reasoning tech report](https://huggingface.co/papers/2504.21318), namely that mixtures can be optimised independently per domain, and then combined into a single dataset. For each ablation, we evaluate on AIME 2024, GPQA Diamond, and LiveCodeBench v4 every epoch and take the best performing model checkpoint. The figure below shows the results from post-training [open-r1/Qwen2.5-Math-7B-RoPE-300k](https://huggingface.co/open-r1/Qwen2.5-Math-7B-RoPE-300k) on each individual domain compared to the final mixture:

<img src="data_mix.png" alt="Centered Image" style="display: block; margin: 0 auto;">

Overall, we find that training on all domains simultaneously yields the best results. See the subsections below for more details on optimising the data mixture per domain.

> [!NOTE]
> We use LiveCodeBench v4 to accelerate evaluation during our ablations as it contains around half the problems of v5, yet is still representative of the full benchmark.

### Code

During the development of [open-r1/OlympicCoder-7B](https://huggingface.co/open-r1/OlympicCoder-7B), we observed that generating R1 reasoning traces in C++ produced better results on the challenging [IOI 2024 benchmark](https://github.com/huggingface/ioi), while Python traces produced better results on LiveCodeBench (a Python-only benchmark). To optimise the data mixture, we therefore used a mix of C++ and Python traces sourced from the following subsets of [open-r1/codeforces-cots](https://huggingface.co/datasets/open-r1/codeforces-cots):

- `solutions`: we prompt R1 to solve the problem and produce code in C++.
- `solutions_py`: same as `solutions`, but with R1 prompted to produce code in Python.
- `solutions_w_editorials`: we prompt R1 to solve the problem and produce code, but also provide it with a human-written solution.
- `solutions_w_editorials_py`: same as `solutions_w_editorials`, but with R1 prompted to produce code in Python.

The figure below shows the evolution of our ablations on these subsets, using [Qwen/Qwen2.5-Coder-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct) as the base model:

<img src="code_mix.png" alt="Centered Image" style="display: block; margin: 0 auto;">

The individual experiments correspond to the following:

* **exp1 - exp3:** scaling the learning rate on the `solutions` subset from 1e-5 to 2e-5, and 4e-5 respectively.
* **exp4 - exp5:** measuring the impact of training on the `solutions_w_editorials` subset vs the combined `solutions` and `solutions_w_editorials` subsets.
* **exp6 - exp9:** measuring the impact of blending in Python traces from the `solutions_py` and `solutions_w_editorials_py` subsets. exp6 combines the `solutions_w_editorials` and `solutions_w_editorials_py` subsets, while exp7 combines the `solutions` and `solutions_py` subsets. Finally, exp8 combines all four subsets.

We found that combining all subsets of C++ and Python traces yielded the best results on LiveCodeBench. We also found that using this data mixture to fine-tune [open-r1/Qwen2.5-Coder-7B-RoPE-300k](https://huggingface.co/open-r1/Qwen2.5-Coder-7B-RoPE-300k) led to comparable performance improvements, which shows the effectiveness of our curation strategy.

### Math

For the math domain, we mostly focused on comparing the `default` and `extended` subsets of [open-r1/OpenR1-Math-220k](https://huggingface.co/datasets/open-r1/OpenR1-Math-220k). The `default` subset contains 93.7k reasoning traces, while the `extended` subset contains an additional 131k traces, containing simpler problems than the `default` subset. The figure below shows performance on each subset, using [Qwen/Qwen2.5-Math-7B-RoPE-300k](https://huggingface.co/Qwen/Qwen2.5-Math-7B-RoPE-300k) as the base model:

<img src="math_mix.png" alt="Centered Image" style="display: block; margin: 0 auto;">

Overall, we found that training on the `default` subset yielded better results than training on the `extended` subset, and that training on both subsets together yielded the best results. Nevertheless, we opted to use the `default` subset only for the final mixture, as including both would have led to a significant increase in the size of the dataset, for a modest improvement in performance.

### Science

For the science domain, we used the `science` subset of [nvidia/Llama-Nemotron-Post-Training-Dataset](https://huggingface.co/datasets/nvidia/Llama-Nemotron-Post-Training-Dataset/viewer/SFT/science), which contains 483k reasoning traces. However, we found that the subset was too large to be used in its entirety, as it would have led to a significant increase in the size of the dataset. Instead, we selected the subset of traces where no Qwen models were used for prompt pre-processing--see this [discussion](https://huggingface.co/datasets/nvidia/Llama-Nemotron-Post-Training-Dataset/discussions/6) for more details. The result was 173k reasoning traces, which we used in the final mixture after ablating on the learning rate.

## Citation

If you find this dataset is useful in your own work, please consider citing it as follows, together with the source of the specific domain you are using:

```bibtex
@misc{openr1,
    title = {Open R1: A fully open reproduction of DeepSeek-R1},
    url = {https://github.com/huggingface/open-r1},
    author = {Hugging Face},
    month = {January},
    year = {2025}
}
```

**open-r1/codeforces-cots**

```bibtex
@misc{penedo2025codeforces,
      title={CodeForces CoTs}, 
      author={Guilherme Penedo and Anton Lozhkov and Hynek Kydlíček and Loubna Ben Allal and Edward Beeching and Agustín Piqueres Lajarín and Quentin Gallouédec and Nathan Habib and Lewis Tunstall and Leandro von Werra},
      year={2025},
      publisher = {Hugging Face},
      journal = {Hugging Face repository},
      howpublished = {\url{https://huggingface.co/datasets/open-r1/codeforces-cots}}
}
```

**open-r1/OpenR1-Math-220k**

```bibtex
@misc{lozhkov2025openr1math220k,
      title={OpenR1-Math-220k},
      author={Anton Lozhkov and Hynek Kydlíček and Loubna Ben Allal and Guilherme Penedo and Edward Beeching and Quentin Gallouédec and Nathan Habib and Lewis Tunstall and Leandro von Werra},
      year={2025},
      publisher = {Hugging Face},
      journal = {Hugging Face repository},
      howpublished = {\url{https://huggingface.co/datasets/open-r1/OpenR1-Math-220k}}
}
```

**nvidia/Llama-Nemotron-Post-Training-Dataset**

```bibtex
@misc{bercovich2025llamanemotronefficientreasoningmodels,
      title={Llama-Nemotron: Efficient Reasoning Models}, 
      author={Akhiad Bercovich and Itay Levy and Izik Golan and Mohammad Dabbah and Ran El-Yaniv and Omri Puny and Ido Galil and Zach Moshe and Tomer Ronen and Najeeb Nabwani and Ido Shahaf and Oren Tropp and Ehud Karpas and Ran Zilberstein and Jiaqi Zeng and Soumye Singhal and Alexander Bukharin and Yian Zhang and Tugrul Konuk and Gerald Shen and Ameya Sunil Mahabaleshwarkar and Bilal Kartal and Yoshi Suhara and Olivier Delalleau and Zijia Chen and Zhilin Wang and David Mosallanezhad and Adi Renduchintala and Haifeng Qian and Dima Rekesh and Fei Jia and Somshubra Majumdar and Vahid Noroozi and Wasi Uddin Ahmad and Sean Narenthiran and Aleksander Ficek and Mehrzad Samadi and Jocelyn Huang and Siddhartha Jain and Igor Gitman and Ivan Moshkov and Wei Du and Shubham Toshniwal and George Armstrong and Branislav Kisacanin and Matvei Novikov and Daria Gitman and Evelina Bakhturina and Jane Polak Scowcroft and John Kamalu and Dan Su and Kezhi Kong and Markus Kliegl and Rabeeh Karimi and Ying Lin and Sanjeev Satheesh and Jupinder Parmar and Pritam Gundecha and Brandon Norick and Joseph Jennings and Shrimai Prabhumoye and Syeda Nahida Akter and Mostofa Patwary and Abhinav Khattar and Deepak Narayanan and Roger Waleffe and Jimmy Zhang and Bor-Yiing Su and Guyue Huang and Terry Kong and Parth Chadha and Sahil Jain and Christine Harvey and Elad Segal and Jining Huang and Sergey Kashirsky and Robert McQueen and Izzy Putterman and George Lam and Arun Venkatesan and Sherry Wu and Vinh Nguyen and Manoj Kilaru and Andrew Wang and Anna Warno and Abhilash Somasamudramath and Sandip Bhaskar and Maka Dong and Nave Assaf and Shahar Mor and Omer Ullman Argov and Scot Junkin and Oleksandr Romanenko and Pedro Larroy and Monika Katariya and Marco Rovinelli and Viji Balas and Nicholas Edelman and Anahita Bhiwandiwalla and Muthu Subramaniam and Smita Ithape and Karthik Ramamoorthy and Yuting Wu and Suguna Varshini Velury and Omri Almog and Joyjit Daw and Denys Fridman and Erick Galinkin and Michael Evans and Katherine Luna and Leon Derczynski and Nikki Pope and Eileen Long and Seth Schneider and Guillermo Siman and Tomasz Grzegorzek and Pablo Ribalta and Monika Katariya and Joey Conway and Trisha Saar and Ann Guan and Krzysztof Pawelec and Shyamala Prayaga and Oleksii Kuchaiev and Boris Ginsburg and Oluwatobi Olabiyi and Kari Briski and Jonathan Cohen and Bryan Catanzaro and Jonah Alben and Yonatan Geifman and Eric Chung and Chris Alexiuk},
      year={2025},
      eprint={2505.00949},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2505.00949}, 
}
```