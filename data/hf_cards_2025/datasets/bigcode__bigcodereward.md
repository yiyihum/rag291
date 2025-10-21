---
license: bigcode-openrail-m
task_categories:
- text-generation
- text-ranking
language:
- en
tags:
- code-generation
- code-evaluation
- human-preferences
- elo-rating
- reward-modeling
- llm-evaluation
- multilingual
dataset_info:
  features:
  - name: chat_session_id
    dtype: string
  - name: instruction
    dtype: string
  - name: human_vote
    dtype: string
  - name: model_A
    dtype: string
  - name: model_B
    dtype: string
  - name: category_id
    dtype: int64
  - name: category_name
    dtype: string
  - name: execution_screenshot_A
    dtype: image
  - name: execution_output_A
    dtype: string
  - name: execution_error_A
    dtype: string
  - name: execution_screenshot_B
    dtype: image
  - name: execution_output_B
    dtype: string
  - name: execution_error_B
    dtype: string
  - name: states
    struct:
    - name: model_A
      struct:
      - name: chat_mode
        dtype: string
      - name: chat_session_id
        dtype: string
      - name: chat_start_time
        dtype: string
      - name: conv_id
        dtype: string
      - name: messages
        sequence:
          sequence: string
      - name: model_name
        dtype: string
      - name: offset
        dtype: int64
      - name: roles
        sequence: string
      - name: sandbox_logs_by_round
        struct:
        - name: '1'
          struct:
          - name: enabled_round
            dtype: int64
          - name: filename
            dtype: string
          - name: sandbox_run_round
            dtype: int64
          - name: sandbox_state
            struct:
            - name: auto_selected_sandbox_environment
              dtype: string
            - name: btn_list_length
              dtype: int64
            - name: chat_session_id
              dtype: string
            - name: code_dependencies
              sequence:
                sequence: string
            - name: code_language
              dtype: string
            - name: code_to_execute
              dtype: string
            - name: conv_id
              dtype: string
            - name: edit_round
              dtype: int64
            - name: enable_sandbox
              dtype: bool
            - name: enabled_round
              dtype: int64
            - name: execution_success
              dtype: bool
            - name: sandbox_environment
              dtype: string
            - name: sandbox_error
              dtype: string
            - name: sandbox_id
              dtype: string
            - name: sandbox_instruction
              dtype: string
            - name: sandbox_output
              dtype: string
            - name: sandbox_run_round
              dtype: int64
            - name: screenshot_base64
              dtype: string
            - name: screenshot_path
              dtype: string
          - name: user_interaction_records
            list:
            - name: height
              dtype: float64
            - name: key
              dtype: string
            - name: scrollLeft
              dtype: float64
            - name: scrollTop
              dtype: float64
            - name: time
              dtype: string
            - name: type
              dtype: string
            - name: width
              dtype: float64
            - name: x
              dtype: float64
            - name: y
              dtype: float64
        - name: '2'
          struct:
          - name: enabled_round
            dtype: int64
          - name: filename
            dtype: string
          - name: sandbox_run_round
            dtype: int64
          - name: sandbox_state
            struct:
            - name: auto_selected_sandbox_environment
              dtype: string
            - name: btn_list_length
              dtype: int64
            - name: chat_session_id
              dtype: string
            - name: code_dependencies
              sequence:
                sequence: string
            - name: code_language
              dtype: string
            - name: code_to_execute
              dtype: string
            - name: conv_id
              dtype: string
            - name: edit_round
              dtype: int64
            - name: enable_sandbox
              dtype: bool
            - name: enabled_round
              dtype: int64
            - name: execution_success
              dtype: bool
            - name: sandbox_environment
              dtype: string
            - name: sandbox_error
              dtype: string
            - name: sandbox_id
              dtype: string
            - name: sandbox_instruction
              dtype: string
            - name: sandbox_output
              dtype: string
            - name: sandbox_run_round
              dtype: int64
            - name: screenshot_base64
              dtype: string
            - name: screenshot_path
              dtype: string
          - name: user_interaction_records
            list:
            - name: height
              dtype: float64
            - name: key
              dtype: string
            - name: scrollLeft
              dtype: float64
            - name: scrollTop
              dtype: float64
            - name: time
              dtype: string
            - name: type
              dtype: string
            - name: width
              dtype: float64
            - name: x
              dtype: float64
            - name: y
              dtype: float64
        - name: '3'
          struct:
          - name: enabled_round
            dtype: int64
          - name: filename
            dtype: string
          - name: sandbox_run_round
            dtype: int64
          - name: sandbox_state
            struct:
            - name: auto_selected_sandbox_environment
              dtype: string
            - name: btn_list_length
              dtype: int64
            - name: chat_session_id
              dtype: string
            - name: code_dependencies
              sequence:
                sequence: string
            - name: code_language
              dtype: string
            - name: code_to_execute
              dtype: string
            - name: conv_id
              dtype: string
            - name: edit_round
              dtype: int64
            - name: enable_sandbox
              dtype: bool
            - name: enabled_round
              dtype: int64
            - name: execution_success
              dtype: bool
            - name: sandbox_environment
              dtype: string
            - name: sandbox_error
              dtype: string
            - name: sandbox_id
              dtype: string
            - name: sandbox_instruction
              dtype: string
            - name: sandbox_output
              dtype: string
            - name: sandbox_run_round
              dtype: int64
            - name: screenshot_base64
              dtype: string
            - name: screenshot_path
              dtype: string
          - name: user_interaction_records
            list:
            - name: height
              dtype: float64
            - name: key
              dtype: string
            - name: scrollLeft
              dtype: float64
            - name: scrollTop
              dtype: float64
            - name: time
              dtype: string
            - name: type
              dtype: string
            - name: width
              dtype: float64
            - name: x
              dtype: float64
            - name: y
              dtype: float64
        - name: '4'
          struct:
          - name: enabled_round
            dtype: int64
          - name: filename
            dtype: string
          - name: sandbox_run_round
            dtype: int64
          - name: sandbox_state
            struct:
            - name: auto_selected_sandbox_environment
              dtype: string
            - name: btn_list_length
              dtype: int64
            - name: chat_session_id
              dtype: string
            - name: code_dependencies
              sequence:
                sequence: string
            - name: code_language
              dtype: string
            - name: code_to_execute
              dtype: string
            - name: conv_id
              dtype: string
            - name: edit_round
              dtype: int64
            - name: enable_sandbox
              dtype: bool
            - name: enabled_round
              dtype: int64
            - name: execution_success
              dtype: bool
            - name: sandbox_environment
              dtype: string
            - name: sandbox_error
              dtype: string
            - name: sandbox_id
              dtype: string
            - name: sandbox_instruction
              dtype: string
            - name: sandbox_output
              dtype: string
            - name: sandbox_run_round
              dtype: int64
            - name: screenshot_base64
              dtype: string
            - name: screenshot_path
              dtype: string
          - name: user_interaction_records
            list:
            - name: height
              dtype: float64
            - name: key
              dtype: string
            - name: scrollLeft
              dtype: float64
            - name: scrollTop
              dtype: float64
            - name: time
              dtype: string
            - name: type
              dtype: string
            - name: width
              dtype: float64
            - name: x
              dtype: float64
            - name: y
              dtype: float64
        - name: '5'
          struct:
          - name: enabled_round
            dtype: int64
          - name: filename
            dtype: string
          - name: sandbox_run_round
            dtype: int64
          - name: sandbox_state
            struct:
            - name: auto_selected_sandbox_environment
              dtype: string
            - name: btn_list_length
              dtype: int64
            - name: chat_session_id
              dtype: string
            - name: code_dependencies
              sequence:
                sequence: string
            - name: code_language
              dtype: string
            - name: code_to_execute
              dtype: string
            - name: conv_id
              dtype: string
            - name: edit_round
              dtype: int64
            - name: enable_sandbox
              dtype: bool
            - name: enabled_round
              dtype: int64
            - name: execution_success
              dtype: bool
            - name: sandbox_environment
              dtype: string
            - name: sandbox_error
              dtype: string
            - name: sandbox_id
              dtype: string
            - name: sandbox_instruction
              dtype: string
            - name: sandbox_output
              dtype: string
            - name: sandbox_run_round
              dtype: int64
            - name: screenshot_base64
              dtype: string
            - name: screenshot_path
              dtype: string
          - name: user_interaction_records
            list:
            - name: height
              dtype: float64
            - name: key
              dtype: string
            - name: scrollLeft
              dtype: float64
            - name: scrollTop
              dtype: float64
            - name: time
              dtype: string
            - name: type
              dtype: string
            - name: width
              dtype: float64
            - name: x
              dtype: float64
            - name: y
              dtype: float64
        - name: '6'
          struct:
          - name: enabled_round
            dtype: int64
          - name: filename
            dtype: string
          - name: sandbox_run_round
            dtype: int64
          - name: sandbox_state
            struct:
            - name: auto_selected_sandbox_environment
              dtype: string
            - name: btn_list_length
              dtype: int64
            - name: chat_session_id
              dtype: string
            - name: code_dependencies
              sequence:
                sequence: string
            - name: code_language
              dtype: string
            - name: code_to_execute
              dtype: string
            - name: conv_id
              dtype: string
            - name: edit_round
              dtype: int64
            - name: enable_sandbox
              dtype: bool
            - name: enabled_round
              dtype: int64
            - name: sandbox_environment
              dtype: string
            - name: sandbox_error
              dtype: string
            - name: sandbox_id
              dtype: string
            - name: sandbox_instruction
              dtype: string
            - name: sandbox_output
              dtype: string
            - name: sandbox_run_round
              dtype: int64
            - name: screenshot_base64
              dtype: string
            - name: screenshot_path
              dtype: string
          - name: user_interaction_records
            dtype: 'null'
        - name: '7'
          struct:
          - name: enabled_round
            dtype: int64
          - name: filename
            dtype: string
          - name: sandbox_run_round
            dtype: int64
          - name: sandbox_state
            struct:
            - name: auto_selected_sandbox_environment
              dtype: string
            - name: btn_list_length
              dtype: int64
            - name: chat_session_id
              dtype: string
            - name: code_dependencies
              sequence:
                sequence: string
            - name: code_language
              dtype: string
            - name: code_to_execute
              dtype: string
            - name: conv_id
              dtype: string
            - name: edit_round
              dtype: int64
            - name: enable_sandbox
              dtype: bool
            - name: enabled_round
              dtype: int64
            - name: execution_success
              dtype: bool
            - name: sandbox_environment
              dtype: string
            - name: sandbox_error
              dtype: string
            - name: sandbox_id
              dtype: string
            - name: sandbox_instruction
              dtype: string
            - name: sandbox_output
              dtype: string
            - name: sandbox_run_round
              dtype: int64
            - name: screenshot_base64
              dtype: string
            - name: screenshot_path
              dtype: string
          - name: user_interaction_records
            dtype: 'null'
      - name: system_message
        dtype: string
      - name: template_name
        dtype: string
      - name: total_rounds
        dtype: int64
    - name: model_B
      struct:
      - name: chat_mode
        dtype: string
      - name: chat_session_id
        dtype: string
      - name: chat_start_time
        dtype: string
      - name: conv_id
        dtype: string
      - name: messages
        sequence:
          sequence: string
      - name: model_name
        dtype: string
      - name: offset
        dtype: int64
      - name: roles
        sequence: string
      - name: sandbox_logs_by_round
        struct:
        - name: '1'
          struct:
          - name: enabled_round
            dtype: int64
          - name: filename
            dtype: string
          - name: sandbox_run_round
            dtype: int64
          - name: sandbox_state
            struct:
            - name: auto_selected_sandbox_environment
              dtype: string
            - name: btn_list_length
              dtype: int64
            - name: chat_session_id
              dtype: string
            - name: code_dependencies
              sequence:
                sequence: string
            - name: code_language
              dtype: string
            - name: code_to_execute
              dtype: string
            - name: conv_id
              dtype: string
            - name: edit_round
              dtype: int64
            - name: enable_sandbox
              dtype: bool
            - name: enabled_round
              dtype: int64
            - name: execution_success
              dtype: bool
            - name: sandbox_environment
              dtype: string
            - name: sandbox_error
              dtype: string
            - name: sandbox_id
              dtype: string
            - name: sandbox_instruction
              dtype: string
            - name: sandbox_output
              dtype: string
            - name: sandbox_run_round
              dtype: int64
            - name: screenshot_base64
              dtype: string
            - name: screenshot_path
              dtype: string
          - name: user_interaction_records
            list:
            - name: height
              dtype: float64
            - name: key
              dtype: string
            - name: scrollLeft
              dtype: float64
            - name: scrollTop
              dtype: float64
            - name: time
              dtype: string
            - name: type
              dtype: string
            - name: width
              dtype: float64
            - name: x
              dtype: float64
            - name: y
              dtype: float64
        - name: '2'
          struct:
          - name: enabled_round
            dtype: int64
          - name: filename
            dtype: string
          - name: sandbox_run_round
            dtype: int64
          - name: sandbox_state
            struct:
            - name: auto_selected_sandbox_environment
              dtype: string
            - name: btn_list_length
              dtype: int64
            - name: chat_session_id
              dtype: string
            - name: code_dependencies
              sequence:
                sequence: string
            - name: code_language
              dtype: string
            - name: code_to_execute
              dtype: string
            - name: conv_id
              dtype: string
            - name: edit_round
              dtype: int64
            - name: enable_sandbox
              dtype: bool
            - name: enabled_round
              dtype: int64
            - name: execution_success
              dtype: bool
            - name: sandbox_environment
              dtype: string
            - name: sandbox_error
              dtype: string
            - name: sandbox_id
              dtype: string
            - name: sandbox_instruction
              dtype: string
            - name: sandbox_output
              dtype: string
            - name: sandbox_run_round
              dtype: int64
            - name: screenshot_base64
              dtype: string
            - name: screenshot_path
              dtype: string
          - name: user_interaction_records
            list:
            - name: height
              dtype: float64
            - name: key
              dtype: string
            - name: scrollLeft
              dtype: float64
            - name: scrollTop
              dtype: float64
            - name: time
              dtype: string
            - name: type
              dtype: string
            - name: width
              dtype: float64
            - name: x
              dtype: float64
            - name: y
              dtype: float64
        - name: '3'
          struct:
          - name: enabled_round
            dtype: int64
          - name: filename
            dtype: string
          - name: sandbox_run_round
            dtype: int64
          - name: sandbox_state
            struct:
            - name: auto_selected_sandbox_environment
              dtype: string
            - name: btn_list_length
              dtype: int64
            - name: chat_session_id
              dtype: string
            - name: code_dependencies
              sequence:
                sequence: string
            - name: code_language
              dtype: string
            - name: code_to_execute
              dtype: string
            - name: conv_id
              dtype: string
            - name: edit_round
              dtype: int64
            - name: enable_sandbox
              dtype: bool
            - name: enabled_round
              dtype: int64
            - name: execution_success
              dtype: bool
            - name: sandbox_environment
              dtype: string
            - name: sandbox_error
              dtype: string
            - name: sandbox_id
              dtype: string
            - name: sandbox_instruction
              dtype: string
            - name: sandbox_output
              dtype: string
            - name: sandbox_run_round
              dtype: int64
            - name: screenshot_base64
              dtype: string
            - name: screenshot_path
              dtype: string
          - name: user_interaction_records
            list:
            - name: height
              dtype: float64
            - name: key
              dtype: string
            - name: scrollLeft
              dtype: float64
            - name: scrollTop
              dtype: float64
            - name: time
              dtype: string
            - name: type
              dtype: string
            - name: width
              dtype: float64
            - name: x
              dtype: float64
            - name: y
              dtype: float64
        - name: '4'
          struct:
          - name: enabled_round
            dtype: int64
          - name: filename
            dtype: string
          - name: sandbox_run_round
            dtype: int64
          - name: sandbox_state
            struct:
            - name: auto_selected_sandbox_environment
              dtype: string
            - name: btn_list_length
              dtype: int64
            - name: chat_session_id
              dtype: string
            - name: code_dependencies
              sequence:
                sequence: string
            - name: code_language
              dtype: string
            - name: code_to_execute
              dtype: string
            - name: conv_id
              dtype: string
            - name: edit_round
              dtype: int64
            - name: enable_sandbox
              dtype: bool
            - name: enabled_round
              dtype: int64
            - name: execution_success
              dtype: bool
            - name: sandbox_environment
              dtype: string
            - name: sandbox_error
              dtype: string
            - name: sandbox_id
              dtype: string
            - name: sandbox_instruction
              dtype: string
            - name: sandbox_output
              dtype: string
            - name: sandbox_run_round
              dtype: int64
            - name: screenshot_base64
              dtype: string
            - name: screenshot_path
              dtype: string
          - name: user_interaction_records
            list:
            - name: height
              dtype: float64
            - name: key
              dtype: string
            - name: scrollLeft
              dtype: float64
            - name: scrollTop
              dtype: float64
            - name: time
              dtype: string
            - name: type
              dtype: string
            - name: width
              dtype: float64
            - name: x
              dtype: float64
            - name: y
              dtype: float64
        - name: '5'
          struct:
          - name: enabled_round
            dtype: int64
          - name: filename
            dtype: string
          - name: sandbox_run_round
            dtype: int64
          - name: sandbox_state
            struct:
            - name: auto_selected_sandbox_environment
              dtype: string
            - name: btn_list_length
              dtype: int64
            - name: chat_session_id
              dtype: string
            - name: code_dependencies
              sequence:
                sequence: string
            - name: code_language
              dtype: string
            - name: code_to_execute
              dtype: string
            - name: conv_id
              dtype: string
            - name: edit_round
              dtype: int64
            - name: enable_sandbox
              dtype: bool
            - name: enabled_round
              dtype: int64
            - name: execution_success
              dtype: bool
            - name: sandbox_environment
              dtype: string
            - name: sandbox_error
              dtype: string
            - name: sandbox_id
              dtype: string
            - name: sandbox_instruction
              dtype: string
            - name: sandbox_output
              dtype: string
            - name: sandbox_run_round
              dtype: int64
            - name: screenshot_base64
              dtype: string
            - name: screenshot_path
              dtype: string
          - name: user_interaction_records
            list:
            - name: height
              dtype: float64
            - name: key
              dtype: string
            - name: scrollLeft
              dtype: float64
            - name: scrollTop
              dtype: float64
            - name: time
              dtype: string
            - name: type
              dtype: string
            - name: width
              dtype: float64
            - name: x
              dtype: float64
            - name: y
              dtype: float64
        - name: '6'
          struct:
          - name: enabled_round
            dtype: int64
          - name: filename
            dtype: string
          - name: sandbox_run_round
            dtype: int64
          - name: sandbox_state
            struct:
            - name: auto_selected_sandbox_environment
              dtype: string
            - name: btn_list_length
              dtype: int64
            - name: chat_session_id
              dtype: string
            - name: code_dependencies
              sequence:
                sequence: string
            - name: code_language
              dtype: string
            - name: code_to_execute
              dtype: string
            - name: conv_id
              dtype: string
            - name: edit_round
              dtype: int64
            - name: enable_sandbox
              dtype: bool
            - name: enabled_round
              dtype: int64
            - name: execution_success
              dtype: bool
            - name: sandbox_environment
              dtype: string
            - name: sandbox_error
              dtype: string
            - name: sandbox_id
              dtype: string
            - name: sandbox_instruction
              dtype: string
            - name: sandbox_output
              dtype: string
            - name: sandbox_run_round
              dtype: int64
            - name: screenshot_base64
              dtype: string
            - name: screenshot_path
              dtype: string
          - name: user_interaction_records
            dtype: 'null'
        - name: '7'
          struct:
          - name: enabled_round
            dtype: int64
          - name: filename
            dtype: string
          - name: sandbox_run_round
            dtype: int64
          - name: sandbox_state
            struct:
            - name: auto_selected_sandbox_environment
              dtype: string
            - name: btn_list_length
              dtype: int64
            - name: chat_session_id
              dtype: string
            - name: code_dependencies
              sequence:
                sequence: string
            - name: code_language
              dtype: string
            - name: code_to_execute
              dtype: string
            - name: conv_id
              dtype: string
            - name: edit_round
              dtype: int64
            - name: enable_sandbox
              dtype: bool
            - name: enabled_round
              dtype: int64
            - name: execution_success
              dtype: bool
            - name: sandbox_environment
              dtype: string
            - name: sandbox_error
              dtype: string
            - name: sandbox_id
              dtype: string
            - name: sandbox_instruction
              dtype: string
            - name: sandbox_output
              dtype: string
            - name: sandbox_run_round
              dtype: int64
            - name: screenshot_base64
              dtype: string
            - name: screenshot_path
              dtype: string
          - name: user_interaction_records
            dtype: 'null'
        - name: '8'
          struct:
          - name: enabled_round
            dtype: int64
          - name: filename
            dtype: string
          - name: sandbox_run_round
            dtype: int64
          - name: sandbox_state
            struct:
            - name: auto_selected_sandbox_environment
              dtype: string
            - name: btn_list_length
              dtype: int64
            - name: chat_session_id
              dtype: string
            - name: code_dependencies
              sequence:
                sequence: string
            - name: code_language
              dtype: string
            - name: code_to_execute
              dtype: string
            - name: conv_id
              dtype: string
            - name: edit_round
              dtype: int64
            - name: enable_sandbox
              dtype: bool
            - name: enabled_round
              dtype: int64
            - name: execution_success
              dtype: bool
            - name: sandbox_environment
              dtype: string
            - name: sandbox_error
              dtype: string
            - name: sandbox_id
              dtype: string
            - name: sandbox_instruction
              dtype: string
            - name: sandbox_output
              dtype: string
            - name: sandbox_run_round
              dtype: int64
            - name: screenshot_base64
              dtype: string
            - name: screenshot_path
              dtype: string
          - name: user_interaction_records
            dtype: 'null'
      - name: system_message
        dtype: string
      - name: template_name
        dtype: string
      - name: total_rounds
        dtype: int64
  splits:
  - name: train
    num_bytes: 1939149578.94
    num_examples: 4731
  download_size: 1385062922
  dataset_size: 1939149578.94
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

