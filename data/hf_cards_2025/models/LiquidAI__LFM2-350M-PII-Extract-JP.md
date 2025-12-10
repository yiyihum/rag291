---
library_name: transformers
language:
- ja
base_model:
- LiquidAI/LFM2-350M
license: other
license_name: lfm1.0
license_link: LICENSE
---

<center>
<div style="text-align: center;">
  <img 
    src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/7_6D7rWrLxp2hb6OHSV1p.png" 
    alt="Liquid AI"
    style="width: 100%; max-width: 66%; height: auto; display: inline-block; margin-bottom: 0.5em; margin-top: 0.5em;"
  />
</div>
<div style="display: flex; justify-content: center;">
<a href="https://playground.liquid.ai/chat">
<svg width="114.8" height="20" viewBox="0 0 900 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Playground" style="margin-bottom: 1em;">
  <title>Playground</title>
  <g>
    <rect fill="#fff" width="200" height="200"></rect>
    <rect fill="url(#x)" x="200" width="800" height="200"></rect>
  </g>
  <g transform="translate(35, 30) scale(0.45, 0.45)">
    <path d="M172.314 129.313L172.219 129.367L206.125 188.18C210.671 195.154 213.324 203.457 213.324 212.382C213.324 220.834 210.956 228.739 206.839 235.479L275.924 213.178L167.853 33.6L141.827 76.9614L172.314 129.313Z" fill="black"/>
    <path d="M114.217 302.4L168.492 257.003C168.447 257.003 168.397 257.003 168.352 257.003C143.515 257.003 123.385 237.027 123.385 212.387C123.385 203.487 126.023 195.204 130.55 188.24L162.621 132.503L135.966 86.7327L60.0762 213.183L114.127 302.4H114.217Z" fill="black"/>
    <path d="M191.435 250.681C191.435 250.681 191.43 250.681 191.425 250.686L129.71 302.4H221.294L267.71 226.593L191.435 250.686V250.681Z" fill="black"/>
  </g>
  <g transform="translate(50, 0)" aria-hidden="true" fill="#fff" text-anchor="start" font-family="Verdana,DejaVu Sans,sans-serif" font-size="110">
    <text x="255" y="148" textLength="619" fill="#000" opacity="0.1">Playground</text>
    <text x="245" y="138" textLength="619">Playground</text>
  </g>
  <linearGradient id="x" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" style="stop-color:#000000"></stop>
    <stop offset="100%" style="stop-color:#000000"></stop>
  </linearGradient>
