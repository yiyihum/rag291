---
base_model: google/gemma-2-9b
datasets:
- orai-nlp/ZelaiHandi
- HuggingFaceFW/fineweb
language:
- eu
library_name: transformers
pipeline_tag: text-generation
license: gemma
---

Gemma-Kimu-9B-Instruct v1.0 is an instruction large language model (LLM)  tailored specifically for the Basque language built from Google's Gemma-2-9b foundational and Gemma-2-9b instruct models,  The used approach decouples language adaptation from post-training alignment by first continually pre-training the foundational LLM on a modest amount of monolingual target-language data while anchoring on English replay, and then injecting instruction-following capabilities via delta-based weight merging from the instructed counterpart of the base LLM.

We first continually pre-train the base LLM on monolingual data in Basque to improve its linguistic capacity. Then, instead of post-training from scratch, we merge the post-training delta into the language-adapted model via weight merging. This simple yet effective method allows us to transfer not only instruction-following capabilities, but also human preference alignment.

Evaluations show that Gemma-Kimu-9b-it exhibits notable improvements over Gemma-2-9b-it in Basque in instruction following, safety, and linguistic correctness.

Want to test this model in a real setting? Join the waitlist:
[PLAYGROUND](https://kimu.orai.eus)

# Training Data

For continual pre-training, we leveraged a combination of Basque and English data to enhance linguistic performance in Basque while maintaining general English capabilities. The goal is to improve cross-lingual transfer by retaining the model's proficiency in English.

ZelaiHandi [ZelaiHandi dataset](https://huggingface.co/datasets/orai-nlp/ZelaiHandi) (San Vicente et al., 2024): ZelaiHandi is the largest collection of freely licensed and high-quality Basque texts gathered from selected web sources. This collection comprises approximately 521 million words which correspond to 1.5 billion tokens (Llama 3.1 tokenizer).

[FineWeb dataset](https://huggingface.co/datasets/HuggingFaceFW/fineweb) (Penedo et al., 2024): FineWeb consists of more than 15T tokens of cleaned and deduplicated English web data from CommonCrawl. We selected a random subset of around 300 million tokens (Llama 3.1 tokenizer)

# Evaluation

To evaluate the instruction-following capabilities of our models in Basque, we use the NoRobotsEU benchmark (Corral et al., 2025), a manually translated subset of the original NoRobots test set. It consists of 100 Basque instructions, each paired with its English counterpart, spanning 9 diverse categories.

<div class="tb tb-eu-l10">

| Model                        | Instruct follow. EU | Instruct follow. EN |
|------------------------------|---------------------|---------------------|
| Gemma-2-2b-it                |          7          |          71         |
| **Gemma-Kimu-2b-it**         |         **48**          |          **60**         |
| Gemma-2-9b-it                |         57          |        86       |
| **Gemma-Kimu-9b-it**         |       **71**        |          **82**         |

</div>

Additional evaluation results across linguistic proficiency and safety are included in (Sarasua et al., 2025).

# License

This model is derived from Gemma 2 and is licensed under the Gemma License. Copyright © Google DeepMind. All Rights Reserved.

# Acknowledgments

This work is part of the BasqueLLM project, titled "bi-SLM: Optimization of Industrial Processes through Bilingual SLMs" (EXP: 2025-CIE4-000048-01), partially funded by the Guipuzcoa Science, Technology and Innovation Network Program of the Provincial Council of Gipuzkoa. Model training and development were conducted using the Hyperion system at the Donostia International Physics Center (DIPC).

# Citation

If you use this model please cite the following reference:
```bibtex
@inproceedings{sarasua2025,
  title={DIPLomA: Efficient Adaptation of Instructed LLMs to Low-Resource Languages via Post-Training Delta Merging},
  author={Sarasua, Ixak and Corral, Ander and Saralegi, Xabier},
  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2025},
  year={2025}
}
```

# Contact

- Ixak Sarasua (i.sarasua@orai.eus)
- Ander Corral (a.corral@orai.eus)
- Xabier Saralegi (x.saralegi@orai.eus)