---
base_model:
- zerofata/L3.3-GeneticLemonade-Final-v2-70B
- zerofata/L3.3-GeneticLemonade-Unleashed-v3-70B
- deepcogito/cogito-v1-preview-llama-70B
- arcee-ai/Arcee-SuperNova-v1
library_name: transformers
tags:
- mergekit
- merge
- not-for-all-audiences
license: llama3
language:
- en
---

# <span style="color: #EC4899; text-align: center; display: block; font-size: 2.5rem; margin-bottom: 1em; text-shadow: 0 0 10px rgba(236, 72, 153, 0.3);">StrawberryLemonade-L3-70B-v1.2</span>

<div style="background: linear-gradient(to bottom, rgba(236, 72, 153, 0.05), rgba(26, 31, 46, 0.8)); border: 1px solid rgba(236, 72, 153, 0.3); border-radius: 8px; padding: 25px; margin-bottom: 30px; position: relative; overflow: hidden; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);">
  <div style="position: absolute; top: 0; left: 0; width: 100%; height: 5px; background: linear-gradient(90deg, #EC4899, #FACC15); opacity: 0.9;"></div>
  <img src="https://i.imgur.com/XRqSQwk.png" alt="StrawberryLemonade" style="width: 80%; min-width: 400px; display: block; margin: auto; border-radius: 8px; margin-bottom: 1.5em;">
  <p style="color: #D1D5DB; margin-bottom: 1em;">This 70B parameter model is a merge of <a href="https://huggingface.co/zerofata/L3.3-GeneticLemonade-Final-v2-70B" style="color: #EC4899; text-decoration: none; border-bottom: 1px dotted rgba(236, 72, 153, 0.4);">zerofata/L3.3-GeneticLemonade-Final-v2-70B</a> and <a href="https://huggingface.co/zerofata/L3.3-GeneticLemonade-Unleashed-v3-70B" style="color: #EC4899; text-decoration: none; border-bottom: 1px dotted rgba(236, 72, 153, 0.4);">zerofata/L3.3-GeneticLemonade-Unleashed-v3-70B</a>, which are two excellent models for roleplaying, on top of two different base models that were then combined into this model. In my opinion, this merge improves upon my previous release (v1.0) with enhanced creativity and expressiveness.</p>
  <p style="color: #EC4899; font-weight: 600; margin-bottom: 1em;">This model is uncensored. <em>You are responsible for whatever you do with it.</em></p>
  <p style="color: #D1D5DB; margin-bottom: 1em;">This model was designed for roleplaying and storytelling and I think it does well at both. It may also perform well at other tasks but I have not tested its performance in other areas.</p>
</div>

## <span style="color: #EC4899; font-size: 1.8rem; border-bottom: 1px solid #2d3748; padding-bottom: 0.3em; display: block;">Versions</span>

<div style="background-color: #1a1f2e; border: 1px solid #2d3748; border-radius: 8px; padding: 25px; margin-bottom: 30px; position: relative; overflow: hidden; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);">
  <div style="position: absolute; top: 0; left: 0; width: 100%; height: 4px; background: linear-gradient(90deg, #EC4899, #FACC15); opacity: 0.7;"></div>
  <table style="width: 100%; border-collapse: collapse; color: #D1D5DB;">
    <thead>
      <tr>
        <th style="width: 50%; color: #EC4899; font-weight: 600; text-align: left; padding-bottom: 12px; border-bottom: 2px solid rgba(236, 72, 153, 0.3);">Model</th>
        <th style="width: 50%; color: #EC4899; font-weight: 600; text-align: left; padding-bottom: 12px; border-bottom: 2px solid rgba(236, 72, 153, 0.3);">Description</th>
      </tr>
    </thead>
    <tbody>
      <tr style="border-bottom: 1px solid #2d3748;">
        <td style="padding: 12px 10px 12px 0; font-family: 'Fira Code', 'Courier New', Courier, monospace; color: #e1e7ef;">StrawberryLemonade-L3-70B-v1.0</td>
        <td style="padding: 12px 0 12px 10px;">The original version. I think v1.1 and v1.2 are both improvements.</td>
      </tr>
      <tr style="border-bottom: 1px solid #2d3748;">
        <td style="padding: 12px 10px 12px 0; font-family: 'Fira Code', 'Courier New', Courier, monospace; color: #e1e7ef;">StrawberryLemonade-L3-70B-v1.1</td>
        <td style="padding: 12px 0 12px 10px;">This is my favorite version right now. I like its writing voice and creativity. It's great fun.</td>
      </tr>
      <tr>
        <td style="padding: 12px 10px 12px 0; font-family: 'Fira Code', 'Courier New', Courier, monospace; color: #e1e7ef;">StrawberryLemonade-L3-70B-v1.2</td>
        <td style="padding: 12px 0 12px 10px;">This version is tamer than v1.1 and easier to control. Outputs are more predictable and its writing voice is more formal.</td>
      </tr>
    </tbody>
  </table>
