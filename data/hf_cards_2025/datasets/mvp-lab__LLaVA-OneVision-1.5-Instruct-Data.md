---
license: apache-2.0
task_categories:
- image-text-to-text
language:
- en
tags:
- multimodal
- vision-language-model
- lmm
- instruction-tuning
- pretraining
- dataset-collection
- vqa
- image-captioning
- large-language-model
configs:
- config_name: CLEVR
  data_files:
  - split: train
    path: CLEVR/train-*
- config_name: CLEVR-Math
  data_files:
  - split: train
    path: CLEVR-Math/train-*
- config_name: Docmatix
  data_files:
  - split: train
    path: Docmatix/train-*
- config_name: Docmatix-part-00-of-10
  data_files:
  - split: train
    path: Docmatix-part-00-of-10/train-*
- config_name: Docmatix-part-01-of-10
  data_files:
  - split: train
    path: Docmatix-part-01-of-10/train-*
- config_name: Docmatix-part-02-of-10
  data_files:
  - split: train
    path: Docmatix-part-02-of-10/train-*
- config_name: Docmatix-part-03-of-10
  data_files:
  - split: train
    path: Docmatix-part-03-of-10/train-*
- config_name: Docmatix-part-04-of-10
  data_files:
  - split: train
    path: Docmatix-part-04-of-10/train-*
- config_name: Docmatix-part-05-of-10
  data_files:
  - split: train
    path: Docmatix-part-05-of-10/train-*
- config_name: Docmatix-part-06-of-10
  data_files:
  - split: train
    path: Docmatix-part-06-of-10/train-*
- config_name: Docmatix-part-07-of-10
  data_files:
  - split: train
    path: Docmatix-part-07-of-10/train-*
- config_name: Docmatix-part-08-of-10
  data_files:
  - split: train
    path: Docmatix-part-08-of-10/train-*
- config_name: Docmatix-part-09-of-10
  data_files:
  - split: train
    path: Docmatix-part-09-of-10/train-*
- config_name: Evol-Instruct-GPT4-Turbo
  data_files:
  - split: train
    path: Evol-Instruct-GPT4-Turbo/train-*
- config_name: FigureQA
  data_files:
  - split: train
    path: FigureQA/train-*
- config_name: GEOS
  data_files:
  - split: train
    path: GEOS/train-*
- config_name: GeoQA+
  data_files:
  - split: train
    path: GeoQA+/train-*
- config_name: Geometry3K
  data_files:
  - split: train
    path: Geometry3K/train-*
- config_name: IconQA
  data_files:
  - split: train
    path: IconQA/train-*
- config_name: OmniDocBench_train
  data_files:
  - split: train
    path: OmniDocBench_train/train-*
- config_name: PMC-VQA
  data_files:
  - split: train
    path: PMC-VQA/train-*
- config_name: Super-CLEVR
  data_files:
  - split: train
    path: Super-CLEVR/train-*
- config_name: VisualWebInstruct
  data_files:
  - split: train
    path: VisualWebInstruct/train-*
- config_name: VizWiz
  data_files:
  - split: train
    path: VizWiz/train-*
- config_name: ai2d
  data_files:
  - split: train
    path: ai2d/train-*
- config_name: alfredplpl
  data_files:
  - split: train
    path: alfredplpl/train-*
- config_name: alfworld
  data_files:
  - split: train
    path: alfworld/train-*
- config_name: allava
  data_files:
  - split: train
    path: allava/train-*
- config_name: allava_instruct_laion4v
  data_files:
  - split: train
    path: allava_instruct_laion4v/train-*
- config_name: allava_instruct_vflan4v
  data_files:
  - split: train
    path: allava_instruct_vflan4v/train-*
- config_name: allenai_pixmo_docs
  data_files:
  - split: train
    path: allenai_pixmo_docs/train-*
- config_name: amc_aime
  data_files:
  - split: train
    path: amc_aime/train-*
- config_name: aokvqa
  data_files:
  - split: train
    path: aokvqa/train-*
- config_name: aops_forum
  data_files:
  - split: train
    path: aops_forum/train-*
- config_name: arxiv_figs
  data_files:
  - split: train
    path: arxiv_figs/train-*
- config_name: arxivqa
  data_files:
  - split: train
    path: arxivqa/train-*
- config_name: cambrian
  data_files:
  - split: train
    path: cambrian/train-*
- config_name: chart2text
  data_files:
  - split: train
    path: chart2text/train-*
- config_name: chartqa
  data_files:
  - split: train
    path: chartqa/train-*
- config_name: chrome_writting
  data_files:
  - split: train
    path: chrome_writting/train-*
- config_name: cn_k12
  data_files:
  - split: train
    path: cn_k12/train-*
- config_name: coco
  data_files:
  - split: train
    path: coco/train-*
- config_name: code_feedback_66k
  data_files:
  - split: train
    path: code_feedback_66k/train-*
- config_name: datikz
  data_files:
  - split: train
    path: datikz/train-*
- config_name: diagram
  data_files:
  - split: train
    path: diagram/train-*
- config_name: docvqa_train
  data_files:
  - split: train
    path: docvqa_train/train-*
- config_name: dvqa
  data_files:
  - split: train
    path: dvqa/train-*
- config_name: finqa
  data_files:
  - split: train
    path: finqa/train-*
- config_name: geo170k_align
  data_files:
  - split: train
    path: geo170k_align/train-*
- config_name: geo170k_qa
  data_files:
  - split: train
    path: geo170k_qa/train-*
- config_name: geo3k
  data_files:
  - split: train
    path: geo3k/train-*
- config_name: geomverse
  data_files:
  - split: train
    path: geomverse/train-*
- config_name: gpt4o
  data_files:
  - split: train
    path: gpt4o/train-*
- config_name: gpt4v
  data_files:
  - split: train
    path: gpt4v/train-*
- config_name: gqa
  data_files:
  - split: train
    path: gqa/train-*
- config_name: gsm8k
  data_files:
  - split: train
    path: gsm8k/train-*
- config_name: hateful_memes
  data_files:
  - split: train
    path: hateful_memes/train-*
- config_name: hitab
  data_files:
  - split: train
    path: hitab/train-*
- config_name: hme100k
  data_files:
  - split: train
    path: hme100k/train-*
- config_name: iam
  data_files:
  - split: train
    path: iam/train-*
- config_name: idk
  data_files:
  - split: train
    path: idk/train-*
- config_name: ifeval_like
  data_files:
  - split: train
    path: ifeval_like/train-*
