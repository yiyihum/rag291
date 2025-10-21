---
license: cc0-1.0
language:
- en
base_model: EleutherAI/pythia-1b
library_name: transformers
tags:
- biology
- scRNAseq
---


# Overview
This is the C2S-Scale-1B pretrained model, based on the Pythia-1b architecture 
developed by EleutherAI, fine-tuned using the Cell2Sentence (C2S) framework on a wide array of single-cell RNA sequencing 
(scRNA-seq) datasets from CellxGene and the Human Cell Atlas. Cell2Sentence is a cutting-edge method that 
adapts large language models (LLMs) to single-cell biology by converting scRNA-seq data into 
"cell sentences" — ordered sequences of gene names based on expression levels. This model has been trained 
to perform a broad range of single- and multi-cell tasks, making it a versatile tool for various single-cell 
and multi-cell analyses.

# Training Data
This model was trained on over 57 million human and mouse cells gathered from over 800 single-cell RNA sequencing 
datasets from CellxGene and the Human Cell Atlas. This dataset covers a broad range of cell types and conditions
from multiple tissues in both human and mouse.

This model was trained with a variable number of genes per cell sentence, with a maximum context length of 8192 tokens.
The context length of the default Pythia model was extended using rotary positional embeddings prior to C2S training.
- Cells: For multi cell samples, each training sample contained between 5 and 20 cells, with the same number of genes for each of the cells in the same sample.
- Genes: For single cell samples, each cell sentence contained between 100 and 2048 genes. For multi cell samples, each cell sentence per cell contained between 100 and 400 genes.

# Tasks
This model is designed for the following tasks:

Single-Cell Tasks
- Unconditional single-cell generation: Generate single cell sentences unconditionally.
- Cell type prediction: Predict the cell type of a given single cell.
- Cell type-conditioned generation: Generate a single cell sentence conditioned on a specific cell type.

Multi-Cell Tasks
- Unconditional multi-cell generation: Generate multiple cell sentences unconditionally.
- Tissue prediction: Predict the tissue of origin for a group of cells.
- Cell type prediction: Predict the cell type for each cell in a group of multiple cells.
- Tissue-conditioned multi-cell generation: Generate multiple cell sentences conditioned on a specific tissue.
- Cell type-conditioned multi-cell generation: Generate multiple cell sentences conditioned on the cell type of each individual cell.
- Multi-cells to abstract: Generate a research paper abstract based on the provided multi-cell sentences.
- Abstract to multi-cells: Generate multiple cell sentences based on a given research paper abstract.

Gene Set Tasks
- Gene set name to genes: Generate an alphabetical list of genes given a gene set name.
- Genes to gene set name: Generate the name of a gene set given an alphabetical list of genes.

# Cell2Sentence Links
- GitHub: https://github.com/vandijklab/cell2sentence (Note: Codebase has CC BY-NC-ND 4.0 license. Only weights shared on Hugging Face are CC0 1.0)
- Paper: https://www.biorxiv.org/content/10.1101/2023.09.11.557287v3

# Pythia Links
- Paper: https://arxiv.org/pdf/2304.01373
- Hugging Face: https://huggingface.co/EleutherAI/pythia-410m