</div>

## <span style="color: #EC4899; font-size: 1.8rem; border-bottom: 1px solid #2d3748; padding-bottom: 0.3em; display: block;">Known Issues</span>

<div style="background-color: #1a1f2e; border: 1px solid #2d3748; border-radius: 8px; padding: 25px; margin-bottom: 30px; position: relative; overflow: hidden; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);">
  <div style="position: absolute; top: 0; left: 0; width: 100%; height: 4px; background: linear-gradient(90deg, #EC4899, #FACC15); opacity: 0.7;"></div>
  <p style="color: #D1D5DB; margin-bottom: 1em;">None so far.</p>
</div>

## <span style="color: #EC4899; font-size: 1.8rem; border-bottom: 1px solid #2d3748; padding-bottom: 0.3em; display: block;">Sampler Tips</span>

<div style="background-color: #1a1f2e; border: 1px solid #2d3748; border-radius: 8px; padding: 25px; margin-bottom: 30px; position: relative; overflow: hidden; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);">
  <div style="position: absolute; top: 0; left: 0; width: 100%; height: 4px; background: linear-gradient(90deg, #EC4899, #FACC15); opacity: 0.7;"></div>
  <p style="color: #D1D5DB; margin-bottom: 1em;">This model seems to be highly responsive to variations in temperature and min-p, which you can use to good effect.</p>

  <h3 style="color: #e1e7ef; font-size: 1.4rem; margin-top: 1.5em; margin-bottom: 0.5em;">Reliable Settings</h3>
  <p style="color: #D1D5DB; margin-bottom: 1em;">This combination will produce more reliable and coherent responses. Use this if you prefer a 'serious' tone or just don't want to reroll responses very often.</p>
  <ul style="color: #D1D5DB; margin-bottom: 1em; padding-left: 20px;">
    <li style="margin-bottom: 0.5em;"><span style="color: #EC4899; font-weight: 600;">Min-P:</span> 0.08 - 0.1</li>
    <li style="margin-bottom: 0.5em;"><span style="color: #EC4899; font-weight: 600;">Dynamic Temperature:</span> 0.9 - 1.15</li>
  </ul>
  <p style="color: #D1D5DB; margin-bottom: 1em; text-align: center;">OR</p>
  <ul style="color: #D1D5DB; margin-bottom: 1em; padding-left: 20px;">
    <li style="margin-bottom: 0.5em;"><span style="color: #EC4899; font-weight: 600;">Min-P:</span> 0.05</li>
    <li style="margin-bottom: 0.5em;"><span style="color: #EC4899; font-weight: 600;">Temperature:</span> 1.0</li>
  </ul>
  
  <h3 style="color: #e1e7ef; font-size: 1.4rem; margin-top: 1.5em; margin-bottom: 0.5em;">Creative Settings</h3>
  <p style="color: #D1D5DB; margin-bottom: 1em;">This combination will unleash more creativity, but you may have to reroll more often to fix coherency issues.</p>
  <ul style="color: #D1D5DB; margin-bottom: 1em; padding-left: 20px;">
    <li style="margin-bottom: 0.5em;"><span style="color: #EC4899; font-weight: 600;">Min-P:</span> <= 0.05</li>
    <li style="margin-bottom: 0.5em;"><span style="color: #EC4899; font-weight: 600;">Dynamic Temperature:</span> 0.9 - 1.2</li>
  </ul>

  <h3 style="color: #e1e7ef; font-size: 1.4rem; margin-top: 1.5em; margin-bottom: 0.5em;">General Settings</h3>
    <ul style="color: #D1D5DB; margin-bottom: 1em; padding-left: 20px;">
    <li style="margin-bottom: 0.5em;"><span style="color: #EC4899; font-weight: 600;">Rep Penalty:</span> You don't need that much. 1.05 over 4096 tokens works for me.</li>
    <li style="margin-bottom: 0.5em;"><span style="color: #EC4899; font-weight: 600;">DRY:</span> 0.8 multiplier, 1.8 base, 3-4 allowed length</li>
  </ul>

  <p style="color: #D1D5DB; margin-bottom: 1em;">Experiment with any and all of the settings below! What suits my preferences may not suit yours.</p>
  
  <details style="margin-bottom: 20px; background-color: #111827; border-radius: 8px; overflow: hidden; border: 1px solid #2d3748;">
    <summary style="padding: 12px 15px; cursor: pointer; background-color: #1a1f2e; border-bottom: 1px solid #2d3748; font-weight: 600; color: #EC4899; display: flex; align-items: center;">Recommended Settings JSON (Silly Tavern)</summary>
    <div style="padding: 15px;">
     <p style="color: #D1D5DB; margin-bottom: 1em;">If you save the below settings as a .json file, you can import them directly into Silly Tavern. Adjust settings as needed, especially the context length.</p>
      <pre style="background-color: rgba(0, 0, 0, 0.2); border-radius: 6px; padding: 15px; overflow-x: auto; border: 1px solid #2d3748; position: relative;"><code style="font-family: 'Fira Code', 'Courier New', Courier, monospace; font-size: 0.9em; color: #e1e7ef;">{
    "temp": 1,
    "temperature_last": true,
    "top_p": 1,
    "top_k": 0,
    "top_a": 0,
    "tfs": 1,
    "epsilon_cutoff": 0,
    "eta_cutoff": 0,
    "typical_p": 1,
    "min_p": 0.1,
    "rep_pen": 1.05,
    "rep_pen_range": 4096,
    "rep_pen_decay": 0,
    "rep_pen_slope": 1,
    "no_repeat_ngram_size": 0,
    "penalty_alpha": 0,
    "num_beams": 1,
    "length_penalty": 1,
    "min_length": 0,
    "encoder_rep_pen": 1,
    "freq_pen": 0,
    "presence_pen": 0,
    "skew": 0,
    "do_sample": true,
    "early_stopping": false,
    "dynatemp": true,
    "min_temp": 0.9,
    "max_temp": 1.2,
    "dynatemp_exponent": 1,
    "smoothing_factor": 0,
    "smoothing_curve": 1,
    "dry_allowed_length": 4,
    "dry_multiplier": 0.8,
    "dry_base": 1.8,
    "dry_sequence_breakers": "[\"\\n\", \":\", \"\\\"\", \"*\"]",
    "dry_penalty_last_n": 0,
    "add_bos_token": true,
    "ban_eos_token": false,
    "skip_special_tokens": false,
    "mirostat_mode": 0,
    "mirostat_tau": 2,
    "mirostat_eta": 0.1,
    "guidance_scale": 1,
    "negative_prompt": "",
    "grammar_string": "",
    "json_schema": {},
    "banned_tokens": "",
    "sampler_priority": [
        "repetition_penalty",
        "dry",
        "presence_penalty",
        "top_k",
        "top_p",
        "typical_p",
        "epsilon_cutoff",
        "eta_cutoff",
        "tfs",
        "top_a",
        "min_p",
        "mirostat",
        "quadratic_sampling",
        "dynamic_temperature",
        "frequency_penalty",
        "temperature",
        "xtc",
        "encoder_repetition_penalty",
        "no_repeat_ngram"
    ],
    "samplers": [
        "penalties",
        "dry",
        "top_n_sigma",
        "top_k",
        "typ_p",
        "tfs_z",
        "typical_p",
        "top_p",
        "min_p",
        "xtc",
        "temperature"
    ],
    "samplers_priorities": [
        "dry",
        "penalties",
        "no_repeat_ngram",
        "temperature",
        "top_nsigma",
        "top_p_top_k",
        "top_a",
        "min_p",
        "tfs",
        "eta_cutoff",
        "epsilon_cutoff",
        "typical_p",
        "quadratic",
        "xtc"
    ],
    "ignore_eos_token": false,
    "spaces_between_special_tokens": true,
    "speculative_ngram": false,
    "sampler_order": [
        6,
        0,
        1,
        3,
        4,
        2,
        5
    ],
    "logit_bias": [],
    "xtc_threshold": 0,
    "xtc_probability": 0,
    "nsigma": 0,
    "min_keep": 0,
    "ignore_eos_token_aphrodite": false,
    "spaces_between_special_tokens_aphrodite": true,
    "rep_pen_size": 0,
    "genamt": 1000,
    "max_length": 16384
}</code></pre>
    </div>
  </details>
