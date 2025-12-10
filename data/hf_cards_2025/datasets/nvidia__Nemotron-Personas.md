---
license: cc-by-4.0
task_categories:
- text-generation
language:
- en
tags:
- synthetic
- personas
- NVIDIA
size_categories:
- 100K<n<1M
---

Nemotron-Personas: Synthetic Personas Aligned to Real-World Distributions
=========================================================================
<center>
  <img src="images/nemotron_persona_approach.png" alt="gretelai/synthetic_text_to_sql v1" width="400px">
  <p><em>A compound AI approach to personas grounded in real-world distributions</em></p>
</center>

## Dataset Overview
Nemotron-Personas is an open-source (CC BY 4.0) dataset of synthetically-generated personas grounded in real-world demographic, geographic and personality trait distributions to capture the diversity and richness of the population. It is the first dataset of its kind aligned with statistics for names, sex, age, background, marital status, education, occupation and location, among other attributes. With an initial release focused on the United States, this dataset provides high-quality personas for a variety of modeling use-cases.

The dataset can be used to improve diversity of synthetically-generated data, mitigate data/model biases, and prevent model collapse. In particular, the dataset is designed to be more representative of underlying demographic distributions along multiple axes, including age (e.g. older personas), geography (e.g., rural personas), education, occupation and ethnicity, as compared to past persona datasets.

