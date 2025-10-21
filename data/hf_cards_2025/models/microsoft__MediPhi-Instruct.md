---
license: mit
datasets:
- microsoft/mediflow
- ncbi/pubmed
- epfl-llm/guidelines
- starmpcc/Asclepius-Synthetic-Clinical-Notes
- akemiH/NoteChat
- zhengyun21/PMC-Patients
- jpcorb20/medical_wikipedia
language:
- en
base_model:
- microsoft/Phi-3.5-mini-instruct
library_name: transformers
tags:
- merge
- mergekit
- medical
- clinical
---
# Model Card for MediPhi-Instruct

## Model Summary

The MediPhi Model Collection comprises 7 small language models of 3.8B parameters from the base model `Phi-3.5-mini-instruct` specialized in the medical and clinical domains. The collection is designed in a modular fashion. Five MediPhi experts are fine-tuned on various medical corpora (i.e. PubMed commercial, Medical Wikipedia, Medical Guidelines, Medical Coding, and open-source clinical documents) and merged back with the SLERP method in their base model to conserve general abilities. One model combined all five experts into one general expert with the multi-model merging method BreadCrumbs. Finally, we clinically aligned this general expert using our large-scale MediFlow corpora (see dataset `microsoft/mediflow`) to obtain the final expert model `MediPhi-Instruct`.

## Model Details
### Model Description

This model is the `MediPhi-Instruct` aligned to accomplish clinical NLP tasks.

- **Developed by:** Microsoft Healthcare \& Life Sciences
- **Model type:** Phi3
- **Language(s) (NLP):** English
- **License:** MIT
- **Finetuned from model:** `microsoft/MediPhi`, and originally from `microsoft/Phi-3.5-mini-instruct`

### Model Sources

