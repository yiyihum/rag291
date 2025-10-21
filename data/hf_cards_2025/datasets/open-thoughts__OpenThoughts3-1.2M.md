---
dataset_info:
  features:
  - name: difficulty
    dtype: int64
  - name: source
    dtype: string
  - name: domain
    dtype: string
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  splits:
  - name: train
    num_bytes: 59763369750
    num_examples: 1200000
  download_size: 28188197544
  dataset_size: 59763369750
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: apache-2.0
task_categories:
- text-generation
tags:
- reasoning
- mathematics
- code
- science
library_name: datasets
---

<p align="center">
    <img src="https://huggingface.co/datasets/open-thoughts/open-thoughts-114k/resolve/main/open_thoughts.png" width="50%">
</p>

<p align="center">
<a href="https://arxiv.org/abs/2506.04178" style="margin-right: 24px;">paper</a> |
<a href="https://huggingface.co/datasets/open-thoughts/OpenThoughts3-1.2M" style="margin-right: 24px; margin-left: 24px;">dataset</a> |
<a href="https://huggingface.co/open-thoughts/OpenThinker3-7B" style="margin-left: 24px;">model</a>
</p>

> [!NOTE]
> We have released a paper for OpenThoughts! See our paper [here](https://arxiv.org/abs/2506.04178).

<a href="https://github.com/bespokelabsai/curator/">
 <img src="https://huggingface.co/datasets/bespokelabs/Bespoke-Stratos-17k/resolve/main/made_with_curator.png" alt="Made with Curator" width=200px>
</a>


# OpenThoughts3-1.2M

## Dataset Description

- **Homepage:** https://www.open-thoughts.ai/
- **Repository:** https://github.com/open-thoughts/open-thoughts

Open-source state-of-the-art reasoning dataset with 1.2M rows. 🚀

[OpenThoughts3-1.2M](https://arxiv.org/abs/2506.04178) is the third iteration in our line of [OpenThoughts](https://openthoughts.ai) datasets, building on our previous [OpenThoughts-114k](https://huggingface.co/datasets/open-thoughts/OpenThoughts-114k) and [OpenThoughts2-1M](https://huggingface.co/datasets/open-thoughts/OpenThoughts2-1M).
This time around, we scale even further and generate our dataset in a much more systematic way -- [OpenThoughts3-1.2M](https://arxiv.org/abs/2506.04178) is the result of a rigorous experimental pipeline, that ablates over design choices surrounding question sourcing and selection, as well as answer generation. 
The final dataset consists of 850,000 math questions, 250,000 code questions, and 100,000 science questions. Annotations are done with QwQ-32B.

This dataset was used to train [OpenThinker3-7B](https://huggingface.co/open-thoughts/OpenThinker3-7B), which beats **all** similarly sized open-data reasoning models.

See our [paper](https://arxiv.org/abs/2506.04178) and [blog post](https://www.open-thoughts.ai/blog/ot3) for more details. OpenThinker3-32B to follow! 👀


# OpenThinker3-7B Model Performance

Our [OpenThinker3-7B](https://huggingface.co/open-thoughts/OpenThinker3-7B) model trained on this dataset is the state-of-the-art open-data reasoning dataset at its scale. 

We conduct all our evaluations using [Evalchemy](https://github.com/mlfoundations/evalchemy). In the table below, we bold values in each column that are within 2 standard errors of the best. 

| Model                                                                                           | Data  | AIME24 | AIME25 |  AMC23 | MATH500 | HMMT O2/25 | LCB 06/24-01/25 | CodeElo | CodeForces | GPQA-D | JEEBench |
| ----------------------------------------------------------------------------------------------- | ----- | ------ | ------ | ------ | ------- | ---------- | --------------- | ------- | ---------- | ------ | -------- |
| [OpenThinker-7B](https://huggingface.co/open-thoughts/OpenThinker-7B)                           | ✅    |  30.7  |  22.0  |  72.5  |   82.8  |   15.7     |    26.1         |  11.1   |  14.9      |  38.6  |  45.3    |
| [OpenThinker2-7B](https://huggingface.co/open-thoughts/OpenThinker2-7B)                         | ✅    |  60.7  |  38.7  |  89.8  |   87.6  |   24.7     |    40.6         |  22.8   |  26.6      |  47.0  |  65.1    |
| **[OpenThinker3-7B](https://huggingface.co/open-thoughts/OpenThinker3-7B)**                     | ✅    |**69.0**|**53.3**|**93.5**| **90.0**|   **42.7** |    **51.7**     |  31.0   |**32.2**    |  53.7  |**72.4**  |
| [DeepSeek-R1-Distill-Qwen-32B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B) | ❌    |  51.3  |  38.0  |  92.0  |   88.0  |   25.0     |    34.5         |  19.9   |  21.1      |  33.2  |  50.4    |
| [OpenR1-Distill-7B](https://huggingface.co/open-r1/OpenR1-Distill-7B)                           | ✅    |  57.7  |  39.7  |  87.0  |   88.0  |   25.7     |    30.7         |  30.1   |  29.3      |**58.9**|  68.7    |
| [Llama-3.1-Nemotron-Nano-8B-v1](https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-8B-v1)    | ✅    |  62.0  |  48.0  |**94.0**|   89.4  |   26.7     |    **50.9**     |  30.9   |**32.9**    |  52.9  |  70.7    |
| [AceReason-Nemotron-7B](https://huggingface.co/nvidia/AceReason-Nemotron-7B)                    | ✅    |**71.0**|  50.7  |**93.8**|   89.8  |   33.3     |    44.3         |**32.9** |**30.9**    |  52.9  |  64.3    |

# OpenThoughts3 Data Curation and Scaling Recipe

Please see our [paper](https://arxiv.org/abs/2506.04178) for full details and experimental results.

[OpenThoughts3-1.2M](https://huggingface.co/datasets/open-thoughts/OpenThoughts3-1.2M) was created through the following steps:

0. Run our 1000+ ablations and find the best datasets, filtering strategies, and annotation strategies.  
1. 🙋 **Source questions** from the best strategies from Step 0. These question strategies can be both human-written (e.g., StackExchange Physics) or synthetic (e.g., [ai2-adapt-dev/openmath-2-math](https://huggingface.co/datasets/ai2-adapt-dev/openmath-2-math)).
2. 🧹 **Filter** the questions down to 180k math, 60k code, 60k science.
3. 🧹 **Deduplicate** datasets. 
4. 🧹 **Downsample** so that we have 75k questions in total.
5. 💡 **Annotate each question 16x** with QwQ-32B, arriving at a 1.2M dataset.

![ot3-datacuration-pipeline](ot3-datacuration-pipeline.png)


# Links
- 📝 [OpenThoughts Paper](https://arxiv.org/abs/2506.04178)
- 📊 [OpenThoughts3-1.2M and OpenThinker3-7B Blog Post](https://www.open-thoughts.ai/blog/ot3)
- 💻 [Open Thoughts GitHub Repository](https://github.com/open-thoughts/open-thoughts)
- 🧠 [OpenThoughts3-1.2M dataset](https://huggingface.co/datasets/open-thoughts/OpenThoughts3-1.2M) - this dataset.
- 🤖 [OpenThinker3-7B model](https://huggingface.co/open-thoughts/OpenThinker3-7B)

# Citation
```
@misc{guha2025openthoughtsdatarecipesreasoning,
  title={OpenThoughts: Data Recipes for Reasoning Models}, 
  author={Etash Guha and Ryan Marten and Sedrick Keh and Negin Raoof and Georgios Smyrnis and Hritik Bansal and Marianna Nezhurina and Jean Mercat and Trung Vu and Zayne Sprague and Ashima Suvarna and Benjamin Feuer and Liangyu Chen and Zaid Khan and Eric Frankel and Sachin Grover and Caroline Choi and Niklas Muennighoff and Shiye Su and Wanjia Zhao and John Yang and Shreyas Pimpalgaonkar and Kartik Sharma and Charlie Cheng-Jie Ji and Yichuan Deng and Sarah Pratt and Vivek Ramanujan and Jon Saad-Falcon and Jeffrey Li and Achal Dave and Alon Albalak and Kushal Arora and Blake Wulfe and Chinmay Hegde and Greg Durrett and Sewoong Oh and Mohit Bansal and Saadia Gabriel and Aditya Grover and Kai-Wei Chang and Vaishaal Shankar and Aaron Gokaslan and Mike A. Merrill and Tatsunori Hashimoto and Yejin Choi and Jenia Jitsev and Reinhard Heckel and Maheswaran Sathiamoorthy and Alexandros G. Dimakis and Ludwig Schmidt},
  year={2025},
  eprint={2506.04178},
  archivePrefix={arXiv},
  primaryClass={cs.LG},
  url={https://arxiv.org/abs/2506.04178}, 
}
```