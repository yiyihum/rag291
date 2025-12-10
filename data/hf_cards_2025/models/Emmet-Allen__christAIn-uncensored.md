---
base_model: dphn/Dolphin3.0-Qwen2.5-0.5B
library_name: peft
pipeline_tag: text-generation
tags:
- base_model:adapter:dphn/Dolphin3.0-Qwen2.5-0.5B
- lora
- sft
- transformers
- trl
---

# ChristAI-uncensored
<!-- Provide a quick summary of what the model is/does. -->


## Model Details
A Small Language Model trained on the King James Version of The Bible.

### Model Description

<!-- Provide a longer summary of what this model is. -->
Created as a critque peoples usage of AI specifically LLMs/SLMs
as a confidant, therapist, and in some cases a new god (think American Gods by Neil Gaiman).

This has lead to cases of people creating AI-centered cults, rash decision making as suggested by AI,
and in a praticular case that sparked the intrest of the creation of this model, a 16 year old boy
commiting [suicide as suggested by ChatGPT](https://www.cnn.com/2025/08/26/tech/openai-chatgpt-teen-suicide-lawsuit). 

This model is the uncensored model, which is able to better answer more nuanced questions that pertain to 
The Bible and how it pertains to the world. 

The model does not hold back.


- **Developed by:** Emmet Allen
- **Model type:** PEFT text-generation
- **Language(s) (NLP):** English
- **License:** MIT
- **Finetuned from model [optional]:** dphn/Dolphin3.0-Qwen2.5-0.5B

### Model Sources [optional]

<!-- Provide the basic links for the model. -->

- **Repository:** (https://huggingface.co/Emmet-Allen/christAIn-uncensored)

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->
Used to answer questions using the KJV bible as a reference point.

**This is a Social Critique Project**

### Direct Use

<!-- This section is for the model use without fine-tuning or plugging into a larger ecosystem/app. -->

[More Information Needed]

### Downstream Use [optional]

<!-- This section is for the model use when fine-tuned for a task, or when plugged into a larger ecosystem/app -->

[More Information Needed]

### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the model will not work well for. -->

[More Information Needed]

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

Trained on the Christian Based KJV Bible. 
Heavily leans towards christian values and opinions.

### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->

Users (both direct and downstream) should be made aware of the risks, biases and limitations of the model. More information needed for further recommendations.

## How to Get Started with the Model

Use the code below to get started with the model.

[More Information Needed]

## Training Details

### Training Data

<!-- This should link to a Dataset Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->

https://huggingface.co/datasets/Emmet-Allen/The-Bible-KJV

[More Information Needed]

### Training Procedure

<!-- This relates heavily to the Technical Specifications. Content here should link to that section when it is relevant to the training procedure. -->

Will include Python Notebook.

[More Information Needed]

## Environmental Impact

<!-- Total emissions (in grams of CO2eq) and additional considerations, such as electricity usage, go here. Edit the suggested text below accordingly -->

Carbon emissions can be estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et al. (2019)](https://arxiv.org/abs/1910.09700).

- **Hardware Type:** NVidia 3070ti 8GB VRAM
- **Hours used:** < 1hr

## Technical Specifications [optional]

### Model Architecture and Objective

[More Information Needed]

### Compute Infrastructure

[More Information Needed]

#### Hardware

[More Information Needed]

#### Software

Void IDE
Jupyter Notebook
Nvidia-SMI
Nvidia CUDA-Toolkit

## Citation [optional]

<!-- If there is a paper or blog post introducing the model, the APA and Bibtex information for that should go in this section. -->

**BibTeX:**

[More Information Needed]

**APA:**

[More Information Needed]

## Glossary [optional]

<!-- If relevant, include terms and calculations in this section that can help readers understand the model or model card. -->

[More Information Needed]

## More Information [optional]

[More Information Needed]

## Model Card Authors [optional]

[More Information Needed]

## Model Card Contact

[More Information Needed]
### Framework versions

- PEFT 0.17.1