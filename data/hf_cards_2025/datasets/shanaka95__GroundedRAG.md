---
pretty_name: GroundedRAG
tags:
- question-answering
- retrieval-augmented-generation
- instruction-tuning
- multi-document
configs:
- config_name: default
  data_files:
  - split: train
    path: dataset-final.jsonl
license: cc-by-4.0
license_details: Creative Commons Attribution 4.0 International License - Allows commercial
  use, modification, and distribution with attribution
---

# Dataset Card for GroundedRAG

## Table of Contents
- [Dataset Description](#dataset-description)
- [Dataset Summary](#dataset-summary)
- [Supported Tasks](#supported-tasks)
- [Languages](#languages)
- [Dataset Structure](#dataset-structure)
- [Data Instances](#data-instances)
- [Data Fields](#data-fields)
- [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
- [Curation Rationale](#curation-rationale)
- [Source Data](#source-data)
- [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
- [Social Impact of Dataset](#social-impact-of-dataset)
- [Discussion of Biases](#discussion-of-biases)
- [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
- [Licensing Information](#licensing-information)
- [Citation Information](#citation-information)
- [Contributions](#contributions)

---

## Dataset Description

### Dataset Summary

GroundedRAG is a large-scale training dataset specifically crafted for fine-tuning language models and Retrieval-Augmented Generation (RAG) systems. It contains **572,598** carefully curated question-answer pairs with rich multi-document contexts, sourced from six high-quality datasets. Each training example features a question, a comprehensive answer, and supporting context from multiple documents that provide the necessary grounding information.

The dataset is optimized for training RAG systems to:
- Process and understand multi-document contexts effectively
- Generate well-grounded answers based on provided information
- Handle diverse question formulations and domains
- Learn to synthesize information from multiple sources
- Recognize when questions cannot be answered from available context
- Adapt to varying context lengths (short, medium, and long)
- Generate responses of appropriate length and complexity

### Supported Tasks
- **RAG Fine-tuning**: Training language models to generate contextually grounded responses
- **Multi-Document QA Training**: Teaching models to answer questions using multiple document sources
- **Instruction Tuning**: Enhancing model capabilities for RAG-based applications
- **Context-Aware Generation**: Training models to leverage provided context effectively

### Languages
- English

---

## Dataset Structure

### Data Instances
Each instance contains a unique question, a multi-document context, and a verified answer that can be derived from the provided context.

### Data Fields
Each sample contains the following fields:

- `context`: Multi-document context containing relevant information for answering the question. Documents are separated by `[Document X]` and `[End of Document X]` markers.
- `question`: The question to be answered based on the provided context
- `answer`: The verified answer that can be derived from the context

### Dataset Characteristics

**Context Length Distribution:**
- Short context (<1,000 characters): 7,454 samples (1.3%)
- Medium context (1,000-3,000 characters): 369,658 samples (64.6%)
- Long context (≥3,000 characters): 195,486 samples (34.1%)

**Answer Length Distribution:**
- Short answers (<100 characters): 266,848 samples (46.6%)
- Medium answers (100-300 characters): 117,102 samples (20.5%)
- Long answers (≥300 characters): 188,648 samples (32.9%)

**Question Types:**
The dataset includes diverse question types to ensure comprehensive model training:
- Factual questions requiring specific information extraction
- Analytical questions requiring information synthesis
- Comparative questions requiring multi-source analysis
- Unanswerable questions to train models to recognize information gaps
- Questions requiring different levels of reasoning complexity

### Data Format Examples

**Example 1: Medium Context with Analytical Question**
```json
{
  "context": "[Document 1] In the world of modern design, professionals often employ advanced techniques to create visually stunning graphics and interfaces. One popular method is using vector-based tools which allow for scalable graphics that maintain high resolution at any size. This approach is essential for creating logos and icons that need to remain crisp across various platforms. Additionally, designers frequently utilize layering techniques to enhance the depth and complexity of their work, integrating textures and patterns to add interest and appeal. The use of color theory is also critical in design, as it influences user perception and emotional response. Designers must understand how colors interact and the psychological effects they can have to effectively communicate the desired message. Furthermore, the integration of typography within designs plays a crucial role. Selecting the right font and arranging text can drastically alter the readability and impact of a design. Modern design tools offer extensive options for customizing text, including adjustments to kerning, leading, and tracking, which are vital for achieving a polished look. Lastly, responsiveness in design ensures that creations look great on any device, requiring a deep understanding of flexible layouts and adaptive design strategies. [End of Document 1] [Document 2] Graphic design has seen significant advancements with the introduction of innovative software that simplifies complex tasks. Programs like Adobe Illustrator and Photoshop have revolutionized the industry, providing tools that enable creators to manipulate images and create artwork with unprecedented precision and control. Features such as layer masks, blending modes, and advanced selection techniques allow designers to refine their work to minute details, enhancing the overall quality and effectiveness. The development of 3D graphic tools has also opened up new possibilities for depth and realism in design. Software now often includes capabilities for animation and interactive elements, which are increasingly important in digital media. Designers can also leverage assets like stock photos, custom brushes, and pattern libraries to enrich their creations without starting from scratch. Collaboration features have become essential, with cloud-based platforms enabling teams to work together seamlessly from different locations. This evolution in graphic design software not only increases productivity but also encourages creativity and experimentation, pushing the boundaries of what is possible in graphic arts. [End of Document 2]",
  "question": "How has the integration of artificial intelligence in design software impacted the efficiency and creativity of graphic designers in large-scale projects?",
  "answer": "The integration of artificial intelligence (AI) in design software has significantly transformed the landscape of graphic design, particularly in the context of large-scale projects. AI-driven tools have automated many routine tasks, such as sorting through large datasets of images, auto-correcting color imbalances, and even generating basic design elements. This automation allows graphic designers to focus more on creative aspects of projects, enhancing both efficiency and innovation. AI also offers predictive analytics that can suggest design adjustments based on user engagement metrics, which helps in refining the visual elements to better meet audience preferences. Furthermore, AI capabilities in software can lead to more personalized designs at a faster rate, accommodating the scale and scope required in large projects. Overall, AI not only streamlines the design process but also empowers designers to experiment with new ideas and complex concepts more freely, pushing the boundaries of creativity and effectiveness in graphic design."
}
```

**Example 2: Short Context with Factual Question**
```json
{
  "context": "[Document 1] Speed Up to a Determined Walking Pace to Burn Fat. The speed to walk for optimal fat-burning is a determined pace, or a brisk walking pace. At this rate, you should be breathing noticeably but able to carry on a conversation in full sentences. Heart rate target should be 60-70% of your maximum heart rate. Target Heart Rate Calculator. [End of Document 1] [Document 2] Walking on the treadmill? An average person walks at a speed of about 2½ to 3 miles an hour (about 20 minutes a mile). To lose weight and get fit you should aim to walk at 3½ to 4 miles an hour (15 minutes a mile). Increasing your pace from 3 mph to 4 mph means you'll burn about one third more calories. [End of Document 2]",
  "question": "how fast do you need to walk to lose weight",
  "answer": "To lose weight, you need to walk three and half to four miles per hour or 15 minutes a mile."
}
```

**Example 3: Unanswerable Question**
```json
{
  "context": "[Document 1] Radiologist, for a stable established practice. - Employer: Berkshire Health Systems - Location: Pittsfield, Massachusetts - Posted: Nov 23, 2021 - Closes: Nov 23, 2022 - Ref: 2128914 - Specialty: Radiology / Imaging. Well established, stable private practice in the Berkshires of Western Massachusetts - Seeks a fellowship trained Neuroradiologist and Body Imager. - Exclusive provider of imaging services for Berkshire Health Systems, including Berkshire Medical Center, Fairview Hospital and multiple satellite facilities. - Stimulating case mix and volume offering a sub specialized environment with the perks of collegial private practice. - Competitive compensation and generous vacation. We understand the importance of balancing work with a healthy personal lifestyle - 4-season resort community - Endless cultural opportunities - Year round recreational activities from skiing to kayaking - Excellent public and private schools. [End of Document 1]",
  "question": "What is the name of the Neuroradiologist who was hired by Berkshire Health Systems on Nov 23, 2021?",
  "answer": "This question cannot be answered."
}
```

**Example 4: Long Context with Complex Analysis**
```json
{
  "context": "[Document 1] BarcodeLib.com's licensing agreement establishes comprehensive control over software distribution and modification through various licensing options and restrictions. The SOFTWARE is protected by copyright laws and international copyright treaties, as well as other intellectual property laws and treaties, and contains confidential information and trade secrets. BarcodeLib.com retains all rights not expressly granted to you in this LICENSE. These protections ensure that only authorized users, who have accepted the terms of the license, can use the SOFTWARE. For distribution, BarcodeLib.com grants licenses such as the WINDOWS APPLICATION DISTRIBUTION LICENSE and SERVER LICENSE, which allow the software to be installed on personal computers and servers respectively, within the terms set by the license. Redistribution rights are perpetual and royalty-free, allowing for the shipping of the SOFTWARE as part of solutions for internal company use, hosted applications, commercial solutions deployed at end-users' sites, or shrink-wrapped software. [End of Document 1]",
  "question": "How does BarcodeLib.com's licensing agreement ensure control over the distribution and modification of its software products, and what are the implications of these controls for a small software development company looking to integrate BarcodeLib.com's technology into their projects?",
  "answer": "BarcodeLib.com's licensing agreement establishes control over the distribution and modification of its software products through a variety of licensing options and restrictions. The SOFTWARE is protected by copyright laws and international copyright treaties, as well as other intellectual property laws and treaties, and contains confidential information and trade secrets. BarcodeLib.com retains all rights not expressly granted to you in this LICENSE. These protections ensure that only authorized users, who have accepted the terms of the license, can use the SOFTWARE. For distribution, BarcodeLib.com grants licenses such as the WINDOWS APPLICATION DISTRIBUTION LICENSE and SERVER LICENSE, which allow the software to be installed on personal computers and servers respectively, within the terms set by the license. Redistribution rights are perpetual and royalty-free, allowing for the shipping of the SOFTWARE as part of solutions for internal company use, hosted applications, commercial solutions deployed at end-users' sites, or shrink-wrapped software. For a small software development company, these licensing terms mean that they can integrate BarcodeLib.com's technology into their projects but must adhere strictly to the scope of the granted licenses. This includes ensuring that any redistribution complies with the terms and that the software cannot be used independently of the solutions they develop. These controls imply that while the company can benefit from the robust features of BarcodeLib.com's software, they must carefully manage how it is integrated and distributed to maintain compliance and avoid legal issues."
}
```

**Total Dataset Size**: 1.9 GB



## Dataset Creation

### Curation Rationale

GroundedRAG was developed to meet the growing demand for high-quality training data for RAG system development. The dataset addresses the challenge of training language models to effectively utilize multi-document contexts and generate well-grounded responses. By combining diverse, high-quality sources, it provides comprehensive training examples that cover various domains and question types, enabling robust model fine-tuning.

### Source Data

The dataset is constructed from six diverse, high-quality datasets:

1. **[Databricks Dolly 15k](https://huggingface.co/datasets/databricks/databricks-dolly-15k)**: A comprehensive instruction-tuning dataset featuring 15,000 human-crafted instruction-response pairs spanning creative writing, question answering, summarization, information extraction, classification, and brainstorming tasks.

2. **[FreedomIntelligence RAG-Instruct](https://huggingface.co/datasets/FreedomIntelligence/RAG-Instruct)**: A purpose-built dataset for RAG instruction tuning, featuring context-dependent question-answer pairs designed to train models in context-aware response generation.

3. **[GlaiveAI RAG-v1](https://huggingface.co/datasets/glaiveai/RAG-v1)**: A diverse RAG dataset offering a wide variety of question types and contextual scenarios for comprehensive model training.

4. **[Neural Bridge RAG Dataset 12000](https://huggingface.co/datasets/neural-bridge/rag-dataset-12000)**: A focused dataset containing 12,000 specialized RAG question-answer pairs for targeted training scenarios.

5. **[Neural Bridge RAG Full 20000](https://huggingface.co/datasets/neural-bridge/rag-full-20000)**: An extended dataset with 20,000 RAG question-answer pairs providing additional training examples for robust model development.

6. **[Traintogpb Marco for 5 Context RAG](https://huggingface.co/datasets/traintogpb/marco-for-5-context-rag)**: A multi-context dataset derived from MS MARCO, featuring scenarios that require information synthesis from multiple document sources.

### Data Processing

The source datasets were processed and cleaned to ensure:
- Consistent formatting across all sources
- High-quality question-answer pairs
- Proper multi-document context structure
- Removal of duplicates and low-quality entries
- Standardization of document markers and formatting

---

## Personal and Sensitive Information

The dataset contains information derived from public sources and carefully curated datasets. No personal or sensitive information is included in the final dataset. All content has been processed to ensure privacy and compliance with data protection standards.

---

## Considerations for Using the Data

### Social Impact of Dataset

GroundedRAG supports the development of more capable and reliable RAG systems by providing high-quality training data. This enables researchers and developers to create AI systems that can better understand and respond to user queries using multiple information sources, ultimately leading to more accurate and helpful AI assistants across various applications and domains.

### Discussion of Biases

The dataset inherits biases from its source datasets, which may include:
- Domain-specific biases based on the topics covered in the source datasets
- Language biases (English-only content)
- Potential biases in question formulation and answer generation patterns

### Other Known Limitations

- The dataset is primarily focused on English language content
- Training examples are derived from existing datasets and may inherit their inherent characteristics
- The multi-document format represents a specific subset of real-world RAG scenarios
- Model performance may be influenced by the specific formatting and structure of the training data

---

## Additional Information

### Licensing Information

This dataset is released under the **Creative Commons Attribution 4.0 International License (CC-BY-4.0)**, which allows for:

- **Commercial use**: You can use this dataset for any commercial purposes
- **Non-commercial use**: You can use this dataset for research, education, and personal projects
- **Modification**: You can modify, adapt, and build upon this dataset
- **Distribution**: You can share and distribute this dataset
- **Attribution requirement**: You must give appropriate credit to the original creators

**Attribution Format:**
```
GroundedRAG Dataset (https://huggingface.co/datasets/shanaka95/GroundedRAG)
Licensed under CC-BY-4.0
```

This license ensures maximum accessibility while maintaining proper attribution to the dataset creators and contributors.

### Citation Information

```bibtex
@misc{groundedrag2024,
  title={GroundedRAG: A Comprehensive Multi-Document Question-Answering Dataset for Retrieval-Augmented Generation},
  author={Shanaka Anuradha},
  year={2024},
  url={https://huggingface.co/datasets/shanaka95/GroundedRAG},
  note={Dataset derived from multiple high-quality RAG datasets}
}
```

### Contributions

This training dataset is built upon the following foundational datasets:

- [Databricks Dolly 15k](https://huggingface.co/datasets/databricks/databricks-dolly-15k): Comprehensive instruction-tuning dataset with diverse task types
- [FreedomIntelligence RAG-Instruct](https://huggingface.co/datasets/FreedomIntelligence/RAG-Instruct): Specialized RAG instruction dataset for context-aware training
- [GlaiveAI RAG-v1](https://huggingface.co/datasets/glaiveai/RAG-v1): Diverse RAG dataset with varied question and context types
- [Neural Bridge RAG Dataset 12000](https://huggingface.co/datasets/neural-bridge/rag-dataset-12000): Focused RAG training dataset with specialized examples
- [Neural Bridge RAG Full 20000](https://huggingface.co/datasets/neural-bridge/rag-full-20000): Extended RAG dataset providing additional training examples
- [Traintogpb Marco for 5 Context RAG](https://huggingface.co/datasets/traintogpb/marco-for-5-context-rag): Multi-context dataset for complex information synthesis training

We extend our gratitude to the creators of these foundational datasets for their valuable contributions to the RAG research and development community.