# BigCodeArena: Unveiling More Reliable Human Preferences in Code Generation via Execution

<p align="center">
  <img src="https://raw.githubusercontent.com/bigcode-project/bigcodearena/refs/heads/main/assets/bigcodearena_banner.svg" alt="BigCodeArena" width="800">
</p>

[Paper](https://huggingface.co/papers/2510.08697) | [Code](https://github.com/bigcode-project/bigcodearena) | [Project Page (Hugging Face Space)](https://huggingface.co/spaces/bigcode/arena)

## About BigCodeArena

**BigCodeArena** is an open human evaluation platform for code generation, built on top of Chatbot Arena with a comprehensive and on-the-fly execution environment. It enables the execution of LLM-generated code and allows humans to interact with execution processes and outcomes, addressing the challenge of manually examining code quality.

This dataset contains over 14,000 raw code-centric conversation sessions across 10 widely used LLMs, spanning 10 languages and 8 types of execution environments. From these, more than 4,700 multi-turn samples with pairwise human preferences were identified. The data is used to systematically examine code understanding and generation capabilities of frontier LLMs, forming the basis for two curated benchmarks: BigCodeReward and AutoCodeArena.

## Sample Usage

This dataset is primarily used with the `BigCodeReward` framework, which evaluates reward model consistency with human preferences on code generation tasks. The following steps, extracted from the [BigCodeArena GitHub repository](https://github.com/bigcode-project/bigcodearena), provide a quick start to evaluate judge models.

First, clone the repository and install the dependencies for `BigCodeReward`:

```bash
git clone https://github.com/bigcode-project/bigcodearena.git
cd bigcodearena

# Install dependencies for BigCodeReward
cd bigcodereward
pip install -r requirements.txt
```

Next, set your API keys (e.g., for OpenAI judge models):

```bash
export OPENAI_API_KEY="sk-..."
```

Then, you can evaluate judge models and analyze consistency with human preferences:

```bash
# Ensure you are in the bigcodereward directory
# cd bigcodereward 

# Evaluate with execution results (recommended)
python eval_hf_data.py --judge-model gpt-4o --workers 8

# Evaluate code-only (without execution)
python eval_hf_data.py --judge-model gpt-4o --no-output --workers 8

# Analyze consistency with human preferences
python analyze_model_judge_results.py

# Compute ELO ratings and correlations
python analyze_elo.py
```

## Citation

If you find our dataset or project useful for your research, please cite the following paper:

```bibtex
@article{zhuo2025bigcodearena,
    title={BigCodeArena: Unveiling More Reliable Human Preferences in Code Generation via Execution},
    author={Terry Yue Zhuo, Xiaolong Jin, Hange Liu, Juyong Jiang, Tianyang Liu, Chen Gong, Bhupesh Bishnoi, Vaisakhi Mishra, Marek Suppa, Noah Ziems, Saiteja Utpala, Ming Xu, Guangyu Song, Kaixin Li, Yuhan Cao, Bo Liu, Zheng Liu, Sabina Abdurakhmanova, Wenhao Yu, Mengzhao Jia, Jihan Yao, Kenneth Hamilton, Kumar Shridhar, Minh Chien Vu, Dingmin Wang, Jiawei Liu, Zijian Wang, Qian Liu, Binyuan Hui, Meg Risdal, Ahsen Khaliq, Atin Sood, Zhenchang Xing, Wasi Uddin Ahmad, John Grundy, David Lo, Banghua Zhu, Xiaoning Du, Torsten Scholak, Leandro von Werra},
    year={2025}
}
```