Produced using [Gretel Data Designer](https://gretel.ai/), an enterprise-grade compound AI system for synthetic data generation (now part of NVIDIA and coming to [NeMo](https://www.nvidia.com/en-us/ai-data-science/products/nemo/) soon), the dataset leverages a proprietary Probabilistic Graphical Model (PGM) along with Apache-2.0 licensed [mistralai/Mistral-Nemo-Instruct-2407](https://huggingface.co/mistralai/Mistral-Nemo-Instruct-2407) and [mistralai/Mixtral-8x22B-v0.1](https://huggingface.co/mistralai/Mixtral-8x22B-v0.1) models and an ever-expanding set of validators and evaluators built into Data Designer. An extended version of Nemotron-Personas is available for use in Data Designer itself.

## What is NOT in the dataset
Given the emphasis on personas, the dataset excludes other fields available in Data Designer, e.g., first/middle/last names and synthetic addresses. Also excluded are personas generally of relevance to enterprise clients (e.g., finance, healthcare). Please [reach out](https://www.nvidia.com/en-us/data-center/products/ai-enterprise/contact-sales/) to explore enterprise use-cases.

All data, while mirroring real-world distributions, is completely artificially generated. Any similarity in names or persona descriptions to actual persons, living or dead, is purely coincidental.

This dataset is ready for commercial/non-commercial use.

# Dataset Details

* 100k records with 22 fields: 6 persona fields and 16 contextual fields
* ~54M tokens, including ~23.6M persona tokens
* Comprehensive coverage across demographic, geographic, and personality trait axes
* Over 560 distinct professional occupations, all grounded in real-world distributions

## Seed Data
In order to capture the socio-demographic and geographic diversity and complexity of the US population, Nemotron-Personas leveraged open-source ([CC0-licensed](https://creativecommons.org/public-domain/cc0/)) aggregated statistical data from
* The US Census Bureau, specifically the [American Community Survey](https://catalog.data.gov/dataset/american-community-survey-5-year-estimates-data-profiles-5-year).
* The study “Race and ethnicity data for first, middle, and surnames,” [Rosenman et al. (2023)](https://www.nature.com/articles/s41597-023-02202-2); specifically, the dataset located [here](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/SGKW0K).

## Schema
The dataset includes 22 fields: 6 persona fields and 16 contextual fields shown below. Researchers will find many contextual fields useful in zoning in on specific personas, which is challenging to do with existing datasets. 
<center>
  <img src="images/nemotron_personas_schema.png" width="700px">
</center>

## Field & Token Counts
54M tokens across 100,000 records and 22 columns, excluding the globally unique identifier. Note that data covers 50 states as well as Puerto Rico and Virgin Islands.
<center>
  <img src="images/nemotron_personas_field_stats.png" width="500px">
</center>


# Dataset Description & Quality Assessment
The analysis below provides a breakdown across various axes of the dataset to emphasize the built-in diversity and pattern complexity of data.

## Names
Since the focus of this dataset is on personas, names aren’t provided as dedicated fields. However, infused into persona prompts are 136,000 unique first_names, 126,000 unique middle names, and 338,000 unique surnames sourced from Rosenman et al. (2023).

## Age distribution
The distribution of our persona ages takes the form of a bulging population pyramid that reflects historical birth rates, mortality trends, and migration patterns. This is in stark contrast to a bell curve distribution typically produced by an LLM alone. Overall the distribution is right-skewed and distinctly non-Gaussian. Note that minors are excluded from this dataset (see the Ethics section below).
<center>
  <img src="images/nemotron_personas_age_group_distribution.png" width="600px">
</center>

## Marital Status by Age Group
The heatmap below displays the fraction of people for each age cohort who are (1) never married, (2) currently married, (3) separated, (4) divorced, or (5) widowed. It highlights how marital status shifts over the life course in the US with “never married” dominating late teens and early twenties, “married” climbing rapidly in twenties and peaking in mid-fourties, divorced and widowed being much more pronounced in later stages of life. All of these considerations are of relevance to informing life experiences and personas.
<center>
  <img src="images/nemotron_personas_marital_status_distribution.png" width="600px">
</center>

## Education Level by Age Group
The heatmap below captures intricate patterns of educational attainment across age cohorts. For example, note how the share of high-school-only and no-diploma individuals ebbs then resurges among the oldest age groups, reflecting historical shifts in access and in social norms.
<center>
  <img src="images/nemotron_personas_education_distribution.png" width="600px">
</center>

## Geographic Intricacies of Education Attainment
This slice of our dataset demonstrates how geography informs education and therefore persona descriptions. The choropleth map shows, for each U.S. state, the share of residents age 25 and older who hold at least a bachelor’s degree. No LLM in our testing was able to generate data of this fidelity.
<center>
  <img src="images/nemotron_personas_education_map.png" width="700px">
  <p><em>Left: Nemotron-Personas dataset. Right: <a href="https://en.wikipedia.org/wiki/Educational_attainment_in_the_United_States">Educational attainment in the United States, Wikipedia</a></em></p>
</center>

## Occupational Categories
The treemap below reflects the richness of our dataset with respect to professional occupations of personas. Represented in our dataset are over 560 occupation categories that are further informed by demographic and geographic distributions.
<center>
  <img src="images/nemotron_personas_occupation_tree_map.png" width="600px">
</center>

## Persona diversity
The attributes above (and many more) ultimately affect the diversity of the synthetic personas being generated. As an example, the analysis below highlights a multitude of clusters within professional persona descriptions. These clusters are identified by clustering embeddings and reducing dimensionality to 2D. 
<center>
  <img src="images/nemotron_personas_professional_personas_clustering.png" width="600px">
</center>

# How to use it
You can load the dataset with the following lines of code.
```python
from datasets import load_dataset

nemotron_personas = load_dataset("nvidia/Nemotron-Personas", "train")
```

# License/Terms of Use
This dataset is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0) available at [https://creativecommons.org/licenses/by/4.0/legalcode](https://creativecommons.org/licenses/by/4.0/legalcode).

Data Developer: NVIDIA

# Use Case:
Developers training LLMs and/or looking to improve diversity of synthetically generated data, mitigate data/model biases, and prevent model collapse.

# Release Date:
06/09/2025

# Data Version
1.0 (06/09/2025)

# Intended use
The Nemotron-Personas dataset is intended to be used by the community to continue to improve open models and push the state of the art. The data may be freely used to train any model. We welcome feedback from the open-source community and invite developers, researchers, and data enthusiasts to explore the dataset and build upon it.

# Ethical Considerations:
NVIDIA believes [Trustworthy AI](https://www.nvidia.com/en-us/ai-data-science/trustworthy-ai/) is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our terms of service, developers should work with their internal teams to ensure this dataset meets requirements for the relevant industry and use case and addresses unforeseen product misuse.

The Nemotron-Personas dataset is grounded in distributions of self-reported demographic data in the US Census. As such, its primary goal is to combat missing data and/or potential biases present in model training data today, especially when it comes to existing persona datasets used in synthetic data generation. Despite the improved data diversity and fidelity to the US population, we are still limited by data availability and reasonable model complexity. This results in some necessary independence assumptions; for instance, that occupations are independent of location (zip code) given education, age and sex. Similarly, comprehensive statistics on gender, independent of sex, are not available from the Census Bureau. We leave further efforts to improve fidelity to future work.

Note that the dataset is focused on adults only.

Please report security vulnerabilities or NVIDIA AI concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).


# Citation
If you find the data useful, please cite:
```
@software{nvidia/Nemotron-Personas,
  author = {Meyer, Yev and Corneil, Dane},
  title = {{Nemotron-Personas}: Synthetic Personas Aligned to Real-World Distributions
},
  month = {June},
  year = {2025},
  url = {https://huggingface.co/datasets/nvidia/Nemotron-Personas}
}
```
