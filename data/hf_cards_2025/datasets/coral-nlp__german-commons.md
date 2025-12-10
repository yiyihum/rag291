---
annotations_creators:
- machine-generated
language_creators:
- found
language:
- de
license:
- odc-by
multilinguality:
- monolingual
size_categories:
- 100B<n
source_datasets: []
task_categories:
- text-generation
task_ids:
- language-modeling
pretty_name: German Commons
tags:
- german
- commons
- legal
- scientific
- cultural
- political
- web
- news
- economic
configs:
- config_name: default
  data_files: subset=*/source=*/*.parquet
  default: true
  features:
  - name: id
    dtype: string
  - name: source
    dtype: string
  - name: subset
    dtype:
      class_label:
        names:
        - Cultural
        - Economic
        - Legal
        - News
        - Political
        - Scientific
        - Web
  - name: text
    dtype: string
  - name: license
    dtype:
      sequence: string
  - name: num_tokens
    dtype: int64
  - name: perplexity
    dtype: float64
  - name: ocr_score
    dtype: int64
  splits:
  - name: train
    num_examples: 36773579
- config_name: cultural
  data_files:
  - split: blbooks
    path: subset=Cultural/source=BLBooks/*.parquet
  - split: dibilit
    path: subset=Cultural/source=DiBiLit/*.parquet
  - split: dibiphil
    path: subset=Cultural/source=DiBiPhil/*.parquet
  - split: germanpd
    path: subset=Cultural/source=GermanPD/*.parquet
  - split: mosel
    path: subset=Cultural/source=MOSEL/*.parquet
  - split: sbbfulltexts
    path: subset=Cultural/source=SBB Fulltexts/*.parquet
  - split: wikisource
    path: subset=Cultural/source=Wikisource/*.parquet
  - split: wikivoyage
    path: subset=Cultural/source=Wikivoyage/*.parquet
  - split: wikiquote
    path: subset=Cultural/source=Wikiquote/*.parquet
  features:
  - name: id
    dtype: string
  - name: source
    dtype: string
  - name: subset
    dtype:
      class_label:
        names:
        - Cultural
        - Economic
        - Legal
        - News
        - Political
        - Scientific
        - Web
  - name: text
    dtype: string
  - name: license
    dtype:
      sequence: string
  - name: num_tokens
    dtype: int64
  - name: perplexity
    dtype: float64
  - name: ocr_score
    dtype: int64
- config_name: economic
  data_files:
  - split: tedeutenders
    path: subset=Economic/source=TEDEUTenders/*.parquet
  features:
  - name: id
    dtype: string
  - name: source
    dtype: string
  - name: subset
    dtype:
      class_label:
        names:
        - Cultural
        - Economic
        - Legal
        - News
        - Political
        - Scientific
        - Web
  - name: text
    dtype: string
  - name: license
    dtype:
      sequence: string
  - name: num_tokens
    dtype: int64
  - name: perplexity
    dtype: float64
  - name: ocr_score
    dtype: int64
- config_name: legal
  data_files:
  - split: bverfgaes
    path: subset=Legal/source=Amtliche Entscheidungssammlung des Bundesverfassungsgerichts/*.parquet
  - split: bundesrecht
    path: subset=Legal/source=Deutsches Bundesrecht/*.parquet
  - split: bag
    path: subset=Legal/source=Entscheidungen des Bundesarbeitsgerichts/*.parquet
  - split: bfh
    path: subset=Legal/source=Entscheidungen des Bundesfinanzhofs/*.parquet
  - split: bgh
    path: subset=Legal/source=Entscheidungen des Bundesgerichtshofs/*.parquet
  - split: bgh20
    path: subset=Legal/source=Entscheidungen des Bundesgerichtshofs in Strafsachen
      aus dem 20. Jahrhundert/*.parquet
  - split: bpatg
    path: subset=Legal/source=Entscheidungen des Bundespatentgerichts/*.parquet
  - split: bverfg
    path: subset=Legal/source=Entscheidungen des Bundesverfassungsgerichts/*.parquet
  - split: bverwg
    path: subset=Legal/source=Entscheidungen des Bundesverwaltungsgerichts/*.parquet
  - split: eurlex
    path: subset=Legal/source=EurLEX/*.parquet
  - split: openlegaldata
    path: subset=Legal/source=Open Legal Data/*.parquet
  features:
  - name: id
    dtype: string
  - name: source
    dtype: string
  - name: subset
    dtype:
      class_label:
        names:
        - Cultural
        - Economic
        - Legal
        - News
        - Political
        - Scientific
        - Web
  - name: text
    dtype: string
  - name: license
    dtype:
      sequence: string
  - name: num_tokens
    dtype: int64
  - name: perplexity
    dtype: float64
  - name: ocr_score
    dtype: int64
- config_name: news
  data_files:
  - split: anno
    path: news_anno_*.parquet
  - split: zeitungsportal
    path: news_deutsches_zeitungsportal_*.parquet
  - split: europeana
    path: news_europeana_newspapers_*.parquet
  - split: wikinews
    path: news_wikinews_*.parquet
  features:
  - name: id
    dtype: string
  - name: source
    dtype: string
  - name: subset
    dtype:
      class_label:
        names:
        - Cultural
        - Economic
        - Legal
        - News
        - Political
        - Scientific
        - Web
  - name: text
    dtype: string
  - name: license
    dtype:
      sequence: string
  - name: num_tokens
    dtype: int64
  - name: perplexity
    dtype: float64
  - name: ocr_score
    dtype: int64
- config_name: political
  data_files:
  - split: btdrucksachen
    path: subset=Political/source=Drucksachen des Bundestages/*.parquet
  - split: eurovoc
    path: subset=Political/source=EuroVoc/*.parquet
  - split: germanpoliticalspeeches
    path: subset=Political/source=German Political Speeches/*.parquet
  - split: btplenarprotokolle
    path: subset=Political/source=Plenarprotokolle des Bundestages/*.parquet
  - split: reichtagsprotokolle
    path: subset=Political/source=Reichtagsprotokolle/*.parquet
  features:
  - name: id
    dtype: string
  - name: source
    dtype: string
  - name: subset
    dtype:
      class_label:
        names:
        - Cultural
        - Economic
        - Legal
        - News
        - Political
        - Scientific
        - Web
  - name: text
    dtype: string
  - name: license
    dtype:
      sequence: string
  - name: num_tokens
    dtype: int64
  - name: perplexity
    dtype: float64
  - name: ocr_score
    dtype: int64
- config_name: scientific
  data_files:
  - split: arxiv
    path: subset=Scientific/source=arXiv/*.parquet
  - split: doab
    path: subset=Scientific/source=Directory of Open Access Books/*.parquet
  - split: polyjournal
    path: subset=Scientific/source=Polytechnisches Journal/*.parquet
  - split: wikibooks
    path: subset=Scientific/source=Wikibooks/*.parquet
  - split: openalex
    path: subset=Scientific/source=OpenAlex/*.parquet
  - split: wikiversity
    path: subset=Scientific/source=Wikiversity/*.parquet
  features:
  - name: id
    dtype: string
  - name: source
    dtype: string
  - name: subset
    dtype:
      class_label:
        names:
        - Cultural
        - Economic
        - Legal
        - News
        - Political
        - Scientific
        - Web
  - name: text
    dtype: string
  - name: license
    dtype:
      sequence: string
  - name: num_tokens
    dtype: int64
  - name: perplexity
    dtype: float64
  - name: ocr_score
    dtype: int64
- config_name: web
  data_files:
  - split: onemillionposts
    path: subset=Web/source=One Million Posts/*.parquet
  - split: thestack
    path: subset=Web/source=The Stack/*.parquet
  - split: wikidiscussions
    path: subset=Web/source=Wiki Discussions/*.parquet
  - split: wikipedia
    path: subset=Web/source=Wikipedia/*.parquet
  - split: youtubecommons
    path: subset=Web/source=Youtube Commons/*.parquet
  features:
  - name: id
    dtype: string
  - name: source
    dtype: string
  - name: subset
    dtype:
      class_label:
        names:
        - Cultural
        - Economic
        - Legal
        - News
        - Political
        - Scientific
        - Web
  - name: text
    dtype: string
  - name: license
    dtype:
      sequence: string
  - name: num_tokens
    dtype: int64
  - name: perplexity
    dtype: float64
  - name: ocr_score
    dtype: int64
---

# German Commons - 154 Billion Tokens of Openly Licensed Text for German Language Models

A comprehensive collection of German-language text data under open licenses for training German language models.

- **Datasheet**: [DATASHEET.md](DATASHEET.md).
- **Paper**: [arxiv.org/abs/2510.13996](https://arxiv.org/abs/2510.13996)
- **Code**: [github.com/coral-nlp/llmdata](https://github.com/coral-nlp/llmdata)
- **Bloom Filter** (DOLMA-compatible): [bloom_filter.bin](bloom_filter.bin)

## Dataset Description

This dataset is aggregated from **41 diverse sources** and contains **154.56 billion tokens** of German text data with **35.78 million documents** spanning **7 thematic domains**:

- 🌐 **Web Commons**: 19.89B tokens source from Wiki projects, online discussions, code repositories, social media posts, YouTube transcripts
- 💬 **Political Commons**: 3.57B tokens sourced from parliamentary documents, speeches, protocols, political vocabulary
- ⚖️ **Legal Commons**: 2.99B tokens sourced from court decisions, federal law, legal databases, EU legal documents
- 📰 **News Commons**: 72.67B tokens sourced from historical and current newspapers archives
- 🏦 **Economics Commons**: 0.11B tokens sourced from EU public tenders
- 📚 **Cultural Commons**: 54.49B tokens sourced from cultural heritage collections
- 🔬 **Scientific Commons**: 0.84B tokens sourced from scholarly papers, books, and technical journals

## Dataset Features

Each record contains the following fields:

- **id**: Unique identifier string, as per each documents' source dataset
- **source**: Source dataset name
- **subset**: Thematic subset (Cultural, Legal, Political, Scientific, News, Web, Economic)
- **text**: Main text content; deduplicated, quality filtered, with consistent formatting and encoding. Can be split at newlines to obtain paragraph text.
- **license**: List of applicable licenses for each document, given as canonical SPDX license URL.
- **num_tokens**: GPT-2 token count
- **perplexity**: Text perplexity measured with a KenLM model trained on German Wikipedia text
- **ocr_score**: OCR quality score measured using [OCRoscope](https://github.com/Pleias/OCRoscope)

## Dataset Usage

- Load the entire dataset

  ```python
  from datasets import load_dataset
  
  ds = load_dataset("coral-nlp/german-commons")
  ```

- Load a thematic subset

  ```python
  ds = load_dataset("coral-nlp/german-commons", "cultural")
  ```

- Load individual source datasets

  ```python
  wikipedia = load_dataset("coral-nlp/german-commons", "web", split="wikipedia")
  ```

Supported splits and constituent datasets are:

| Subset | Split Key | Dataset Name | Docs | Tokens | License | Text Type | Source |
|:-------------|:----------------------------|:------------------------------------------------------|----------:|---------------:|:-------------|:---------------------------|:----------------------------------------------------------------- |
| `web` | `wikipedia` | Wikipedia | 2,930,224 | 2,948,751,608 | CC-BY-SA-4.0 | Various | [🔗](https://zenodo.org/records/14748605) |
| `web` | `wikivoyage` | Wikivoyage | 20,370 | 42,025,478 | CC-BY-SA-4.0 | Travel | [🔗](https://zenodo.org/records/14748553) |
| `web` | `wikidiscussions` | Wikipedia Discussions | 8,349,076 | 1,218,210,917 | CC-BY-SA-4.0 | Online Discussions | [🔗](https://corpora.ids-mannheim.de/pub/wikipedia-deutsch/2024/) |
| `web` | `youtubecommons` | YouTube Commons | 2,809,714 | 14,478,850,964 | Various | Video Subtitles | [🔗](https://huggingface.co/datasets/PleIAs/YouTube-Commons) |
| `web` | `onemillionposts` | One Million Posts Corpus | 946,082 | 94,872,633 | CC-BY-4.0 | Online Discussions | [🔗](https://ofai.github.io/million-post-corpus/) |
| `web` | `thestack` | The Stack (Markdown and TXT Subsets) | 421,466 | 1,105,173,228 | Various | Various | [🔗](https://huggingface.co/datasets/bigcode/the-stack-dedup) |
| `political` | `reichtagsprotokolle` | Reichtagsprotokolle | 522 | 703,495,637 | CC-BY-SA-4.0 | Parliamentary Protocols | [🔗](https://zenodo.org/records/10225467) |
| `political` | `germanpoliticalspeeches` | German Political Speeches | 6,678 | 29,409,655 | CC-BY-4.0 | Speech Transcripts | [🔗](https://zenodo.org/records/3611246) |
| `political` | `btdrucksachen` | Corpus der Drucksachen des Deutschen Bundestages | 3,017 | 528,769,669 | CC0-1.0 | Parliamentary Publications | [🔗](https://zenodo.org/records/4643066) |
| `political` | `btplenarprotokolle` | Corpus der Plenarprotokolle des Deutschen Bundestages | 1,833 | 316,034,708 | CC0-1.0 | Parliamentary Protocols | [🔗](https://zenodo.org/records/4542662) |
| `political` | `eurovoc` | EuroVoc | 245,838 | 1,988,111,462 | EUPL | Parliamentary Publications | [🔗](https://huggingface.co/datasets/EuropeanParliament/Eurovoc) |
| `legal` | `bundesrecht` | Corpus des Deutschen Bundesrechts | 3,217 | 1,004,294 | CC0-1.0 | German Federal Laws | [🔗](https://zenodo.org/records/14592346) |
| `legal` | `openlegaldata` | OpenLegalData | 249,909 | 1,915,956,613 | CC0-1.0 | Court Decisions | [🔗](https://huggingface.co/datasets/schneiderai/openlegaldata) |
| `legal` | `bfh` | Corpus der Entscheidungen des BFH | 10,885 | 67,791,931 | CC0-1.0 | Court Decisions | [🔗](https://zenodo.org/records/14622341) |
| `legal` | `bgh20` | Entscheidungen des BGH in Strafsachen des 20. Jhd. | 36,062 | 92,873,390 | CC0-1.0 | Court Decisions | [🔗](https://zenodo.org/records/4540377) |
| `legal` | `bgh` | Corpus der Entscheidungen des BGH | 77,258 | 292,832,709 | CC0-1.0 | Court Decisions | [🔗](https://zenodo.org/records/12814022) |
| `legal` | `bverfg` | Corpus der Entscheidungen des BVerfG | 8,028 | 39,503,223 | CC0-1.0 | Court Decisions | [🔗](https://zenodo.org/records/12705674) |
| `legal` | `bpatg` | Corpus der Entscheidungen des BpatG | 30,705 | 185,099,188 | CC0-1.0 | Court Decisions | [🔗](https://zenodo.org/records/10849977) |
| `legal` | `bverwg` | Corpus der Entscheidungen des BVerwG | 27,185 | 123,487,739 | CC0-1.0 | Court Decisions | [🔗](https://zenodo.org/records/10809039) |
| `legal` | `bverfgaes` | Corpus der amtl. Entscheidungssammlung des BVerfG | 919 | 24,427,294 | CC0-1.0 | Court Decisions | [🔗](https://zenodo.org/records/10783177) |
| `legal` | `bag` | Corpus der Entscheidungen des BAG | 5,624 | 48,248,111 | CC0-1.0 | Court Decisions | [🔗](https://zenodo.org/records/4006645) |
| `legal` | `eurlex` | EurLEX | 64,934 | 201,263,562 | CC-BY-4.0 | European Union Laws | [🔗](https://zenodo.org/record/5363165/) |
| `news` | `zeitungsportal` | Deutsches Zeitungsportal | 8,076,164 | 43,871,094,547 | CC0-1.0 | News Articles | [🔗](https://www.deutsche-digitale-bibliothek.de/newspaper) |
| `news` | `europeana` | Europeana Newspapers | 3,256,341 | 20,684,418,365 | CC0-1.0 | News Articles | [🔗](https://huggingface.co/datasets/biglam/europeana_newspapers) |
| `news` | `anno` | ANNO | 1,910,281 | 8,103,825,248 | CC0-1.0 | News Articles | [🔗](https://labs.onb.ac.at/en/datasets/anno/) |
| `news` | `wikinews` | WikiNews | 23,266 | 14,222,520 | CC-BY-4.0 | News Articles | [🔗](https://de.wikinews.org) |
| `economic` | `tedeutenders` | TEDEUTenders | 57,214 | 110,611,112 | CC0-1.0 | Procurement Notices | [🔗](https://huggingface.co/datasets/PleIAs/TEDEUTenders) |
| `cultural` | `dibilit` | DiBiLit-Korpus | 2,062 | 216,391,448 | CC-BY-SA-4.0 | Literature | [🔗](https://zenodo.org/records/5786725) |
| `cultural` | `dibiphil` | DiBiPhil-Korpus | 269 | 32,151,997 | CC-BY-SA-4.0 | Literature | [🔗](https://github.com/deutschestextarchiv/DiBiPhil) |
| `cultural` | `wikisource` | Wikisource | 240,689 | 347,770,430 | CC-BY-SA-4.0 | Various | [🔗](https://dumps.wikimedia.org/dewikisource/20250801/) |
| `cultural` | `germanpd` | German-PD | 123,592 | 49,333,198,231 | CC0-1.0 | Literature | [🔗](https://huggingface.co/datasets/PleIAs/German-PD) |
| `cultural` | `blbooks` | BLBooks | 3,714 | 1,012,047,216 | CC0-1.0 | Literature | [🔗](https://huggingface.co/datasets/biglam/blbooks-parquet) |
| `cultural` | `mosel` | MOSEL | 3,127,203 | 3,181,917,752 | CC-BY-4.0 | Speech Transcripts | [🔗](https://huggingface.co/datasets/FBK-MT/mosel) |
| `cultural` | `sbbfulltexts` | SBB Fulltexts | 2,605,569 | 358,514,283 | CC-BY-4.0 | Literature | [🔗](https://zenodo.org/records/7716098) |
| `cultural` | `wikiquote` | Wikiquote | 8,612 | 6,688,458 | CC-BY-4.0 | Quotes & Proverbs | [🔗](https://de.wikiquote.org) |
| `scientific` | `wikibooks` | Wikibooks | 346 | 180,257,799 | CC-BY-SA-4.0 | Educational Books | [🔗](https://zenodo.org/records/14748586) |
| `scientific` | `polyjournal` | Digitalisierung des Polytechnischen Journals | 27,292 | 50,434,996 | CC-BY-SA-4.0 | Scholarly Papers | [🔗](https://github.com/deutschestextarchiv/dingler) |
| `scientific` | `doab` | Directory of Open Access Books | 1,939 | 166,920,321 | Various | Scholarly Books | [🔗](https://www.doabooks.org) |
| `scientific` | `arxiv` | arXiv | 8 | 103,478 | Various | Scholarly Papers | [🔗](https://www.kaggle.com/datasets/Cornell-University/arxiv) |
| `scientific` | `openalex` | OpenAlex | 47,733 | 413,632,648 | Various | Educational Content | [🔗](https://de.wikiversity.org) |
| `scientific` | `wikiversity` | Wikiversity | 16,371 | 27,802,099 | CC-BY-SA-4.0 | Scholarly Papers | [🔗](https://openalex.org) |

## Citation

If you use this dataset, please cite the correponding paper:

```bibtex
@article{gienapp:2025d,
	title        = {{The German Commons -- 154 Billion Tokens of Openly Licensed Text for German Language Models}},
	author       = {Lukas Gienapp and
                    Christopher Schr\"oder and
                    Stefan Schweter and
                    Christopher Akiki and
                    Ferdinand Schlatt and
                    Arden Zimmermann and
                    Phillipe Gen\^et and
                    Martin Potthast},
	year         = 2025,
	month        = oct,
	journal      = {CoRR},
	volume       = {abs/2510.13996},
	url          = {https://arxiv.org/abs/2510.13996}
}
```

## License

This dataset aggregation and metadata is released under ODC-BY license. Individual documents have their own specific licenses - please check the `license` field for each record.