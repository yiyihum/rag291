---
license: mit
task_categories:
- text-generation
language:
- en
pretty_name: Kyoto Corpus
size_categories:
- 1B<n<10B
---

# Kyoto-Corpus

**Kyoto-Corpus** is a high-quality, small-scale dataset designed for the instruction tuning of Small Language Models (SLMs).

![Lille-Header](assets/lille-header.png)

The philosophy behind Kyoto-Corpus is "quality over quantity." Instead of being an entirely new dataset, it is a carefully curated, filtered, and unified collection of some of the best publicly available instruction and chat datasets. This process creates a clean, diverse, and effective corpus for training capable models like **Lille-130M-Instruct**.

---

## ✨ Features

*   **Diverse & High-Quality Sources:** The corpus is built by aggregating well-regarded datasets covering general chat, instruction following, mathematics, and knowledge-based Q&A.
*   **Unified Chat Format:** All data is standardized into a consistent chat format using special tokens (`<|startoftext|>`, `<|user|>`, `<|assistant|>`, `<|endoftext|>`), making it ready to use with the **[Hastings](https://github.com/Nikityyy/Hastings)** tokenizer.
*   **Careful Filtering & Deduplication:** The creation pipeline applies strict quality controls, including filtering out conversations that are too long (max 512 tokens), ensuring proper turn structure, and removing duplicate entries across all source datasets.
*   **Optimized for Small Models:** The token limit and curated nature make this dataset particularly well-suited for training and fine-tuning SLMs without requiring massive computational resources.
*   **Multiple Formats:** The dataset is available in two formats:
    *   **Parquet**
    *   **Plain Text**
*   **Transparent & Reproducible:** The scripts used to generate the entire corpus from the source datasets are included in this repository, ensuring full transparency.

## 📊 Dataset Composition

Kyoto-Corpus is a blend of the following open-source datasets. The creation script processes, filters, and deduplicates the combined data to form the final corpus.

| Source Dataset | Type | Original Hugging Face Link |
| :--- | :--- | :--- |
| **ultrachat_200k** | General Purpose | [`HuggingFaceH4/ultrachat_200k`](https://huggingface.co/datasets/HuggingFaceH4/ultrachat_200k) |
| **smoltalk2** | General Purpose | [`HuggingFaceTB/smoltalk2`](https://huggingface.co/datasets/HuggingFaceTB/smoltalk2) |
| **smol-smoltalk** | General Purpose | [`HuggingFaceTB/smol-smoltalk`](https://huggingface.co/datasets/HuggingFaceTB/smol-smoltalk) |
| **WildChat-1M** | General Purpose | [`allenai/WildChat-1M`](https://huggingface.co/datasets/allenai/WildChat-1M) |
| **WizardLM_evol_instruct_V2** | General Purpose | [`WizardLMTeam/WizardLM_evol_instruct_V2_196k`](https://huggingface.co/datasets/WizardLMTeam/WizardLM_evol_instruct_V2_196k) |
| **ifeval-like-data** | Instruction | [`argilla/ifeval-like-data`](https://huggingface.co/datasets/argilla/ifeval-like-data) |
| **tulu-3-sft-personas** | Instruction | [`allenai/tulu-3-sft-personas-instruction-following`](https://huggingface.co/datasets/allenai/tulu-3-sft-personas-instruction-following) |
| **mmlu** | Knowledge | [`cais/mmlu`](https://huggingface.co/datasets/cais/mmlu) |
| **gsm8k** | Math | [`openai/gsm8k`](https://huggingface.co/datasets/openai/gsm8k) |
| **math_qa** | Math | [`allenai/math_qa`](https://huggingface.co/datasets/allenai/math_qa) |
| **MetaMathQA** | Math | [`meta-math/MetaMathQA`](https://huggingface.co/datasets/meta-math/MetaMathQA) |

## 📝 Data Format

Each entry in the dataset follows a strict conversational structure.

#### Parquet Format (Structured)

The Parquet file contains a `messages` column, which holds a list of dictionaries, and a `hf_dataset` column indicating the original source.

```json
{
  "messages": [
    {"role": "user", "content": "What is the capital of Japan?"},
    {"role": "assistant", "content": "The capital of Japan is Tokyo."}
  ],
  "hf_dataset": "Username/Repository"
}
```

#### Plain Text Format

The `train.txt` file contains the fully formatted string for each conversation, ready for tokenization.

```
<|startoftext|><|user|>What is the capital of Japan?<|assistant|>The capital of Japan is Tokyo.<|endoftext|>
```

## 🚀 Usage

You can easily load Kyoto-Corpus from the Hugging Face Hub using the `datasets` library.

```python
from datasets import load_dataset

ds_parquet = load_dataset("Nikityyy/Kyoto-Corpus", split="train")
print(ds_parquet[0])
```

## 🛠️ How It Was Created

The entire corpus was generated using the scripts in this repository (`script_parquet.py` and `script_small.py`). The process is as follows:

1.  **Stream Data:** The script streams each source dataset from the Hugging Face Hub to minimize local storage requirements.
2.  **Process in Parallel:** Data is processed in batches using Python's `multiprocessing` to leverage all available CPU cores.
3.  **Format Unification:** Each entry is converted from its original format (e.g., `flat`, `mcq`, conversational) into the standardized chat structure.
4.  **Filter & Truncate:** Conversations are validated for correctness (e.g., must start with a user turn). They are truncated or skipped if their tokenized length exceeds the `MAX_TOKENS` limit (512).
5.  **Deduplicate:** A hash of each processed entry is generated (using `xxhash` for speed), and only unique entries are kept, ensuring no duplicates exist within or across datasets.
6.  **Save Output:** The final, clean entries are saved to the Parquet and plain text files, along with a `data.json` file containing detailed statistics about the creation process.

## 🛠️ The truly open-source repos

Kyoto-Corpus is a key component of my initiative to build and release a complete, truly open-source stack for language modeling. All components are designed to work together seamlessly.

*   **Tokenizer:** **[Hastings](https://github.com/Nikityyy/Hastings)** - A modern, efficient tokenizer with a 32k vocabulary.
*   **Dataset:** **[Kyoto-Corpus](https://github.com/Nikityyy/Kyoto-Corpus)** (this repository) - A high-quality, small-scale dataset for instruction tuning.
*   **Model:** **[lille](https://github.com/Nikityyy/lille)** - A powerful 130-million-parameter model trained from scratch using the Hastings tokenizer.
*   **Optimizer:** **[Sophia-Triton](https://github.com/Nikityyy/Sophia-Triton)** - A memory-efficient, Triton-based implementation of the SophiaG optimizer.
*   **Evaluations:** **[simple-eval](https://github.com/Nikityyy/simple-eval)** - A straightforward framework for evaluating model performance using an LLM as a Judge.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/Nikityyy/Kyoto-Corpus/blob/main/LICENSE) file for details.