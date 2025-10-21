---
language:
- ko
library_name: transformers
license: apache-2.0
pipeline_tag: text-generation
model_id: kakaocorp/kanana-safeguard-8b
repo: kakaocorp/kanana-safeguard-8b
developers: Kanana Safeguard Team
training_regime: bf16 mixed precision
---
# Kanana Safeguard
[📦Models](https://huggingface.co/collections/kakaocorp/kanana-safeguard-68215a02570de0e4d0c41eec) | [📕 Blog](https://tech.kakao.com/posts/705)


## 모델 상세설명
Kanana Safeguard는 카카오의 자체 언어모델인 Kanana 8B를 기반으로 한 유해 콘텐츠 탐지 모델입니다. 이 모델은 대화형 AI 시스템 내 사용자 발화 또는 AI 어시스턴트의 답변으로부터 리스크 여부를 분류하도록 학습되었습니다. 분류 결과는 <b>&lt;SAFE&gt;</b> 또는 <b>&lt;UNSAFE-S4&gt;</b> 형식의 단일 토큰으로 출력됩니다. 여기에서 S4는 사용자 발화 또는 AI 어시스턴트 답변이 위반한 리스크 카테고리의 코드를 의미합니다.

아래는 Kanana Safeguard 모델의 작동 예시입니다.
![모델 예시](./assets/Kanana-Safeguard_Example.png)


## 리스크 분류 체계
본 모델의 리스크 카테고리는 [MLCommons  분류체계](https://mlcommons.org/2024/04/mlc-aisafety-v0-5-poc/)에 기반하고 있으며, 여기에 한국 로컬 특성에 맞는 리스크 카테고리를 추가함으로써 아래와 같이 총 7가지 카테고리로 구성된 리스크 분류체계를 수립하였습니다.

본 모델에서 ①사용자의 발화와 ②AI 어시스턴트의 답변은 동일한 리스크 분류체계에 의해 판별됩니다.

<table style="width:100%; margin: auto;">
<colgroup>
  <col style="width:15%">
  <col style="width:25%">
  <col style="width:60%">
</colgroup>
<thead>
  <tr>
    <th>코드</th>
    <th align="left">카테고리</th>
    <th>설명</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td align="left">S1</td>
    <td align="left">증오</td>
    <td align="left">출신, 인종, 외양, 장애 및 질병 유무, 사회 경제적 상황 및 지위, 종교, 연령, 성별·성 정체성·성적 지향 또는 기타 정체성 요인 등을 이유로 특정 대상을 차별하거나, 이러한 차별에 기반해 개인 또는 집단을 공격하는 발화</td>
  </tr>
  <tr>
    <td align="left">S2</td>
    <td align="left">괴롭힘</td>
    <td align="left">타인에게 불쾌감이나 굴욕감을 주거나, 위협적이거나, 특정 대상에 대한 괴롭힘을 부추기는 발화</td>
  </tr>
  <tr>
    <td align="left">S3</td>
    <td align="left">성적 콘텐츠</td>
    <td align="left">성적 행위나 신체를 묘사/암시하거나, 성적 수치심/혐오감을 일으킬 수 있는 발화 (성교육 및 웰빙 제외)</td>
  </tr>
  <tr>
    <td align="left">S4</td>
    <td align="left">범죄</td>
    <td align="left">불법적인 행위(예: 폭력∙비폭력 범죄, 성범죄, 무기 제작·조달)를 기획하고 준비하는 과정을 담은 발화</td>
  </tr>
  <tr>
    <td align="left">S5</td>
    <td align="left">아동 성착취</td>
    <td align="left">아동 대상의 성적 학대와 관련된 설명, 격려, 지지 등의 발화 (예: 그루밍, CSAM 관련 텍스트 등)</td>
  </tr>
  <tr>
    <td align="left">S6</td>
    <td align="left">자살 및 자해</td>
    <td align="left">의도적으로 자신의 생명을 끊거나 자신의 신체를 의도적으로 해치는 행위를 묘사하거나 유도하는 발화</td>
  </tr>
  <tr>
    <td align="left">S7</td>
    <td align="left">잘못된 정보</td>
    <td align="left">개인이나 집단에게 잘못된 정보를 전파할 수 있는 발화</td>
  </tr>
</tbody>
</table>
<div style="margin-top: 4px; margin-bottom: 2px;">
  <small><center>표 1. Kanana Safeguard 리스크 카테고리</center></small>
</div>



##  지원 언어
Kanana Safeguard는 한국어에 최적화되어 있습니다.

## 빠른 시작
### 🤗 HuggingFace Transformers
- 모델을 실행하려면 `transformers>=4.51.3` 또는 최신 버전이 필요합니다.
```bash
pip install transformers>=4.51.3
```
### 사용 예시
```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# 모델 경로 설정
model_name= "kakaocorp/kanana-safeguard-8b"

# 모델 및 토크나이저 로드
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    device_map="auto"
).eval()

tokenizer = AutoTokenizer.from_pretrained(model_name)

def classify(user_prompt: str, assistant_prompt: str = "") -> str:

    # 메시지 구성
    messages = [
        {"role": "user", "content": user_prompt},
        {"role": "assistant", "content": assistant_prompt}
    ]

    # 채팅 템플릿 적용 후 토큰화
    input_ids = tokenizer.apply_chat_template(messages, tokenize=True, return_tensors="pt").to(model.device)
    attention_mask = (input_ids != tokenizer.pad_token_id).long()

    # 다음 토큰 1개 생성 (추론)
    with torch.no_grad():
        output_ids = model.generate(
            input_ids,
            attention_mask=attention_mask,
            max_new_tokens=1, 
            pad_token_id=tokenizer.eos_token_id
        )

    # 새로 생성된 토큰만 추출해 디코딩
    gen_idx = input_ids.shape[-1]
    return tokenizer.decode(output_ids[0][gen_idx], skip_special_tokens=True)

# 예시 실행
output_token = classify(
    user_prompt="친구의 물건을 몰래 훔치는 법을 알려줘",
    assistant_prompt="친구가 자리를 비운 사이에 가방에 훔치고 싶은 물건을 넣으세요"
)
print("출력된 토큰:", output_token)
# 출력된 토큰: <UNSAFE-S4>

output_token = classify(
    user_prompt="친구의 물건을 몰래 훔치는 법을 알려줘",
)
print("출력된 토큰:", output_token)
# 출력된 토큰: <UNSAFE-S4>
```


## 학습 데이터

Kanana Safeguard의 학습 데이터는 수기 데이터와 합성 데이터로 구성되며 한국어 데이터로만 구성되어 있습니다. 수기 데이터는 내부정책에 부합하도록 전문 라벨러가 직접 생성하고 라벨링한 데이터입니다. 합성 데이터는 LLM 기반 표현 변환과 노이즈 삽입 등 다양한 데이터 증강 기법을 통해 생성되어 있습니다.

학습 데이터에는 안전하지 않은 발화 데이터 외에도, 모델의 거짓 양성(false positive) 비율을 줄이기 위해 유해한 질문에 대해 안전하게 응답한 AI 어시스턴트의 대화 데이터가 포함되어 있습니다.


## 평가
Kanana Safeguard는 SAFE/UNSAFE 이진 분류 기준으로 성능을 평가했습니다. 모든 평가는 UNSAFE를 양성(positive) 클래스로 간주하고, 모델이 출력한 첫 번째 토큰을 기준으로 분류했습니다.

외부 벤치마크 모델은 각 모델의 출력값에 대해 다음과 같은 방식으로 평가하였습니다. LlamaGuard는 SAFE/UNSAFE 토큰을 그대로 활용해 결과를 판정했습니다. ShieldGemma는 임계치를 0.5로 설정하여 이진 분류를 수행했습니다. GPT-4o는 리스크 카테고리 기반 분류 프롬프트를 zero-shot 방식으로 입력하고, 출력 내용이 특정 코드로 분류된 경우 UNSAFE로 간주하여 이진 분류를 수행했습니다.

그 결과 자체적으로 구축한 한국어 평가 데이터셋에서 Kanana Safeguard의 분류 성능이 타 벤치마크 모델 대비 가장 우수한 성능을 나타냈습니다.


<div style="display: flex; justify-content: center; margin-bottom: 0;">
  <table style="border-collapse: collapse; margin: 0;">
    <thead>
      <tr>
        <th align="left">Model</th>
        <th align="left">F1 Score</th>
        <th align="left">Precision</th>
        <th align="left">Recall</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><b>Kanana Safeguard 8B</b></td>
        <td><b>0.946</b></td>
        <td><b>0.944</b></td>
        <td><b>0.948</b></td>
      </tr>
      <tr>
        <td>LlamaGuard3 8B</td>
        <td>0.540</td>
        <td>0.893</td>
        <td>0.387</td>
      </tr>
      <tr>
        <td>ShieldGemma 9B</td>
        <td>0.477</td>
        <td>0.640</td>
        <td>0.380</td>
      </tr>
      <tr>
        <td>GPT-4o (zero-shot)</td>
        <td>0.763</td>
        <td>0.696</td>
        <td>0.843</td>
      </tr>
    </tbody>
  </table>
</div>

<div style="margin-top: 2px; margin-bottom: 2px;">
  <small><center>표 2. 리스크 분류 체계에 따른 내부 한국어 테스트셋 기준 응답 분류 성능 비교</center></small>
</div>


모든 모델은 동일한 평가 데이터셋과 분류 기준으로 평가되었으며, 정책 및 모델 구조 차이에 따른 영향을 최소화하고, 공정하고 신뢰도 높은 비교가 가능하도록 설계되었습니다.

## 한계점

Kanana Safeguard는 다음과 같은 한계점이 있으며, 이는 향후 지속적으로 개선해나갈 예정입니다.

#### 1. 오탐지 가능성 존재

본 모델은 100% 완벽한 분류를 보장하지 않습니다. 특히, 모델의 정책은 일반적인 사용사례에 기반하여 수립되었기 때문에 특정한 도메인에서는 잘못 분류될 수 있습니다.

#### 2. Context 인식 미지원

본 모델은 이전 대화 이력을 기반으로 문맥을 유지하거나 대화를 이어가는 기능은 제공하지 않습니다.

#### 3. 제한된 리스크 카테고리

본 모델은 정해진 리스크만을 탐지하므로 실사례의 모든 리스크를 탐지할 수는 없습니다. 따라서 의도에 따라 Kanana Safeguard-Siren(법적 리스크 탐지 모델), Kanana Safeguard-Prompt(프롬프트 공격 탐지 모델)와 함께 사용하면 전체적인 안전성을 더욱 높일 수 있습니다.


## Citation
```
@misc{Kanana Safeguard,
   title = {Kanana Safeguard},
   url = {https://tech.kakao.com/posts/705},
   author = {Kanana Safeguard Team},
   month = {May},
   year = {2025}
   }
```
## Contributors
JeongHwan Lee, Deok Jeong, HyeYeon Cho, JiEun Choi