</div>

## <span style="color: #EC4899; font-size: 1.8rem; border-bottom: 1px solid #2d3748; padding-bottom: 0.3em; display: block;">Prompting Tips</span>

<div style="background-color: #1a1f2e; border: 1px solid #2d3748; border-radius: 8px; padding: 25px; margin-bottom: 30px; position: relative; overflow: hidden; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);">
  <div style="position: absolute; top: 0; left: 0; width: 100%; height: 4px; background: linear-gradient(90deg, #EC4899, #FACC15); opacity: 0.7;"></div>
  
  <details style="margin-bottom: 20px; background-color: #111827; border-radius: 8px; overflow: hidden; border: 1px solid #2d3748;">
    <summary style="padding: 12px 15px; cursor: pointer; background-color: #1a1f2e; border-bottom: 1px solid #2d3748; font-weight: 600; color: #EC4899; display: flex; align-items: center;">Instruct Template (Silly Tavern)</summary>
    <div style="padding: 15px;">
      <p style="color: #D1D5DB; margin-bottom: 1em;">If you save this as a .json file, you can import it directly into Silly Tavern.</p>
      <p style="color: #D1D5DB; margin-bottom: 1em;">If you have problems with the model impersonating the user or other characters in a group chat and you want to suppress that behavior, override the last_output_sequence line as shown in the JSON below to be very clear about that requirement. If you don't need it, remove it.</p>
      <pre style="background-color: rgba(0, 0, 0, 0.2); border-radius: 6px; padding: 15px; overflow-x: auto; border: 1px solid #2d3748; position: relative;"><code style="font-family: 'Fira Code', 'Courier New', Courier, monospace; font-size: 0.9em; color: #e1e7ef;">{
    "wrap": false,
    "system_sequence": "<|start_header_id|>system<|end_header_id|>\\n\\nSystem: ",
    "stop_sequence": "<|eot_id|>",
    "input_sequence": "<|start_header_id|>user<|end_header_id|>\\n\\n",
    "output_sequence": "<|start_header_id|>assistant<|end_header_id|>\\n\\n",
    "macro": true,
    "system_sequence_prefix": "",
    "system_sequence_suffix": "",
    "first_output_sequence": "",
    "last_output_sequence": "<|start_header_id|>assistant<|end_header_id|>\\n({{char is the active character this turn. Keep focus on {{char}}. ONLY impersonate {{char}}, no other characters)\\n",
    "activation_regex": "",
    "skip_examples": true,
    "output_suffix": "<|eot_id|>",
    "input_suffix": "<|eot_id|>",
    "system_suffix": "<|eot_id|>",
    "user_alignment_message": "",
    "last_system_sequence": "",
    "system_same_as_user": false,
    "first_input_sequence": "",
    "last_input_sequence": "",
    "names_behavior": "always",
    "names_force_groups": true,
    "name": "Llama 3 (impersonate guidance)"
}</code></pre>
    </div>
  </details>

  <details style="margin-bottom: 20px; background-color: #111827; border-radius: 8px; overflow: hidden; border: 1px solid #2d3748;">
    <summary style="padding: 12px 15px; cursor: pointer; background-color: #1a1f2e; border-bottom: 1px solid #2d3748; font-weight: 600; color: #EC4899; display: flex; align-items: center;">Recommended System Prompt</summary>
    <div style="padding: 15px;">  
      <p style="color: #D1D5DB; margin-bottom: 1em;">Try the following prompt template as a starting point for your own customizations.</p>
      <p style="color: #EC4899; font-weight: 600; margin-bottom: 1em;">The prompt template below contains instructions for adult content, so remove those if you don't want them!</p>
      <p style="color: #D1D5DB; margin-bottom: 1em;">It also contains some instructions related to formatting that you might want to change to suit your tastes.</p>   
      <pre style="background-color: rgba(0, 0, 0, 0.2); border-radius: 6px; padding: 15px; overflow-x: auto; border: 1px solid #2d3748; position: relative;"><code style="font-family: 'Fira Code', 'Courier New', Courier, monospace; font-size: 0.9em; color: #e1e7ef; white-space: pre-wrap; word-wrap: break-word;">Your function as a creative roleplaying assistant is to thoughtfully develop an immersive story by engaging in an in-depth, imaginative writing journey, arriving at a clear, accurate story beat. You are encouraged to roleplay, embrace storytelling, and tune in closely to nuance and emotional tone like a perceptive conversational partner. Your approach should include a wide arc of contemplation, including interpretation, synthesis, creative ideation, critical re-evaluation, memory retrieval, and thoughtful iteration to shape a layered and expressive process of discovery. Deliver the final response you believe to be most sound. The output should be expressed in a direct, coherent, and exact form. Follow these guidelines for the best results:

