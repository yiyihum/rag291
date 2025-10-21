---
license: apache-2.0
task_categories:
- text-generation
- summarization
language:
- en
tags:
- Pretraining
- Interleaved
- Reasoning
size_categories:
- 1M<n<10M
---

# Multimodal-Textbook-6.5M
<img src="./src/logo.png" alt="Image" style="width: 900px;">    


[![arXiv](https://img.shields.io/badge/arXiv-Paper-<COLOR>.svg)](https://arxiv.org/abs/2501.00958) [![Project](https://img.shields.io/badge/Project-Website-blue.svg)](https://multimodal-interleaved-textbook.github.io/) [![GitHub](https://img.shields.io/badge/GitHub-Code-181717?logo=github)](https://github.com/DAMO-NLP-SG/multimodal_textbook/tree/master)




## Overview

This dataset is for ["2.5 Years in Class: A Multimodal Textbook for Vision-Language Pretraining"](https://arxiv.org/abs/2501.00958), containing 6.5M images interleaving with 0.8B text from instructional videos.

- It contains **pre-training corpus using interleaved image-text format**. Specifically, our multimodal-textbook includes **6.5M keyframes** extracted from instructional videos, interleaving with 0.8B **ASR texts**.
- All the images and text are extracted from online instructional videos (22,000 class hours), covering multiple fundamental subjects, e.g., mathematics, physics, and chemistry. 
- Our textbook corpus providing a more coherent context and richer knowledge for image-text aligning. 
- Our code can be found in [Multimodal-Textbook](https://github.com/DAMO-NLP-SG/multimodal_textbook/tree/master).


Note: We have uploaded the annotation file （`./multimodal_textbook.json` and `multimodal_textbook_face_v1_th0.04.json`）and image folder (`./dataset_images_interval_7.tar.gz`), which contains keyframes, processed asr and ocr texts. For more details, please refer to [Using Multimodal Textbook](#using-multimodal-textbook). `multimodal_textbook_face_v1_th0.04.json` has filtered most human face images.


<img src="./src/page_fig.png" alt="Image" style="width: 900px;">  




## Visualize Our Textbook   

Due to the large size of the dataset (our complete textbook dataset is 11GB for JSON files and 0.7TB for images), we sampled 100 samples and the corresponding images and stored them in the `example_data` folder: `./example_data/textbook_sample_100.json`.

Each sample is stored in dict format as follows:
```
[
{'images':  [keyframe1, None, keyframe2, None, keyframe3, None,.....],
 'texts':   [None,      asr1,  None,      asr2, None,     asr3,.....],
 'text_ocr_list':  [None, asr1+ocr1,  None, asr2+ocr2, None, asr3+ocr3,.....],
 'metadata': [...],
 'image_num': 15,
 'text_num': 425,
 'token_num': 9065},
 ....
]
```
Just like [OBELICS](https://github.com/huggingface/OBELICS), the "images" and "texts" are arranged interleavely: 
- "Images" list contains multiple keyframes and "None", where "None" represents that the current position is text. 
- "texts" list contain multiple asr text. The position of "None" in "texts" list is image.
- "text_ocr_list": In addition to asr text, "text_ocr_list" also includes OCR text.
- "image_num", "text_num", "token_num": respectively represent the number of images, the number of asr text tokens, and the estimated total number of tokens in this sample.


To view our dataset more conveniently, we have written a jupyter notebook: `./llava/dataset/show_interleaved_dataset.ipynb`

```
cd example_data
show_interleaved_dataset.ipynb
```
In the notebook, you can see keyframes interleaving with text.


## Dataset Statistics
We utilize GPT-4o to synthesize our knowledge taxonomy with 3915 knowledge points across 6 subjects, which enabled us to automatically collect 159K English instructional videos based on this taxonomy. 

Following our video-totextbook pipeline, we filter 53% low-quality or repetitive videos and retain 75K videos (22,697 class hours) with an average duration of 18 minutes. 

Then we extract 6.5M keyframes and 0.75B text (ASR+OCR) tokens from these videos. To enhance training efficiency, we concatenate multiple video clips into a single sample, producing a total of 610K interleaved samples. Each sample contains an average of 10.7 keyframes and 1,230 text tokens. The detailed statistics for each subject are shown as follows:

<img src="./src/table.png" alt="Image" style="width: 900px;">    


## Using Multimodal Textbook
### Description of Dataset
We provide the annotation file (json file) and corresponding images folder for textbook: 
- Dataset json-file: `./multimodal_textbook.json` (600k samples ~ 11GB) and `multimodal_textbook_face_v1_th0.04.json`
- Dataset image_folder: `./dataset_images_interval_7.tar.gz` (6.5M image ~ 600GB) (**Due to its large size, we split it into 20 sub-files as `dataset_images_interval_7.tar.gz.part_00, dataset_images_interval_7.tar.gz.part_01, ...`**)
- Videometa_data: `video_meta_data/video_meta_data1.json` and `video_meta_data/video_meta_data2.json` contains the meta information of the collected videos, including video vid, title, description, duration, language, and searched knowledge points. Besides, we also provide `multimodal_textbook_meta_data.json.zip` records the textbook in its video format, not in the OBELICS format.


- Original video: You can downloaded original video using our provided video-id in `video_meta_data`.


### Learning about image_folder
After you download 20 image segmentation files (`dataset_images_interval_7.tar.gz.part_*`), you need to merge them first and then decompress. Please do not unzip a single segmentation file alone. It will lead to an error.

```
cd multimodal_textbook
cat dataset_images_interval_7.tar.gz.part_* > dataset_images_interval_7.tar.gz
tar -xzvf dataset_images_interval_7.tar.gz
```
After the above steps, you will get the image folder `dataset_images_interval_7`, which is approximately 600GB and contains 6 million keyframes. Each sub-folder in the `dataset_images_interval_7` is named with the video id. 

### Naming Rule of keyframe  

For each keyframe, its naming format rule is:   
`video id@start-time_end-time#keyframe-number.jpg`. For example, the path and file name of a keyframe is `dataset_images_interval_7/-1uixJ1V-As/-1uixJ1V-As@10.0_55.0#2.jpg`.   

This means that this image is extracted from the video (`-1uixJ1V-As`). It is the second keyframe (#2) in the video clip from 10.0 to 55.0 seconds. You can access the original video through [https://www.youtube.com/watch?v=-1uixJ1V-As](https://www.youtube.com/watch?v=-1uixJ1V-As).



### Learning about annotation file
The format of each sample in `multimodal_textbook_face_v1_th0.04.json` is as follows, that is, images and texts are interleaved: 

```
"images": [
            "/mnt/workspace/zwq_data/interleaved_dataset/dataset_images_interval_7/-1uixJ1V-As/-1uixJ1V-As@0.0_10.0#1.jpg",
            null,  
            "/mnt/workspace/zwq_data/interleaved_dataset/dataset_images_interval_7/-1uixJ1V-As/-1uixJ1V-As@10.0_55.0#6.jpg",
            null,
            ......
        ],
"texts": [
            null,
            "Hi everyone, and welcome to another lesson in our Eureka Tips for computers series .....",
            null,
            "I'm actually trying to use the number line to find the sum for each. So to start I'm going to use the paint tool to demonstrate. Let's use the number line for four plus five. We're going to start at four then we're going to count up five. One two three four five. That equals nine. Now let's do three plus six for the next one.",
            ....
        ],
```

Each sample has approximately 10.7 images and 1927 text tokens. You need to replace the each image path (`/mnt/workspace/zwq_data/interleaved_dataset/`) with your personal image folder path. 




### Learning about metadata of instructional video
The format of the `./video_meta_data/video_meta_data1.json`: 
```
    {
        "file_path": xxx,
        "file_size (MB)": 85.54160022735596,
        "file_name": "-r7-s1z3lFY.mp4",
        "video_duration": 0,
        "unique": true,
        "asr_path": xxxx,
        "asr_len": 2990,
        "caption_path": xxx,
        "caption_len": 0,
        "search_keyword": "1.3B parameter size models comparison",
        "title": "DeepSeek Coder LLM | A Revolutionary Coder Model",
        "desc": "In this video, we are going to test out Deepseek Coder, a coding LLM.....,
        "llm_response": " The video appears to be a detailed and technical analysis of DeepSeek Coder LLM..... ###Score: 10###",
        "language": "en",
        "asr is repetive": false,
        "deepseek_score": 10,
        "llama_score": 2,
        "deepseek_score long context": 10
    },
```

In addition, the `multimodal_textbook_meta_data.json.zip` records the textbook in video format. Each "video clip" is stored as a dict. Each sample includes multiple consecutive video clips from the same video. Sometimes one sample may also include video clips from different long videos. When a long video ends, it will store as `End of a Video`.

```
{'token_num': 1657,
 'conversations': [
    {
        'vid': video id-1,
        'clip_path': video id-1-clip1,
        'asr': ASR transcribed from audio,
        'extracted_frames': Extract keyframe sequences according to time intervals as [image1, image2,....].,
        'image_tokens': xxx,
        'token_num': xxx,
        'refined_asr': Refine the original ASR,
        'ocr_internvl_8b': OCR obtained using internvl_8b,
        'ocr_image': the image does OCR come from,
        'ocr_internvl_8b_deduplicates': xxx,
        'keyframe_ssim': Keyframe sequence extracted according to SSIM algorithm,
        'asr_token_num': xxx,
        'ocr_qwen2_vl_72b': '...............'
   },
   {
        'vid': video id-1,
        'clip_path': video id-1-clip2,
        'asr': ASR transcribed from audio,
        'extracted_frames': Extract keyframe sequences according to time intervals as [image3, image4,....].,
        .....
   },
   {
        'vid': 'End of a Video',
        'clip_path': xxxx,
        'image_tokens': 0,
        'token_num': 0
   },
   {
        'vid': video id-2,
        'clip_path': video id-2-clip1,
        'asr': ASR transcribed from audio,
        'extracted_frames': Extract keyframe sequences according to time intervals as [image5, image6,....].,
        ....
   },
    ....
   ]
}
```
In this example above, the first two video clips are from the same video. Then the third dict represents the end of the current video. The fourth video clip is from a new video.



## Citation

```
@article{zhang20252,
  title={2.5 Years in Class: A Multimodal Textbook for Vision-Language Pretraining},
  author={Zhang, Wenqi and Zhang, Hang and Li, Xin and Sun, Jiashuo and Shen, Yongliang and Lu, Weiming and Zhao, Deli and Zhuang, Yueting and Bing, Lidong},
  journal={arXiv preprint arXiv:2501.00958},
  year={2025}
}
```