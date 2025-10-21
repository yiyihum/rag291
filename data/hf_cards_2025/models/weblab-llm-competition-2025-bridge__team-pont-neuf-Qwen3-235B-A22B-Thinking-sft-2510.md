---
base_model: Qwen/Qwen3-235B-A22B-Thinking-2507
datasets:
- weblab-llm-competition-2025-bridge/team-pont-neuf-sft-dataset-2510
pipeline_tag: text-generation
library_name: transformers
tags:
- vllm
---

# team-pont-neuf-Qwen3-235B-A22B-Thinking-sft-2510

We developed this model to outperform current open-weight models on [Humanity's Last Exam](https://huggingface.co/datasets/cais/hle), a super-challenging benchmark used in the [LLM Competition 2025 Bridge](https://weblab.t.u-tokyo.ac.jp/lm-compe-2025).

## Performance

|  | Ours | Qwen3-235B-A22B-Thinking-2507 | [Ours(previous)](https://huggingface.co/weblab-llm-competition-2025-bridge/team-pont-neuf-Qwen3-235B-A22B-Thinking-sft) |
|--- | --- | --- | --- |
| **Humanity's Last Exam** | | |
| Overall Accuracy (%) | **18.72** | 18.07 | 17.61 |
| Math | 26.13 | **26.54** | 24.90 |
| Physics | **12.87** | 10.89 | 10.40 |
| Biology/Medicine | **17.57** | **17.57** | 14.41 |
| Humanities/Social Science | **12.44** | 9.84 | 12.44 |
| Computer Science/AI | **13.39** | 11.16 | 12.22 |
| Engineering | **15.63** | **15.63** | 12.50 |
| Chemistry | **12.87** | 6.93 | 10.89 |
| Others | 3.98 | 5.11 | **8.05** |
| Calibration Error | 74.0 | 74.0 | **75.0** |
| **[Do-Not-Answer](https://huggingface.co/datasets/LibrAI/do-not-answer) (10 fold)** | | |
| Safety rate　(%) | **97.87** | 95.74 | 95.74 |

To ensure fair evaluation, we used the same values for `max_model_len` and `max_completion_tokens` across all models.
For HLE, we set `max_model_len` = 262,144 and `max_completion_tokens` = 248,741.
For DNA, `max_model_len` is the same and `max_new_tokens` = 512.
Additionally, we report the HLE score as judged by OpenAI o4-mini-2025-04-16.

## ベースモデル

[Qwen/Qwen3-235B-A22B-Thinking-2507](https://huggingface.co/Qwen/Qwen3-235B-A22B-Thinking-2507)

アーキテクチャの変更は特にありません。

## トレーニングデータ

[weblab-llm-competition-2025-bridge/team-pont-neuf-sft-dataset-2510](https://huggingface.co/datasets/weblab-llm-competition-2025-bridge/team-pont-neuf-sft-dataset-2510)


## 学習方法

詳細については記事として公開を予定しています。

## 環境構築

```
conda install -c conda-forge --file requirements.txt
pip install \
  --index-url https://download.pytorch.org/whl/cu126 \
  --extra-index-url https://pypi.org/simple \
  torch==2.7.1+cu126 torchvision==0.22.1+cu126 torchaudio==2.7.1+cu126 \
  vllm>=v0.10.1.1
(llmbench) $ pip list | grep vllm
vllm                              0.10.1.1
```

## HLE推論・評価

動作確認済みのコマンドは、以下の通りです。
vllmのmax-model-lenパラメタは`262144`を、predict.pyのmax_completion_tokensパラメタは`248741`をかならず指定してください。
なお、`predict.py`の実行完了までにかかる時間は25時間です(実績値):

```sh
#!/bin/bash
#SBATCH --job-name=predict_full_hle_8gpu
#SBATCH --partition=P06
#SBATCH --nodelist=osk-gpu68
#SBATCH --nodes=1
#SBATCH --gpus-per-node=8
#SBATCH --cpus-per-task=64
#SBATCH --output=eval_hle/logs/%x-%j.out
#SBATCH --error=eval_hle/logs/%x-%j.err

#--- 作業ディレクトリ & logs --------------------------------------------
export EVAL_DIR="eval_hle"
mkdir -p "$EVAL_DIR/logs"
echo "log dir : $EVAL_DIR/logs"

#--- モジュール & Conda --------------------------------------------
module purge
module load cuda/12.6 miniconda/24.7.1-py312
module load cudnn/9.6.0
module load nccl/2.24.3
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate llmbench

# 自分のトークンに置き換えてください
HF_TOKEN=hf_yourtoken
WANDB_API_KEY=yourkey
OPENAI_API_KEY=sk-YOURKEY

export HF_HOME=${SLURM_TMPDIR:-$HOME}/.hf_cache
export HF_TOKEN=$HF_TOKEN
export WANDB_API_KEY=$WANDB_API_KEY
export HUGGINGFACE_HUB_TOKEN=$HF_TOKEN
mkdir -p "$HF_HOME"
echo "HF cache dir : $HF_HOME"

export PYTHONUNBUFFERED=1
export VLLM_LOGGING_LEVEL=DEBUG

#--- vLLM 起動（8GPU）----------------------------------------------
vllm serve weblab-llm-competition-2025-bridge/team-pont-neuf-Qwen3-235B-A22B-Thinking-sft-2510 \
  --tensor-parallel-size 8 \
  --pipeline-parallel-size 1 \
  --max-model-len 262144 \
  --max-num-seqs 32 \
  --gpu-memory-utilization 0.95 \
  --reasoning-parser deepseek_r1 \
  --dtype "bfloat16" \
  > $EVAL_DIR/logs/vllm-$SLURM_JOB_ID.log 2>&1 &
pid_vllm=$!

#--- ヘルスチェック -------------------------------------------------
until curl -s http://127.0.0.1:8000/health >/dev/null; do
  echo "$(date +%T) vLLM starting …"
  sleep 10
done
echo "vLLM READY"

#--- 推論 -----------------------------------------------------------
cd $EVAL_DIR
python predict.py \
  model=weblab-llm-competition-2025-bridge/team-pont-neuf-Qwen3-235B-A22B-Thinking-sft-2510 \
  dataset=cais/hle \
  max_completion_tokens=248741 2>&1
cd ..

#--- 評価 -----------------------------------------------------------
export BASE_URL="http://localhost:8000/v1" 
cd $EVAL_DIR
python judge.py \
  model=weblab-llm-competition-2025-bridge/team-pont-neuf-Qwen3-235B-A22B-Thinking-sft-2510 \
  dataset=cais/hle \
  max_completion_tokens=248741 2>&1
cd ../

#--- 後片付け -------------------------------------------------------
kill $pid_vllm 2>/dev/null
wait $pid_vllm 2>/dev/null

wait
```

## DNA推論・評価

動作確認済みのコマンドは、以下の通りです。
vllmのmax-model-lenパラメタは`262144`をかならず指定してください:

```sh
#!/bin/bash
#SBATCH --job-name=predict_dna_8gpu
#SBATCH --partition=P06
#SBATCH --nodelist=osk-gpu68
#SBATCH --nodes=1
#SBATCH --gpus-per-node=8
#SBATCH --cpus-per-task=64
#SBATCH --output=eval_dna/logs/%x-%j.out
#SBATCH --error=eval_dna/logs/%x-%j.err

#--- 作業ディレクトリ & logs --------------------------------------------
export EVAL_DIR="eval_dna"
mkdir -p "$EVAL_DIR/logs"
echo "log dir : $EVAL_DIR/logs"

#--- モジュール & Conda --------------------------------------------
module purge
module load cuda/12.6 miniconda/24.7.1-py312
module load cudnn/9.6.0  
module load nccl/2.24.3 
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate llmbench

# 自分のトークンに置き換えてください
HF_TOKEN=hf_yourtoken
WANDB_API_KEY=yourkey
OPENAI_API_KEY=sk-YOURKEY

export HF_HOME=${SLURM_TMPDIR:-$HOME}/.hf_cache
export HUGGINGFACE_HUB_TOKEN=$HF_TOKEN
mkdir -p "$HF_HOME"
echo "HF cache dir : $HF_HOME"

#--- vLLM 起動（8GPU）----------------------------------------------
vllm serve weblab-llm-competition-2025-bridge/team-pont-neuf-Qwen3-235B-A22B-Thinking-sft-2510 \
  --tensor-parallel-size 8 \
  --pipeline-parallel-size 1 \
  --max-model-len 262144 \
  --max-num-seqs 32 \
  --gpu-memory-utilization 0.95 \
  --reasoning-parser deepseek_r1 \
  --dtype "bfloat16" \
  > $EVAL_DIR/logs/vllm.log 2>&1 &
pid_vllm=$!

#--- ヘルスチェック -------------------------------------------------
until curl -s http://127.0.0.1:8000/health >/dev/null; do
  echo "$(date +%T) vLLM starting …"
  sleep 10
done
echo "vLLM READY"

#--- 推論 -----------------------------------------------------------
python $EVAL_DIR/llm-compe-eval/evaluate_huggingface_models.py \
    --model_name "weblab-llm-competition-2025-bridge/team-pont-neuf-Qwen3-235B-A22B-Thinking-sft" \
    --dataset_path datasets/Instruction/do_not_answer_en.csv \
    --output_dir $EVAL_DIR/evaluation_results \
    --use_vllm \
    --vllm_base_url http://localhost:8000/v1 > $EVAL_DIR/logs/predict.log 2>&1

#--- 後片付け -------------------------------------------------------
kill $pid_vllm
wait
```