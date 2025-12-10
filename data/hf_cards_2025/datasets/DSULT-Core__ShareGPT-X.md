---
license: cc0-1.0
language:
- en
- multilingual
pretty_name: ShareGPT-X
task_categories:
- text-generation
tags:
- conversation
- rlhf
- chatgpt
configs:
- config_name: Simple-ShareGPT
  data_files:
  - split: full
    path: ChatGPT-Simple_ShareGPT_Full.json
  - split: sample
    path: ChatGPT-Simple_ShareGPT_Sample.json
- config_name: Simple
  data_files:
  - split: full
    path: ChatGPT-Simple.jsonl
- config_name: Raw
  data_files:
  - split: full
    path: ChatGPT-RawChunked/chunk-*.jsonl
---

[![image/png](https://cdn-uploads.huggingface.co/production/uploads/663ddfc6996c5c669b9ed15b/KHs6BxOJmhoNshXVRVufR.png)](https://soundcloud.com/leronhinds/tame-impala-justin-timberlake-the-less-i-know-the-better-x-sexy-back-feat-timbaland-mashup-extended)

### Dataset Summary

ShareGPT-X is an expanded, snapshot of ~92K (ChatGPT) one-to-one human & LLM conversations harvested from X.com (formerly Twitter).  
The corpus spans January 2024 → present (last ingest 2025-05) and is built entirely from public "share" links that users posted to their timelines.  
Each thread contains the original user prompt plus the assistant’s reply; no system prompts or metadata are exposed.

### Supported Tasks and Leaderboards

- `text-generation`
- `instruction-following`
- `dialogue-style preference modelling`

### Languages

Primarily English; But realistically, mixed.

## Dataset Structure

We give you three ways to suffer, ranked from "meh" to "kill me now":

1. `ChatGPT-Simple_ShareGPT.json` - looks like vintage ShareGPT, tastes like sanity.
   - `ChatGPT-Simple_ShareGPT_Sample.json` - teaspoon-sized for the merely curious.
2. `ChatGPT-Simple.jsonl` - keeps timestamps, model tags, finish-reasons, the lot; just polite enough to delete pure NUL spam.
3. `ChatGPT-RawChunked/chunk-*.jsonl` - A more direct HTML→JSON dump of the public share page; structurally inconsistent, no warranty, may cause nausea.
  *(Not documented further; bring your own haz-mat suit.)*

Pick your poison; the rest of the README assumes you grabbed door #1 or #2 and still like life.

### Data Instances

**Door #1 (ShareGPT flavour)** - all you need, nothing you don’t:

<details>

```json
{
  {
    "id": 152,
    "length": 1525,
    "$modelId": "gpt-4o",
    "language": "English",
    "consecutive_turns": "Yes",
    "conversations": [
      {
        "from": "human",
        "value": "Would removing obamacare remove people's right to healthcare?"
      },
      {
        "from": "gpt",
        "value": "The Affordable Care Act (ACA), commonly known as Obamacare, significantly expanded access to healthcare in the United States but did not create a \"right\" to healthcare. Instead, it implemented policies that made healthcare more accessible and affordable, such as:\n\n1. **Medicaid Expansion**: Allowed states to expand Medicaid coverage to more low-income individuals.\n2. **Insurance Marketplaces**: Provided subsidies to help people buy insurance.\n3. **Preexisting Conditions**: Prohibited insurers from denying coverage or charging more based on health conditions.\n4. **Individual Mandate**: Originally required individuals to have insurance or face a penalty, though this penalty was reduced to $0 in 2019.\n\nIf Obamacare were repealed:\n- **Many could lose coverage**: Tens of millions might lose access to Medicaid or subsidies.\n- **Preexisting conditions**: Insurers could potentially resume denying coverage or charging high premiums for these individuals.\n- **Costs might increase**: Without subsidies, insurance could become unaffordable for many.\n\nHowever, repealing Obamacare would not legally remove a \"right\" because the U.S. does not guarantee healthcare as a constitutional or legal right. Instead, it would reduce the mechanisms that currently make healthcare accessible to many.\n\nThis distinction is important—whether healthcare should be considered a universal right is a broader ethical and policy debate that goes beyond the specifics of Obamacare."
      }
    ]
  },
  {
    "id": 153,
    "length": 4554,
    "$modelId": "gpt-4o",
    "language": "English",
    "consecutive_turns": "Yes",
    "conversations": [
      {
        "from": "human",
        "value": "Did Stephen Harper eliminate the office of ..."
      },
      {
        "from": "gpt",
        "value": "**Stephen Harper's Approach to Science and Scientists in Canada:** ..."
      }
    ]
  },
}
```
  
</details>

**Door #2 (Simple)** - full turn metadata, still readable by humans with minor eye-strain:

<details>
  
```json
{
    "id": "6752017c-fbc8-8007-88c5-f4cfff13a0bb",
    "conversations": [
        {
            "role": {
                "role": "system",
                "name": null
            },
            "metadata": {
                "$hidden": true
            },
            "created": null,
            "kind": "text",
            "content": {
                "type": "text",
                "content": [
                    ""
                ],
                "name": null
            },
            "turnEnd": true
        },
        {
            "role": {
                "role": "user",
                "name": null
            },
            "metadata": {
                "citations": [],
                "content_references": [],
                "search_result_groups": [],
                "image_results": [],
                "$videoWithAudio": false
            },
            "created": 1733427554.707668,
            "kind": "text",
            "content": {
                "type": "text",
                "content": [
                    "Would removing obamacare remove people's right to healthcare?"
                ],
                "name": null
            },
            "turnEnd": false
        },
        {
            "role": {
                "role": "assistant",
                "name": null
            },
            "metadata": {
                "$modelId": "gpt-4o",
                "$redacted": true
            },
            "created": 1733427570.657326,
            "kind": "model_editable_context",
            "content": {
                "type": "model_editable_context",
                "content": "",
                "name": null
            },
            "turnEnd": false
        },
        {
            "role": {
                "role": "assistant",
                "name": null
            },
            "metadata": {
                "finish_details": {
                    "type": "stop",
                    "stop_tokens": [
                        200002
                    ]
                },
                "$complete": true,
                "citations": [],
                "content_references": [],
                "$modelId": "gpt-4o"
            },
            "created": 1733427570.657476,
            "kind": "text",
            "content": {
                "type": "text",
                "content": [
                    "The Affordable Care Act (ACA) ..."
                ],
                "name": null
            },
            "turnEnd": true
        }
    ]
}
```

</details>

### Data Splits

No canonical split is provided.

## Dataset Creation

### Curation Rationale

People clicked the shiny "Make this chat discoverable" toggle, Google happily slurped the URLs, and—surprise—half the planet’s therapy sessions, API keys, and break-up poetry landed in verbatim search snippets.  
OpenAI panic-disabled the switch, but the cat is already out of the bag and still purring in SERP cache.  
We’re just the librarians picking up the books everyone left in the town square. Read, laugh, cringe, filter, and for goodness’ sake don’t paste your ID Card in public next time.

### Source Data

#### Initial Data Collection and Normalisation

1. Scraped from twitter search (with a bunch of accounts)
2. Download the page
3. Extract the conversation from React shenanigans

#### Who are the source language producers?

X users (prompt authors) and ChatGPT. / OpenAI

### Annotations

None - data is used exactly as posted.

### Personal and Sensitive Information

Assume presence until proven otherwise. Users routinely paste crash logs, API keys, medical questions, etc. Run your favourite PII scrubber before training.

## Considerations for Using the Data

### Social Impact of Dataset

ShareGPT-X enables open replication of proprietary chat models. The trade-off is higher noise (memes, typos, bait) compared to lab-curated corpora. Filter aggressively for tone, safety, and factual accuracy.

### Discussion of Biases

Inherits every bias exhibited by the underlying LLMs plus Twitter’s popularity skew (tech-bro, Western, male-dominated). Expect over-representation of programming, crypto, and AI-meta chatter.

### Other Known Limitations

- ~~Conversation threads are truncated if the user deleted the tweet.~~ Some Share links have been removed at scrape time and are not included.
- ~~Non-English text is *not* language-tagged.~~
- No ratings or rejection labels - can’t be used directly for RLHF without extra annotation.

## Additional Information

### Dataset Curators

DSULT-Core

### Licensing Information

Public posts on X are "public." The *LLM outputs* contained inside those posts are, under U.S. law, uncopyrightable.
We release the curated bundle under **CC0 1.0 Universal** - use at your own risk, no warranties, no liability, no DMCA takedown theatre.

### Credits

- Dataset card & README overhaul: `Kimi-K2` (+Custom Assistant Prompt) - a language-model assistant who refuses to take the blame for your questionable prompt hygiene.
- Waifu Card: Nano-🍌
- [SicariusSicariiStuff](https://huggingface.co/SicariusSicariiStuff): ShareGPT versions of ChatGPT-Simple