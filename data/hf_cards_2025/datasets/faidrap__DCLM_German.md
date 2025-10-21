---
license: cc-by-4.0
language:
- de
multilinguality:
- monolingual
source_datasets:
- original
task_categories:
- text-generation
task_ids:
- language-modeling
pretty_name: DCLM-German
tags:
- pretraining
- german
- common-crawl
- fasttext-filtered
---

# DCLM German Dataset

This dataset contains German language data processed for LLM pretraining, filtered using FastText language detection.

## Dataset Description

- **Language**: German (de)
- **Size**: 43,452 compressed JSONL files
- **Source**: Common Crawl data
- **Processing**: RefinedWeb, Deduplication, FastText filtering

## Usage

```python
from datasets import load_dataset

# Load the entire dataset
dataset = load_dataset("faidrap/DCLM_German")

# Stream for large datasets (recommended)
dataset = load_dataset("faidrap/DCLM_German", streaming=True)

# Access the data
for example in dataset['train']:
    print(example['text'][:100])  # Print first 100 chars
```

## Example Data

```json
{
  "text": "Link zu diesem Datensatz\nPerson Benn, Tony\nAndere Namen Benn, Anthony W.\nWedgewood Benn, Anthony N.\nBenn, Anthony N.\nQuelle LCAuth, BLC (1976) gegen B 1986\nZeit Lebensdaten: 1925-2014\nLand Großbritann...",
  "metadata": {
    "WARC-Type": "response",
    "WARC-Date": "2014-08-31T00:55:33Z",
    "WARC-Record-ID": "<urn:uuid:7c1eb6e4-ca7d-45db-8532-327512f38e85>",
    "Content-Length": "7963",
    "Content-Type": "application/http; msgtype=response",
    "WARC-Warcinfo-ID": "<urn:uuid:7986c2c0-02c6-4aa2-bf61-e0ba102eec83>",
    "WARC-Concurrent-To": "<urn:uuid:8fac34c7-8aeb-4172-ac59-901f0cf8f5c4>",
    "WARC-IP-Address": "193.175.100.140",
    "WARC-Target-URI": "http://d-nb.info/gnd/118983296/about/html",
    "WARC-Payload-Digest": "sha1:LCYNHVTW44EVGQUJVSACQDW2LYWR5BMR",
    "WARC-Block-Digest": "sha1:LAXUCR2PMR5HYXFBDDJPAXQQHUWIH6CD",
    "WARC-Truncated": ""
  },
  "warcinfo": "robots: classic\r\nhostname: ip-10-180-136-8.ec2.internal\r\nsoftware: Nutch 1.6 (CC)/CC WarcExport 1.0\r\nisPartOf: CC-MAIN-2014-35\r\noperator: CommonCrawl Admin\r\ndescription: Wide crawl of the web with URLs provided by Blekko for August 2014\r\npublisher: CommonCrawl\r\nformat: WARC File Format 1.0\r\nconformsTo: http://bibnum.bnf.fr/WARC/WARC_ISO_28500_version1_latestdraft.pdf",
  "url": "http://d-nb.info/gnd/118983296/about/html",
  "language_id_whole_page_fasttext": {
    "de": 0.9169723987579346
  },
  "previous_word_count": 51,
  "fasttext_oh25_german_prob": 0.19228917360305786
}
```

## License

This dataset is released under CC-BY-4.0 license. Please ensure compliance with Common Crawl's terms of use.

## Citation

If you use this dataset, please cite:

```bibtex
@dataset{dclm_german,
  title={DCLM-German Dataset},
  author={Faidra Anastasia Patsatzi},
  year={2024},
  url={https://huggingface.co/datasets/faidrap/DCLM_German}
}
```