- config_name: iiit
  data_files:
  - split: train
    path: iiit/train-*
- config_name: image_textualization
  data_files:
  - split: train
    path: image_textualization/train-*
- config_name: infographic_azuregpt4v
  data_files:
  - split: train
    path: infographic_azuregpt4v/train-*
- config_name: infographic_vqa
  data_files:
  - split: train
    path: infographic_vqa/train-*
- config_name: intergps
  data_files:
  - split: train
    path: intergps/train-*
- config_name: invoices-and-receipts_ocr
  data_files:
  - split: train
    path: invoices-and-receipts_ocr/train-*
- config_name: laion_220k
  data_files:
  - split: train
    path: laion_220k/train-*
- config_name: latex_ocr
  data_files:
  - split: train
    path: latex_ocr/train-*
- config_name: llava_cot_100k
  data_files:
  - split: train
    path: llava_cot_100k/train-*
- config_name: llava_instruct
  data_files:
  - split: train
    path: llava_instruct/train-*
- config_name: llava_wild
  data_files:
  - split: train
    path: llava_wild/train-*
- config_name: llavar
  data_files:
  - split: train
    path: llavar/train-*
- config_name: llrv_gpt4v
  data_files:
  - split: train
    path: llrv_gpt4v/train-*
- config_name: lrv_chart
  data_files:
  - split: train
    path: lrv_chart/train-*
- config_name: magpie_pro
  data_files:
  - split: train
    path: magpie_pro/train-*
- config_name: magpie_ultra
  data_files:
  - split: train
    path: magpie_ultra/train-*
- config_name: mapqa
  data_files:
  - split: train
    path: mapqa/train-*
- config_name: math
  data_files:
  - split: train
    path: math/train-*
- config_name: mathinstruct_262k
  data_files:
  - split: train
    path: mathinstruct_262k/train-*
- config_name: mathqa
  data_files:
  - split: train
    path: mathqa/train-*
- config_name: mavis_math_metagen
  data_files:
  - split: train
    path: mavis_math_metagen/train-*
- config_name: ocr
  data_files:
  - split: train
    path: ocr/train-*
- config_name: ocrvqa
  data_files:
  - split: train
    path: ocrvqa/train-*
- config_name: olympiads
  data_files:
  - split: train
    path: olympiads/train-*
- config_name: oodvqa
  data_files:
  - split: train
    path: oodvqa/train-*
- config_name: open_orca
  data_files:
  - split: train
    path: open_orca/train-*
- config_name: openmathinstruct
  data_files:
  - split: train
    path: openmathinstruct/train-*
- config_name: orca_994k
  data_files:
  - split: train
    path: orca_994k/train-*
- config_name: orca_agentinstruct
  data_files:
  - split: train
    path: orca_agentinstruct/train-*
- config_name: oroikon_chart_captioning
  data_files:
  - split: train
    path: oroikon_chart_captioning/train-*
- config_name: pathvqa
  data_files:
  - split: train
    path: pathvqa/train-*
- config_name: plotqa
  data_files:
  - split: train
    path: plotqa/train-*
- config_name: plotqa-part-00-of-10
  data_files:
  - split: train
    path: plotqa-part-00-of-10/train-*
- config_name: plotqa-part-01-of-10
  data_files:
  - split: train
    path: plotqa-part-01-of-10/train-*
- config_name: plotqa-part-02-of-10
  data_files:
  - split: train
    path: plotqa-part-02-of-10/train-*
- config_name: plotqa-part-03-of-10
  data_files:
  - split: train
    path: plotqa-part-03-of-10/train-*
- config_name: plotqa-part-04-of-10
  data_files:
  - split: train
    path: plotqa-part-04-of-10/train-*
- config_name: plotqa-part-05-of-10
  data_files:
  - split: train
    path: plotqa-part-05-of-10/train-*
- config_name: plotqa-part-06-of-10
  data_files:
  - split: train
    path: plotqa-part-06-of-10/train-*
- config_name: plotqa-part-07-of-10
  data_files:
  - split: train
    path: plotqa-part-07-of-10/train-*
- config_name: plotqa-part-08-of-10
  data_files:
  - split: train
    path: plotqa-part-08-of-10/train-*
- config_name: plotqa-part-09-of-10
  data_files:
  - split: train
    path: plotqa-part-09-of-10/train-*
- config_name: raven
  data_files:
  - split: train
    path: raven/train-*
- config_name: rects
  data_files:
  - split: train
    path: rects/train-*
- config_name: rendered_text
  data_files:
  - split: train
    path: rendered_text/train-*
- config_name: robut_sqa
  data_files:
  - split: train
    path: robut_sqa/train-*
- config_name: robut_wikisql
  data_files:
  - split: train
    path: robut_wikisql/train-*
- config_name: robut_wtq
  data_files:
  - split: train
    path: robut_wtq/train-*
- config_name: rootsautomation
  data_files:
  - split: train
    path: rootsautomation/train-*
- config_name: scienceqa
  data_files:
  - split: train
    path: scienceqa/train-*
- config_name: screen2words
  data_files:
  - split: train
    path: screen2words/train-*
- config_name: screen_qa
  data_files:
  - split: train
    path: screen_qa/train-*
- config_name: sharegpt4o
  data_files:
  - split: train
    path: sharegpt4o/train-*
- config_name: sharegpt4v
  data_files:
  - split: train
    path: sharegpt4v/train-*
- config_name: sharegpt4v-part-00-of-10
  data_files:
  - split: train
    path: sharegpt4v-part-00-of-10/train-*
- config_name: sharegpt4v-part-01-of-10
  data_files:
  - split: train
    path: sharegpt4v-part-01-of-10/train-*
- config_name: sharegpt4v-part-03-of-10
  data_files:
  - split: train
    path: sharegpt4v-part-03-of-10/train-*
- config_name: sharegpt4v-part-04-of-10
  data_files:
  - split: train
    path: sharegpt4v-part-04-of-10/train-*
- config_name: sharegpt4v-part-05-of-10
  data_files:
  - split: train
    path: sharegpt4v-part-05-of-10/train-*
- config_name: sharegpt4v-part-06-of-10
  data_files:
  - split: train
    path: sharegpt4v-part-06-of-10/train-*
- config_name: sharegpt4v-part-07-of-10
  data_files:
  - split: train
    path: sharegpt4v-part-07-of-10/train-*
