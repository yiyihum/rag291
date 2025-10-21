---
license: mit
multilinguality:
- multilingual
source_datasets:
- original
task_categories:
- text-classification
- token-classification
- question-answering
- summarization
- text-generation
task_ids:
- sentiment-analysis
- topic-classification
- named-entity-recognition
- language-modeling
- text-scoring
- multi-class-classification
- multi-label-classification
- extractive-qa
- news-articles-summarization
---


# Bittensor Subnet 13 Reddit Dataset

<center>
    <img src="https://huggingface.co/datasets/macrocosm-os/images/resolve/main/bittensor.png" alt="Data-universe: The finest collection of social media data the web has to offer">
</center>

<center>
    <img src="https://huggingface.co/datasets/macrocosm-os/images/resolve/main/macrocosmos-black.png" alt="Data-universe: The finest collection of social media data the web has to offer">
</center>


## Dataset Description

- **Repository:** veyhoranohy/reddit_dataset_248
- **Subnet:** Bittensor Subnet 13
- **Miner Hotkey:** 5CqkgVCUz6wXE2S92adiRjsqYH4euHAMkU3QGwT3YoQgbCha

### Dataset Summary

This dataset is part of the Bittensor Subnet 13 decentralized network, containing preprocessed Reddit data. The data is continuously updated by network miners, providing a real-time stream of Reddit content for various analytical and machine learning tasks.
For more information about the dataset, please visit the [official repository](https://github.com/macrocosm-os/data-universe).

### Supported Tasks

The versatility of this dataset allows researchers and data scientists to explore various aspects of social media dynamics and develop innovative applications. Users are encouraged to leverage this data creatively for their specific research or business needs.
For example:

- Sentiment Analysis
- Topic Modeling
- Community Analysis
- Content Categorization

### Languages

Primary language: Datasets are mostly English, but can be multilingual due to decentralized ways of creation.

## Dataset Structure

### Data Instances

Each instance represents a single Reddit post or comment with the following fields:


### Data Fields

- `text` (string): The main content of the Reddit post or comment.
- `label` (string): Sentiment or topic category of the content.
- `dataType` (string): Indicates whether the entry is a post or a comment.
- `communityName` (string): The name of the subreddit where the content was posted.
- `datetime` (string): The date when the content was posted or commented.
- `username_encoded` (string): An encoded version of the username to maintain user privacy.
- `url_encoded` (string): An encoded version of any URLs included in the content.

### Data Splits

This dataset is continuously updated and does not have fixed splits. Users should create their own splits based on their requirements and the data's timestamp.

## Dataset Creation

### Source Data

Data is collected from public posts and comments on Reddit, adhering to the platform's terms of service and API usage guidelines.

### Personal and Sensitive Information

All usernames and URLs are encoded to protect user privacy. The dataset does not intentionally include personal or sensitive information.

## Considerations for Using the Data

### Social Impact and Biases

Users should be aware of potential biases inherent in Reddit data, including demographic and content biases. This dataset reflects the content and opinions expressed on Reddit and should not be considered a representative sample of the general population.

### Limitations

- Data quality may vary due to the nature of media sources.
- The dataset may contain noise, spam, or irrelevant content typical of social media platforms.
- Temporal biases may exist due to real-time collection methods.
- The dataset is limited to public subreddits and does not include private or restricted communities.

## Additional Information

### Licensing Information

The dataset is released under the MIT license. The use of this dataset is also subject to Reddit Terms of Use.

### Citation Information

If you use this dataset in your research, please cite it as follows:

```
@misc{veyhoranohy2025datauniversereddit_dataset_248,
        title={The Data Universe Datasets: The finest collection of social media data the web has to offer},
        author={veyhoranohy},
        year={2025},
        url={https://huggingface.co/datasets/veyhoranohy/reddit_dataset_248},
        }
```

### Contributions

To report issues or contribute to the dataset, please contact the miner or use the Bittensor Subnet 13 governance mechanisms.

## Dataset Statistics

[This section is automatically updated]

- **Total Instances:** 56067482
- **Date Range:** 2010-09-29T00:00:00Z to 2025-03-26T00:00:00Z
- **Last Updated:** 2025-04-25T17:27:08Z

### Data Distribution

- Posts: 3.75%
- Comments: 96.25%

### Top 10 Subreddits

For full statistics, please refer to the `stats.json` file in the repository.

| Rank | Topic | Total Count | Percentage |
|------|-------|-------------|-------------|
| 1 | r/politics | 649928 | 1.16% |
| 2 | r/wallstreetbets | 535654 | 0.96% |
| 3 | r/worldnews | 497491 | 0.89% |
| 4 | r/AskReddit | 258937 | 0.46% |
| 5 | r/NoStupidQuestions | 239987 | 0.43% |
| 6 | r/AITAH | 239072 | 0.43% |
| 7 | r/marvelrivals | 229252 | 0.41% |
| 8 | r/teenagers | 224336 | 0.40% |
| 9 | r/AmIOverreacting | 205289 | 0.37% |
| 10 | r/pcmasterrace | 194969 | 0.35% |


## Update History

| Date | New Instances | Total Instances |
|------|---------------|-----------------|
| 2025-02-20T20:10:30Z | 5444082 | 5444082 |
| 2025-02-21T13:33:27Z | 420610 | 5864692 |
| 2025-02-22T08:04:54Z | 477447 | 6342139 |
| 2025-02-23T01:15:55Z | 406101 | 6748240 |
| 2025-02-23T19:18:01Z | 368923 | 7117163 |
| 2025-02-24T13:20:14Z | 365364 | 7482527 |
| 2025-02-25T06:34:31Z | 408274 | 7890801 |
| 2025-02-26T00:36:39Z | 368754 | 8259555 |
| 2025-02-26T17:47:22Z | 148810 | 8408365 |
| 2025-02-27T11:48:26Z | 43324 | 8451689 |
| 2025-02-28T05:49:22Z | 28476 | 8480165 |
| 2025-02-28T23:04:14Z | 637354 | 9117519 |
| 2025-03-01T16:15:22Z | 1070059 | 10187578 |
| 2025-03-02T16:40:59Z | 1691152 | 11878730 |
| 2025-03-03T10:49:18Z | 1694956 | 13573686 |
| 2025-03-03T10:57:38Z | 760 | 13574446 |
| 2025-03-03T11:28:02Z | 2866 | 13577312 |
| 2025-03-04T05:39:00Z | 1693143 | 15270455 |
| 2025-03-05T00:10:45Z | 1569580 | 16840035 |
| 2025-03-05T18:18:44Z | 1450407 | 18290442 |
| 2025-03-06T12:05:34Z | 1560641 | 19851083 |
| 2025-03-07T06:01:48Z | 1422494 | 21273577 |
| 2025-03-08T00:11:01Z | 1446715 | 22720292 |
| 2025-03-08T17:51:20Z | 1260178 | 23980470 |
| 2025-03-09T12:00:07Z | 1477820 | 25458290 |
| 2025-03-10T06:08:31Z | 1613925 | 27072215 |
| 2025-03-11T00:27:56Z | 1502707 | 28574922 |
| 2025-03-11T18:37:08Z | 1411361 | 29986283 |
| 2025-03-12T13:07:21Z | 1496385 | 31482668 |
| 2025-03-13T07:18:16Z | 1713308 | 33195976 |
| 2025-03-14T00:33:44Z | 1672598 | 34868574 |
| 2025-03-14T18:51:37Z | 1100835 | 35969409 |
| 2025-03-15T13:03:24Z | 1423483 | 37392892 |
| 2025-03-16T07:15:27Z | 1484592 | 38877484 |
| 2025-03-17T01:52:05Z | 1196168 | 40073652 |
| 2025-03-17T20:04:20Z | 1158283 | 41231935 |
| 2025-03-18T14:20:28Z | 1320572 | 42552507 |
| 2025-03-19T08:46:57Z | 1577810 | 44130317 |
| 2025-03-20T03:17:19Z | 1321500 | 45451817 |
| 2025-03-20T21:49:41Z | 1204206 | 46656023 |
| 2025-03-21T16:27:48Z | 1328704 | 47984727 |
| 2025-03-22T11:08:55Z | 1541092 | 49525819 |
| 2025-03-23T05:52:17Z | 1412406 | 50938225 |
| 2025-03-24T00:29:46Z | 1149943 | 52088168 |
| 2025-03-24T19:06:12Z | 1175367 | 53263535 |
| 2025-03-25T13:46:14Z | 1522521 | 54786056 |
| 2025-03-26T08:27:03Z | 1281387 | 56067443 |
| 2025-03-27T03:03:26Z | 1 | 56067444 |
| 2025-03-27T21:39:11Z | 1 | 56067445 |
| 2025-03-28T16:15:53Z | 1 | 56067446 |
| 2025-03-29T10:53:23Z | 1 | 56067447 |
| 2025-03-30T05:31:01Z | 1 | 56067448 |
| 2025-03-31T00:08:13Z | 1 | 56067449 |
| 2025-03-31T18:46:07Z | 1 | 56067450 |
| 2025-04-01T13:23:27Z | 1 | 56067451 |
| 2025-04-02T09:52:10Z | 1 | 56067452 |
| 2025-04-03T04:29:18Z | 1 | 56067453 |
| 2025-04-03T23:07:08Z | 1 | 56067454 |
| 2025-04-04T17:44:45Z | 1 | 56067455 |
| 2025-04-05T12:23:10Z | 1 | 56067456 |
| 2025-04-06T07:01:23Z | 1 | 56067457 |
| 2025-04-07T01:39:20Z | 1 | 56067458 |
| 2025-04-07T20:17:40Z | 1 | 56067459 |
| 2025-04-08T14:55:52Z | 1 | 56067460 |
| 2025-04-09T09:34:23Z | 1 | 56067461 |
| 2025-04-10T04:12:51Z | 1 | 56067462 |
| 2025-04-10T22:51:11Z | 1 | 56067463 |
| 2025-04-11T17:29:43Z | 1 | 56067464 |
| 2025-04-12T12:08:26Z | 1 | 56067465 |
| 2025-04-13T06:47:01Z | 1 | 56067466 |
| 2025-04-14T01:25:42Z | 1 | 56067467 |
| 2025-04-14T20:04:39Z | 1 | 56067468 |
| 2025-04-15T14:43:55Z | 1 | 56067469 |
| 2025-04-16T09:23:02Z | 1 | 56067470 |
| 2025-04-17T04:04:42Z | 1 | 56067471 |
| 2025-04-17T22:46:39Z | 1 | 56067472 |
| 2025-04-18T17:26:23Z | 1 | 56067473 |
| 2025-04-19T12:06:29Z | 1 | 56067474 |
| 2025-04-20T06:46:08Z | 1 | 56067475 |
| 2025-04-21T01:26:16Z | 1 | 56067476 |
| 2025-04-21T20:06:03Z | 1 | 56067477 |
| 2025-04-22T14:45:51Z | 1 | 56067478 |
| 2025-04-23T09:25:57Z | 1 | 56067479 |
| 2025-04-24T04:06:04Z | 1 | 56067480 |
| 2025-04-24T22:46:18Z | 1 | 56067481 |
| 2025-04-25T17:27:08Z | 1 | 56067482 |
