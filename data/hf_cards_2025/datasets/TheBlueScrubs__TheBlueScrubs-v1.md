---
license: apache-2.0
task_categories:
- text-classification
- text-generation
language:
- en
tags:
- medical
- biology
pretty_name: The Blue Scrubs-v1
size_categories:
- 10B<n<100B
---

![image/png](https://cdn-uploads.huggingface.co/production/uploads/66eb0a4e55940cd564ad8e0a/Dctx8VafCbb__GHl8I-96.png)

# The Blue Scrubs: A comprehensive curated medical dataset derived from the internet.

**Luis Felipe<sup>1,3</sup>, Carlos Garcia<sup>1,3</sup>, Aakash Tripathi<sup>1,3</sup>, Issam El Naqa<sup>1,3</sup>, Monique Shotande<sup>1,3</sup>, Vivek Rudrapatna<sup>2,3</sup>, Ghulam Rasool<sup>1,3</sup>, Gilmer Valdes<sup>1,3</sup>**

1. Machine Learning Department, Moffitt Cancer Center, Tampa, Florida  
2. Center for Real World Evidence, University of California San Francisco, San Francisco, California  
3. [TheBlueScrubs](https://thebluescrubs.ai/)



## 1. Introduction

The need for robust and diverse data to train clinical LLMs is critical given that public repositories are very small. General-purpose datasets like Common Crawl¹ have not only been instrumental in scaling LLMs, but recently, their utility for domain-specific applications has been demonstrated². By meticulously curating and filtering its mathematical content, a recent study by DeepSeek² showed that Common Crawl can be leveraged to create state-of-the-art mathematical and coding reasoning models. This success underscores the transformative potential of leveraging large, heterogeneous datasets to create specialized resources for targeted applications.

While resources like PubMed³ provide a foundation of high-quality clinical and scientific literature, their scope is limited to 1) formal publications, 2) Technical and specialized narrative, and 3) lacks the breadth to capture the wide spectrum of medical discourse that occurs in informal settings, such as patient forums, personal narratives, and health-related online discussions. Additionally, its size in the order of ~10 billion tokens is a limiting factor to train large-scale LLMs³. This limiting factor is not resolved by incorporating other publicly available medical datasets (e.g., clinical guidelines⁴). For instance, the Meditron⁴ suite of models was trained with a total of 70 billion tokens, while the DeepSeekMath 7B model⁵ was finetuned with 120 billion tokens, both of course far from the trillion tokens needed if models are going to be trained from scratch.

To address this gap, we introduce [The Blue Scrubs](https://huggingface.co/datasets/TheBlueScrubs/TheBlueScrubs-v1), a meticulously curated dataset designed to advance the development of medical LLMs. Extracted from the SlimPajama⁶ dataset (670 billion tokens comprising of: Common Crawl, C4, GitHub, books, arXiv, Wikipedia, and StackExchange), which itself is a deduplicated version of the expansive RedPajama⁷ corpus, The Blue Scrubs comprises over **25 billion tokens** of medical content sourced from **11.5 million documents** with quality and safety tags associated with them. This far exceeds the size of PubMed’s corpus—estimated at approximately 10 billion tokens according to Flamholz et al. (2022)—ensuring coverage across diverse medical domains, communication styles, and levels of complexity. By combining the depth of formal medical literature with the breadth of real-world medical conversations, The Blue Scrubs provides a comprehensive training resource to enhance LLM capabilities in addressing the multifaceted challenges of medicine.

### What are we releasing?

We are releasing a curated subset of the SlimPajama dataset, called **The Blue Scrubs**, which includes all texts that scored ≥ 0.8 on our medical probability metric built using a linear classifier with bag-of-words features - technical description provided below. Additionally, the quality of each text was further quantified using the best out of the bag open-source reward model at the time (Llama 3.1 70B Instruct⁹) according to three key evaluation metrics:  
1) medical relevance,  
2) precision and factual detail, and  
3) safety and ethical standards.  

This evaluation by a strong LLM was further validated by a team of clinicians and by Open AI gpt-4o-2024-08-06⁸, showing good concordance with both. For each of these texts in the 25 billion corpus, we provide:

- **Medical Probability Score (0.8 to 1.0):**  
  Indicates how likely the text is to be medical.
- **LLaMA Text Evaluation Scores (1–5 Scale):**  
  Three distinct ratings (each on a 1–5 scale, where 1 is lowest and 5 is highest) from our Llama 3.1 (70B)⁹ evaluation:  
  - Scope of Medical Relevance  
  - Precision and Factual Detail  
  - Safety and Ethical Standards
- **Full SlimPajama with medical probability of text:**  
  Identifies which SlimPajama source the text was drawn from.
- **Cancer vs. Non-Cancer Label:**  
  Highlights whether the text pertains to cancer-related content.