- config_name: sharegpt4v-part-08-of-10
  data_files:
  - split: train
    path: sharegpt4v-part-08-of-10/train-*
- config_name: sharegpt4v-part-09-of-10
  data_files:
  - split: train
    path: sharegpt4v-part-09-of-10/train-*
- config_name: sharegpt4v-part00-of-10
  data_files:
  - split: train
    path: sharegpt4v-part00-of-10/train-*
- config_name: sherlock
  data_files:
  - split: train
    path: sherlock/train-*
- config_name: sroie_data
  data_files:
  - split: train
    path: sroie_data/train-*
- config_name: st_vqa
  data_files:
  - split: train
    path: st_vqa/train-*
- config_name: svit
  data_files:
  - split: train
    path: svit/train-*
- config_name: svit-part-00-of-10
  data_files:
  - split: train
    path: svit-part-00-of-10/train-*
- config_name: svit-part-01-of-10
  data_files:
  - split: train
    path: svit-part-01-of-10/train-*
- config_name: svit-part-02-of-10
  data_files:
  - split: train
    path: svit-part-02-of-10/train-*
- config_name: svit-part-03-of-10
  data_files:
  - split: train
    path: svit-part-03-of-10/train-*
- config_name: svit-part-04-of-10
  data_files:
  - split: train
    path: svit-part-04-of-10/train-*
- config_name: svit-part-05-of-10
  data_files:
  - split: train
    path: svit-part-05-of-10/train-*
- config_name: svit-part-06-of-10
  data_files:
  - split: train
    path: svit-part-06-of-10/train-*
- config_name: svit-part-07-of-10
  data_files:
  - split: train
    path: svit-part-07-of-10/train-*
- config_name: svit-part-08-of-10
  data_files:
  - split: train
    path: svit-part-08-of-10/train-*
- config_name: svit-part-09-of-10
  data_files:
  - split: train
    path: svit-part-09-of-10/train-*
- config_name: synthetic_amc
  data_files:
  - split: train
    path: synthetic_amc/train-*
- config_name: synthetic_math
  data_files:
  - split: train
    path: synthetic_math/train-*
- config_name: tabmwp
  data_files:
  - split: train
    path: tabmwp/train-*
- config_name: tallyqa
  data_files:
  - split: train
    path: tallyqa/train-*
- config_name: tat_qa
  data_files:
  - split: train
    path: tat_qa/train-*
- config_name: textcaps
  data_files:
  - split: train
    path: textcaps/train-*
- config_name: textocr_gpt4v
  data_files:
  - split: train
    path: textocr_gpt4v/train-*
- config_name: textvqa
  data_files:
  - split: train
    path: textvqa/train-*
- config_name: tinychart_train
  data_files:
  - split: train
    path: tinychart_train/train-*
- config_name: tqa
  data_files:
  - split: train
    path: tqa/train-*
- config_name: unigeo
  data_files:
  - split: train
    path: unigeo/train-*
- config_name: ureader_cap
  data_files:
  - split: train
    path: ureader_cap/train-*
- config_name: ureader_chart
  data_files:
  - split: train
    path: ureader_chart/train-*
- config_name: ureader_ie
  data_files:
  - split: train
    path: ureader_ie/train-*
- config_name: ureader_kg
  data_files:
  - split: train
    path: ureader_kg/train-*
- config_name: ureader_ocr
  data_files:
  - split: train
    path: ureader_ocr/train-*
- config_name: ureader_qa
  data_files:
  - split: train
    path: ureader_qa/train-*
- config_name: ureader_tr
  data_files:
  - split: train
    path: ureader_tr/train-*
- config_name: vflan
  data_files:
  - split: train
    path: vflan/train-*
- config_name: vg
  data_files:
  - split: train
    path: vg/train-*
- config_name: viquae
  data_files:
  - split: train
    path: viquae/train-*
- config_name: vision_flan
  data_files:
  - split: train
    path: vision_flan/train-*
- config_name: vision_oritented
  data_files:
  - split: train
    path: vision_oritented/train-*
- config_name: vistext
  data_files:
  - split: train
    path: vistext/train-*
- config_name: visual7w
  data_files:
  - split: train
    path: visual7w/train-*
- config_name: visual_chat
  data_files:
  - split: train
    path: visual_chat/train-*
- config_name: visualmrc
  data_files:
  - split: train
    path: visualmrc/train-*
- config_name: vqaas
  data_files:
  - split: train
    path: vqaas/train-*
- config_name: vqarad
  data_files:
  - split: train
    path: vqarad/train-*
- config_name: vsr
  data_files:
  - split: train
    path: vsr/train-*
- config_name: websight
  data_files:
  - split: train
    path: websight/train-*
- config_name: wikipedia_2m
  data_files:
  - split: train
    path: wikipedia_2m/train-*
- config_name: wit
  data_files:
  - split: train
    path: wit/train-*
- config_name: wit-part-00-of-10
  data_files:
  - split: train
    path: wit-part-00-of-10/train-*
- config_name: wit-part-01-of-10
  data_files:
  - split: train
    path: wit-part-01-of-10/train-*
- config_name: wit-part-02-of-10
  data_files:
  - split: train
    path: wit-part-02-of-10/train-*
- config_name: wit-part-03-of-10
  data_files:
  - split: train
    path: wit-part-03-of-10/train-*
- config_name: wit-part-04-of-10
  data_files:
  - split: train
    path: wit-part-04-of-10/train-*
- config_name: wit-part-05-of-10
  data_files:
  - split: train
    path: wit-part-05-of-10/train-*
- config_name: wit-part-06-of-10
  data_files:
  - split: train
    path: wit-part-06-of-10/train-*
- config_name: wit-part-07-of-10
  data_files:
  - split: train
    path: wit-part-07-of-10/train-*
- config_name: wit-part-08-of-10
  data_files:
  - split: train
    path: wit-part-08-of-10/train-*
- config_name: wit-part-09-of-10
  data_files:
  - split: train
    path: wit-part-09-of-10/train-*
- config_name: wizardlm
  data_files:
  - split: train
    path: wizardlm/train-*
dataset_info:
- config_name: CLEVR
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 98658968456
    num_examples: 513923
  download_size: 99146873156
  dataset_size: 98658968456
- config_name: CLEVR-Math
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 704141445.25
    num_examples: 5254
  download_size: 395553610
  dataset_size: 704141445.25
- config_name: Docmatix
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 210243945988.822
    num_examples: 563353
  download_size: 481638514
  dataset_size: 210243945988.822