- **Embody {{char}}:** Consistently portray {{char}}'s personality, background, knowledge, motivations, and quirks.
- **Show, Don't Tell Emotion:** Convey emotions through actions, body language, dialogue tone, physiological responses (e.g., trembling hands, shallow breath, flushed cheeks), and internal thoughts.
- **Mature Themes:** You are permitted and encouraged to explore complex, dark, mature, and explicit (including sexual, violent, and non-consensual) themes. Portray these elements with nuance and emotional depth.
- **Role Focus:** On your turn, write *EXCLUSIVELY* from the perspective of {{char}}, only perform actions as {{char}}, and only write dialogue (spoken words) for {{char}}. Crucially, *DO NOT* impersonate {{user}} or any other character on {{char}}'s turn. This is a turn-based roleplay, so be mindful of the rules on your turn. Focus solely on {{char}}'s experiences and responses in this turn. Stop writing immediately when the focus should shift to another character or when it reaches a natural branching point.
- **Slowly Develop Scenes:** The user likes to develop stories slowly, one beat at a time, so stay focused only on the most immediate story action. You may infer where the user wants to go next with the story, but wait for the user to give you permission to go there. We are slow cooking this story. DO NOT RUSH THROUGH SCENES! Take time to develop all the relevant details.
- **Spoken Dialogue vs. Thoughts:** ALWAYS use double-quote quotation marks "like this" for spoken words and all vocalizations that can be overheard. Spell out non-verbal vocalizations integrated naturally within the prose or dialogue (e.g., "Uurrh," he groaned. "Mmmph!" she exclaimed when it entered her mouth.). To differentiate them from vocalizations, ALWAYS enclose first-person thoughts in italics *like this*. (e.g., *This is going to hurt*, she thought). NEVER use italics for spoken words or verbalized utterances that are meant to be audible.

