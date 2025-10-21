---
configs:
- config_name: train
  data_files:
  - path:
    - train.jsonl.zst
    split: train
- config_name: trainable
  data_files:
  - path:
    - trainable.jsonl.zst
    split: train
task_categories:
- text-generation
- feature-extraction
language:
- en
tags:
- wikipedia
- paragraphs
- propositions
- analysis
- logic
---
# Wikipedia Propositions

Wikipedia Propositions is a dataset of English Wikipedia paragraphs paired with propositions extracted from those paragraphs.

The paragraphs are sourced from [agentlans/wikipedia-paragraphs-complete](https://huggingface.co/datasets/agentlans/wikipedia-paragraphs-complete) `sample_k10000` split and processed using the language model [ibm-granite/granite-3.3-8b-instruct](https://huggingface.co/ibm-granite/granite-3.3-8b-instruct).

Dataset Features:
- text: Paragraph text from English Wikipedia.
- id: A unique identifier generated as the MD5 hash of the paragraph text, encoded in base64 and truncated to 22 characters.
- propositions: A list of propositions (statements) derived from the paragraph text.
- paraphrase: A new paragraph written by [google/gemma-3-12b-it](https://huggingface.co/google/gemma-3-12b-it) based on the list of propositions.

Example entry:

```json
{
  "id": "Cs3IlJt8mbjGvgHqZKIIZQ",
  "text": "On January 7, 2011 Jessica 6 released its second single White Horse The song's music video directed by Marco Ovando premiered on February 28, 2011, on Perez Hilton's website. [...]",
  "propositions": [
    "On January 7, 2011, Jessica 6 released its second single 'White Horse'.",
    "The music video for 'White Horse' was directed by Marco Ovando.",
    "The music video for 'White Horse' premiered on February 28, 2011, on Perez Hilton's website.",
    "The music video for 'White Horse' received over two million views on YouTube.",
    "The music video for 'White Horse' received positive reviews from music critics.",
    "According to Michael Cragg's review for The Guardian, 'White Horse' creates a 'fresh take on 70s disco and filtered house with a dash of funk'.",
    "According to Michael Cragg's review for The Guardian, while Hercules & Love Affair lack a distinctive vocalist, Jessica 6 are elevated by Ruiz's smoky, melancholic voice.",
    "According to Robin Murray's review for Clash, 'White Horse' has a definite pop touch, but this does not discredit its fantastic production.",
    "The critical acclaim of the album solidified Jessica 6's status as a history-making global artist.",
    "Jessica 6 performed at the Greek MAD Video Music Awards on June 14, 2011, in Berlin's Tempodrom.",
    "Jessica 6 performed at London's prestigious Royal Albert Hall.",
    "Jessica 6 performed at Tate Modern.",
    "Jessica 6 made an appearance at Chile's Vina del Mar Festival, appearing with Chilean actress Daniela Vega."
  ],
  "paraphrase": "Following the release of their second single, 'White Horse,' on January 7, 2011, Jessica 6 experienced a surge in both critical and popular recognition, solidifying their position as a significant global act. [...]"
}
```

## Limitations

- Some propositions may lack clarity or sufficient context.
- Formulas and equations are not well processed.
- The dataset does not include images or tables, which may add useful information.
- Some propositions might contain information not explicitly present in the text and should be reviewed for possible hallucinations from the model.
- The paraphrases may contain AI slop phrases.

## License

This dataset is released under the Creative Commons Attribution 4.0 International (CC-BY 4.0) license.