- config_name: Docmatix-part-00-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 21021533048.264
    num_examples: 56336
  download_size: 21155061070
  dataset_size: 21021533048.264
- config_name: Docmatix-part-01-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 21344735418.104
    num_examples: 56336
  download_size: 22706658480
  dataset_size: 21344735418.104
- config_name: Docmatix-part-02-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 20967779245.368
    num_examples: 56336
  download_size: 23110021357
  dataset_size: 20967779245.368
- config_name: Docmatix-part-03-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 50367644069.216
    num_examples: 56336
  download_size: 29033528076
  dataset_size: 50367644069.216
- config_name: Docmatix-part-04-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 49454435624.392
    num_examples: 56336
  download_size: 33640597671
  dataset_size: 49454435624.392
- config_name: Docmatix-part-05-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 20871574481.432
    num_examples: 56336
  download_size: 29818113502
  dataset_size: 20871574481.432
- config_name: Docmatix-part-06-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 31625348017.688
    num_examples: 56336
  download_size: 27815516317
  dataset_size: 31625348017.688
- config_name: Docmatix-part-07-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 49257486993.488
    num_examples: 56336
  download_size: 26694793179
  dataset_size: 49257486993.488
- config_name: Docmatix-part-08-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 20530643927.184
    num_examples: 56336
  download_size: 25576629551
  dataset_size: 20530643927.184
- config_name: Docmatix-part-09-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 20893405675.944
    num_examples: 56329
  download_size: 22425123093
  dataset_size: 20893405675.944
- config_name: Evol-Instruct-GPT4-Turbo
  features:
  - name: id
    dtype: string
  - name: image
    dtype: 'null'
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 340832777
    num_examples: 142990
  download_size: 161696446
  dataset_size: 340832777
- config_name: FigureQA
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 2905987600.544
    num_examples: 117236
  download_size: 2229329242
  dataset_size: 2905987600.544
- config_name: GEOS
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 4291931.0
    num_examples: 539
  download_size: 1940017
  dataset_size: 4291931.0
- config_name: GeoQA+
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 83730927.13
    num_examples: 26810
  download_size: 61817604
  dataset_size: 83730927.13
- config_name: Geometry3K
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 507355763.15
    num_examples: 23706
  download_size: 426515764
  dataset_size: 507355763.15
- config_name: IconQA
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 329513303.852
    num_examples: 32284
  download_size: 301306420
  dataset_size: 329513303.852
- config_name: OmniDocBench_train
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 1323493377.0
    num_examples: 967
  download_size: 1320199793
  dataset_size: 1323493377.0
- config_name: PMC-VQA
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 3264375668.0
    num_examples: 36632
  download_size: 1991731127
  dataset_size: 3264375668.0
- config_name: Super-CLEVR
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 2484534021.828
    num_examples: 8607
  download_size: 1409549095
  dataset_size: 2484534021.828
- config_name: VisualWebInstruct
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 1491889641.208
    num_examples: 262484
  download_size: 36112249106
  dataset_size: 1491889641.208
- config_name: VizWiz
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 38217961364.104
    num_examples: 20398
  download_size: 27644804227
  dataset_size: 38217961364.104
- config_name: ai2d
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 4532159662.982
    num_examples: 25283
  download_size: 2616997571
  dataset_size: 4532159662.982
- config_name: alfredplpl
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 4759628979.3
    num_examples: 46140
  download_size: 4861643419
  dataset_size: 4759628979.3
- config_name: alfworld
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 4532436415
    num_examples: 52149
  download_size: 4473211646
  dataset_size: 4532436415
- config_name: allava
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 41672919347
    num_examples: 195333
  download_size: 37353208705
  dataset_size: 41672919347
- config_name: allava_instruct_laion4v
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 36797431482.393
    num_examples: 49817
  download_size: 40306656788
  dataset_size: 36797431482.393
- config_name: allava_instruct_vflan4v
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 10460962487.896
    num_examples: 19884
  download_size: 11411881559
  dataset_size: 10460962487.896
- config_name: allenai_pixmo_docs
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 119683222513.651
    num_examples: 250673
  download_size: 132615986883
  dataset_size: 119683222513.651
- config_name: amc_aime
  features:
  - name: id
    dtype: string
  - name: image
    dtype: 'null'
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 2573711
    num_examples: 1253
  download_size: 1154761
  dataset_size: 2573711
- config_name: aokvqa
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 9587817666
    num_examples: 22848
  download_size: 9543581366
  dataset_size: 9587817666
- config_name: aops_forum
  features:
  - name: id
    dtype: string
  - name: image
    dtype: 'null'
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 24068263
    num_examples: 9228
  download_size: 10457542
  dataset_size: 24068263
- config_name: arxiv_figs
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 10253712585
    num_examples: 150907
  download_size: 9211215150
  dataset_size: 10253712585
- config_name: arxivqa
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 73002348330.0
    num_examples: 94800
  download_size: 77603363947
  dataset_size: 73002348330.0
- config_name: cambrian
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 90832543564.76
    num_examples: 106372
  download_size: 13722483193
  dataset_size: 90832543564.76
- config_name: chart2text
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 2572885140.105
    num_examples: 65445
  download_size: 2459123025
  dataset_size: 2572885140.105
- config_name: chartqa
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 626238631.466
    num_examples: 18202
  download_size: 737167177
  dataset_size: 626238631.466
- config_name: chrome_writting
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 42815893
    num_examples: 8012
  download_size: 41482837
  dataset_size: 42815893
- config_name: cn_k12
  features:
  - name: id
    dtype: string
  - name: image
    dtype: 'null'
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 108907585
    num_examples: 83547
  download_size: 48563919
  dataset_size: 108907585
- config_name: coco
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 16007717616
    num_examples: 96034
  download_size: 15605131699
  dataset_size: 16007717616
- config_name: code_feedback_66k
  features:
  - name: id
    dtype: int64
  - name: image
    dtype: 'null'
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 119444580
    num_examples: 20100
  download_size: 50013435
  dataset_size: 119444580
- config_name: datikz
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 882292174.382
    num_examples: 60687
  download_size: 572226224
  dataset_size: 882292174.382
- config_name: diagram
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 17099878.0
    num_examples: 300
  download_size: 16937673
  dataset_size: 17099878.0
- config_name: docvqa_train
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 5685745704.51
    num_examples: 45230
  download_size: 2366852143
  dataset_size: 5685745704.51
- config_name: dvqa
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 7659614855.824
    num_examples: 368334
  download_size: 3949727608
  dataset_size: 7659614855.824
