---
annotations_creators:
- machine-generated
language:
- code
license: apache-2.0
multilinguality: monolingual
pretty_name: Jupyter Agent Dataset
tags:
- jupyter
- kaggle
- agents
- code
- synthetic
task_categories:
- question-answering
- text-generation
size_categories:
- 10K<n<100K
dataset_info:
  features:
  - name: messages
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
    - name: tool_calls
      list:
      - name: function
        struct:
        - name: arguments
          struct:
          - name: answer
            dtype: string
          - name: code
            dtype: string
        - name: name
          dtype: string
  - name: id
    dtype: string
  - name: edu_score
    dtype: int64
  - name: files_used
    list: string
  - name: packages_used
    list: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: kaggle_dataset_name
    dtype: string
  - name: executor_type
    dtype: string
  - name: original_notebook
    dtype: string
  - name: tools
    list:
    - name: function
      struct:
      - name: description
        dtype: string
      - name: name
        dtype: string
      - name: parameters
        struct:
        - name: properties
          struct:
          - name: answer
            struct:
            - name: description
              dtype: string
            - name: type
              dtype: string
          - name: code
            struct:
            - name: description
              dtype: string
            - name: type
              dtype: string
        - name: required
          list: string
        - name: type
          dtype: string
    - name: type
      dtype: string
  splits:
  - name: thinking
    num_bytes: 51081197281
    num_examples: 51389
  - name: non_thinking
    num_bytes: 51075702887
    num_examples: 51389
  download_size: 71781735066
  dataset_size: 102156900168
configs:
- config_name: default
  data_files:
  - split: thinking
    path: data/thinking-*
  - split: non_thinking
    path: data/non_thinking-*
---

# Jupyter Agent Dataset

