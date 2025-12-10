---
license: mit
task_categories:
- question-answering
- text-generation
language:
- ja
tags:
- japanese
- question-answering
- sft
- instruction-tuning
size_categories:
- 10K<n<100K
---

# softjapan/jaquad-sft

## データセットの概要

このデータセットは、JaQuAD（Japanese Question Answering Dataset）をSFT（Supervised Fine-Tuning）形式に変換したものです。日本語の質問応答タスクに特化したinstruction tuning用のデータセットです。

## データセットの詳細

- **言語**: 日本語
- **タスク**: 質問応答、instruction tuning
- **形式**: SFT（instruction/input/output）
- **訓練データ**: 31,748件
- **検証データ**: 3,939件
- **合計**: 35,687件

## データ形式

各サンプルは以下の形式で構成されています：

```json
{
  "id": "tr-000-00-000",
  "instruction": "次の文脈に基づいて質問に答えてください。可能なら短く正確に答えてください。",
  "input": "【文脈】手塚治虫(てづかおさむ、本名:手塚治(読み同じ)、1928年(昭和3年)11月3日-1989年(平成元年)2月9日)は、日本の漫画家、アニメーター、アニメ監督である。\n戦後日本においてストーリー漫画の第一人者として、漫画表現の開拓者的な存在として活躍した。\n\n兵庫県宝塚市出身(出生は大阪府豊能郡豊中町、現在の豊中市)同市名誉市民である。\n大阪帝国大学附属医学専門部を卒業。\n医師免許取得のち医学博士(奈良県立医科大学・1961年)。\n\n【質問】戦後日本のストーリー漫画の第一人者で、医学博士の一面もある漫画家は誰?",
  "output": "手塚治虫"
}
```

## 使用方法

### データセットの読み込み

```python
from datasets import load_dataset

# データセットを読み込み
dataset = load_dataset("softjapan/jaquad-sft")

# 訓練データの例を表示
print(dataset["train"][0])
```

### LoRAファインチューニングでの使用

```python
import os
import math
import random
import inspect

import transformers
from datasets import load_dataset
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    DataCollatorForLanguageModeling,
    Trainer,
)
# 衝突回避: HF の TrainingArguments を明示別名
from transformers import TrainingArguments as HFTrainingArguments
from peft import LoraConfig, get_peft_model, TaskType

# -------- 0) 再現性（任意） --------
SEED = int(os.environ.get("SEED", 42))
random.seed(SEED)
os.environ["PYTHONHASHSEED"] = str(SEED)

# -------- 1) データ読み込み --------
dataset = load_dataset("softjapan/jaquad-sft")  # train / validation あり

# remove_columns 用に元カラム名を控える
if "train" in dataset:
    original_columns = dataset["train"].column_names
else:
    first_split = list(dataset.keys())[0]
    original_columns = dataset[first_split].column_names

# -------- 2) トークナイザー & モデル --------
model_name = "Qwen/Qwen2-1.5B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = "right"

# torch_dtype は非推奨 → dtype へ
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    dtype="auto",
    device_map="auto",
)

# -------- 3) LoRA 設定 --------
lora_config = LoraConfig(
    r=8,
    lora_alpha=16,
    lora_dropout=0.05,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],
    task_type=TaskType.CAUSAL_LM,
    bias="none",
)
model = get_peft_model(model, lora_config)

# -------- 4) 前処理（batched=False） --------
def format_row(ex):
    inst = (ex.get("instruction") or "").strip()
    inp  = (ex.get("input") or "").strip()
    out  = (ex.get("output") or "").strip()
    return f"### 指示\n{inst}\n\n### 入力\n{inp}\n\n### 応答\n{out}"

def tokenize(example):
    text = format_row(example)
    return tokenizer(
        text,
        truncation=True,
        max_length=1024,
        padding="max_length",
    )

tokenized = {}
for split in dataset.keys():
    tokenized[split] = dataset[split].map(
        tokenize,
        batched=False,
        remove_columns=original_columns,
        desc=f"Tokenizing {split}",
    )

train_ds = tokenized.get("train")
eval_ds  = tokenized.get("validation")

# validation が無い（将来の互換）場合のフォールバック
if train_ds is None:
    only_name = list(tokenized.keys())[0]
    only_ds = tokenized[only_name]
    n = len(only_ds)
    cut = max(1, int(n * 0.02))
    eval_ds = only_ds.select(range(cut))
    train_ds = only_ds.select(range(cut, n))

# -------- 5) Collator（Pad を -100 に）--------
collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

# -------- 6) TrainingArguments（衝突耐性） --------
print("Transformers version:", transformers.__version__)

common_args = dict(
    output_dir="./qwen2-jaquad-lora",
    num_train_epochs=3,
    per_device_train_batch_size=2,
    per_device_eval_batch_size=2,
    gradient_accumulation_steps=8,
    learning_rate=2e-4,
    lr_scheduler_type="cosine",
    warmup_ratio=0.03,
    weight_decay=0.0,
    logging_steps=50,
    save_steps=500,
    save_total_limit=2,
    report_to="none",
    bf16=True,                   # 対応GPUなら True
    gradient_checkpointing=False, # VRAM節約
)

# 実際に使われるクラスのシグネチャを確認（名前衝突や古い版でも動くように）
sig = inspect.signature(HFTrainingArguments.__init__).parameters
if "evaluation_strategy" in sig:
    training_args = HFTrainingArguments(
        **common_args,
        evaluation_strategy="steps",
        eval_steps=500,
    )
else:
    # 古い版互換（基本的に今は通らない想定だが保険）
    training_args = HFTrainingArguments(
        **common_args,
        do_eval=True,
    )

# -------- 7) Trainer --------
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_ds,
    eval_dataset=eval_ds,
    data_collator=collator,
)

# -------- 8) 学習 & 評価 & 保存 --------
trainer.train()
metrics = trainer.evaluate()
eval_loss = metrics.get("eval_loss", None)
if eval_loss is not None:
    try:
        ppl = math.exp(eval_loss)
        print(f"Eval loss: {eval_loss:.4f} | PPL: {ppl:.2f}")
    except OverflowError:
        print(f"Eval loss: {eval_loss:.4f} | PPL: overflow")

save_dir = "./qwen2-jaquad-lora-adapter"
trainer.model.save_pretrained(save_dir)
tokenizer.save_pretrained(save_dir)
print(f"Saved LoRA adapter to: {save_dir}")
```

## ライセンス

このデータセットはMITライセンスの下で公開されています。

## 引用

```bibtex
@dataset{softjapan/jaquad-sft,
  title={softjapan/jaquad-sft: Japanese Question Answering Dataset for SFT},
  author={Your Name},
  year={2024},
  url={https://huggingface.co/datasets/softjapan/jaquad-sft}
}
```

## 関連リンク

- [元データセット: SkelterLabsInc/jaquad](https://huggingface.co/datasets/SkelterLabsInc/jaquad)
- [変換スクリプト](https://github.com/softjapan/jaquad-to-sft)