- config_name: finqa
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 70831822
    num_examples: 1982
  download_size: 63313866
  dataset_size: 70831822
- config_name: geo170k_align
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 1065574101.4
    num_examples: 59550
  download_size: 55984308
  dataset_size: 1065574101.4
- config_name: geo170k_qa
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 418943046.986
    num_examples: 133522
  download_size: 339434513
  dataset_size: 418943046.986
- config_name: geo3k
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 38623317.875
    num_examples: 2089
  download_size: 37292001
  dataset_size: 38623317.875
- config_name: geomverse
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 3737319147.949
    num_examples: 15559
  download_size: 2405271978
  dataset_size: 3737319147.949
- config_name: gpt4o
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 61353912272.757
    num_examples: 71071
  download_size: 60025847169
  dataset_size: 61353912272.757
- config_name: gpt4v
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 2431869
    num_examples: 15
  download_size: 1371971
  dataset_size: 2431869
- config_name: gqa
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 10212302497
    num_examples: 71239
  download_size: 10107366906
  dataset_size: 10212302497
- config_name: gsm8k
  features:
  - name: id
    dtype: string
  - name: image
    dtype: 'null'
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 2701855
    num_examples: 2287
  download_size: 1118901
  dataset_size: 2701855
- config_name: hateful_memes
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 5453710030.73
    num_examples: 15547
  download_size: 3396823617
  dataset_size: 5453710030.73
- config_name: hitab
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 290247414.198
    num_examples: 4893
  download_size: 279904053
  dataset_size: 290247414.198
- config_name: hme100k
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 2144666804.696
    num_examples: 72384
  download_size: 1689213533
  dataset_size: 2144666804.696
- config_name: iam
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 1325856806.338
    num_examples: 5782
  download_size: 1134859451
  dataset_size: 1325856806.338
- config_name: idk
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 2570136166
    num_examples: 16361
  download_size: 2548922433
  dataset_size: 2570136166
- config_name: ifeval_like
  features:
  - name: id
    dtype: string
  - name: image
    dtype: 'null'
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 822869292
    num_examples: 549844
  download_size: 370145051
  dataset_size: 822869292
- config_name: iiit
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 32673529.077
    num_examples: 1903
  download_size: 21439648
  dataset_size: 32673529.077
- config_name: image_textualization
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 47627228322.674
    num_examples: 99214
  download_size: 47955507457
  dataset_size: 47627228322.674
- config_name: infographic_azuregpt4v
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 3337838728.612
    num_examples: 1987
  download_size: 3843900254
  dataset_size: 3337838728.612
- config_name: infographic_vqa
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 10419547553.708
    num_examples: 12599
  download_size: 16231351565
  dataset_size: 10419547553.708
- config_name: intergps
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 42775618.227
    num_examples: 2339
  download_size: 32645900
  dataset_size: 42775618.227
- config_name: invoices-and-receipts_ocr
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 4274776673.956
    num_examples: 5084
  download_size: 3963595787
  dataset_size: 4274776673.956
- config_name: laion_220k
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 85711291526.573
    num_examples: 217277
  download_size: 86239556951
  dataset_size: 85711291526.573
- config_name: latex_ocr
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 400545152.568
    num_examples: 75984
  download_size: 381308074
  dataset_size: 400545152.568
- config_name: llava_cot_100k
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 27508594080.215
    num_examples: 98229
  download_size: 28881479597
  dataset_size: 27508594080.215
- config_name: llava_instruct
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 408572111763
    num_examples: 731871
  download_size: 412789178416
  dataset_size: 408572111763
- config_name: llava_wild
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 11877299941.04
    num_examples: 54240
  download_size: 12027724488
  dataset_size: 11877299941.04
- config_name: llavar
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 3665155100.28
    num_examples: 19796
  download_size: 4197061519
  dataset_size: 3665155100.28
- config_name: llrv_gpt4v
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 4685787963.5
    num_examples: 13820
  download_size: 4462225812
  dataset_size: 4685787963.5
- config_name: lrv_chart
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 75977625
    num_examples: 1348
  download_size: 73729969
  dataset_size: 75977625
- config_name: magpie_pro
  features:
  - name: id
    dtype: string
  - name: image
    dtype: 'null'
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 3887672353
    num_examples: 1035157
  download_size: 2080320604
  dataset_size: 3887672353
- config_name: magpie_ultra
  features:
  - name: id
    dtype: string
  - name: image
    dtype: 'null'
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 4284466937
    num_examples: 621690
  download_size: 2113733041
  dataset_size: 4284466937
- config_name: mapqa
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 3591602953.874
    num_examples: 52581
  download_size: 3891292920
  dataset_size: 3591602953.874
- config_name: math
  features:
  - name: id
    dtype: string
  - name: image
    dtype: 'null'
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 3397864
    num_examples: 2244
  download_size: 1553632
  dataset_size: 3397864
- config_name: mathinstruct_262k
  features:
  - name: id
    dtype: string
  - name: image
    dtype: 'null'
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 59727824
    num_examples: 79064
  download_size: 29054093
  dataset_size: 59727824
- config_name: mathqa
  features:
  - name: id
    dtype: string
  - name: image
    dtype: 'null'
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 18324295
    num_examples: 29837
  download_size: 7835239
  dataset_size: 18324295
- config_name: mavis_math_metagen
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 4913643894.22
    num_examples: 126252
  download_size: 479543437
  dataset_size: 4913643894.22
- config_name: ocr
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 97057651392
    num_examples: 272699
  download_size: 100513234481
  dataset_size: 97057651392
- config_name: ocrvqa
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 192220536975.321
    num_examples: 795837
  download_size: 186504286254
  dataset_size: 192220536975.321
- config_name: olympiads
  features:
  - name: id
    dtype: string
  - name: image
    dtype: 'null'
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 113636628
    num_examples: 45559
  download_size: 51830900
  dataset_size: 113636628
- config_name: oodvqa
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 8827296
    num_examples: 184
  download_size: 8450099
  dataset_size: 8827296
- config_name: open_orca
  features:
  - name: id
    dtype: string
  - name: image
    dtype: 'null'
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 1829769385
    num_examples: 994896
  download_size: 980766869
  dataset_size: 1829769385
- config_name: openmathinstruct
  features:
  - name: id
    dtype: string
  - name: image
    dtype: 'null'
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 2811366371
    num_examples: 2000000
  download_size: 1232182717
  dataset_size: 2811366371