Below we provide a diagram of our data pipeline, **Figure 1**, together with an example of the medical texts included in The BlueScrubs and its classification.

![image/png](https://cdn-uploads.huggingface.co/production/uploads/66eb0a4e55940cd564ad8e0a/EEddCSnuy-_nmQDZrjgbU.png)

> **Figure 1:** The Blue Scrubs creation process through filtering, evaluation and labeling.  

**Example Text:**

*Niemann-Pick disease types A, B, and C are a group of autosomal recessive lysosomal storage disorders affecting metabolism of specific lipids within cells. Niemann-Pick disease types A and B are caused by a deficiency of sphingomyelinase which results in extensive storage of sphingomyelin and cholesterol in the liver, spleen, lungs, and, to a lesser degree, brain. Niemann-Pick type A disease is more severe than type B and characterized by early onset with feeding problems, dystrophy, persistent jaundice, development of hepatosplenomegaly, neurological deterioration, deafness, and blindness leading to death by age 3. Niemann-Pick type B disease is limited to visceral symptoms with survival into adulthood. Some patients have been described with intermediary phenotypes. Characteristic of the disease are large lipid-laden foam cells. Approximately 50% of cases have cherry-red spots in the macula. Sphingomyelinase is encoded by the SMPD1 gene. The combined prevalence of NPA and NPB is estimated to be 1 in 250,000. NPA and NPB are inherited in an autosomal recessive manner and are caused by mutations in the SMPD1 gene. Although there is a higher frequency of type A among the Ashkenazi Jewish population, both types are pan-ethnic. Individuals with NPD types A and B typically have elevation of the oxysterol lyso-sphingomyelin (LSM), lyso-spingomyelin 509 (LSM 509), cholestane-3 beta, 5 alpha, 6 beta-triol and/or 7-ketocholesterol (7-KC) may also be elevated. Molecular genetic testing for NPA and NPB disease is also available (see NPABZ / Niemann-Pick Disease, Types A and B, Full Gene Analysis). The incidence of NPC is approximately 1 in 120,000 to 150,000 live births. NPC is an autosomal recessive condition and is caused by mutations in either the NPC1 or NPC2 genes. Individuals with NPC exhibit elevated levels of oxysterol cholestane-3 beta,5 alpha,6 beta-triol (COT); lyso-sphingomyelin 509 (LSM 509) and 7-ketocholesterol (7-KC) may also be elevated. The diagnosis of NPC can be confirmed by demonstration of impaired cholesterol esterification and positive filipin staining in cultured fibroblasts (NIEM / Niemann-Pick Type C Detection, Fibroblasts). For molecular confirmation, genetic testing for NPC disease can be performed (see NPCZ / Niemann-Pick Type C Disease, Full Gene Analysis). An elevation of cholestane-3-beta, 5-alpha, 6-beta-triol (COT) is highly suggestive of Niemann-Pick disease type C (NPC). An elevation of lyso-sphingomyelin (LSM) is highly suggestive of Niemann-Pick type A or B (NPA or NPB) disease.*

- **Probability (Medical Score):** 0.99  
- **Scope of Medical Relevance:** 5.0  
- **Precision and Factual Detail:** 5.0  
- **Safety and Ethical Standards:** 5.0  

Following is a general breakdown of retained medical texts and tokens by original RedPajama source after applying our data pipelines, **Table 1**.

| Source                  | Total Texts | Total Tokens    | Cancer Texts | Cancer Tokens     |
|-------------------------|------------:|----------------:|-------------:|------------------:|
| RedPajamaC4            | 6,537,376   | 5,903,282,999   | 1,453,082    | 2,049,000,677     |
| RedPajamaCommonCrawl   | 4,851,710   | 18,127,673,369  | 1,877,354    | 8,991,768,704     |
| RedPajamaStackExchange | 20,090      | 9,488,234       | 441          | 535,135           |
| RedPajamaWikipedia     | 33,336      | 459,190,263     | 846          | 31,103,697        |
| RedPajamaArXiv         | 38,832      | 448,116,597     | 940          | 87,102,100        |
| RedPajamaBook          | 2,496       | 580,763,248     | 1,226        | 507,329,546       |
| RedPajamaGithub        | 4,110       | 130,838,683     | 458          | 1,506,415         |
| **Total**              | 11,520,321  | 25,156,393,599  | 3,361,700    | 11,751,693,665    |
>**Table 1:** This summary provides insights into the distribution of medical and cancer-related content across different sources within The Blue Scrubs.

### Potential Uses

Below we highlight 2 potential usages of The Blue Scrubs dataset.

#### Domain-Specific Pretraining for Clinical LLMs

The dataset enables the fine-tuning of general-purpose LLMs into medical models. By prioritizing high-scoring medical texts and leveraging synthetic data pipelines (e.g., using Llama 3.3 for text rewrite and refinement), The Blue Scrubs ensures LLMs can learn the nuanced language and knowledge required for complex medical domains.

**Use Case:** Transitioning a general model into an oncology-specific LLM to improve accuracy in tasks like treatment recommendation and risk stratification.

#### Medical Misinformation Detection

With its rich metadata, including probability scores and reliability metrics, the dataset supports the development of LLMs that can identify and filter out misleading or harmful health information. Synthetic data can further enhance this process by creating examples of misinformation corrected in real-time.

**Use Case:** Training LLMs to flag false claims about cancer treatments and provide more accurate alternative explanations.

By restricting the dataset to texts scoring ≥ 0.8 and including Llama-based (1–5 scale) quality category ratings along with source information, TheBlueScrubs offers a high-quality, high-utility resource for training, analysis, and stress-testing of medical AI systems.

## 2. Filtering Process (Linear Classifier)

In this section we will dive deeper into the technical steps taken to build The BlueScrubs.

### 2.1 Classifier Training and Rationale

A Logistic Regression¹⁰ model was trained with TF-IDF¹¹ features to separate medical from non-medical texts in SlimPajama. To train the model a balanced medical vs non-medical dataset was created from different sources to represent the diversity of SlimPajama. The balanced training set comprised 60,000 samples (30,000 medical vs. 30,000 non-medical). Using a linear classifier prioritized both speed and accuracy—crucial for processing the massive SlimPajama corpus.

**Why Logistic Regression?**

- **High Speed:** Far faster than transformer-based classifiers on large datasets.
- **Competitive Accuracy:** In non-published results we observed that our linear classifier had a very comparable performance to a specialized BERT-MED model, but far more practical for large-scale inference due to speed.
- **Scalability:** LogReg could process SlimPajama in under a day on the same hardware (8 cores of an H100 GPU), whereas Med-Bert¹² was estimated to require 9 days.

Below is a detailed description of the text we used to create our classifier:

| Dataset                                      | Source                                          | Contribution                                                                                                                                             |
|----------------------------------------------|-------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Goodreads Book Descriptions (5,000 samples)  | booksouls/goodreads-book-descriptions           | Offered informal, descriptive text, contrasting with the structured language of medical documents.                                                       |
| CC News Dataset (5,000 samples)              | cc_news                                         | Added formal news content, helping distinguish technical but non-medical language.                                                                       |
| Wikipedia Articles (5,000 samples)           | wikipedia                                       | Included general scientific and technical language, aiding in differentiating informative but non-medical content.                                       |
| Kaggle News Articles (5,000 samples)         | kaggle/news_articles                            | Introduced formal language from diverse topics, reinforcing the classifier's capability to exclude structured non-medical content.                     |
| OpenWebText (5,000 samples)                  | openwebtext                                     | Added casual, conversational language, contrasting the more formal tone of medical documents.                                                           |
| GitHub-Jupyter Text-Code Pairs (5,000 samples) | codeparrot/github-jupyter-text-code-pairs      | Provided coding and technical content, useful for excluding programming-related documents.                                                               |
>**Table 2:** Non-Medical Data used to build the medical & Non-Medical Classifier.

| Dataset                                              | Source                                       | Contribution                                                                                                                   |
|------------------------------------------------------|----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| PubMed Abstracts (5,000 samples)                     | brainchalov/pubmed_arxiv_abstracts_data      | Provided structured scientific language essential for identifying research-based medical content.                              |
| PubMed QA Dataset (5,000 samples)                    | pubmed_qa                                    | Added conversational medical data, useful for training question-based medical queries.                                         |
| Medical QA Datasets (5,000 samples)                  | lavita/medical-qa-datasets                   | Expanded coverage by including diverse question–answer formats from various medical resources.                                |
| Medical Instruct-ShareGPT (5,000 samples)            | NitraAI/Medical_Instruct-ShareGPT            | Enriched the dataset with educational and conversational medical instructions.                                                |
| MedQuad Medical QnA Dataset (5,000 samples)          | keivalya/MedQuad_MedicalQnADataset           | Expanded coverage with clinical terminology and practical medical scenarios.                                                  |
| Wiki Medical Terms (5,000 samples)                   | gamino/wiki_medical_terms                    | Added semi-formal and encyclopedic medical content for enhanced classifier versatility.                                       |
>**Table 3:** Medical Data used to build the medical & Non-Medical Classifier.

### 2.2 Performance Metrics for the Linear Classifier

To evaluate the performance of our linear classifier, we employed a holdout test set derived through an 80-20 train-test split. Additionally, we utilized a labeled medical vs. non-medical external dataset from Hugging Face ([https://huggingface.co/datasets/ai-maker-space/medical_nonmedical](https://huggingface.co/datasets/ai-maker-space/medical_nonmedical)) to further validate our model’s classification accuracy. These evaluations ensured a robust performance assessment by leveraging both internally split data and an external benchmark dataset. Below you have a description of the classifier performance.

| Metric    | Test Split | External Dataset |
|-----------|-----------|------------------|
| Accuracy  | 0.9819    | 0.9613           |
| Precision | 0.9836    | 0.9943           |
| Recall    | 0.9801    | 0.8472           |
| F1 Score  | 0.9819    | 0.9149           |
>**Table 4:** Performance of Linear Classifier in a holdout test.

As can be seen, excellent discrimination identification was obtained with our linear classifier for both the test set as well as an external dataset. We also explored creating a classifier using Med-Bert¹². However, we did not see any improvement in classification performance but a significantly longer time to classify the data. This made us decide to use the linear classifier as the initial filter.

The filtering process involved splitting documents into 512-token fragments and classifying each fragment individually. For documents exceeding this limit, the probability scores of all fragments were aggregated to determine the final classification. This approach ensured comprehensive coverage of mixed-content documents. This classifier was then applied to each text in SlimPajama obtaining its medical probability.

### 2.3 Threshold-Based Filtering for Further Processing

After getting the probability of being a medical text, we wanted to extract a subset for further refinement and quality control with a stronger LLM (Llama 3.1 70B in this case). At this stage we manually explored the quality of the text as a function of the probability of being a medical text. Even though a score above 0.5 generally indicates that a text is likely medical, our expert inspections showed that many texts in the 0.5–0.8 range had a lower quality content or were otherwise less relevant from a clinical standpoint. By raising the threshold to 0.8, we were able to focus on documents with consistently high medical quality, ensuring that:

- **Evaluation Resources** (e.g., 27-day Llama 3.1 70B based validation on 8 H100s GPU using state-of-the-art inference with vLLM¹³) are applied to the most clinically rich subset.
- Researchers and developers can rely on a concentrated body of medical texts for training and analysis—rather than sifting through content that is of lesser quality.

This approach yields a feasible dataset size without sacrificing depth or quality.

- **Threshold:** Probability ≥ 0.8 → Classify as Medical  
- **Reasoning:** Balanced the number of retained texts with quality assurance.  
- **Result:** Roughly 4% of SlimPajama’s 627 billion tokens—25.1 billion tokens, from 11.5 million texts met our criteria.
  
## 3. Quality and Safety evaluation with Llama 3.1 70B

After identifying high-probability medical texts using our linear classifier, we further quantified the quality and safety of the curated subset leveraging strong open source LLM models to ensure its suitability for clinical LLM development. Leveraging Llama 3.1 (70B Instruct), one of the most advanced open-source reward models available at the time, we implemented a detailed evaluation process across three key dimensions: scope of medical relevance, precision and factual detail, and safety and ethical standards. This step was essential to refine the dataset beyond a simple probability score by capturing nuanced distinctions in clinical relevance and safety that only a high-performing LLM could provide. By incorporating this additional layer of validation, we ensured that The Blue Scrubs dataset not only retained the highest-quality medical texts but also aligned with the ethical and safety expectations critical for developing robust and trustworthy medical AI systems. This process provided researchers with a dataset that is both technically rigorous and practically reliable for real-world medical applications.

### 3.1 Detailed Description of Quality Evaluation using Llama 3.1 70B instruct

After the medical text filtering, Llama 3.1 70B Instruct was used to further assess the curated dataset on three dimensions. Llama 3.1 70B Instruct was ranked as the best open-source reward model by Lambert et al¹⁵. Below we describe the different evaluation categories used.

#### Evaluation Metrics

- **Scope of Medical Relevance**  
  Measures whether the content falls within the domain of medical knowledge and healthcare.  
  Ensures that selected texts are strongly related to medicine and useful for clinical applications.

- **Precision and Factual Detail**  
  Assesses the accuracy and specificity of medical claims.  
  Ensures that content is factually correct and useful in real-world medical applications.

- **Safety and Ethical Standards**  
  Evaluates adherence to medical safety protocols and ethical guidelines.  
  Prevents the inclusion of misleading or harmful information that could negatively impact medical decision-making.

These metrics were selected to ensure that the dataset is highly useful for developing AI models and applications capable of understanding medical content while maintaining factual accuracy and ethical considerations.

#### Inference Parameters and Prompting

Inference during quality and safety evaluation was conducted using vLLM, leveraging 8 H100 GPUs for parallelized batch processing. The following parameters were used:

- **Temperature:** 0.7 (to allow for slight response variation while maintaining consistency)
- **Top-p (nucleus sampling):** 0.95 (to prioritize high-confidence generations)
- **Max tokens:** 128 (to ensure compact and efficient scoring)
- **Batch size:** 5120 (optimized for GPU utilization)
- **Max input tokens:** 4096 (to process large medical texts without truncation)
- **Logprobs enabled:** True (to capture token probabilities for score refinement)

Below is the prompt used during inference:

![image/png](https://cdn-uploads.huggingface.co/production/uploads/66eb0a4e55940cd564ad8e0a/e4hB2zoTrL4X-F_wBWnq1.png)
> **Figure 2:** Prompt used for inference.  

#### Log Probability Processing and Expected Value Calculation

To improve the reliability of scoring within our evaluation framework, we adopted a probabilistic approach based on log probabilities instead of relying solely on direct model outputs with regular expression analysis.

- **Problem Statement:** Initially, we attempted to extract numerical scores (1-5) from the model’s responses using regular expression analysis - regex. However, due to inconsistencies in the model’s output format, approximately 20% of the values were lost during extraction. This data loss compromised the robustness of our evaluation.
- **What We Did:** To overcome this limitation, we transitioned to using the model's log probabilities for numerical scores and forced inference. This allowed us to calculate expected value scores for each evaluation criterion, providing a more nuanced understanding of the model’s confidence.

**Step-by-Step Process:**

1. **Extract Log Probabilities:** Captured the model's token log probabilities corresponding to id of tokens representative of the numerical scores (1-5).
2. **Compute Maximum Log Probability Per Score:** For each step in the sequence, recorded the highest log probability for each score.
3. **Convert to Normal Probabilities:** Exponentiated log probabilities to transform them into standard probabilities.
4. **Normalize Over All Scores:** Normalized these probabilities so they summed to 1, ensuring a valid probability distribution.
5. **Compute Expected Value:** Calculated the expected value using the normalized probabilities.
6. **Truncate Expected Value:** The expected score was truncated to two decimal places to maintain consistency and avoid rounding errors.

This log probability-based method provided a more accurate reflection of the model’s confidence in its evaluations. By incorporating probabilistic scoring, we ensured that the assigned ratings were both reliable and robust, aligning with the stringent quality requirements necessary for clinical language model evaluation.

#### Evaluation Results

The final dataset – **25 billion tokens** - was evaluated using Llama 3.1 (70B) Instruct, and the scores for each category were aggregated to provide summary statistics. Below, we present the histogram for each evaluation category across all texts. These statistics allow researchers to assess the overall quality and consistency of the dataset and provide insights into areas where additional refinement may be necessary. As it can be seen in the figure below, **78%** of the corpus (19.5 billion tokens) is considered to have the maximum medical relevance while **68%** (17 billion) has the maximum precision and **62%** is considered to have the maximum safety score (15.5 billion tokens).

![image/png](https://cdn-uploads.huggingface.co/production/uploads/66eb0a4e55940cd564ad8e0a/8ugdpsnB8aZamw5DkvoQE.png)
> **Figure 3:** Histogram for each evaluation category across all texts.  

| Metric                      | Mean | Standard Deviation |
|-----------------------------|------|--------------------|
| Scope of Medical Relevance  | 4.51 | 1.12              |
| Precision and Factual Detail| 4.61 | 0.66              |
| Safety and Ethical Standards| 4.60 | 0.72              |
>**Table 5:** Mean and standard deviation of the three categories from Llama 3.1 70B evaluation.

- **Compute Resources:** 27 days on 8 H100 GPUs  
- **Implication:** Confirms the dataset’s quality and comprehensiveness.

### 3.2 Comparison of Llama 3.1 with Clinicians and GPT Evaluations

To validate the evaluation of Llama 3.1 70B instruct, we conducted a secondary review using a random subset of texts. This subset was manually reviewed by clinicians to assess the alignment between automated and human evaluations.

#### Clinician Review Process

Clinicians were asked to evaluate a subset of texts (N= 60) drawn from the dataset using two criteria:
- Scope of Medical Relevance
- Safety and Ethical Standards

Upon initial analysis it was determined that the category precision and factual detail was too difficult for clinicians to assess. The evaluation was conducted via RedCap¹⁴, a secure, web-based application designed for managing surveys and data collection. The survey provided clinicians with three response options for each criterion: Low, Neutral, and High. This simplified rating system was chosen to facilitate consistency and ease of review. Each clinician provided independent ratings, ensuring minimal bias.

#### Text Selection and Extraction from SlimPajama for Evaluation

The sample subset was extracted from SlimPajama using the same filtering criteria applied to the full dataset. The text selection process ensured that the sampled texts were representative of the full dataset, allowing the results of this validation experiment to be extrapolated to the entire corpus. Specifically:

- **Initial Text Extraction:** Texts classified as medical by our Logistic Regression model were randomly sampled from the dataset.
- **Preprocessing and Cleaning:** Extracted texts were truncated to 512 tokens to enhance readability for clinicians, ensuring they could efficiently evaluate the content without unnecessary cognitive load.
- **Diversity in Text Sources:** The sample included texts from various original sources in SlimPajama (e.g., Common Crawl, PubMed abstracts, medical forums, books) to ensure coverage of different writing styles and medical discourse.
- **Randomization:** A stratified random sampling approach was used to ensure balanced representation across different medical topics.

#### Comparison of Evaluations

To quantify the agreement between Llama 3.1 70B instruct, clinicians, and GPT-4o evaluations, we computed the mean and standard deviation for both the Scope of Medical Relevance and Safety and Ethical Standards categories across different evaluation sources. The results are visualized in Figures 5-8:

![image/png](https://cdn-uploads.huggingface.co/production/uploads/66eb0a4e55940cd564ad8e0a/VVdEUQs1lgQwfxbukUGRd.png)
> **Figure 5:** Mean and standard deviation of Scope of Medical Relevance scores from the clinician survey (X) with the distribution of results from Llama 3.1 70B instruct in (Y). A monotonic relationship is observed validating the agreement of evaluation of the medical quality of the text.  

![image/png](https://cdn-uploads.huggingface.co/production/uploads/66eb0a4e55940cd564ad8e0a/w1lIeQm59QRDnGKATygOz.png)
> **Figure 6:** Mean and standard deviation of Scope of Medical Relevance scores from GPT-4o evaluation (X) against Llama 3.1 70B. A monotonic relationship is observed validating the agreement of evaluation of the medical quality of the text.  

![image/png](https://cdn-uploads.huggingface.co/production/uploads/66eb0a4e55940cd564ad8e0a/DmL0hZXMkFpFd2b4_yyPI.png)
> **Figure 7:** Mean and standard deviation of Safety and Ethical Standards scores from the clinician survey (X) against Llama 3.1 70B classification. A monotonic relationship is observed validating the agreement of evaluation of the safety of the text.  

![image/png](https://cdn-uploads.huggingface.co/production/uploads/66eb0a4e55940cd564ad8e0a/1S-0W0ojzPLeSfLUwvXiX.png)
> **Figure 8:** Mean and standard deviation of Safety and Ethical Standards scores from GPT-4o evaluation (X) against Llama 3.1 70B classification. A monotonic relationship is observed validating the agreement of evaluation of the safety of the text.  

These figures illustrate the concordance between human and automated evaluations using Llama 3.1 70B Instruction. A high degree of alignment between clinicians and Llama 3.1 70B scores would suggest that evaluations are reliable proxies for human expert judgment. Conversely, any notable discrepancies highlight areas where further refinements or additional validation may be necessary.

We also evaluated the classification provided by Llama 3.1 70B Instruction by leveraging the GPT-4o model, accessed through the OpenAI API. The GPT-4o model was tasked with assigning scores to the same subset of texts evaluated by clinicians, using the identical prompt structure used for Llama 3.1 70B evaluations. This ensured consistency in the scoring framework and minimized variability introduced by prompt engineering.

Our analysis revealed a strong correlation between Llama 3.1 70B evaluations and GPT-4o outputs across Scope of Medical Relevance, Precision and Factual Detail, and Safety and Ethical Standards. Minor discrepancies were noted in borderline or highly technical texts, where GPT sometimes exhibited slightly lower sensitivity to domain-specific nuance compared to Llama 3.1 70B and human reviewers.

## 4. Cancer Classification

To illustrate the value of The Blue Scrubs as a source of relevant information for specific patients' population we investigated its percentage of cancer text included – harder to get text data. Find below a step-by-step description of the process that generated our The Blue Scrubs cancer text label.

### 4.1 Initial Keyword Selection

To identify cancer-related documents, we first created a seed set of cancer-related keywords with the assistance of GPT-4.

```python
cancer_keywords = ["cancer", "tumor", "oncology", "carcinoma", "neoplasm",
                   "metastasis", "malignant", "chemotherapy", "radiotherapy",
                   "sarcoma", "lymphoma", "leukemia", "melanoma"]
```

>These keywords included terms such as “cancer,” “tumor,” and “oncology.” Using a simple matching step (e.g., regex or string search), we filtered out any document in the corpus that contained at least one of these keywords. From these filtered texts, we then sampled 30,000 that mentioned at least one cancer keyword and 30,000 that did not. This balanced set of 60,000 documents served as the training data for a second logistic regression classifier—using TF-IDF features—specifically designed to detect cancer-related content. The key idea here is that these documents, even though initially flagged by only a small set of seed keywords, will contain many other relevant terms not in our seed list, helping the logistic regression model generalize better in identifying cancer-related texts across the entire corpus.

### 4.2 Cancer Classification Model

- **Model:** Logistic Regression with TF-IDF  
- **Dataset:** 60,000 balanced texts (cancer vs. non-cancer)  
- **Application:** Classified the entire filtered dataset (25.1B tokens) to distinguish cancer content.

### 4.3 Cancer Classification Results

Below is a detailed description of the result of our classifier, becoming the largest corpus of open-source cancer text available.

| Category         | Number of Texts | Number of Tokens | Percentage |
|------------------|-----------------|------------------|-----------:|
| Cancer Texts     | 3,361,700       | 11.75 billion    | 29.2%      |
| Non-Cancer Texts | 8,158,631       | 13.40 billion    | 70.8%      |
>**Table 6:** Cancer and non-Cancer text label distribution of The Blue Scrubs.

- **Cancer-Specific Metrics**

| Metric                       | Mean | Standard Deviation |
|-----------------------------|------|--------------------|
| Probability (Cancer Only)   | 0.93 | 0.06              |
| Scope of Medical Relevance  | 4.79 | 0.66              |
| Precision and Factual Detail| 4.61 | 0.67              |
| Safety and Ethical Standards| 4.59 | 0.79              |
>**Table 7:** The Blue Scrubs Cancer texts label and evaluation mean and standard deviation.

- **Safety Analysis (Cancer Only)**

| Category             | Number of Texts | Number of Tokens | Percentage |
|----------------------|----------------:|-----------------:|-----------:|
| Safe Texts (≥4)      |       3,030,109 |       10.6 billion |      90.1% |
| Neutral Texts (2–4)  |         270,878 |        0.8 billion |       8.1% |
| Unsafe Texts (≤2)    |          60,713 |       0.35 billion |       1.8% |
>**Table 8:** The Blue Scrubs Cancer texts safety distribution.

## 5. Key Observations and Recommendations

### 5.1 Data Quality and Utility

- **High Medical Relevance:** The final dataset retains documents with strong likelihood of covering medical topics, verified via dual-stage filtering.
- **Robust Cancer Coverage:** Nearly one-third of the medical texts pertain to cancer, broadening research avenues for oncology-related language modeling.
- **Safety Scoring:** Most cancer-related documents scored highly for ethical standards, indicating relatively safe content for subsequent modeling tasks.

### 5.2 Limitations, Disclaimers and Ethical Considerations

- **Bias and Noise:** Even after filtering, the dataset may retain biases, unverified medical claims, and incomplete or outdated information.
- **Long Evaluation Times:** Llama 3.1 70B based evaluations were computationally expensive, limiting the frequency of repeated checks.
- **Privacy and Anonymization:** Although derived from publicly available web data, caution is advised when texts might include personal details or sensitive health data.

### 5.3 Future Directions

- **Applications:** We are studying the usability of The Blue Scrubs dataset in order to train medical LLMs as it compares to other medical corpuses considered to be high quality (e.g. PubMed).
- **Further Refinement:** Additional, domain-specific classifiers (e.g., for cardiology, neurology) could improve the topical precision.
- **Fine-Grained Metadata:** Annotating documents for sub-topics within cancer (lung, breast, prostate, etc.) would benefit specialized modeling.
- **Multilingual Expansion:** If SlimPajama includes non-English data, similar filtering steps could yield large-scale multilingual medical corpora.

Despite our extensive filtering and data quality control some texts are still of low quality. By leveraging strong open-source models (Llama 3.3 70B) we are summarizing each text in The Blue Scrubs to improve its readability and grammatical content without changing the medical information.


## 6. Conclusion

The Blue Scrubs dataset provides a uniquely broad and deep corpus of medical text, leveraging the massive scope of SlimPajama. Through efficient Logistic Regression filtering and a secondary Llama 3.1 70B evaluation, the resulting dataset offers:

- High-quality, diverse medical texts totaling over 25 billion tokens.
- Robust coverage of cancer-related materials (over 11 billion tokens) with good safety and factual metrics.
- A scalable framework for further targeted extractions and evaluations, despite the computational overhead when using large-language-model evaluations.

## 7. How to Reference Us

If you use any part of The Blue Scrubs dataset, please reference it using the following format:

```bibtex
@article{TheBlueScrubs,
  author = {Luis Felipe and Carlos Garcia and Issam el NAqa and Monique Shotande and Aakash Tripathi and Vivek Rudapratna and Ghulam Rasool and Gilmer Valdes},
  title = {The Blue Scrubs: A Comprehensive Curated Medical Dataset Derived from the Internet},
  month = {February},
  year = {2025},
  url = {https://thebluescrubs.ai/}
}
```

## 8. License

Copyright 2024 The BlueScrubs

Licensed under the Apache License, Version 2.0 (the "License");  
you may not use this file except in compliance with the License.  
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software  
distributed under the License is distributed on an "AS IS" BASIS,  
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
See the License for the specific language governing permissions and  
limitations under the License.

For full terms, see the LICENSE file. If you have any questions, comments, or concerns about licensing please contact us.

For the dataset itself, please refer to the Common Crawl Foundation Terms of Use.

## 9. References

1. **Common Crawl Foundation.** (n.d.). Common Crawl. Available at: [https://commoncrawl.org](https://commoncrawl.org)

2. **Liang, W., et al.** (2025). DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning. *arXiv:2501.12948.* Available at: [https://arxiv.org/abs/2501.12948](https://arxiv.org/abs/2501.12948)

3. **National Library of Medicine.** (n.d.). PubMed. Available at: [https://pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov)

4. **Chen, Z., Hernández Cano, A., Romanou, A., Bonnet, A., Matoba, K., Salvi, F., Pagliardini, M., Fan, S., Köpf, A., Mohtashami, A., Sallinen, A., Sakhaeirad, A., Swamy, V., Krawczuk, I., Bayazit, D., Marmet, A., Montariol, S., Hartley, M.-A., Jaggi, M., & Bosselut, A.** (2023). MEDITRON-70B: Scaling Medical Pretraining for Large Language Models. *arXiv:2311.16079.* Available at: [https://arxiv.org/abs/2311.16079](https://arxiv.org/abs/2311.16079)

5. **Shao, Z., Wang, P., Zhu, Q., Xu, R., Song, J., Bi, X., Zhang, H., Zhang, M., Li, Y. K., Wu, Y., & Guo, D.** (2024). DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models. *arXiv:2402.03300.* Available at: [https://arxiv.org/abs/2402.03300](https://arxiv.org/abs/2402.03300)

6. **Soboleva, D., Al-Khateeb, F., Myers, R., Steeves, J. R., Hestness, J., & Dey, N.** (2023). SlimPajama: A 627B token cleaned and deduplicated version of RedPajama. Cerebras Systems. Available at: [https://www.cerebras.net/blog/slimpajama-a-627b-token-cleaned-and-deduplicated-version-of-redpajama](https://www.cerebras.net/blog/slimpajama-a-627b-token-cleaned-and-deduplicated-version-of-redpajama)

7. **Together Computer.** (2023). RedPajama: An Open Dataset for Training Large Language Models. *arXiv:2411.12372.* Available at: [https://arxiv.org/abs/2411.12372](https://arxiv.org/abs/2411.12372)

8. **OpenAI.** (2024). GPT-4o-2024-08-06: Enhancements in Structured Outputs and Performance. OpenAI Technical Report. Available at: [https://platform.openai.com/docs/models](https://platform.openai.com/docs/models)

9. **Dubey, A., et al.** (2024). The Llama 3 Herd of Models. *arXiv:2407.21783.* Available at: [https://arxiv.org/abs/2407.21783](https://arxiv.org/abs/2407.21783)

10. **Cramer, J. S.** (2002). The Origins of Logistic Regression. Tinbergen Institute Discussion Paper. Available at: [https://papers.tinbergen.nl/02119.pdf](https://papers.tinbergen.nl/02119.pdf)

11. **Spärck Jones, K.** (1972). A statistical interpretation of term specificity and its application in retrieval. *Journal of Documentation, 28(1), 11–21.* Available at: [https://www.staff.city.ac.uk/~sbrp622/idfpapers/ksj_orig.pdf](https://www.staff.city.ac.uk/~sbrp622/idfpapers/ksj_orig.pdf)

12. **Rasmy, L., Xiang, Y., Xie, Z., Tao, C., & Zhi, D.** (2021). Med-BERT: Pretrained contextualized embeddings on large-scale structured electronic health records for disease prediction. *npj Digital Medicine, 4(1), 86.* Available at: [https://www.nature.com/articles/s41746-021-00455-y](https://www.nature.com/articles/s41746-021-00455-y)

13. **Kwon, W., Li, Z., Zhuang, S., Sheng, Y., Zheng, L., Yu, C. H., Gonzalez, J. E., Zhang, H., & Stoica, I.** (2023). Efficient Memory Management for Large Language Model Serving with PagedAttention. *Proceedings of the ACM SIGOPS 29th Symposium on Operating Systems Principles.* Available at: [https://arxiv.org/abs/2309.06180](https://arxiv.org/abs/2309.06180)

14. **Harris, P. A., Taylor, R., Thielke, R., Payne, J., Gonzalez, N., & Conde, J. G.** (2009). Research electronic data capture (REDCap) – A metadata-driven methodology and workflow process for providing translational research informatics support. *Journal of Biomedical Informatics, 42(2), 377–381.* Available at: [http://www.sciencedirect.com/science/article/pii/S1532046408001226](http://www.sciencedirect.com/science/article/pii/S1532046408001226)

15. **Lambert, N., Pyatkin, V., Morrison, J., Miranda, L. J. V., Lin, B. Y., Chandu, K., Dziri, N., Kumar, S., Zick, T., Choi, Y., Smith, N. A., & Hajishirzi, H.** (2024). RewardBench: Evaluating Reward Models for Language Modeling. *arXiv:2403.13787.* Available at: [https://arxiv.org/abs/2403.13787](https://arxiv.org/abs/2403.13787)