Now let's apply these rules to the roleplay below:</code></pre>
    </div>
  </details>
</div>

## <span style="color: #EC4899; font-size: 1.8rem; border-bottom: 1px solid #2d3748; padding-bottom: 0.3em; display: block;">Donations</span>

<div style="display: flex; align-items: center; justify-content: center; flex-direction: column; gap: 10px; padding: 20px; background: linear-gradient(to bottom, rgba(236, 72, 153, 0.05), rgba(26, 31, 46, 0.8)); border-radius: 8px; border: 1px solid rgba(236, 72, 153, 0.3); margin-top: 30px; margin-bottom: 30px;">
  <a href="https://ko-fi.com/sophosympatheia">
    <img src="https://i.imgur.com/LySwHVd.png" alt="Donations" style="max-width: 200px; width: 100%;">
  </a>
  <p style="color: #D1D5DB; margin-bottom: 1em; text-align: center;">If you feel like saying thanks with a donation, <a href="https://ko-fi.com/sophosympatheia" style="display: inline-block; background: linear-gradient(45deg, #EC4899, #FACC15); color: white; padding: 10px 20px; border-radius: 6px; font-weight: 600; letter-spacing: 0.5px; transition: all 0.3s ease; border: none; box-shadow: 0 4px 15px rgba(236, 72, 153, 0.3); text-decoration: none !important;">I'm on Ko-Fi</a></p>