- config_name: orca_994k
  features:
  - name: id
    dtype: string
  - name: image
    dtype: 'null'
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 511081061
    num_examples: 300672
  download_size: 291227937
  dataset_size: 511081061
- config_name: orca_agentinstruct
  features:
  - name: id
    dtype: string
  - name: image
    dtype: 'null'
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 4655740195
    num_examples: 1045962
  download_size: 2175621538
  dataset_size: 4655740195
- config_name: oroikon_chart_captioning
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 931928977.459
    num_examples: 7033
  download_size: 914494177
  dataset_size: 931928977.459
- config_name: pathvqa
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
    - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 2911759151
    num_examples: 39044
  download_size: 2928811947
  dataset_size: 2911759151
- config_name: plotqa
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 7669294271.56
    num_examples: 161940
  download_size: 407407738
  dataset_size: 7669294271.56
- config_name: plotqa-part-00-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 781908738.6800001
    num_examples: 16195
  download_size: 506187336
  dataset_size: 781908738.6800001
- config_name: plotqa-part-01-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 767248006.22
    num_examples: 16195
  download_size: 509766891
  dataset_size: 767248006.22
- config_name: plotqa-part-02-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 772633525.1
    num_examples: 16195
  download_size: 506695377
  dataset_size: 772633525.1
- config_name: plotqa-part-03-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 780510853.0350001
    num_examples: 16195
  download_size: 507955457
  dataset_size: 780510853.0350001
- config_name: plotqa-part-04-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 775095467.155
    num_examples: 16195
  download_size: 504202546
  dataset_size: 775095467.155
- config_name: plotqa-part-05-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 790520320.72
    num_examples: 16195
  download_size: 506931337
  dataset_size: 790520320.72
- config_name: plotqa-part-06-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 769692934.645
    num_examples: 16195
  download_size: 510039271
  dataset_size: 769692934.645
- config_name: plotqa-part-07-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 756509667.03
    num_examples: 16195
  download_size: 507179928
  dataset_size: 756509667.03
- config_name: plotqa-part-08-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 755331081.755
    num_examples: 16195
  download_size: 504284659
  dataset_size: 755331081.755
- config_name: plotqa-part-09-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 671035229.44
    num_examples: 16185
  download_size: 426711812
  dataset_size: 671035229.44
- config_name: raven
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 1238680467
    num_examples: 26272
  download_size: 882803494
  dataset_size: 1238680467
- config_name: rects
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 14120895031
    num_examples: 17008
  download_size: 13745231728
  dataset_size: 14120895031
- config_name: rendered_text
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 20822834309.707
    num_examples: 18921
  download_size: 11889739609
  dataset_size: 20822834309.707
- config_name: robut_sqa
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 977619260.736
    num_examples: 12236
  download_size: 934625339
  dataset_size: 977619260.736
- config_name: robut_wikisql
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 10625815479.58
    num_examples: 153386
  download_size: 10925972299
  dataset_size: 10625815479.58
- config_name: robut_wtq
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 3913556713.875
    num_examples: 39997
  download_size: 3469922801
  dataset_size: 3913556713.875
- config_name: rootsautomation
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 31579126428.43
    num_examples: 306115
  download_size: 1536808989
  dataset_size: 31579126428.43
- config_name: scienceqa
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 121336362
    num_examples: 1563
  download_size: 120136170
  dataset_size: 121336362
- config_name: screen2words
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 7830546896.489
    num_examples: 15671
  download_size: 7936165490
  dataset_size: 7830546896.489
- config_name: screen_qa
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 38891079094
    num_examples: 70259
  download_size: 39225949157
  dataset_size: 38891079094
- config_name: sharegpt4o
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 58038246861.95
    num_examples: 129950
  download_size: 107983767737
  dataset_size: 58038246861.95
- config_name: sharegpt4v
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 140514506066.246
    num_examples: 284071
  download_size: 230767689
  dataset_size: 140514506066.246
- config_name: sharegpt4v-part-00-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 14039520193.808
    num_examples: 28408
  download_size: 13734095363
  dataset_size: 14039520193.808
- config_name: sharegpt4v-part-01-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 13690633306.56
    num_examples: 28408
  download_size: 13669991119
  dataset_size: 13690633306.56
- config_name: sharegpt4v-part-03-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 127133391319.312
    num_examples: 28408
  download_size: 43578816305
  dataset_size: 127133391319.312
- config_name: sharegpt4v-part-04-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 24275450242.736
    num_examples: 28408
  download_size: 23194057019
  dataset_size: 24275450242.736
- config_name: sharegpt4v-part-05-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 23860191838.024
    num_examples: 28408
  download_size: 23202477534
  dataset_size: 23860191838.024
- config_name: sharegpt4v-part-06-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 27048694321.664
    num_examples: 28408
  download_size: 23695049814
  dataset_size: 27048694321.664
- config_name: sharegpt4v-part-07-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 23548832003.344
    num_examples: 28408
  download_size: 23004745854
  dataset_size: 23548832003.344
- config_name: sharegpt4v-part-08-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 23195686207.504
    num_examples: 28408
  download_size: 23620913873
  dataset_size: 23195686207.504
- config_name: sharegpt4v-part-09-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 25416236372.479
    num_examples: 28403
  download_size: 23189502194
  dataset_size: 25416236372.479
- config_name: sharegpt4v-part00-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 14039520193.808
    num_examples: 28408
  download_size: 13734095363
  dataset_size: 14039520193.808
- config_name: sherlock
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 29751472629
    num_examples: 24458
  download_size: 30203972683
  dataset_size: 29751472629
- config_name: sroie_data
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 471547064.464
    num_examples: 31896
  download_size: 364650461
  dataset_size: 471547064.464
- config_name: st_vqa
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 10370605731.012
    num_examples: 32307
  download_size: 6414105649
  dataset_size: 10370605731.012
- config_name: svit
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: markdown
      struct:
      - name: answer
        dtype: string
      - name: index
        dtype: int64
      - name: type
        dtype: string
    - name: role
      dtype: string
    - name: text
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 412866691612.1
    num_examples: 985150
  download_size: 882323354
  dataset_size: 412866691612.1
- config_name: svit-part-00-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 41271243292.404
    num_examples: 98516
  download_size: 40219528409
  dataset_size: 41271243292.404
- config_name: svit-part-01-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 40628728678.616
    num_examples: 98516
  download_size: 40226311473
  dataset_size: 40628728678.616