- **Repository:** Current HF repo
- **Paper:** [A Modular Approach for Clinical SLMs Driven by Synthetic Data with Pre-Instruction Tuning, Model Merging, and Clinical-Tasks Alignment](https://arxiv.org/abs/2505.10717)

## Intended Uses
### Primary Use Cases
The model is intended for research use in English, especially clinical natural language processing. The model provides uses for research which require:

- **Medically adapted language models**
- Memory/compute constrained environments
- Latency bound scenarios

Our model is designed to accelerate research on language models in medical and clinical scenarios. It should be used for research purposes, i.e., in benchmarking context or with expert user verification of the outputs.

### Use Case Considerations
Our models are not specifically designed or evaluated for all downstream purposes. Researchers (or developers) should consider common limitations of language models as they select use cases, and evaluate and mitigate for accuracy, safety, and fariness before using within a specific downstream use case, particularly for high risk scenarios. Researchers (or developers) should be aware of and adhere to applicable laws or regulations (including privacy, trade compliance laws, etc.) that are relevant to their use case.

**Nothing contained in this Model Card should be interpreted as or deemed a restriction or modification to the license the model is released under.**

### Responsible AI Considerations
Like other language models, the Phi family of models and the MediPhi collection can potentially behave in ways that are unfair, unreliable, or offensive. Some of the limiting behaviors to be aware of include:

- Quality of Service: The Phi and MediPhi models are trained primarily on English text and some additional multilingual text. Languages other than English will experience worse performance as well as performance disparities across non-English. English language varieties with less representation in the training data might experience worse performance than standard American English.
- Multilingual performance and safety gaps: We believe it is important to make language models more widely available across different languages, but the Phi 3 models still exhibit challenges common across multilingual releases. As with any deployment of LLMs, developers will be better positioned to test for performance or safety gaps for their linguistic and cultural context and customize the model with additional fine-tuning and appropriate safeguards.
- Representation of Harms & Perpetuation of Stereotypes: These models can over- or under-represent groups of people, erase representation of some groups, or reinforce demeaning or negative stereotypes. Despite safety post-training, these limitations may still be present due to differing levels of representation of different groups, cultural contexts, or prevalence of examples of negative stereotypes in training data that reflect real-world patterns and societal biases.
- Inappropriate or Offensive Content: These models may produce other types of inappropriate or offensive content, which may make it inappropriate to deploy for sensitive contexts without additional mitigations that are specific to the case.
Information Reliability: Language models can generate nonsensical content or fabricate content that might sound reasonable but is inaccurate or outdated.
- Limited Scope for Code: Majority of Phi-3 training data is based in Python and use common packages such as "typing, math, random, collections, datetime, itertools". If the model generates Python scripts that utilize other packages or scripts in other languages, we strongly recommend users manually verify all API uses.
- Long Conversation: Phi-3 models, like other models, can in some cases generate responses that are repetitive, unhelpful, or inconsistent in very long chat sessions in both English and non-English languages. Developers are encouraged to place appropriate mitigations, like limiting conversation turns to account for the possible conversational drift

Researchers should apply responsible AI best practices, including mapping, measuring, and mitigating risks associated with their specific use case and cultural, linguistic context. They are encouraged to rigorously evaluate the model for their use case, fine-tune the models when possible and leverage the models as part of broader AI systems with language-specific safeguards in place. Important areas for consideration include:

- Allocation: Models may not be suitable for scenarios that could have consequential impact on legal status or the allocation of resources or life opportunities (ex: housing, employment, credit, etc.) without further assessments and additional debiasing techniques.
- High-Risk Scenarios: Researchers should assess the suitability of using models in high-risk scenarios where unfair, unreliable or offensive outputs might be extremely costly or lead to harm. This includes providing advice in sensitive or expert domains where accuracy and reliability are critical (ex: legal or health advice). Additional safeguards should be implemented at the application level according to the deployment context.
- Misinformation: Models may produce inaccurate information. Researchers should follow transparency best practices and inform end-users they are interacting with an AI system. At the application level, developers can build feedback mechanisms and pipelines to ground responses in use-case specific, contextual information, a technique known as Retrieval Augmented Generation (RAG).
- Generation of Harmful Content: Researchers should assess outputs for their context and use available safety classifiers or custom solutions appropriate for their use case.
- Misuse: Other forms of misuse such as fraud, spam, or malware production may be possible, and developers should ensure that their applications do not violate applicable laws and regulations.

## How to Get Started with the Model

### Input Format

    <|system|>
    GIVE A ROLE AND INSTRUCTIONS FOR CLINICAL NLPTASKS<|end|>
    <|user|>
    INPUT DOCUMENT<|end|>
    <|assistant|>

### Loading the model locally

    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline, StoppingCriteria

    torch.random.manual_seed(0)

    model_name = "microsoft/MediPhi-Instruct"
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="cuda",
        torch_dtype="auto",
        trust_remote_code=True,
    )
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    prompt = "Operative Report:\nPerformed: Cholecystectomy\nOperative Findings: The gallbladder contained multiple stones and had thickening of its wall. Mild peritoneal fluid was noted."

    messages = [
        {"role": "system", "content": "Extract medical keywords from this operative notes focus on anatomical, pathological, or procedural vocabulary."},
        {"role": "user", "content": prompt},
    ]

    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
    )

    class EosListStoppingCriteria(StoppingCriteria):
      def __init__(self, eos_sequence = [32007]):
          self.eos_sequence = eos_sequence
  
      def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor, **kwargs) -> bool:
          last_ids = input_ids[:,-len(self.eos_sequence):].tolist()
          return self.eos_sequence in last_ids

    generation_args = {
        "max_new_tokens": 500,
        "return_full_text": False,
        "temperature": 0.0,
        "do_sample": False,
        "generation_kwargs": {"stopping_criteria": EosListStoppingCriteria()}
    }

    output = pipe(messages, **generation_args)
    print(output[0]['generated_text'])
    # gallbladder stones, wall thickening, peritoneal fluid

Notes: If you want to use flash attention, call `AutoModelForCausalLM.from_pretrained()` with `attn_implementation="flash_attention_2"`.

### More Information

Check `microsoft/Phi-3.5-mini-instruct` for details about the tokenizer, requirements and basic capabilities.

## Training Details

### Training Data

Continual Pre-training:
- PubMed (commercial subset) and abstracts from `ncbi/pubmed`.
- Medical Guideline `epfl-llm/guidelines`.
- Medical Wikipedia `jpcorb20/medical_wikipedia`.
- Medical Coding: ICD10CM, ICD10PROC, ICD9CM, ICD9PROC, and ATC.
- Clinical documents:
    - `zhengyun21/PMC-Patients`, `akemiH/NoteChat`, and `starmpcc/Asclepius-Synthetic-Clinical-Notes` (only commercial-friendly licenses across all three datasets)
    - mtsamples

Clinical alignment:
- `microsoft/mediflow`

See paper for details.

### Training Procedure

Modular training making five experts from the base model with pre-instruction tuning, merging them into one model and finally clinically aligning it. See paper for details.

## Evaluation

#### CLUE+ Benchmark

