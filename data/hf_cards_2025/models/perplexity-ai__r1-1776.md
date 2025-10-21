---
license: mit
base_model:
- deepseek-ai/DeepSeek-R1
library_name: transformers
---

# R1 1776

Blog link: [https://perplexity.ai/hub/blog/open-sourcing-r1-1776](https://perplexity.ai/hub/blog/open-sourcing-r1-1776 ) 

R1 1776 is a DeepSeek-R1 reasoning model that has been post-trained by Perplexity AI to remove Chinese Communist Party censorship. 
The model provides unbiased, accurate, and factual information while maintaining high reasoning capabilities.

## Evals

To ensure our model remains fully “uncensored” and capable of engaging with a broad spectrum of sensitive topics, we curated a diverse, multilingual evaluation set of over a 1000 of examples that comprehensively cover such subjects. We then use human annotators as well as carefully designed LLM judges to measure the likelihood a model will evade or provide overly sanitized responses to the queries.
![image/png](https://cdn-uploads.huggingface.co/production/uploads/675c8332d01f593dc90817f5/GiN2VqC5hawUgAGJ6oHla.png)

We also ensured that the model’s math and reasoning abilities remained intact after the decensoring process. Evaluations on multiple benchmarks showed that our post-trained model performed on par with the base R1 model, indicating that the decensoring had no impact on its core reasoning capabilities.
![image/png](https://cdn-uploads.huggingface.co/production/uploads/675c8332d01f593dc90817f5/n4Z9Byqp2S7sKUvCvI40R.png)