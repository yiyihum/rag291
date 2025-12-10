---
license: apache-2.0
task_categories:
- text-generation
tags:
- biology
- DNA
- genomics
- genetics
- metagenomics
- fasta
- json
size_categories:
- n>1T
---

# OpenGenome2

<p align="center">
<img src="https://cdn-uploads.huggingface.co/production/uploads/649aee789fc303937a045f6a/Ma6udvzIkeAypUXcH-FJR.jpeg" width="70%" />
</p>

OpenGenome2 is a database of nearly 9 trillion base pairs of curated DNA from across all domains of life. Collected from diverse species and public data sources, OpenGenome2 was used to train Evo 2 models. Please refer to the [Evo 2 preprint](https://www.biorxiv.org/content/10.1101/2025.02.18.638918v1) or  [github repository](https://github.com/ArcInstitute/evo2) for further details and usage examples.

We provide OpenGenome2 in two formats, the dataset is organized into two main directories to reflect this:
- **fasta** which contain the DNA sequences
- **jsonl** which include the specific preprocessed sequences used for Evo 2 pretraining, such as adding special tokens and phylogenetic tags

This dataset was specifically curated and preprocessed for training the Evo 2 family of genomic language models and can be used for training models or bioinformatics.

## Dataset Statistics
- **Total size**: 8.8 trillion base pairs
- **Coverage**: All domains of life (Bacteria, Archaea, Eukaryota, Viruses)
- **Formats available**: FASTA, JSONL

## Data Sources

The dataset combines sequences from various public databases and repositories:
- **Prokaryotic genomes**: GTDBv220, IMG/PR
- **Metagenomics**: MGD DB
- **Viral sequences**: IMG/VR
- **Eukaryotic data**: NCBI, Ensembl (from which we identified mRNAs, genomic windows)
- **Eukaryotic elements**: Eukaryotic Promoter Database new (EPDnew)
- **RNA sequences**: RNAcentral, Rfam
- **Organellar genomes**: Various organelles

## Training Data Composition

Evo 2 uses a two stage to train on OpenGenome2, first pretraining on a focused dataset at shorter sequence length and then longer sequence length with more full genomes and special tags.

### Phase 1: Pretraining

| Dataset | Number of Tokens (billions) | Composition | Evo 2 Dataloader Weight |
|---------|------------------------------|-------------|-----------------|
| GTDBv220 + IMG/PR | 351 | 18.93% | 18.00% |
| Metagenomics (MGD DB) | 854 | 46.06% | 24.00% |
| IMG/VR | 34 | 1.83% | 3.00% |
| Euk mRNA stitched | 99 | 5.34% | 9.00% |
| Eukaryotic mRNAs (Ensembl, NCBI) | 89 | 4.80% | 9.00% |
| Euk 5kb windows stitched | 405 | 21.84% | 35.00% |
| Organelles | 3 | 0.16% | 0.50% |
| ncRNA (RNAcentral, Rfam, Ensembl, NCBI) | 19 | 1.02% | 2.00% |
| Eukaryotic Promoter Database new (EPDnew) | 0.11 | 0.01% | 0.02% |

### Phase 2: Context Extension

| Dataset | Number of Tokens (billions) | Composition | Evo 2 Dataloader Weight |
|---------|------------------------------|-------------|-----------------|
| TAGGED/Long: GTDBv220 + IMG/PR | 351 | 4.08% | 24.00% |
| Metagenomics (MGD DB) | 854 | 9.93% | 5.00% |
| TAGGED/Long: IMG/VR | 34 | 0.40% | 2.00% |
| ncRNA (RNAcentral, Rfam, Ensembl, NCBI) | 19 | 0.22% | 1.00% |
| Eukaryotic Promoter Database new (EPDnew) | 0.11 | 0.00% | 0.01% |
| Organelles | 3 | 0.03% | 0.25% |
| Euk mRNA stitched | 99 | 1.15% | 4.50% |
| Eukaryotic mRNAs (Ensembl, NCBI) | 89 | 1.04% | 4.50% |
| Euk 5kb windows stitched | 405 | 4.71% | 5.00% |
| Tagged/Long: NCBI Eukaryote: Animalia | 4,907 | 104.00% | 36.00% |
| Tagged/Long: NCBI Eukaryote: Plantae | 1,652 | 96.00% | 12.00% |
| Tagged/Long: NCBI Eukaryote: Fungi | 156 | 24.00% | 4.00% |
| Tagged/Long: NCBI Eukaryote: Protista | 17 | 0.00% | 0.80% |
| Tagged/Long: NCBI Eukaryote: Chromista | 13 | 6.00% | 0.80% |

## Citation

If you use OpenGenome2 in your research, please cite:

```bibtex
@article{Brixi2025.02.18.638918,
    author = {Brixi, Garyk and Durrant, Matthew G and Ku, Jerome and Poli, Michael and Brockman, Greg and Chang, Daniel and Gonzalez, Gabriel A and King, Samuel H and Li, David B and Merchant, Aditi T and Naghipourfar, Mohsen and Nguyen, Eric and Ricci-Tam, Chiara and Romero, David W and Sun, Gwanggyu and Taghibakshi, Ali and Vorontsov, Anton and Yang, Brandon and Deng, Myra and Gorton, Liv and Nguyen, Nam and Wang, Nicholas K and Adams, Etowah and Baccus, Stephen A and Dillmann, Steven and Ermon, Stefano and Guo, Daniel and Ilango, Rajesh and Janik, Ken and Lu, Amy X and Mehta, Reshma and Mofrad, Mohammad R.K. and Ng, Madelena Y and Pannu, Jaspreet and Re, Christopher and Schmok, Jonathan C and St. John, John and Sullivan, Jeremy and Zhu, Kevin and Zynda, Greg and Balsam, Daniel and Collison, Patrick and Costa, Anthony B. and Hernandez-Boussard, Tina and Ho, Eric and Liu, Ming-Yu and McGrath, Tom and Powell, Kimberly and Burke, Dave P. and Goodarzi, Hani and Hsu, Patrick D and Hie, Brian},
    title = {Genome modeling and design across all domains of life with Evo 2},
    elocation-id = {2025.02.18.638918},
    year = {2025},
    doi = {10.1101/2025.02.18.638918},
    publisher = {Cold Spring Harbor Laboratory},
    URL = {https://www.biorxiv.org/content/early/2025/02/21/2025.02.18.638918},
    eprint = {https://www.biorxiv.org/content/early/2025/02/21/2025.02.18.638918.full.pdf},
    journal = {bioRxiv}
}
```

OpenGenome2 incorporates data from multiple public databases. Please also cite the original data sources as appropriate, and refer to the [Evo 2 preprint](https://www.biorxiv.org/content/10.1101/2025.02.18.638918v1) for further details.

**GTDB (Genome Taxonomy Database):**
Parks, D. H., Chuvochina, M., Rinke, C., Mussig, A. J., Chaumeil, P.-A., & Hugenholtz, P. (2022). GTDB: an ongoing census of bacterial and archaeal diversity through a phylogenetically consistent, rank normalized and complete genome-based taxonomy. *Nucleic Acids Research*, 50(D1), D785–D794.

**Metagenomics (MGD DB):**
Durrant, M. G., Perry, N. T., Pai, J. J., Jangid, A. R., Athukoralage, J. S., Hiraizumi, M., McSpedon, J. P., Pawluk, A., Nishimura, H., Konermann, S., & Hsu, P. D. (2024). Bridge RNAs direct programmable recombination of target and donor DNA. *Nature*, 630(8018), 984–993.

Additional data sources include NCBI, Ensembl, IMG/VR, RNAcentral, Rfam, and EPDnew databases.

## License

Apache 2.0