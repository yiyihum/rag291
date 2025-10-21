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

- **Repository:** James096/reddit_dataset_127
- **Subnet:** Bittensor Subnet 13
- **Miner Hotkey:** 5D2KKAGcf1bHnT71v5jsw9TJBmQto5PhYKRSPcJDhk8gqSXj

### Miner Data Compliance Agreement 

In uploading this dataset, I am agreeing to the [Macrocosmos Miner Data Compliance Policy](https://github.com/macrocosm-os/data-universe/blob/add-miner-policy/docs/miner_policy.md). 

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
@misc{James0962025datauniversereddit_dataset_127,
        title={The Data Universe Datasets: The finest collection of social media data the web has to offer},
        author={James096},
        year={2025},
        url={https://huggingface.co/datasets/James096/reddit_dataset_127},
        }
```

### Contributions

To report issues or contribute to the dataset, please contact the miner or use the Bittensor Subnet 13 governance mechanisms.

## Dataset Statistics

[This section is automatically updated]

- **Total Instances:** 10915360
- **Date Range:** 2012-06-21T00:00:00Z to 2025-06-03T00:00:00Z
- **Last Updated:** 2025-06-03T16:18:20Z

### Data Distribution

- Posts: 3.45%
- Comments: 96.55%

### Top 10 Subreddits

For full statistics, please refer to the `stats.json` file in the repository.

| Rank | Topic | Total Count | Percentage |
|------|-------|-------------|-------------|
| 1 | r/AskReddit | 152709 | 1.40% |
| 2 | r/politics | 136506 | 1.25% |
| 3 | r/AITAH | 132615 | 1.21% |
| 4 | r/mildlyinfuriating | 92530 | 0.85% |
| 5 | r/AmItheAsshole | 90197 | 0.83% |
| 6 | r/AmIOverreacting | 84806 | 0.78% |
| 7 | r/NoStupidQuestions | 84652 | 0.78% |
| 8 | r/nba | 84276 | 0.77% |
| 9 | r/wallstreetbets | 77760 | 0.71% |
| 10 | r/teenagers | 74272 | 0.68% |


## Update History

| Date | New Instances | Total Instances |
|------|---------------|-----------------|
| 2025-05-08T22:57:09Z | 36948 | 36948 |
| 2025-05-10T03:39:39Z | 34434 | 71382 |
| 2025-05-10T21:17:24Z | 86590 | 157972 |
| 2025-05-11T17:07:08Z | 547082 | 705054 |
| 2025-05-12T11:25:53Z | 667301 | 1372355 |
| 2025-05-13T05:28:33Z | 826594 | 2198949 |
| 2025-05-14T10:10:22Z | 8411 | 2207360 |
| 2025-05-14T13:32:14Z | 20223 | 2227583 |
| 2025-05-14T18:53:53Z | 19763 | 2247346 |
| 2025-05-15T10:45:33Z | 36654 | 2284000 |
| 2025-05-15T13:16:12Z | 62706 | 2346706 |
| 2025-05-15T15:00:31Z | 56121 | 2402827 |
| 2025-05-15T16:30:17Z | 51510 | 2454337 |
| 2025-05-15T20:29:03Z | 3551 | 2457888 |
| 2025-05-15T22:38:15Z | 82539 | 2540427 |
| 2025-05-16T15:58:54Z | 1307817 | 3848244 |
| 2025-05-17T10:01:57Z | 1305467 | 5153711 |
| 2025-05-18T03:29:24Z | 442993 | 5596704 |
| 2025-05-18T21:29:51Z | 536473 | 6133177 |
| 2025-05-19T15:32:29Z | 881295 | 7014472 |
| 2025-05-20T09:35:04Z | 970121 | 7984593 |
| 2025-05-21T03:03:49Z | 772190 | 8756783 |
| 2025-05-21T21:32:01Z | 382597 | 9139380 |
| 2025-05-22T15:17:01Z | 760318 | 9899698 |
| 2025-06-01T13:29:42Z | 291158 | 10190856 |
| 2025-06-02T12:26:27Z | 28205 | 10219061 |
| 2025-06-02T22:08:58Z | 31304 | 10250365 |
| 2025-06-03T16:18:20Z | 664995 | 10915360 |