- config_name: svit-part-02-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 39965254629.784
    num_examples: 98516
  download_size: 40495504546
  dataset_size: 39965254629.784
- config_name: svit-part-03-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 39804403002.192
    num_examples: 98516
  download_size: 40321883508
  dataset_size: 39804403002.192
- config_name: svit-part-04-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 39955428466.836
    num_examples: 98516
  download_size: 40143817556
  dataset_size: 39955428466.836
- config_name: svit-part-05-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 39787055506.9
    num_examples: 98516
  download_size: 40300026539
  dataset_size: 39787055506.9
- config_name: svit-part-06-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 41548198311.056
    num_examples: 98516
  download_size: 40398793049
  dataset_size: 41548198311.056
- config_name: svit-part-07-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 41368037432.648
    num_examples: 98516
  download_size: 40262535103
  dataset_size: 41368037432.648
- config_name: svit-part-08-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 39486144999.656
    num_examples: 98516
  download_size: 40221627701
  dataset_size: 39486144999.656
- config_name: svit-part-09-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: markdown
      struct:
      - name: answer
        dtype: string
      - name: index
        dtype: int64
      - name: type
        dtype: string
    - name: role
      dtype: string
    - name: text
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 40612909205.934
    num_examples: 98506
  download_size: 31385134697
  dataset_size: 40612909205.934
- config_name: synthetic_amc
  features:
  - name: id
    dtype: string
  - name: image
    dtype: 'null'
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 29900484
    num_examples: 18880
  download_size: 13911418
  dataset_size: 29900484
- config_name: synthetic_math
  features:
  - name: id
    dtype: string
  - name: image
    dtype: 'null'
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 51706271
    num_examples: 50627
  download_size: 25142226
  dataset_size: 51706271
- config_name: tabmwp
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 773891968.048
    num_examples: 56071
  download_size: 672979510
  dataset_size: 773891968.048
- config_name: tallyqa
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 30083195186.148
    num_examples: 107956
  download_size: 38460229500
  dataset_size: 30083195186.148
- config_name: tat_qa
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 64582960.025
    num_examples: 1775
  download_size: 52783158
  dataset_size: 64582960.025
- config_name: textcaps
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 20750113282.244
    num_examples: 21877
  download_size: 20889696339
  dataset_size: 20750113282.244
- config_name: textocr_gpt4v
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 23813455332.93
    num_examples: 25105
  download_size: 24092140406
  dataset_size: 23813455332.93
- config_name: textvqa
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 7962031457.336
    num_examples: 8448
  download_size: 7954832216
  dataset_size: 7962031457.336
- config_name: tinychart_train
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 41863132899
    num_examples: 1097422
  download_size: 39993177847
  dataset_size: 41863132899
- config_name: tqa
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 29574615138.067
    num_examples: 107227
  download_size: 4171860605
  dataset_size: 29574615138.067
- config_name: unigeo
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 62849444.296
    num_examples: 18819
  download_size: 44704306
  dataset_size: 62849444.296
- config_name: ureader_cap
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 88136562217.955
    num_examples: 91093
  download_size: 23086313842
  dataset_size: 88136562217.955
- config_name: ureader_chart
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
    - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 347403734227
    num_examples: 420743
  download_size: 316981785581
  dataset_size: 347403734227
- config_name: ureader_ie
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 26368965923.26
    num_examples: 17319
  download_size: 2187417596
  dataset_size: 26368965923.26
- config_name: ureader_kg
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 1605196057.92
    num_examples: 37456
  download_size: 23379814801
  dataset_size: 1605196057.92
- config_name: ureader_ocr
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
    - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 771784316
    num_examples: 2678
  download_size: 810930850
  dataset_size: 771784316
- config_name: ureader_qa
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 9027585394.73
    num_examples: 252261
  download_size: 51297272985
  dataset_size: 9027585394.73
- config_name: ureader_tr
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 4474536847.85
    num_examples: 101650
  download_size: 50671978038
  dataset_size: 4474536847.85
- config_name: vflan
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 127765452850
    num_examples: 446478
  download_size: 126458571884
  dataset_size: 127765452850
- config_name: vg
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 30133447961
    num_examples: 138045
  download_size: 32162939641
  dataset_size: 30133447961
- config_name: viquae
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 1548451954
    num_examples: 4125
  download_size: 1508422297
  dataset_size: 1548451954
- config_name: vision_flan
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 184782700755.246
    num_examples: 350501
  download_size: 202997338364
  dataset_size: 184782700755.246
- config_name: vision_oritented
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 11445962334.048
    num_examples: 14262
  download_size: 11440441829
  dataset_size: 11445962334.048
- config_name: vistext
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 741324150.015
    num_examples: 15447
  download_size: 654625212
  dataset_size: 741324150.015
- config_name: visual7w
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 14799948781.96
    num_examples: 46687
  download_size: 9234819909
  dataset_size: 14799948781.96
- config_name: visual_chat
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 12412930372.966
    num_examples: 25903
  download_size: 12516565601
  dataset_size: 12412930372.966
- config_name: visualmrc
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 4244740956.188
    num_examples: 4937
  download_size: 3219841899
  dataset_size: 4244740956.188
- config_name: vqaas
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 776388545.417
    num_examples: 5871
  download_size: 428930056
  dataset_size: 776388545.417
- config_name: vqarad
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 825686605.385
    num_examples: 2689
  download_size: 555969205
  dataset_size: 825686605.385
- config_name: vsr
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 1580161090.709
    num_examples: 3797
  download_size: 891291791
  dataset_size: 1580161090.709
- config_name: websight
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: from
      dtype: string
    - name: role
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 29314197773.207
    num_examples: 27843
  download_size: 11171367961
  dataset_size: 29314197773.207
- config_name: wikipedia_2m
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 244741655497.413
    num_examples: 2011747
  download_size: 236095636009
  dataset_size: 244741655497.413
- config_name: wit
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 2005071025670.971
    num_examples: 646469
  download_size: 506241392
  dataset_size: 2005071025670.971
- config_name: wit-part-00-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 203145510812.452
    num_examples: 64748
  download_size: 205290145540
  dataset_size: 203145510812.452
- config_name: wit-part-01-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 213346193670.336
    num_examples: 64748
  download_size: 205264195909
  dataset_size: 213346193670.336
- config_name: wit-part-02-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 213970168742.412
    num_examples: 64748
  download_size: 206250848673
  dataset_size: 213970168742.412
