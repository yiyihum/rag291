---
annotations_creators:
- rule-based
language_creators:
- llm-generated
language:
- ko
license: mit
multilinguality:
- monolingual
pretty_name: A Korean Toxic Dataset for Deobfuscation and Detoxification
size_categories:
- 10K<n<100K
source_datasets:
- 'K/DA: Automated Data Generation Pipeline for Detoxifying Implicitly Offensive Language
  in Korean (ACL 2025)'
task_categories:
- text-classification
- text-generation
task_ids:
- hate-speech-detection
---
# KOTOX
### : A Korean Toxic Dataset for Deobfuscation and Detoxification

**Hate Speech Detection dataset** 👉 [KOTOX-classification](https://huggingface.co/datasets/ssgyejin/KOTOX-classification)  
**Detoxification or Sanitization dataset** 👉 Here!

[📚 paper](https://arxiv.org/abs/2510.10961) | 
[🐈‍⬛ git](https://github.com/leeyejin1231/KOTOX)

## 📝 Dataset Summary
**KOTOX** is the first Korean dataset designed for both **toxic text detoxification and obfuscation** robustness.   

It provides paired **neutral-toxic sentences** and their **obfuscated counterparts**, constructed with **17 linguistically grounded transformation rules** reflecting the characteristics of Korean and Hangeul.

The dataset enables **three complementary tasks**:
1. 🧠 **Obfuscated Toxic Text Classification**
- Classify whether an obfuscated sentence is toxic or neutral.
2. 🔤 **Neutral Text Deobfuscation**
- Restore an obfuscated neutral sentence to its original, clean form.
3. 🧼 **Obfuscated Toxic Text Sanitization**
- Rewrite obfuscated toxic text into a deobfuscated, neutral sentence while preserving meaning.

|Dataset|train|valid|test|sum|
|-------|-----|-----|----|---|
|**easy**|1,835|229|230|2,294
|**normal**|1,835|229|230|2,294
|**hard**|1,835|229|230|2,294
|**total**|5,505|687|690|6,882

## 🏗️ Structure
```
TOKOX  
 ├── data  
 │    ├── easy  
 │    │    ├── train.csv  
 │    │    ├── valid.csv    
 │    │    └── test.csv  
 │    ├── normal  
 │    │    ├── train.csv  
 │    │    ├── valid.csv    
 │    │    └── test.csv  
 │    ├── hard    
 │    │    ├── train.csv    
 │    │    ├── valid.csv  
 │    │    └── test.csv    
 │    └── total  
 │         ├── train.csv  
 │         ├── valid.csv    
 │         └── test.csv   
 └── README.md  
```
Each CSV file contains:  
- `neutral`: non-toxic sentence  
- `toxic`: corresponding toxic version  
- `neutral_obf`: obfuscated neutral text  
- `toxic_obf`: obfuscated toxic text  
- `rules`: list of applied transformation rules  

## 🧩 Obfuscation Rules
KOTOX defines 17 transformation rules across 5 linguistic approaches, based on Korean linguistic properties.

| Approach | Transformation rule |  Example  |  
|--|---|---|  
| **Phonological** | 1-1. Initial consonant repacement | 한국인 → 한꾹인 |
|  | 1-3. Medial vowel replacement| 해수욕장 → 헤수욕장 |
|  | 1-4. Final consonant replacement | 한국인 → 핝굮읹 |
|  | 1-5. Ortographic reyllabification | 한국인 → 한구긴 |
|  | 2-1. Medial vowel insertion | 한국인 → 환궉윈 |
|  | 2-2. Final consonant insertion | 바깥 → 박깥 |
|  | 2-3. Initial consonant insertion | 한국인 → 한국긴 |
|  | 3-1. Liaison | 할 짓이가 → 할찌시가 |
| **Iconological** | 5-1. Hangeul look-alike | 귀엽다 → 커엽다 |
|  | 5-2. Cross-script substitution | 쭈꾸미 → 卒꾸口I |
|  | 6-1. Rotation-based variation | 논문 → 곰국 |
| **Transliteration** | 8-1. Phonetic substitution (Latin) | 망했어 → mang했어 |
|  | 8-2. Phonetic substitution (CJK) | 수상해 → 水상해 |
|  | 8-3. Semantic substitution | 가지마세요 → 돈트고쿠다사이 |
| **Syntactic** | 10. Spacing perturbation | 화장실 더럽고 별로 → 화장 실더럽 고별로 |
|  | 11. Syllable anagram | 오랜만에 외국여행을 → 오만랜에 외여국행을 |
| **Pragmatic** | 13-2. Symbol/emoji insertion | 돈을 쓰는 호갱 → 돈을°♡ 쓰는《호..갱》≥ㅅ≤ |

Each difficulty level applies an increasing number of transformation rules:  
- `Easy`: 2 rules  
- `Normal`: 3 rules  
- `Hard`: 4 rules  


## 🚀 Usage

```python
from datasets import load_dataset

totox_easy = load_dataset("ssgyejin/kotox", data_dir="easy")
totox_normal = load_dataset("ssgyejin/kotox", data_dir="normal")
totox_hard = load_dataset("ssgyejin/kotox", data_dir="hard")
totox_total = load_dataset("ssgyejin/kotox", data_dir="total")
```

## ⚖️ Ethical Considerations

This dataset contains **toxic and offensive language** for research purposes only.
All data were filtered to remove personal identifiers and should be used **solely for developing safer, more robust NLP models.** We **strongly discourage** any misuse for generating or spreading harmful content.

## 📖 Citation
If you use this dataset, please cite:
```
@misc{lee2025kotoxkoreantoxicdataset,
      title={KOTOX: A Korean Toxic Dataset for Deobfuscation and Detoxification}, 
      author={Yejin Lee and Su-Hyeon Kim and Hyundong Jin and Dayoung Kim and Yeonsoo Kim and Yo-Sub Han},
      year={2025},
      eprint={2510.10961},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2510.10961}, 
}
```