|              | Phi-3.5-mini-instruct | PubMed | Clinical | MedWiki | Guideline | MedCode | MediPhi | MediPhi-Instruct |
|:-------------|----------------------:|-------:|---------:|--------:|----------:|--------:|--------:|-----------------:|
| **MedNLI**       | 66.6 | 68.3 | 69.2 | 72.8 | 70.3 | 68.5 | 66.9 | 71.0 |
| **PLS**          | 28.4 | 29.2 | 29.4 | 29.2 | 29.8 | 22.3 | 28.8 | 26.0 |
| **MeQSum**       | 36.7 | 37.6 | 38.1 | 37.6 | 37.6 | 33.5 | 37.9 | 42.8 |
| **LH**           | 45.9 | 45.7 | 43.5 | 43.6 | 41.1 | 45.7 | 45.7 | 45.0 |
| **MeDiSumQA**    | 25.9 | 26.3 | 26.7 | 25.1 | 25.1 | 23.6 | 26.1 | 29.1 |
| **MeDiSumCode**  | 41.1 | 41.0 | 40.5 | 41.7 | 41.9 | 39.0 | 41.7 | 37.2 |
| **RRS QA**       | 41.2 | 44.1 | 52.1 | 46.7 | 48.9 | 45.6 | 44.5 | 61.6 |
| **MedicationQA** | 11.2 | 10.3 | 12.0 | 12.2 | 11.9 | 12.0 | 11.3 | 19.3 |
| **MEDEC**        | 14.8 | 22.2 | 34.5 | 28.8 | 28.3 | 18.1 | 29.1 | 34.4 |
| **ACI**          | 42.3 | 42.7 | 43.9 | 44.7 | 44.7 | 39.0 | 44.3 | 43.5 |
| **SDoH**         | 35.1 | 35.8 | 35.8 | 43.6 | 41.0 | 24.8 | 39.7 | 56.7 |
| **ICD10CM**      | 49.3 | 49.5 | 49.6 | 50.2 | 49.8 | 68.7 | 55.5 | 54.9 |
| **Average**      | **36.5** | **37.7** | **39.6** | **39.7** | **39.2** | **36.7** | **39.3** | **43.4** |

New real-world benchmarking also demonstrated good performances on clinical information extraction task: [2507.05517](https://arxiv.org/abs/2507.05517).

#### Red Teaming

We carried out a [Medical Red Teaming Protocol of Language Models](https://arxiv.org/abs/2507.07248) in which we demonstrate broad conversation of original Phi3.5 safety abilities (see [Phi-3 Safety Post-Training](https://arxiv.org/abs/2407.13833)). All six merged MediPhi models fully conserve their base model's safety capabilities. For `MediPhi-Instruct`, it conserved safe behaviors towards jailbreaking and harmfulness, as well as it is improving considerably on groundedness. We further demonstrate safe behaviours at refusing or giving warnings with limited responses for nearly all harmful queries from clinican and patient user perspectives, based on MedSafetyBench and our PatientSafetyBench.

## Technical Specifications

### Model Architecture

Phi-3.5-mini has 3.8B parameters and is a dense decoder-only Transformer model using the same tokenizer as Phi-3 Mini. It is best suited for prompts using chat format but plain text is also possible. The default context length is of 128K tokens.

#### Hardware

Note that by default, the Phi-3.5-mini-instruct model uses flash attention, which requires certain types of GPU hardware to run. We have tested on the following GPU types:
- NVIDIA A100
- NVIDIA A6000
- NVIDIA H100

If you want to run the model on:
- NVIDIA V100 or earlier generation GPUs: call AutoModelForCausalLM.from_pretrained() with attn_implementation="eager"

#### Software

- [PyTorch](https://github.com/pytorch/pytorch)
- [Transformers](https://github.com/huggingface/transformers)
- [Flash-Attention](https://github.com/HazyResearch/flash-attention)

## License

The model is licensed under the [MIT license](https://huggingface.co/microsoft/Phi-3.5-mini-instruct/blob/main/LICENSE).

## Trademarks
This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft trademarks or logos is subject to and must follow [Microsoft’s Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks). Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship. Any use of third-party trademarks or logos are subject to those third-party’s policies.

## Citation

    @article{corbeil2025modular,
        title={A Modular Approach for Clinical SLMs Driven by Synthetic Data with Pre-Instruction Tuning, Model Merging, and Clinical-Tasks Alignment},
        author={Corbeil, Jean-Philippe and Dada, Amin and Attendu, Jean-Michel and Abacha, Asma Ben and Sordoni, Alessandro and Caccia, Lucas and Beaulieu, Fran{\c{c}}ois and Lin, Thomas and Kleesiek, Jens and Vozila, Paul},
        journal={arXiv preprint arXiv:2505.10717},
        year={2025}
    }


## Model Card Authors

Jean-Philippe Corbeil

## Model Card Contact

jcorbeil@microsoft.com
