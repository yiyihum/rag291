---
license: other
language: en
pretty_name: Bitcoin Price Prediction Instruction Dataset
tags:
- time-series
- instruction-tuning
- finance
- bitcoin
- llm
- prediction
- multimodal
dataset_info:
  features:
  - name: instruction
    dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 51594253
    num_examples: 2312
  download_size: 24504955
  dataset_size: 51594253
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

# Bitcoin Price Prediction Instruction-Tuning Dataset

## Dataset Description

This is a comprehensive, instruction-based dataset formatted specifically for **fine-tuning Large Language Models (LLMs)** to perform financial forecasting. The dataset is structured as a collection of prompt-response pairs, where each record challenges the model to predict the next 10 days of Bitcoin's price based on a rich, multimodal snapshot of daily data.

The dataset covers the period from **early 2018 to mid-2024**, with each of the 2,312 examples representing a single day. The goal is to train models that can synthesize financial, social, and on-chain data to act as specialized cryptocurrency analysts.

## Dataset Structure

The dataset consists of a single split (`train`) and follows a standard instruction-tuning format with three columns: `instruction`, `input`, and `output`.

### Data Fields

-   **`instruction`** (string): This is the main prompt provided to the LLM. It contains a comprehensive, human-readable summary of all available data for a specific day, framed as a request for a financial forecast. It includes:
    -   A directive defining the role of an "expert financial analyst".
    -   The complete historical closing prices of Bitcoin for the **past 60 days**.
    -   Daily news and social media text from Twitter, Reddit, and news sites.
    -   Macroeconomic indicators like the daily closing prices of Gold and Oil.
    -   Fundamental Bitcoin on-chain metrics (hash rate, difficulty, transaction volume, active addresses, etc.).
    -   Social sentiment indicators like the Fear & Greed Index.
    -   AI-generated sentiment and trading action classifications from another LLM.

-   **`input`** (string): This field is **intentionally left empty** (`""`) for all records. This structures the task as a "zero-shot" instruction problem, where all necessary information is contained within the `instruction` prompt itself.

-   **`output`** (string): This is the target response for the LLM to learn. It contains a string representation of a list of the **next 10 days** of Bitcoin's closing prices.

### How the Data was Created

This instruction dataset was derived from a daily time-series dataset built by aggregating multiple sources:
-   **Prices & Commodities:** Real-time financial data for BTC-USD, Gold (GC=F), and Crude Oil (CL=F) was sourced from **Yahoo Finance** via the `yfinance` library.
-   **On-Chain, Social, & LLM Metrics:** A wide range of features, including on-chain data, sentiment indices, and additional text sources, were sourced from the **`danilocorsi/LLMs-Sentiment-Augmented-Bitcoin-Dataset`**.
-   **Primary News Source:** Daily news articles were sourced from the **`edaschau/bitcoin_news`** dataset.
-   **Primary Tweet Source:** Daily tweets were sourced from a user-provided `mbsa.csv` file originating from a larger Kaggle dataset.

Each row from the time-series data was programmatically serialized into the detailed `instruction` and `output` format described above.

## Use Cases

The primary use case for this dataset is to **fine-tune instruction-following Large Language Models** (e.g., Llama, Mistral, Gemini, Gemma) to specialize in financial forecasting. By training on this data, a model can learn to:
-   Ingest and reason about complex, multimodal data (text, time-series, numerical).
-   Identify patterns between news sentiment, on-chain activity, and price movements.
-   Generate structured, numerical forecasts in a specific format.

This dataset can also be used for research in prompt engineering and for evaluating the quantitative reasoning abilities of LLMs in the financial domain.