![image/png](https://cdn-uploads.huggingface.co/production/uploads/650ed7adf141bc34f91a12ae/ZyF9foqe5SLECwkq0dOpT.png)

## Dataset Details

### Dataset Description

The dataset uses real Kaggle notebooks processed through a multi-stage pipeline to de-duplicate, fetch referenced datasets, score educational quality, filter to data-analysis–relevant content, generate dataset-grounded question–answer (QA) pairs, and produce executable reasoning traces by running notebooks. The resulting examples include natural questions about a dataset/notebook, verified answers, and step-by-step execution traces suitable for agent training.

You can load the dataset using the following code:

```python
from datasets import load_dataset
# To load the train split of a specific subset, such as non-thinking, you can do
ds = load_dataset("jupyter-agent/jupyter-agent-dataset", split="non-thinking")
# apply chat template
tokenizer.apply_chat_template(ds[0]["text"])
```

The dataset contains in total 51389 synthetic notebooks, which amounts to ~200M training tokens. The dataset is provided in two subsets - `thinking` and `non-thinking`, where the code generation thinking commentary is wrapped with or without thinkinng tags, depending on base model type. We provide both subsets for convenince and ability to use the dataset for fine-tuning out-of-the-box.

- Created by: [Hugging Face Jupyter-Agent Team](https://huggingface.co/jupyter-agent) ([Baptiste Colle](https://huggingface.co/baptistecolle), [Hanna Yukhymenko](https://huggingface.co/hannayukhymenko), [Leandro von Werra](https://huggingface.co/lvwerra))
- Source Code: [github link](https://github.com/huggingface/jupyter-agent)
- Blog: [blog link](https://huggingface.co/blog/jupyter-agent-2)
- Demo: [Jupyter Agent 2 Demo](https://huggingface.co/spaces/lvwerra/jupyter-agent-2)
- License: Apache-2.0

### Updates

**04/09/2025**: We have added original tool calls used in the notebook generation and renamed `text` column to `messages` to enable straightforward out-of-the-box training with [TRL](https://github.com/huggingface/trl)! Now you just need `messages` and `tools` columns in your training dataset which you can directly pass to [SFTTrainer](https://huggingface.co/docs/trl/en/dataset_formats#tool-calling).

## Uses

Jupyter Agent Dataset allows users to train code agents that are able to:
- Read notebook and dataset context
- Execute Python code (e.g., pandas, numpy, matplotlib) to answer dataset-grounded questions
- Produce step-by-step solutions with intermediate computations

We trained [Qwen-3-4b-Instruct-2507](https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507) and [Qwen-3-4b-Thinking-2507](https://huggingface.co/Qwen/Qwen3-4B-Thinking-2507) on Jupyter Agent Dataset using [TRL](https://github.com/huggingface/trl) and evaluated the agent efficiency on DABstep benchmarks, which evaluates models on their ability to generate code which answers questions about provided datasets.

The dataset helps both models to achieve significant gains **up to 20%** on the DABstep easy score:
![image/png](https://cdn-uploads.huggingface.co/production/uploads/650ed7adf141bc34f91a12ae/WAgyjhdh-ObZ_bmT-9R59.png)

We also observed the ability of the dataset to enhance model's EDA and coding skills which improve the hard score:
![image/png](https://cdn-uploads.huggingface.co/production/uploads/650ed7adf141bc34f91a12ae/8FHBTNSpfbCtHY3Ti0G4e.png)

## Dataset Structure

Each example contains the LLM-generated notebook and its respective QA pair, derived from the linked Kaggle notebook using real Kaggle datasets with the following keys:

- `id`: Unique identifier for the notebook and question pair number.
- `messages`: Synthetic notebook in ChatML format which enables out-of-the-box training.
- `question`: Natural-language question grounded in the notebook/dataset.
- `answer`: Verified final answer in short form.
- `edu_score`: Educational quality score used for filtering (LLM-assigned).
- `files_used`: Files used in the original referenced Kaggle notebook for which the analysis was done.
- `packages_used`: Packages used in the original referenced Kaggle notebook whic were used for the analysis.
- `kaggle_dataset_name`: Full Kaggle source dataset name, suited for Kaggle Hub download.
- `executor_type`: Code executor, used for generating execution traces (either E2B or LLM/Qwen-Coder).
- `original_notebook`: Original Kaggle source notebook, used for QA and code generation.
- `tools`: Tool calls used for the notebook generation.

Notes:
- The dataset contains derived synthetic QA pairs and traces; it does not redistribute original Kaggle datasets or full notebook contents.

## Dataset Creation

![image/png](https://cdn-uploads.huggingface.co/production/uploads/650ed7adf141bc34f91a12ae/Qbu-WR9wcbWVquy7bZlYg.png)

### Data Sourcing and Preparation

1. Large-scale deduplication of Kaggle notebooks — Derived from public Kaggle notebooks ([Meta Kaggle Code](https://www.kaggle.com/datasets/kaggle/meta-kaggle-code)) and linked datasets metadata using [Datatrove](https://github.com/huggingface/datatrove/).
2. Downloading linked datasets — Auto-fetched via Kaggle metadata ([Meta Kaggle](https://www.kaggle.com/datasets/kaggle/meta-kaggle)); ensured notebooks are end-to-end runnable for trace execution and agent training.
3. Educational scoring — Used [Qwen-32B](https://huggingface.co/Qwen/Qwen3-32B) scoring notebooks for their educational quality; selected high-quality sections (not whole notebooks) to avoid trivial/broken code - better notebook sources allowed us to yield better synthetic data.
4. Filtering irrelevant notebooks — Excluded LLM-training and non–data analysis notebooks; removed notebooks that didn’t use datasets via an LLM-assisted filter.

You can use sourced Kaggle datasets directly with E2B code execution using the following code:

```python
import kagglehub
import e2b_code_interpreter as e2b
from datasets import load_dataset

# load the Jupyter Agent Dataset
ds = load_dataset("jupyter-agent/jupyter-agent-dataset", split="thinking")
# get the kaggle dataset name
dataset_name = ds[0]["kaggle_dataset_name"]
# load the dataset locally from Kaggle Hub
path = kagglehub.dataset_download(dataset_name)
print(path) # this is the folder path where the dataset is downloaded
# initialize sandbox
sandbox_init = e2b.Sandbox(timeout=240)
# write used file to E2B sandbox
file_name = ds[0]["files_used"][0]
file_name = file_name.split('/')[-1] if '/' in file_name else file_name
with open(f"{path}/{file_name}", "rb") as file:
    sandbox_init.files.write(f"/home/user/input/{file_name}", file)
# execute code with E2B
execution = sandbox_init.run_code("<some code>")
```

### Synthetic Notebook Generation

1. QA generation — Produced dataset-grounded QA pairs from cleaned notebooks using a two-step process: (a) [Qwen-32B](https://huggingface.co/Qwen/Qwen3-32B) generates question and candidate answer, (b) another LLM validates with notebook context to reduce hallucinations.
2. Traces generation — Used [Qwen-Coder-480B](https://huggingface.co/Qwen/Qwen3-Coder-480B-A35B-Instruct) for code/thinking; executed with [E2B](https://e2b.dev/) when Kaggle datasets were locally available, otherwise simulated an LLM sandbox with Qwen-Coder.

### Summary

- [Datatrove](https://github.com/huggingface/datatrove/) for large-scale processing of real Kaggle notebooks and their linked Kaggle datasets.
- [Qwen-32B](https://huggingface.co/Qwen/Qwen3-32B) for scoring and QA generation; [Qwen-Coder-480B](https://huggingface.co/Qwen/Qwen3-Coder-480B-A35B-Instruct) for notebook and code execution traces generation.
- [E2B](https://e2b.dev/) for secure, sandboxed execution with authetntic code execution traces.

### Recommendations

Users should be made aware of the risks, biases and limitations of the dataset:
- Licensing and terms: upstream Kaggle notebooks and datasets have their own licenses/ToS. This dataset provides derived artifacts and references; users are responsible for complying with Kaggle ToS and any upstream licenses when accessing original content.
- Data quality: notebooks may contain errors, non-deterministic outputs, or environment-specific behavior. Traces may not be perfectly reproducible across environments.
- LLM-generated artifacts: QA pairs and validations are machine-generated and may contain mistakes. Verify results before use in critical settings.
- Bias: source notebooks and datasets may reflect author/domain biases; generated QAs may inherit those biases.
- Safety: executable traces may include environment-specific code. Run code in secure E2B sandboxes and review before execution.

## Additional Information

### Dataset Creators

1. Baptiste Colle, Hugging Face, baptiste.colle@huggingface.co
2. Hanna Yukhymenko, Hugging Face, hanna.yukhymenko@huggingface.co
3. Leandro von Werra, Hugging Face, leandro@huggingface.co

### Licensing Information

This dataset is released under the Apache License 2.0.
- SPDX identifier: Apache-2.0
- License text: https://www.apache.org/licenses/LICENSE-2.0

Note: While this dataset is Apache-2.0 licensed, any use of referenced Kaggle notebooks or datasets must comply with Kaggle’s Terms of Service and the original authors’ licenses. This dataset aims to include only derived artifacts (e.g., QA pairs, execution traces, metadata references) and not redistribute upstream data.

### Citation Information

```
@misc{jupyteragentdataset,
      title={Jupyter Agent Dataset},
      author={Baptiste Colle and Hanna Yukhymenko and Leandro von Werra},
      year={2025}
}
```