</svg>
</a>
<a href="https://leap.liquid.ai/?utm_source=huggingface&utm_medium=modelcards">
<svg width="114.8" height="20" viewBox="0 0 900 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Leap" style="margin-bottom: 1em;">
  <title>Leap</title>
  <g>
    <rect fill="#000" width="500" height="200"></rect>
  </g>
  <g transform="translate(100, 45) scale(3.5, 3.5)" fill="#fff">
    <path d="M13.8512 28.0769C12.5435 28.0769 11.4025 27.8205 10.4281 27.3077C9.45375 26.7692 8.68452 26.0128 8.12042 25.0385C7.58196 24.0641 7.31273 22.9359 7.31273 21.6538V3.76923H0.389648V0H11.4666V21.6538C11.4666 22.4744 11.6973 23.1282 12.1589 23.6154C12.6204 24.0769 13.2486 24.3077 14.0435 24.3077H20.582V28.0769H13.8512Z"/>
    <path d="M29.6439 28.4615C27.9259 28.4615 26.4131 28.1282 25.1054 27.4615C23.8233 26.7692 22.8362 25.8077 22.1439 24.5769C21.4516 23.3462 21.1054 21.9103 21.1054 20.2692V14.7308C21.1054 13.0641 21.4516 11.6282 22.1439 10.4231C22.8362 9.19231 23.8233 8.24359 25.1054 7.57692C26.4131 6.88462 27.9259 6.53846 29.6439 6.53846C31.3875 6.53846 32.9003 6.88462 34.1823 7.57692C35.4644 8.24359 36.4516 9.19231 37.1439 10.4231C37.8362 11.6282 38.1823 13.0641 38.1823 14.7308V18.5H25.1054V20.2692C25.1054 21.8333 25.49 23.0256 26.2592 23.8462C27.0541 24.6667 28.1951 25.0769 29.6823 25.0769C30.8875 25.0769 31.8618 24.8718 32.6054 24.4615C33.349 24.0256 33.8105 23.3974 33.99 22.5769H38.1054C37.7977 24.3718 36.8746 25.8077 35.3362 26.8846C33.7977 27.9359 31.9003 28.4615 29.6439 28.4615ZM34.1823 16V14.6923C34.1823 13.1538 33.7977 11.9615 33.0285 11.1154C32.2592 10.2692 31.131 9.84615 29.6439 9.84615C28.1823 9.84615 27.0541 10.2692 26.2592 11.1154C25.49 11.9615 25.1054 13.1667 25.1054 14.7308V15.6923L34.49 15.6538L34.1823 16Z"/>
    <path d="M46.3596 28.4615C44.1545 28.4615 42.4109 27.8974 41.1288 26.7692C39.8724 25.6154 39.2442 24.0513 39.2442 22.0769C39.2442 20.0769 39.9109 18.5128 41.2442 17.3846C42.6032 16.2308 44.4622 15.6538 46.8211 15.6538H52.7058V13.6923C52.7058 12.5385 52.3468 11.641 51.6288 11C50.9109 10.359 49.8981 10.0385 48.5904 10.0385C47.4365 10.0385 46.475 10.2949 45.7058 10.8077C44.9365 11.2949 44.4878 11.9487 44.3596 12.7692H40.2827C40.5135 10.8718 41.3852 9.35897 42.8981 8.23077C44.4365 7.10256 46.3724 6.53846 48.7058 6.53846C51.2186 6.53846 53.2058 7.17949 54.6673 8.46154C56.1288 9.71795 56.8596 11.4359 56.8596 13.6154V28.0769H52.8211V24.1923H52.1288L52.8211 23.4231C52.8211 24.9615 52.2314 26.1923 51.0519 27.1154C49.8724 28.0128 48.3083 28.4615 46.3596 28.4615ZM47.5904 25.2692C49.0776 25.2692 50.2955 24.8974 51.2442 24.1538C52.2186 23.3846 52.7058 22.4103 52.7058 21.2308V18.4615H46.8981C45.8211 18.4615 44.9622 18.7564 44.3211 19.3462C43.7058 19.9359 43.3981 20.7436 43.3981 21.7692C43.3981 22.8462 43.7699 23.7051 44.5135 24.3462C45.257 24.9615 46.2827 25.2692 47.5904 25.2692Z"/>
    <path d="M58.9984 35V6.92308H63.1138V10.9615H63.9984L63.1138 11.9231C63.1138 10.2564 63.6266 8.94872 64.6523 8C65.7036 7.02564 67.101 6.53846 68.8446 6.53846C70.9728 6.53846 72.6651 7.25641 73.9215 8.69231C75.2036 10.1026 75.8446 12.0385 75.8446 14.5V20.4615C75.8446 22.1026 75.5497 23.5256 74.96 24.7308C74.3959 25.9103 73.5882 26.8333 72.5369 27.5C71.5113 28.141 70.2805 28.4615 68.8446 28.4615C67.1266 28.4615 65.742 27.9872 64.6907 27.0385C63.6395 26.0641 63.1138 24.7436 63.1138 23.0769L63.9984 24.0385H63.0369L63.1523 28.9615V35H58.9984ZM67.4215 24.8462C68.7805 24.8462 69.8318 24.4615 70.5754 23.6923C71.3446 22.8974 71.7292 21.7564 71.7292 20.2692V14.7308C71.7292 13.2436 71.3446 12.1154 70.5754 11.3462C69.8318 10.5513 68.7805 10.1538 67.4215 10.1538C66.1138 10.1538 65.0754 10.5641 64.3061 11.3846C63.5369 12.1795 63.1523 13.2949 63.1523 14.7308V20.2692C63.1523 21.7051 63.5369 22.8333 64.3061 23.6538C65.0754 24.4487 66.1138 24.8462 67.4215 24.8462Z"/>
  </g>
  <linearGradient id="y" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" style="stop-color:#000000"></stop>
  </linearGradient>
