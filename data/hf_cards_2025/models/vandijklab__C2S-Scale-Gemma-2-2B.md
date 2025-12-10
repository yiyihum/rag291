---
license: cc-by-4.0
language:
- en
base_model: google/gemma-2-2b
library_name: transformers
pipeline_tag: text-generation
tags:
- biology
- scRNAseq
- gemma2
- genomics
- computational-biology
- bioinformatics
- gene-expression
- cell-biology
- transformers
- pytorch
- cell-type-annotation
- Question Answering
---

# C2S-Scale-Gemma-2B model card

**GitHub homepage:** [Cell2Sentence GitHub](https://github.com/vandijklab/cell2sentence)

**Model documentation:** [Cell2Sentence Documentation](https://vandijklab-cell2sentence.readthedocs.io/en/latest/)

**Resources:**

*   C2S-Scale Paper: [Scaling Large Language Models for Next-Generation Single-Cell Analysis](https://www.biorxiv.org/content/10.1101/2025.04.14.648850v1)
*   HuggingFace C2S Collection: [C2S-Scale Models](https://huggingface.co/collections/vandijklab/c2s-scale-gemma-models-68ed5e4d3b55c8c29682d842)
*   GitHub Repository: [vandijklab/cell2sentence](https://github.com/vandijklab/cell2sentence) (for code, tutorials, and discussions)
*   Google Research Blog Post: [Teaching machines the language of biology](https://research.google/blog/teaching-machines-the-language-of-biology-scaling-large-language-models-for-next-generation-single-cell-analysis/)

**Author:** van Dijk Lab (Yale), Google Research, Google DeepMind


## Model information

This section describes the C2S-Scale model and how to use it.

### Description

C2S-Scale-Gemma-2B is a state-of-the-art, open language model built upon the Gemma-2 2B 
architecture and fine-tuned for single-cell biology. Developed through the Cell2Sentence 
(C2S) framework, the model processes and understands single-cell RNA sequencing 
(scRNA-seq) data by treating it as a language. It converts high-dimensional scRNA-seq 
expression data into "cell sentences" - ordered sequences of gene names - enabling a 
wide range of biological analyses.

This work is the result of a collaboration between Yale University, Google Research, 
and Google DeepMind to scale up C2S models. The C2S-Scale models were trained on 
Google's TPU v5s, which allowed for a significant increase in model size and 
capability. These models excel at tasks such as cell type prediction, tissue 
classification, and generating biologically meaningful cell representations.

**Key Features**

*   Versatility: Demonstrates strong performance across a diverse set of single-cell and multi-cell tasks.
*   Scalability: Trained on a massive dataset of over 57 million cells, showcasing the power of scaling LLMs for biological data.
*   Generative Power: Capable of generating realistic single-cell gene expression profiles.
*   Foundation for Fine-tuning: Can serve as a powerful pretrained foundation for specialized, domain-specific single-cell analysis tasks.

**Potential Applications**

C2S-Scale can be a valuable tool for researchers in the following areas:

*   In Silico Experiments: Generate cells under specific conditions or predict perturbational changes to form and test new biological hypotheses.
*   Cell Atlas Annotation: Streamline the process of annotating large-scale single-cell datasets by predicting cell types and tissues.
*   Biomarker Discovery: Analyze gene patterns within cell sentences to identify potential markers for specific cell states or diseases.

### How to use

Below are code snippets to help you get started running the model locally on a GPU. 
The model can be used for various tasks, further described in the C2S-Scale paper.

#### Formatting prompts for cell type prediction

To perform cell type prediction, the model expects a prompt containing the cell sentence followed by a query.

```python
# A "cell sentence" is a space-separated string of gene names
# ordered by expression level, from highest to lowest.
cell_sentence = "MALAT1 TMSB4X B2M EEF1A1 H3F3B ACTB FTL RPL13 ..." # Truncated for example purposes
num_genes = 1000
organism = "Homo sapiens"

# Construct the prompt for cell type prediction
prompt = f"""The following is a list of {num_genes} gene names ordered by descending expression level in a {organism} cell. Your task is to give the cell type which this cell belongs to based on its gene expression.
Cell sentence: {cell_sentence}.
The cell type corresponding to these genes is:"""

print(prompt)
```

The resulting prompt is in the format expected by the model for this task:
```none
The following is a list of 1000 gene names ordered by descending expression level in a Homo sapiens cell. Your task is to give the cell type which this cell belongs to based on its gene expression.
Cell sentence: MALAT1 TMSB4X B2M EEF1A1 H3F3B ACTB FTL RPL13 ... .
The cell type corresponding to these genes is:
```

#### Running the model on predictive tasks

```python
# pip install accelerate transformers sentencepiece
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"

# Load model directly from Hugging Face Hub
model_id = "vandijklab/C2S-Scale-Gemma-2-2B"

# Load tokenizer; requires sentencepiece to be installed
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
).to(device)

# Format prompt (see previous section)
cell_sentence = "MALAT1 TMSB4X B2M EEF1A1 H3F3B ACTB FTL RPL13 ..." # Truncated for example, use at least 200 genes for inference
num_genes = 1000
organism = "Homo sapiens"

prompt = f"""The following is a list of {num_genes} gene names ordered by descending expression level in a {organism} cell. Your task is to give the cell type which this cell belongs to based on its gene expression.
Cell sentence: {cell_sentence}.
The cell type corresponding to these genes is:"""

# Prepare tokenized inputs
input_ids = tokenizer(prompt, return_tensors="pt").to(device)

# Generate response
outputs = model.generate(**input_ids, max_new_tokens=20)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)

# The predicted cell type will be the text immediately following the prompt
predicted_cell_type = response.split("The cell type corresponding to these genes is:")[1].strip()
print(f"Predicted Cell Type: {predicted_cell_type}")
```

### Examples

See the following Colab notebooks in our GitHub repository for examples of how to use C2S-Scale models:

*   To quickly get started with the model for tasks like cell type prediction and generation: [C2S Tutorials](https://github.com/vandijklab/cell2sentence/tree/master/tutorials)

### Model architecture overview

*   C2S-Scale is based on the Gemma 2 family of lightweight, state-of-the-art open LLMs, which utilizes a decoder-only transformer architecture.
*   Base Model: Gemma-2 2B.
*   Fine-tuning Data: A comprehensive collection of over 800 datasets from CellxGene and the Human Cell Atlas, totaling over 57 million human and mouse cells.
*   Training Approach: Instruction fine-tuning using the Cell2Sentence framework, which converts scRNA-seq expression data into sequences of gene tokens.


### Technical Specifications

*   Model type: Decoder-only Transformer (based on Gemma-2)
*   Key publication: [Scaling Large Language Models for Next-Generation Single-Cell Analysis](https://www.biorxiv.org/content/10.1101/2025.04.14.648850v1)


### Performance & Validation

The performance of C2S-Scale models was validated on a wide range of single-cell and multi-cell 
tasks, including advanced downstream tasks such as cluster captioning, question answering, 
and perturbation prediction. C2S-Scale models demonstrated significant improvements over 
other open and closed-source models, establishing new state-of-the-art benchmarks for LLMs 
in single-cell biology. Please see our preprint for a full breakdown of performance metrics.

### Inputs and outputs

*   Input: Text. For best performance, prompts should be structured according to the specific task (e.g., cell type prediction, conditioned generation). Inputs are "cell sentences"—ordered, space-separated lists of gene names.
*   Output: Text. The model generates text as a response, which can be a predicted label (like a cell type or tissue), a full cell sentence, or a natural language abstract.

## Dataset details

### Training dataset

**CellxGene and Human Cell Atlas:** The model was trained on a curated collection of over 800 
public scRNA-seq datasets, encompassing more than 57 million cells. This data covers a broad 
range of tissues, cell types, and experimental conditions from both human and mouse, ensuring 
the model learns a robust and generalizable representation of cellular states.

### Evaluation dataset

Evaluation was performed using held-out datasets and standardized benchmarks designed to 
test the model's capabilities on the tasks listed above. All evaluation methodologies followed 
established best practices for splitting data to ensure robust and unbiased assessment.

## License

The model weights shared on Huggingface are CC-by-4.0.

## Implementation information

### Software

The model was trained using [JAX](https://github.com/jax-ml/jax), leveraging Google's TPU v5 
hardware for efficient and large-scale training.

## Use and limitations

### Intended use

*   Research in single-cell genomics and computational biology.
*   As a foundational model for fine-tuning on specific biological domains or datasets.
*   To aid in the annotation and interpretation of large-scale scRNA-seq experiments.

### Benefits

C2S-Scale provides a powerful, versatile, and scalable tool for single-cell analysis. It offers:
*   State-of-the-art performance on a wide range of scRNA-seq tasks.
*   A unified framework for handling diverse single-cell analysis challenges.
*   A foundation for building more specialized models from private or proprietary data.
*   The ability to perform in silico generation of cellular data to explore biological hypotheses.

### Limitations

*   The model is trained on public data and its knowledge is limited to the genes, cell types, and conditions present in that data.
*   Performance on out-of-distribution data (e.g., completely novel cell types or technologies) is not guaranteed and requires validation.
*   Performance of the models on input prompt formats that greatly deviate from training prompt formatting is not guaranteed.

## Citation

```bibtex
@article{Rizvi2025.04.14.648850,
	abstract = {Single-cell RNA sequencing has transformed our understanding of cellular diversity, yet current single-cell foundation models (scFMs) remain limited in their scalability, flexibility across diverse tasks, and ability to natively integrate textual information. In this work, we build upon the Cell2Sentence (C2S) framework, which represents scRNA-seq profiles as textual {\textquotedblleft}cell sentences,{\textquotedblright} to train Large Language Models (LLMs) on a corpus comprising over one billion tokens of transcriptomic data, biological text, and metadata. By scaling model size to 27 billion parameters, we observe consistent improvements in predictive and generative capabilities, as well as the capacity for advanced downstream tasks requiring synthesis of information across multicellular contexts. Through targeted fine-tuning supported by modern reinforcement learning techniques, our approach excels in tasks such as perturbation response prediction, natural language interpretation, and complex biological reasoning. By unifying transcriptomic and textual data at unprecedented scales, this approach not only surpasses both specialized single-cell models and general-purpose LLMs, but also establishes a powerful platform for next-generation single-cell analysis, paving the way for the development of {\textquotedblleft}virtual cells.{\textquotedblright}Competing Interest StatementThe authors have declared no competing interest.},
	author = {Rizvi, Syed Asad and Levine, Daniel and Patel, Aakash and Zhang, Shiyang and Wang, Eric and He, Sizhuang and Zhang, David and Tang, Cerise and Lyu, Zhuoyang and Darji, Rayyan and Li, Chang and Sun, Emily and Jeong, David and Zhao, Lawrence and Kwan, Jennifer and Braun, David and Hafler, Brian and Ishizuka, Jeffrey and Dhodapkar, Rahul M. and Chung, Hattie and Azizi, Shekoofeh and Perozzi, Bryan and van Dijk, David},
	doi = {10.1101/2025.04.14.648850},
	elocation-id = {2025.04.14.648850},
	eprint = {https://www.biorxiv.org/content/early/2025/04/17/2025.04.14.648850.full.pdf},
	journal = {bioRxiv},
	publisher = {Cold Spring Harbor Laboratory},
	title = {Scaling Large Language Models for Next-Generation Single-Cell Analysis},
	url = {https://www.biorxiv.org/content/early/2025/04/17/2025.04.14.648850},
	year = {2025},
	Bdsk-Url-1 = {https://www.biorxiv.org/content/early/2025/04/17/2025.04.14.648850},
	Bdsk-Url-2 = {https://doi.org/10.1101/2025.04.14.648850}}
```

# C2S-Scale Links
- Paper: [Scaling Large Language Models for Next-Generation Single-Cell Analysis](https://www.biorxiv.org/content/10.1101/2025.04.14.648850v1)
- Google Research Blog Post: [Teaching machines the language of biology: Scaling large language models for next-generation single-cell analysis](https://research.google/blog/teaching-machines-the-language-of-biology-scaling-large-language-models-for-next-generation-single-cell-analysis/)
- GitHub: https://github.com/vandijklab/cell2sentence (Note: Codebase has CC BY-NC-ND 4.0 license. Only weights shared on Hugging Face are CC-by-4.0)

# Gemma-2 Links
- HuggingFace: https://huggingface.co/google/gemma-2-2b
- Gemma-2 Blog Post: [Gemma explained: What's new in Gemma 2](https://developers.googleblog.com/en/gemma-explained-new-in-gemma-2/)
- Technical report: https://storage.googleapis.com/deepmind-media/gemma/gemma-2-report.pdf