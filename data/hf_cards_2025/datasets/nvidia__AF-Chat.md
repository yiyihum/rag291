---
language:
- en
license: other
size_categories:
- 10K<n<100K
task_categories:
- audio-text-to-text
tags:
- synthetic
- audio-llm
- audio-question-answering
- reasoning
- chat
- speech
- sound
- music
library_name: datasets
configs:
- config_name: default
  data_files:
  - split: sound
    path: afchat/sound.json
  - split: msd
    path: afchat/MSD.json
---

# AF-Chat Dataset

[Project page](https://research.nvidia.com/labs/adlr/AF3/) | [Paper](https://huggingface.co/papers/2507.08128) | [Code](https://github.com/NVIDIA/audio-flamingo/tree/audio_flamingo_3)

## Dataset Description

**AF-Chat** is a high-quality fine-tuning dataset of **~75K** multi-turn, multi-audio conversations (avg. 4.6 clips & 6.2 turns; range 2–8 clips & 2–10 turns) spanning speech, environmental sounds, and music. The dataset is partitioned into subsets based on each audio’s source dataset:

1. **Sound (`sound.json`)**
   - Domain: Sound and Speech
   - Additional Note: Audios are primarily sourced from YouTube8m and AudioSet, both which can be downloaded from https://github.com/JishengBai/AudioSetCaps. If any audio is not found, please contact corresponding authors.

2. **Music4ALL (`Music4ALL.json`)**
    - Domain: Music
    - Link to original dataset: https://github.com/amaai-lab/Music4All
    - Additional Note: Please email the corresponding authors with approved license for access to this JSON.

3. **Million Song Dataset (`MSD.json`)**
    - Domain: Music
    - Link to original dataset: http://millionsongdataset.com/.

By releasing AF-Chat, researchers can train models for multi-turn, multi-audio chat. **Please note: we only provide the text QA annotations—not the audio files themselves. You must download each clip from its original source (e.g., YouTube-8M, AudioSet, Music4All) using the file name in the `"sound"` field of the JSON. In conversations, a tag like `<sound-i>` refers to the *i*-th item in that list. We recognize this lookup can be cumbersome; if you run into issues, please open an issue or contact the corresponding authors for assistance.**

## Dataset Owner(s)
NVIDIA Corporation

## Dataset Creation Date
2025/07/10

## License / Terms of Use
The use of AF-Chat is governed by the [NVIDIA OneWay Noncommercial License](licenses/NVIDIA%20OneWay%20Noncommercial%20License.docx).
Synthetic data generation may be subject to OpenAI’s [Terms of Use](https://openai.com/policies/terms-of-use) and [Qwen Research License](https://huggingface.co/Qwen/Qwen2.5-7B/blob/main/LICENSE). Additionally, audios may be governed by its own dataset license, which users should review before downloading or using the audio content.

## Intended Usage
AF-Chat is intended to support:
- Training and fine-tuning (large) audio-language models for multi-turn, multi-audio chat/dialogue.

## Dataset Characterization
The dataset has no special characterization. Each example is a pair of a long clip and a corresponding QA item. Audio encompasses environmental sounds, speech (primarily English), and music. Audios are sourced from open-source datasets (see Table 8 in paper). Text QA is generated using a variety of methods mentioned in the paper. Metadata from the original datasets (if available) is used to for QA generation.

## Data Curation Method
- Audio is drawn from open-source datasets.
- Metadata (captions, transcripts, tags) is gathered from each source. Additional meta-data, if required, is generated.
- For each seed audio, we retrieve its top 8 semantically similar and 8 dissimilar clips using NV-Embed-v2 embeddings and FAISS clustering.
- An LLM is prompted with expert exemplars and clustering constraints to produce natural multi-turn, multi-audio dialogues.
- Human-in-the-loop refinement: clustering parameters, prompts, and data sources are iteratively tuned based on model outputs and qualitative feedback.

## Data Collection Method
Hybrid: Human, Synthetic and Automated

## Labeling Method
Synthetic

## Dataset Format
- **Modality**: Audio (WAV/MP3/FLAC) + Text (JSON)
- **JSON Schema Example**:
```json
[
  {
    "id": "Arbitary ID",
    "sound": "List of wav files.",
    "conversations": [
      {
        "from": "human",
        "value": "<sound-i>
The Question."
      },
      {
        "from": "gpt",
        "value": "The Answer."
      }
    ]
  },
]
```

## Reference(s):
- Audio Flamingo 3
```
@misc{goel2025audioflamingo3advancing,
      title={Audio Flamingo 3: Advancing Audio Intelligence with Fully Open Large Audio Language Models},
      author={Arushi Goel and Sreyan Ghosh and Jaehyeon Kim and Sonal Kumar and Zhifeng Kong and Sang-gil Lee and Chao-Han Huck Yang and Ramani Duraiswami and Dinesh Manocha and Rafael Valle and Catanzaro, Bryan},
      year={2025},
      eprint={2507.08128},
      archivePrefix={arXiv},
      primaryClass={cs.SD},
      url={https://arxiv.org/abs/2507.08128},
}
```
- Audio Flamingo
```
@inproceedings{kong2024audio,
  title={Audio Flamingo: A Novel Audio Language Model with Few-Shot Learning and Dialogue Abilities},
  author={Kong, Zhifeng and Goel, Arushi and Badlani, Rohan and Ping, Wei and Valle, Rafael and Catanzaro, Bryan},
  booktitle={International Conference on Machine Learning},
  pages={25125--25148},
  year={2024},
  organization={PMLR}
}
```
- Audio Flamingo 2
```
@article{ghosh2025audio,
  title={Audio Flamingo 2: An Audio-Language Model with Long-Audio Understanding and Expert Reasoning Abilities},
  author={Ghosh, Sreyan and Kong, Zhifeng and Kumar, Sonal and Sakshi, S and Kim, Jaehyeon and Ping, Wei and Valle, Rafael and Manocha, Dinesh and Catanzaro, Bryan},
  journal={arXiv preprint arXiv:2503.03983},
  year={2025}
}
```

## Ethical Considerations:
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.

Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).