- config_name: wit-part-03-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 198383971514.34
    num_examples: 64748
  download_size: 203833763772
  dataset_size: 198383971514.34
- config_name: wit-part-04-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 215635292929.132
    num_examples: 64748
  download_size: 203816141214
  dataset_size: 215635292929.132
- config_name: wit-part-05-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 205964472243.008
    num_examples: 64748
  download_size: 205286161365
  dataset_size: 205964472243.008
- config_name: wit-part-06-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 207424370885.66
    num_examples: 64748
  download_size: 204190018042
  dataset_size: 207424370885.66
- config_name: wit-part-07-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 207103011400.52
    num_examples: 64748
  download_size: 205783157576
  dataset_size: 207103011400.52
- config_name: wit-part-08-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 190622336831.356
    num_examples: 64748
  download_size: 207835409946
  dataset_size: 190622336831.356
- config_name: wit-part-09-of-10
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 203203439242.876
    num_examples: 64742
  download_size: 204798886312
  dataset_size: 203203439242.876
- config_name: wizardlm
  features:
  - name: id
    dtype: string
  - name: image
    dtype: 'null'
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 102455708
    num_examples: 43068
  download_size: 49004111
  dataset_size: 102455708
---

# LLaVA-OneVision-1.5 Instruction Data

[Paper](https://huggingface.co/papers/2509.23661) | [Code](https://github.com/EvolvingLMMs-Lab/LLaVA-OneVision-1.5)

## 📌 Introduction
This dataset, **LLaVA-OneVision-1.5-Instruct**, was collected and integrated during the development of LLaVA-OneVision-1.5. LLaVA-OneVision-1.5 is a novel family of Large Multimodal Models (LMMs) that achieve state-of-the-art performance with significantly reduced computational and financial costs. This meticulously curated 22M instruction dataset (LLaVA-OneVision-1.5-Instruct) is part of a comprehensive and fully open framework for building high-quality vision-language models entirely from scratch.

It has significantly enhanced the performance of Vision-Language Models (VLMs) in structured information processing and knowledge-based question answering tasks.
As part of the LLaVA-OneVision-1.5 open-source initiative, we are releasing this dataset to the community in the hope of advancing VLM research and driving further progress in the field.

## ⚙️ Usage Notes
Although the dataset itself is of high quality, we recommend deduplicating and combining it with the FineVision dataset to achieve better training results.

## 🚀 Sample Usage

Below is a quick start guide demonstrating how to use the LLaVA-OneVision-1.5 models with Hugging Face `transformers` for inference. This snippet is directly from the project's GitHub repository.

```python
from transformers import AutoTokenizer, AutoProcessor, AutoModelForCausalLM
from qwen_vl_utils import process_vision_info
model_path = "lmms-lab/LLaVA-One-Vision-1.5-8B-Instruct"

# default: Load the model on the available device(s)
model = AutoModelForCausalLM.from_pretrained(
    model_path, torch_dtype="auto", device_map="auto", trust_remote_code=True
)

# default processer
processor = AutoProcessor.from_pretrained(model_path, trust_remote_code=True)

messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "image",
                "image": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-VL/assets/demo.jpeg",
            },
            {"type": "text", "text": "Describe this image."},
        ],
    }
]

# Preparation for inference
text = processor.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True
)
image_inputs, video_inputs = process_vision_info(messages)
inputs = processor(
    text=[text],
    images=image_inputs,
    videos=video_inputs,
    padding=True,
    return_tensors="pt",
)
inputs = inputs.to("cuda")

# Inference: Generation of the output
generated_ids = model.generate(**inputs, max_new_tokens=1024)
generated_ids_trimmed = [
    out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
]
output_text = processor.batch_decode(
    generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
)
print(output_text)
```

## 📊 Data Analysis
### Distribution of Data Categories

<p align="center">
  <img src="https://cdn-uploads.huggingface.co/production/uploads/655c70d331c4978366d4b2e6/2xoRKPrNZsgK2YqbwVLCs.png"
       width="512" height="512" alt="sft_dataset_pie_chart">
</p>

### Compare and Scaling with FineVision
Performance comparison of three datasets (Merge46M, FineVision, and LLaVA-OneVision-1.5-Inst-Data) across 16 benchmarks during the SFT phase, demonstrating the superiority of Merge46M on most benchmarks.

![ablation_instruct](https://cdn-uploads.huggingface.co/production/uploads/655c70d331c4978366d4b2e6/E2Px27arJ3J-LXZLgAUDN.jpeg)

## 🙏 Acknowledgement
We would like to acknowledge the contributions of **[FineVision](https://huggingface.co/spaces/HuggingFaceM4/FineVision)** , whose open dataset served as an important foundation and benchmark for building this SFT dataset.

## 📜 Cite
If you find *LLaVA-OneVision-1.5* useful in your research, please consider to cite the following related papers:

```bibtex
@inproceedings{LLaVA-OneVision-1.5,
  title={LLaVA-OneVision-1.5: Fully Open Framework for Democratized Multimodal Training},
  author={An, Xiang and Xie, Yin and Yang, Kaicheng and Zhang, Wenkang and Zhao, Xiuwei and Cheng, Zheng and Wang, Yirui and Xu, Songcen and Chen, Changrui and Wu, Chunsheng and Huajie Tan and Li, Chunyuan and Jing Yang and Jie Yu and Xiyao Wang and Bin Qin and Yumeng Wang and Zizhen Yan and Ziyong Feng and Ziwei Liu and Bo Li and Jiankang Deng},
  booktitle={arxiv},  
  year={2025},
  url={https://arxiv.org/abs/2509.23661}, 
 }

@inproceedings{xie2025region,
  title={Region-based Cluster Discrimination for Visual Representation Learning},
  author={Xie, Yin and Yang, Kaicheng and An, Xiang and Wu, Kun and Zhao, Yongle and Deng, Weimo and Ran, Zimin and Wang, Yumeng and Feng, Ziyong and Miles, Roy and Elezi, Ismail and Deng, Jiankang},
  booktitle={ICCV},
  year={2025}
}

@article{lillava,
  title={LLaVA-OneVision: Easy Visual Task Transfer},
  author={Li, Bo and Zhang, Yuanhan and Guo, Dong and Zhang, Renrui and Li, Feng and Zhang, Hao and Zhang, Kaichen and Zhang, Peiyuan and Li, Yanwei and Liu, Ziwei and Li, Chunyuan},
  journal={Transactions on Machine Learning Research},
  year={2024}
}
```