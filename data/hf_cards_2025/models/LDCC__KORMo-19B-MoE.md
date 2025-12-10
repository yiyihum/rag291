---
library_name: transformers
tags:
- moe
base_model:
- KORMo-Team/KORMo-10B-sft
license: apache-2.0
---

# KORMo-MoE (2-Experts)

본 모델은 **KORMo-Team/KORMo-10B-sft**를 기반으로,
두 개의 Expert를 갖는 **Mixture of Experts (MoE)** 구조로 확장한 버전입니다.

---

## 개요

이 모델은 다음 두 개의 한국어 데이터셋을 활용하여 **QLoRA 기반 미세조정(fine-tuning)**을 수행한 후,
**2-Expert MoE 모델**로 변환한 실험용 연구 모델입니다.

* **사용 데이터셋**

  * [jaeyong2/Code-Qwen3-14B-Ko](https://huggingface.co/jaeyong2/Code-Qwen3-14B-Ko)
  * [LGAI-EXAONE/Ko-LongRAG](https://huggingface.co/LGAI-EXAONE/Ko-LongRAG)

* **베이스 모델**

  * [KORMo-Team/KORMo-10B-sft](https://huggingface.co/KORMo-Team/KORMo-10B-sft)

---

## 학습 구성

* **미세조정 방식:** QLoRA
* **Expert 수:** 2
* **MoE 변환 도구:** mergekit
* **베이스 모델:** KORMo-10B-sft

---

## vLLM 호환성

본 모델을 vLLM에서 실행하기 위해서는 별도의 패치 적용이 필요합니다.
다음 스크립트를 사용하여 설치를 진행할 수 있습니다.

* [install_vllm_support.sh](https://huggingface.co/dev7halo/KORMo-10B-sft-moe/blob/main/install_vllm_support.sh)

---

## 참고 및 감사

본 연구는 **KORMo-Team**에서 공개한 오픈소스 모델인
[KORMo-10B-sft](https://huggingface.co/KORMo-Team/KORMo-10B-sft)를 기반으로 수행되었습니다.
모델을 공개해주신 KORMo-Team에 감사의 뜻을 전합니다.

---