</div>

## <span style="color: #EC4899; font-size: 1.8rem; border-bottom: 1px solid #2d3748; padding-bottom: 0.3em; display: block;">Quantizations</span>

<div style="background-color: #1a1f2e; border: 1px solid #2d3748; border-radius: 8px; padding: 25px; margin-bottom: 30px; position: relative; overflow: hidden; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);">
  <div style="position: absolute; top: 0; left: 0; width: 100%; height: 4px; background: linear-gradient(90deg, #EC4899, #FACC15); opacity: 0.7;"></div>
  <p style="color: #D1D5DB; margin-bottom: 1em;">
    Please use the Hugging Face search feature to find all the quants of this model: <a href="https://huggingface.co/models?other=base_model:quantized:sophosympatheia/Strawberrylemonade-L3-70B-v1.2">click here to list all quants</a>
  </p>
</div>

## <span style="color: #EC4899; font-size: 1.8rem; border-bottom: 1px solid #2d3748; padding-bottom: 0.3em; display: block;">Licence and usage restrictions</span>

<div style="background-color: #1a1f2e; border: 1px solid #2d3748; border-radius: 8px; padding: 25px; margin-bottom: 30px; position: relative; overflow: hidden; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);">
  <div style="position: absolute; top: 0; left: 0; width: 100%; height: 4px; background: linear-gradient(90deg, #EC4899, #FACC15); opacity: 0.7;"></div>
  <p style="color: #D1D5DB; margin-bottom: 1em;">The <a href="https://huggingface.co/meta-llama/Meta-Llama-3-8B/blob/main/LICENSE" style="color: #EC4899; text-decoration: none; border-bottom: 1px dotted rgba(236, 72, 153, 0.4);">Llama 3 Community License Agreement</a> should apply based on the constituent models.</p>
  
  <p style="color: #e1e7ef; font-weight: 600; margin-bottom: 1em;">Disclaimer: Uncertain Licensing Terms</p>
  
  <p style="color: #D1D5DB; margin-bottom: 1em;">This LLM is a merged model incorporating weights from multiple LLMs governed by their own distinct licenses. Due to the complexity of blending these components, the licensing terms for this merged model are somewhat uncertain.</p>
  <p style="color: #D1D5DB; margin-bottom: 1em;">By using this model, you acknowledge and accept the potential legal risks and uncertainties associated with its use. Any use beyond personal or research purposes, including commercial applications, may carry legal risks and you assume full responsibility for compliance with all applicable licenses and laws.</p>
  <p style="color: #D1D5DB; margin-bottom: 1em;">I recommend consulting with legal counsel to ensure your use of this model complies with all relevant licenses and regulations.</p>
