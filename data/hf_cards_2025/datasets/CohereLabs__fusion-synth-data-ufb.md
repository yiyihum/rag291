---
language:
- en
- fr
- de
- es
- it
- pt
- ja
- ko
- zh
- ar
pretty_name: Fusion-of-N Offline Synthetic Data (UFB)
tags:
- multilingual
- synthetic
license: mit
task_categories:
- text-generation
---

# Offline Synthetic Data (UFB) for: Making, not taking, the Best-of-N

## Content
This data contains completions for a 10,000 subset of the  [UFB](https://huggingface.co/datasets/HuggingFaceH4/ultrafeedback_binarized) prompts (translated into 9 languages)  from 5 different `teacher` models and 2 aggregations:

Teachers: We sample one completion from each of the following models at temperature T=0.3. For kimik2, qwen3, and deepseek-v3 we use TogetherAI, for gemma3-27b and command-a we use locally hosted images.
  1. gemma3-27b: GEMMA3-27B-IT
  2. kimik2: KIMI-K2-INSTRUCT
  3. qwen3: QWEN3-235B
  4. deepseek-v3: DEEPSEEK-V3
  5. command-a: COMMAND A 

Aggregations:
  1. `Fusion` : The 5 teachers completions for each prompt are combined into a single response using Command-A.
  2. `BoN` : The 5 teachers completions are ranked with a Reward Model and then the highest-scoring completion is selected.


For an analysis and context of this data, check out the [paper](https://arxiv.org/abs/2510.00931).

## Format
The data is organized in Jsonlines format where each line contains all the information for a single prompt completions.

Below we explain the format for a sample entry, with annotations shown in angle brackets (< >):

```
{
  prompt: <text of this prompt>
  language_code: <Language code of this prompt>
  input_hash: <unique id generated based on the prompt text and language code>
  BoN: <A dict containing Four keys, 'completion': the selected completion for this prompt, 'score': RM score for this completion, 'selection_method': will always be `BoN` and 'teachers': commma-sperated list of all the 5 teachers used>
  Fusion: <A dict containing Four keys, 'completion': the fused completion for this prompt, 'score': RM score for this completion, 'selection_method': will always be `Fusion` and 'teachers': commma-sperated list of all the 5 teachers used>
  gemma3-27b: <A dict containing Four keys, 'completion': this teacher completion for this prompt, 'score': RM score for this completion, 'selection_method': will always be `Single` and 'teachers': the teacher name>
  kimik2:     <A dict containing Four keys, 'completion': this teacher completion for this prompt, 'score': RM score for this completion, 'selection_method': will always be `Single` and 'teachers': the teacher name>
  qwen3:      <A dict containing Four keys, 'completion': this teacher completion for this prompt, 'score': RM score for this completion, 'selection_method': will always be `Single` and 'teachers': the teacher name>
  deepseek-v3:<A dict containing Four keys, 'completion': this teacher completion for this prompt, 'score': RM score for this completion, 'selection_method': will always be `Single` and 'teachers': the teacher name>
  command-a:  <A dict containing Four keys, 'completion': this teacher completion for this prompt, 'score': RM score for this completion, 'selection_method': will always be `Single` and 'teachers': the teacher name>
}
```


## Use
You may use this data to train models, conduct analyses of model differences or evaluate other aggregation methods. 

Make sure to additionally respect the licenses of the underlying models whose outputs are included: Gemma, Kimi, Qwen, DeepSeek, Command A models.

## Citation
If you use this data for your research, please cite our work accordingly:
```
@misc{khairi2025makingtakingbestn,
      title={Making, not Taking, the Best of N}, 
      author={Ammar Khairi and Daniel D'souza and Marzieh Fadaee and Julia Kreutzer},
      year={2025},
      eprint={2510.00931},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2510.00931}, 
}
```