</svg>
</a>
</div>
</center>

（[_日本語はこちらから_](#lfm2-350m-pii-extract-jp-日本語)）

# LFM2-350M-PII-Extract-JP

Based on [LFM2-350M](https://huggingface.co/LiquidAI/LFM2-350M), this checkpoint is designed to **extract personally identifiable information (PII) from Japanese text and output it in JSON format.**
The output can then be used to mask out sensitive information in contracts, emails, personal medical reports, insurance bills, etc. directly on-device.

In particular, it is trained to extract:
* Address/locations (JSON key: `address`)
* Company/institute/organization names (JSON key: `company_name`)
* Email addresses (JSON key: `email_address`)
* Human names (JSON key: `human_name`)
* Phone numbers (JSON key: `phone_number`)
from Japanese documents and texts.

### Demo

<video src="https://cdn-uploads.huggingface.co/production/uploads/65d6b6c1a07ad79084a0d214/z5og84hVLGgIm1Z2c98PP.mp4" controls preload></video>
Running on a macbook pro.

## Extraction Quality 

We evaluated several models, including GPT-5 and a 32B-parameter Qwen3 model with thinking mode enabled.  
The image below shows the average recall score on 1,000 random samples, chunked into segments of 100–1,000 characters, taken from [finepdf](https://huggingface.co/datasets/HuggingFaceFW/finepdfs).  
Overall, we found **LFM2-350M-PII-Extract-JP** to achieve GPT-5–level performance with only 350 million parameters—bringing cloud-grade performance to on-device applications!

![Model Size vs Recall Score](https://cdn-uploads.huggingface.co/production/uploads/65d6b6c1a07ad79084a0d214/ToNbcFk-7Pyr-aReyErEm.png)

### Sample Responses

<table>
  <colgroup>
    <col style="width: 50%">
    <col style="width: 50%">
  </colgroup>
  <thead>
    <tr>
      <th>Input text</th>
      <th>Output JSON</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>田中　太郎 様<br><br>平素より格別のご高配を賜り、誠にありがとうございます。<br><br>このたび、山田　花子 が ABCコーポレーション赤坂オフィス へ 田中　太郎 様をご招待いたしました。<br><br>ご来訪当日は、本メールに記載の「受付番号」または「受付QRコード」を使用してチェックインを行っていただきます。以下のいずれかの方法でご準備をお願いいたします。<br><br>・本メールを印刷してご持参いただく<br>・スマートフォンで本メールを表示いただく<br><br>■ご来訪情報<br>受付番号: 594813<br>日付: 2025-10-03<br>時間: 11:00<br>担当者: 山田　花子<br>場所: 東京都港区赤坂1-2-3 赤坂ビジネスタワー5階</td>
      <td>{"address": ["東京都港区赤坂1-2-3 赤坂ビジネスタワー5階"], "company_name": ["ABCコーポレーション赤坂オフィス"], "email_address": [], "human_name": ["田中　太郎", "山田　花子"], "phone_number": []}</td>
    </tr>
    <tr>
      <td>山口さん<br><br>CCに佐藤さんも追加させていただきました<br><br>打ち合わせ可能なお時間をご連絡いただきありがとうございます。<br>佐藤さんたちは御社との初回の打ち合わせのため、御社についての基本的なところからご紹介いただく場としていただき、<br>お忙しいところ恐縮ですが、我々の打ち合わせについては別枠として、１０月８日（水）１７：００～の佐藤さんたちとの打ち合わせの後に開催はいかがでしょうか。<br><br>終了時間が１８時を過ぎてしまう可能性が高いため、ご都合が悪ければ別日で調整させてください。<br>お手数をおかけしますが、ご確認のほどどうぞよろしくお願いいたします。<br><br>中村　正信<br><br>Email: nakamura@japan.co.jp</td>
      <td>{"address": [], "company_name": [], "email_address": ["nakamura@japan.co.jp"], "human_name": ["山口", "佐藤", "中村　正信"], "phone_number": []}</td>
    </tr>
    <tr>
      <td>差出人： モンスタカード株式会社（自動配信）<br>件名： 【モスカードフリー】ご利用内容のお知らせ<br><br>⸻<br><br>夢野 みな 様<br><br>いつもモスカードフリーをご利用いただきありがとうございます。<br>お客様のカードご利用内容をお知らせいたします。<br><br>⸻<br><br>ご利用内容<br>	•	利用日：2025年10月6日 18:38:15<br>	•	利用先：ライトペイ<br>	•	ご利用金額：1000円<br>	•	承認番号：294816<br></td>
      <td>{"address": [], "company_name": ["モンスタカード株式会社", "ライトペイ"], "email_address": [], "human_name": ["夢野 みな"], "phone_number": []}</td>
    </tr>
    <tr>
      <td>株式会社ネットワークソリューションズ<br><br>請求書<br><br>発行日：2024年10月27日<br>請求番号：NS-20241027-001<br><br>田中電気工業<br>東京都渋谷区神南1-23-10<br>電話番号：+81373453302<br><br>--------------------------------------------------------------------------------<br><br>**請求先**<br><br>伊藤潔文 様<br>ryuma@izumiya.cloud<br><br>--------------------------------------------------------------------------------<br></td>
      <td>{"address": ["東京都渋谷区神南1-23-10"], "company_name": ["株式会社ネットワークソリューションズ", "田中電気工業"], "email_address": ["ryuma@izumiya.cloud"], "human_name": ["伊藤潔文"], "phone_number": ["+81373453302"]}</td>
    </tr>
    <tr>
      <td>機材等借用書（一般化・架空化済）<br><br>作成日：2025年4月18日<br><br>貸主：ネオテック株式会社<br>住所：東京都中央区銀星町三丁目<br>担当者：山田　廉（yamada@neotech.example.jp）<br><br>借主：グローバルデバイスホールディングス株式会社<br>住所：東京都新都区青海一丁目<br>担当者：佐藤　翔（sato@globaldevices.example.com）<br><br>⸻<br><br>借用物品のリスト<br>- スマートフォン　型番：Nova X10 Pro　数量：1台　状態：良好<br>- モデル（Conversa 1B LFM, Conversa 3B LFM, Focus 1B LFM, Focus 1B VLM）<br><br>⸻<br><br>借用条件<br>- 借用期間：2025年4月18日から2025年6月30日まで<br>- 借用目的：オンデバイスモデルの動作検証<br>- 使用責任：物品は善良な管理者の注意をもって使用し、破損した場合は貸主に即時報告すること。<br>- 紛失・盗難時の対応：同等の物品を貸主に弁償すること。<br><br>⸻<br><br>貸主署名：中島　誠一<br>借主署名：高橋　健吾</td>
      <td>{"address": ["東京都中央区銀星町三丁目", "東京都新都区青海一丁目"], "company_name": ["ネオテック株式会社", "グローバルデバイスホールディングス株式会社"], "email_address": ["yamada@neotech.example.jp"], "human_name": ["中島　誠一", "山田　廉", "佐藤　翔"], "phone_number": []}</td>
    </tr>
  </tbody>
</table>

> [!NOTE]  
> 📝 While LFM2-350M-PII-Extract-JP provides strong out-of-the-box PII entity extraction for the categories listed above, our primary goal is to deliver a versatile, community-driven base model—a foundation that makes it easy to build best-in-class, privacy-focused masking systems.  
>  
> Like any base model, there remain areas for continued development, particularly for specialized use cases:  
> - Supporting extraction of organization-specific identification numbers
> - Expanding coverage to additional categories such as date of birth, passport numbers
> - Further improving extraction performance on particular categories
> 
> These are precisely the kinds of challenges that fine-tuning—by both Liquid AI and our developer community can address. We see this model not just as an endpoint, but as a catalyst for a rich ecosystem of fine-tuned PII extraction models tailored to real-world needs.

## Model Details

**Generation parameters**: We strongly recommend using greedy decoding with a `temperature=0`.

**System prompts**: This checkpoint **requires** the following system prompt:
```
Extract <address>, <company_name>, <email_address>, <human_name>, <phone_number>
```

Note the model can handle extraction of particular entities. E.g. The model will only output human names when the system prompt is set to `Extract <human_name>`.

> [!WARNING]
> ⚠️ For best performance, ensure alphabetical order of entity categories as shown above.


**Chat template**: LFM2-PII-Extract-JP uses a ChatML-like chat template as follows:

```
<|startoftext|><|im_start|>system
Extract <address>, <company_name>, <email_address>, <human_name>, <phone_number><|im_end|>
<|im_start|>user
こんにちは、ラミンさんに B200 GPU を 10000 台 至急請求してください。連絡先は celegans@liquid.ai (電話番号010-000-0000) で、これは C. elegans 線虫に着想を得たニューラルネットワークアーキテクチャを 今すぐ構築するために不可欠です。<|im_end|>
<|im_start|>assistant
{"address": [], "company_name": [], "email_address": ["celegans@liquid.ai"], "human_name": ["ラミン"], "phone_number": ["010-000-0000"]}<|im_end|>
```

You can automatically apply it using the dedicated [`.apply_chat_template()`](https://huggingface.co/docs/transformers/en/chat_templating#applychattemplate) function from Hugging Face transformers.

> [!WARNING]
> ⚠️ The model is intended for single turn conversations.

**Output format**

The model outputs a JSON object containing the fields it was prompted to extract.
If no entities are found in a particular category, it returns an empty list for that category. 
If entities are found, they are returned as a list for each prompted category.
The model is trained to output entities exactly as they appear in the text. 
If the same entity appears multiple times with slight formatting variations, the model outputs all variations to ensure subsequent masking can be performed using exact matches.


## 🏃 How to run LFM2

- Huggingface: [LFM2-350M](https://huggingface.co/LiquidAI/LFM2-350M)
- llama.cpp: [LFM2-350M-PII-Extract-JP-GGUF](https://huggingface.co/LiquidAI/LFM2-350M-PII-Extract-JP-GGUF)
- LEAP: [LEAP model library](https://leap.liquid.ai/models?model=lfm2-350m-pii-extract-jp)

## 📬 Contact

If you are interested in custom solutions with edge deployment, please contact [our sales team](https://www.liquid.ai/contact).

# LFM2-350M-PII-Extract-JP (日本語)

[**LFM2-350M**](https://huggingface.co/LiquidAI/LFM2-350M) をベースにしたこのチェックポイントは、**日本語文書から個人を特定できる情報（PII）を抽出し、JSON 形式で出力します**。  
契約書、電子メール、個人の医療報告書、並びに保険請求書などの機密情報を、デバイス上で直接マスキングできます。

特に以下の情報を抽出するように訓練されています。
* 住所／所在地（JSON key: `address`）
* 企業／研究機関／組織名（JSON key: `company_name`）
* メールアドレス（JSON key: `email_address`）
* 人名（JSON key: `human_name`）
* 電話番号（JSON key: `phone_number`）

これらの情報を日本語の文書から抽出します。

---

### デモ

<video src="https://cdn-uploads.huggingface.co/production/uploads/65d6b6c1a07ad79084a0d214/z5og84hVLGgIm1Z2c98PP.mp4" controls preload></video>

---

## 性能

[**finepdf**](https://huggingface.co/datasets/HuggingFaceFW/finepdfs) から無作為に抽出した 1,000 サンプルを用いて、GPT5 や 32B パラメータの Qwen3 モデル（思考モードあり）など、複数のモデルとの比較評価を行いました。  
**LFM2-350M-PII-Extract-JP** は、わずか **350M パラメータ** という軽量モデルながら GPT5 と同等レベルの性能を発揮し、クラウドレベルの品質をあなたのデバイス上で実現します！

![Model Size vs Recall Score](https://cdn-uploads.huggingface.co/production/uploads/65d6b6c1a07ad79084a0d214/ToNbcFk-7Pyr-aReyErEm.png)

> [!NOTE]  
> 📝 LFM2-350M-PII-Extract-JP は、上記カテゴリに対して優れた PII 抽出性能を有しますが、私たちの主な目的は、**コミュニティによって継続的に改良される柔軟な基盤モデルを提供すること**です。  
> このモデルで、誰でもプライバシー重視の高品質なマスキングシステムを容易に構築できます。  
>  
> ただし、ベースモデルとして今後さらなる改善の余地があります。特に以下のような専門的な利用用途が想定されます。 
> - 組織固有の識別番号の抽出対応  
> - 生年月日、パスポート番号などの追加カテゴリへの拡張  
> - 特定カテゴリにおける抽出性能のさらなる改善 
>
> これらの課題は、**Liquid AI** および開発者コミュニティによるファインチューニングによって解決できると考えています。  
> LFM2-350M-PII-Extract-JP は完成形ではなく、**実運用ニーズに応じた多様な PII 抽出モデル群を生み出す出発点**であると位置づけています。

---

## モデル詳細

**生成パラメータ**: `temperature=0` の貪欲デコード（greedy decoding）の使用を強く推奨します。

**システムプロンプト**: このチェックポイントでは以下のシステムプロンプトが**必須**です：

```
Extract <address>, <company_name>, <email_address>, <human_name>, <phone_number>
```

モデルは特定のエンティティのみを抽出するように設定することも可能です。  
例: `Extract <human_name>` と設定した場合、人名のみを出力します。

> [!WARNING]
> ⚠️ モデルの性能を最大限発揮させるには、上記のように **エンティティカテゴリをアルファベット順** に並べてください。

---

**チャットテンプレート**  
LFM2-PII-Extract-JP は以下のような ChatML 風テンプレートを使用します。

```
<|startoftext|><|im_start|>system
Extract , <company_name>, <email_address>, <human_name>, <phone_number><|im_end|>
<|im_start|>user
こんにちは、ラミンさんに B200 GPU を 10000 台 至急請求してください。連絡先は celegans@liquid.ai (電話番号010-000-0000) で、これは C. elegans 線虫に着想を得たニューラルネットワークアーキテクチャを 今すぐ構築するために不可欠です。<|im_end|>
<|im_start|>assistant
{“address”: [], “company_name”: [], “email_address”: [“celegans@liquid.ai”], “human_name”: [“ラミン”], “phone_number”: [“010-000-0000”]}<|im_end|>
```

このテンプレートは、Hugging Face Transformers の専用関数 [`.apply_chat_template()`](https://huggingface.co/docs/transformers/en/chat_templating#applychattemplate) を使用して自動的に適用できます。

> [!WARNING]
> ⚠️ このモデルは **一問一答形式　（単一ターン）　の会話** に最適化されています。

---

**出力形式**

モデルは、指定されたエンティティを含んだ JSON 形式で出力します。  
各カテゴリに該当するエンティティが見つからない場合は、空のリストを返します。  
該当するエンティティが存在する場合は、そのカテゴリごとに抽出された文字列のリストを返します。  

モデルは、**テキスト中に現れる形式で正確にエンティティを出力**するように訓練されています。  
同じエンティティが複数回登場し表記に揺れがある場合でも、すべての表記バリエーションを出力し、マスキング時に完全一致で対応できるようになっています。

---

## 🏃 LFM2 の実行方法

- Hugging Face: [LFM2-350M](https://huggingface.co/LiquidAI/LFM2-350M)
- llama.cpp: [LFM2-350M-PII-Extract-JP-GGUF](https://huggingface.co/LiquidAI/LFM2-350M-PII-Extract-JP-GGUF)
- LEAP: [LEAP モデルライブラリ](https://leap.liquid.ai/models?model=lfm2-350m-pii-extract-jp)

---

## 📬 お問い合わせ

エッジ環境への導入を含むカスタムソリューションにご興味がある方は、[営業チーム](https://www.liquid.ai/ja/contact)までお問い合わせください。