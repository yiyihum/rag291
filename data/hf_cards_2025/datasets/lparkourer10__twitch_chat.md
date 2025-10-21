---
license: cc-by-sa-4.0
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
dataset_info:
  features:
  - name: Message
    dtype: string
  splits:
  - name: train
    num_bytes: 171194856
    num_examples: 8923544
  - name: validation
    num_bytes: 943300
    num_examples: 61113
  download_size: 98397571
  dataset_size: 172138156
task_categories:
- text-classification
- text-generation
language:
- en
tags:
- twitch
- y2k
- chat
- genz
pretty_name: twitch
size_categories:
- 1M<n<10M
---

#  Twitch Chat Dataset
![Twitch logo](twitch.png)


This dataset is a large-scale collection of Twitch chat logs aggregated from multiple streamers across various categories. It is designed to support the research and development of models for real-time, informal, and community-driven conversation, such as:

- Chatbots tailored for livestream platforms  
- Simulating the behavior of Twitch chat  
- Modeling how chat reacts during hype moments, events, or memes  

The code for it can be found [here](https://gist.github.com/Parkourer10/1a563c7359e786b40f8bf600d8d04573)

---

## 📂 Dataset Structure

- All files are combined into the **`train`** split, except the last one, which is used as the **`validation`** split.
- The `message` column contains raw Twitch chat messages.

---

## 💡 Use Cases

- Fine-tuning language models (e.g., LLaMA, Mistral, GPT) on informal, emoji-heavy, meme-rich dialogue.
- Building generative agents or NPCs that mimic Twitch chat behavior.
- Training moderation, toxicity, or sentiment classifiers for real-world fast-paced chat.
- Analyzing the dynamics of online communities, virality, and meme propagation.

---

## 🔒 Ethics

- **Usernames are removed** to protect individual privacy.
- **No private messages, subscriptions, or off-platform data** are included.  
  If you find any such data, please open a discussion so it can be removed.
- Always review and comply with [Twitch's Terms of Service](https://www.twitch.tv/p/en/legal/terms-of-service/) when using, modifying, or deploying models trained on this dataset.

---

## 📜 License

This dataset is licensed under **[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)**.  
You may use it for research or commercial purposes, provided that you give appropriate credit and share any derivative works under the same license.

---

## 🙏 Acknowledgements

Special thanks to the Twitch community and to the streamers whose public broadcasts and chat logs made this dataset possible.

---

## 🔗 Citation

If you use this dataset in your research or applications, please cite it as:

```bibtex
@misc{twitchchat2025,
  title = {Twitch Chat},
  author = {parkourer10},
  year = {2025},
  publisher = {Hugging Face Datasets},
  url = {https://huggingface.co/datasets/lparkourer10/twitch_chat}
}