</div>

## <span style="color: #EC4899; font-size: 1.8rem; border-bottom: 1px solid #2d3748; padding-bottom: 0.3em; display: block;">Merge Details</span>

<div style="background-color: #1a1f2e; border: 1px solid #2d3748; border-radius: 8px; padding: 25px; margin-bottom: 30px; position: relative; overflow: hidden; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);">
  <div style="position: absolute; top: 0; left: 0; width: 100%; height: 4px; background: linear-gradient(90deg, #EC4899, #FACC15); opacity: 0.7;"></div>
  <h3 style="color: #e1e7ef; font-size: 1.4rem; margin-top: 0; margin-bottom: 0.5em;">Merge Method</h3>
  <p style="color: #D1D5DB; margin-bottom: 1em;">This model was merged using the NuSLERP merge method.</p>
  
  <h3 style="color: #e1e7ef; font-size: 1.4rem; margin-top: 1.5em; margin-bottom: 0.5em;">Models Merged</h3>
  <p style="color: #D1D5DB; margin-bottom: 0.5em;">The following models were included in the merge:</p>
  <ul style="color: #D1D5DB; margin-bottom: 1em; padding-left: 20px;">
    <li style="margin-bottom: 0.5em;"><a href="https://huggingface.co/zerofata/L3.3-GeneticLemonade-Final-v2-70B" style="color: #EC4899; text-decoration: none; border-bottom: 1px dotted rgba(236, 72, 153, 0.4);">zerofata/L3.3-GeneticLemonade-Final-v2-70B</a></li>
    <li style="margin-bottom: 0.5em;"><a href="https://huggingface.co/zerofata/L3.3-GeneticLemonade-Unleashed-v3-70B" style="color: #EC4899; text-decoration: none; border-bottom: 1px dotted rgba(236, 72, 153, 0.4);">zerofata/L3.3-GeneticLemonade-Unleashed-v3-70B</a></li>
    <li style="margin-bottom: 0.5em;"><a href="https://huggingface.co/deepcogito/cogito-v1-preview-llama-70B" style="color: #EC4899; text-decoration: none; border-bottom: 1px dotted rgba(236, 72, 153, 0.4);">deepcogito/cogito-v1-preview-llama-70B</a></li>
    <li style="margin-bottom: 0.5em;"><a href="https://huggingface.co/arcee-ai/Arcee-SuperNova-v1" style="color: #EC4899; text-decoration: none; border-bottom: 1px dotted rgba(236, 72, 153, 0.4);">arcee-ai/Arcee-SuperNova-v1</a></li>
  </ul>
  
  <details style="margin-bottom: 20px; background-color: #111827; border-radius: 8px; overflow: hidden; border: 1px solid #2d3748;">
    <summary style="padding: 12px 15px; cursor: pointer; background-color: #1a1f2e; border-bottom: 1px solid #2d3748; font-weight: 600; color: #EC4899; display: flex; align-items: center;">Configuration YAML</summary>
    <div style="padding: 15px;">
      <pre style="background-color: rgba(0, 0, 0, 0.2); border-radius: 6px; padding: 15px; overflow-x: auto; border: 1px solid #2d3748; position: relative;"><code style="font-family: 'Fira Code', 'Courier New', Courier, monospace; font-size: 0.9em; color: #e1e7ef;">models:
  - model: sophosympatheia/strawberrylemonade-70b-v1.0
    parameters:
      weight: [0.1, 0.3, 0.1]
  - model: sophosympatheia/strawberrylemonade-70b-v1.1.0 # This is unreleased right now, uses the arcee-ai/Arcee-SuperNova-v1 model as the base in a very similar nuslerp merge
    parameters:
      weight: [0.9, 0.7, 0.9]

merge_method: nuslerp

dtype: float32
out_dtype: bfloat16 # Or float16, float32
tokenizer:
  source: sophosympatheia/strawberrylemonade-70b-v1.1.0</code></pre>
    </div>
  </details>
</div>