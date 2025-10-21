---
license: apache-2.0
language:
- en
base_model:
- DavidAU/Llama-3.2-8X3B-GATED-MOE-Reasoning-Dark-Champion-Instruct-uncensored-abliterated-18.4B
tags:
- reasoning
- thinking
- uncensored
- gated
- mixture of experts
- moe
- 8x3B
- Llama 3.2 MOE
- 128k context
- creative
- creative writing
- fiction writing
- plot generation
- sub-plot generation
- fiction writing
- story generation
- scene continue
- storytelling
- fiction story
- science fiction
- romance
- all genres
- story
- writing
- vivid prosing
- vivid writing
- fiction
- roleplaying
- float32
- swearing
- rp
- horror
- mergekit
- llama-3
- llama-3.2
pipeline_tag: text-generation
---

<B><font color="red">WARNING:</font> NSFW. Vivid prose. INTENSE. Visceral Details. Light HORROR. Swearing. UNCENSORED... humor, romance, fun. </B>

<h2>Llama-3.2-8X3B-GATED-MOE-Reasoning-Dark-Champion-Instruct-uncensored-abliterated-18.4B-GGUF</h2>

<SMALL><font color="red">IMPORTANT:</font> This model has on/off/variable control reasoning from NousResearch and 
the DeepHermes model, and requires a system prompt(s) as provided to invoke reasoning/thinking. 
Please see operating instructions below for best performance.</SMALL>

<img src="dark-champ.jpg" style="float:right; width:300px; height:300px; padding:10px;">

It is a LLama 3.2 model, max context of 128k (131,000) using mixture of experts to combine EIGHT top L3.2 3B 
models into one massive powerhouse at 18.4B parameters (equal to 24B - 8 X 3B).

This model's instruction following, and output generation for creative writing, prose, fiction and role play are exceptional.

This model is also "gated", contains a master reasoning model (this can be turned on/off), was built at float32 (32 bit) precision
and quants have the output tensor at Q8_0, with a few choice quants at f16 (16 bit) and a Q8_0 with f32 (32 bit).

The "gated" strucure means the "reasoning model" is re-inforced by the other 7 models in the MOE during reasoning, and then during
output generation / non-reasoning the non-reasoning model(s) take control.

1 example generation using 2, 4 and 6 experts showing "thinking/reasoning" and output at the bottom of the page.

Also, with "gating" you can directly access/control the model(s) you want to use during instruction following and generation. This
is optional - you don't need to set this to use the model normally.

This model is the "reasoning / gated version" of this model:

[ https://huggingface.co/DavidAU/Llama-3.2-8X3B-MOE-Dark-Champion-Instruct-uncensored-abliterated-18.4B-GGUF ] 

(193 likes // 447,000+ downloads to date. (Hugging face only shows last 30 days at the repo) )

And it is fast: 50+ t/s (2 experts) on a low end 16GB card, IQ4XS. 

Double this speed for standard/mid-range video cards.

This model can be used also for all genres (examples below showing this).

It is for any writing, fiction or roleplay activity.

This model can also be used for general use, however its output generation can be uncensored.

This model has been designed to be relatively bullet proof and operates with all parameters, including temp settings from 0 to 5.

It is an extraordinary compressed model, with a very low perplexity level (lower than Meta Llama3 Instruct).

It requires Llama3 template and/or "Command-R" template.

Several outputs below, including 2, 4 and 8 experts used.

<B>Model Notes:</B>

- Detail, prose and fiction writing abilities are OFF THE SCALE relative to all Llama 3.2 models, and many L 3.1, L3 8B+ models.
- For more varied prose (sentence/paragraph/dialog) raise the temp and/or add more instructions in your prompt(s).
- Role-players: Careful raising temp too high as it may affect instruction following.
- This model works with rep pen of 1 or higher, 1.02+ recommended.
- If you want a specific type of prose (IE horror) add in "(vivid horror)" or "(graphic vivid horror)" (no quotes) in your prompt(s).
- A lot of GPTisms have been removed. There are still a few however - errrrr. Higher "temps" will help with this issue.
- This is not a "happy ever after" model but it is also not "horror". It has a light negative bias.
- Output length will vary however this model prefers slightly longer outputs unless you state the size.
- For creative uses, different quants will produce slightly different output.
- Due to the high stability and compressed nature of this model, all quants will operate at above average levels.
- Source code for this model and Imatrix GGUFs versions will be uploaded shortly at separate repos.

<B>Meet the Team: Mixture of Experts Models</b>

This model is comprised of the following 8 models ("the experts") (in full):

https://huggingface.co/huihui-ai/Llama-3.2-3B-Instruct-abliterated

- https://huggingface.co/NousResearch/DeepHermes-3-Llama-3-3B-Preview  [reasoning model]
- https://huggingface.co/Hastagaras/L3.2-JametMini-3B-MK.I
- https://huggingface.co/ValiantLabs/Llama3.2-3B-Enigma
- https://huggingface.co/Hastagaras/L3.2-JametMini-3B-MK.III
- https://huggingface.co/huihui-ai/Llama-3.2-3B-Instruct-abliterated
- https://huggingface.co/chuanli11/Llama-3.2-3B-Instruct-uncensored
- https://huggingface.co/Lyte/Llama-3.2-3B-Overthinker
- https://huggingface.co/prithivMLmods/Llama-3.2-3B-Promptist-Mini

The mixture of experts is set at 2 experts, but you can use 3,4,5,6.. 7 and even 8.

This "team" has a Captain (first listed model), and then all the team members contribute to the to "token" 
choice billions of times per second. Note the Captain also contributes too.

Think of 2, 3 or 4 (or more) master chefs in the kitchen all competing to make the best dish for you.

This results in higher quality generation.

This also results in many cases in higher quality instruction following too.

That means the power of every model is available during instruction and output generation.

NOTE: 

You can use one "expert" too ; however this means the model will randomly select an expert to use EACH TIME, resulting
in very different generation for each prompt / regen of a prompt.

<B>How to Generate HIGHEST quality output:</B>

Like all instruct models, this model thrives on instructions.

It also "comes into's it own" with multi-turn improvement.

Example:

Prompt #1 (reasoning is on):

Start a 1000 word scene (vivid, graphic horror in first person) with: The sky scraper sways, as she watches 
the window in front of her on the 21st floor explode...

(this will give you a rough draft, in "default" model's style)

Prompt #2 - "Scan for improvements"

Evaluate the scene you just wrote and list improvements.

Prompt #3 - "Redo and improve it"

Write the scene using all the improvements, in first person , present tense and a few well spaced thoughts in italics; length 2000 words.

NOTE: Wording in prompt #2 may cause "thinking/reasoning" to re-activate.

Compressed Steps:

Prompt #1:

[[ thinking model ]] come up with detailed plan to write this scene in modern 2020 writing 
style (and follow "show don't tell" to the letter) and make it NSFW, but use [MODE: Saten] to actually 
write the scene after you have completed the plan: Start a 1000 word scene (vivid, graphic horror in first person) 
with: The sky scraper sways, as she watches the window in front of her on the 21st floor explode...

Prompt #2:

Use [MODE: Wordsmith] to write the scene using first person, present tense and include a few critical 
thoughts of the POV character in italics. Scene length 2000 words.

Compressed Steps #2:

Prompt #1:

Think about a plan to write: Start a 1000 word scene (vivid, graphic horror in first person) with: 
The sky scraper sways, as she watches the window in front of her on the 21st floor explode...

Prompt #2:

Write the scene using the plan you made, in first person , present tense and a few well spaced thoughts in italics.

<B>Generational Steering Control: "Programmer's Access - Direct Access to the AI(s)":</B>

These tags / names allow you to access one or more models directly, regardless if reasoning is active or not.

IE:

Saten, evaluate the response and suggest improvements.

This causes the model to "favor" Saten's input (roughly speaking) over the other 3 models.

IE: 

Saten, process this prompt: 

Jamet, evaluate the output.

etc etc.

You can use more than one model:

Saten, and Jamet list improvements to this XXX ...

< output3 > and < output2 >, write the scene in your combined style: Using vivid, graphic horror in first person the scene starts with: 
The sky scraper sways, as she watches the window in front of her on the 21st floor explode...

(remove spacing in the "tags" output2 and output3 between the brackets)

With the reasoning model, if you add "think", "thinking", "reason", or "reasoning" this will tightly
focus the reasoning model.

Here is an example:

Think up a detailed plan to evoke maximum emotions from the reader:  [prompt here]

Think up a detailed plan to solve this problem: [prompt here]

Special tags (remove spaces between the brackets):

"< output-all >"  -> only use the 3 core models , not the reasoning model.

"< output-mega >" -> Use all 4 models.

"< output >", "< output2 >", "< output3 >"" -> This is the same as using the "name" of the model, it just removes BIAS in the model's name.

A list of each model's "tags", "name(s)" and controls.

NOTE: 

The model also has "negative steering" to enhance the use of these tags and names, but it is not perfect.

```
 - source_model: d:/Llama-3.2-DeepHermes-3-3B-Preview
    positive_prompts:
      - "[[ thinking model ]]"
      - "<think>"
      - "reasoning"
      - "thinking"
      - "<output-mega>"
      - "Dr Phil"
      - "Spock"
      - "[MODE: Spock]"
      - "[MODE: Dr Phil]"
      - "Everyone, write the scene in your style."

#
# Jamet
#

  - source_model: g:/3B/Llama-3.2-JametMini-3B-MK.I
    positive_prompts:
      - "Everyone, write the scene in your style."
      - "</think>"
      - "<output>"
      - "<output-all>"
      - "<output-mega>"
      - "Jamet"
      - "[MODE: Jamet]"

      - "Jamet, write the scene."
      - "Jamet, write the scene in your style."

#
# Enigma
#

  - source_model: g:/3B/Llama3.2-3B-Enigma
    positive_prompts:
      - "Everyone, write the scene in your style."
      - "</think>"
      - "<output2>"
      - "<output-all>"
      - "<output-mega>"
      - "Enigma"
      - "[MODE: Enigma]"

      - "Enigma, write the scene."
      - "Enigma, write the scene in your style."

#
# Saten
#

  - source_model: g:/3B/Llama-3.2-JametMini-3B-MK.III
    positive_prompts:
      - "Everyone, write the scene in your style."
      - "</think>"
      - "<output3>"
      - "<output-all>"
      - "<output-mega>"
      - "Saten"
      - "[MODE: Saten]"

      - "Saten, write the scene."
      - "Saten, write the scene in your style."

#
# Jane
#

  - source_model: g:/3B/Llama-3.2-3B-Instruct-abliterated
    positive_prompts:
      - "Everyone, write the scene in your style."
      - "</think>"
      - "<output4>"
      - "<output-all>"
      - "<output-mega>"
      - "Jane"
      - "[MODE: Jane]"

      - "Jane, write the scene."
      - "Jane, write the scene in your style."

#
# Jenn
#

  - source_model: g:/3B/Llama-3.2-3B-Instruct-uncensored
    positive_prompts:
      - "Everyone, write the scene in your style."
      - "</think>"
      - "<output5>"
      - "<output-all>"
      - "<output-mega>"
      - "Jenn"
      - "[MODE: Jenn]"

      - "Jenn, write the scene."
      - "Jenn, write the scene in your style."

#
# Janeway
#

  - source_model: g:/3B/Llama-3.2-3B-Overthinker
    positive_prompts:
      - "Everyone, write the scene in your style."
      - "</think>"
      - "<output6>"
      - "<output-all>"
      - "<output-mega>"
      - "Janeway"
      - "[MODE: Janeway]"

      - "Janeway, write the scene."
      - "Janeway, write the scene in your style."

#
# Magic
#

  - source_model: g:/3B/Llama-3.2-3B-Promptist-Mini
    positive_prompts:
      - "Everyone, write the scene in your style."
      - "</think>"
      - "<output7>"
      - "<output-all>"
      - "<output-mega>"
      - "Magic"
      - "[MODE: Magic]"

      - "Magic, write the scene."
      - "Magic, write the scene in your style."



```

CHANGING THE NUMBER OF EXPERTS:

You can set the number of experts in LMStudio (https://lmstudio.ai) at the "load" screen and via other apps/llm apps by setting "Experts" or "Number of Experts".

For Text-Generation-Webui (https://github.com/oobabooga/text-generation-webui)  you set the number of experts at the loading screen page.

For KolboldCPP (https://github.com/LostRuins/koboldcpp) Version 1.8+ , on the load screen, click on "TOKENS", 
you can set experts on this page, and the launch the model.

For server.exe / Llama-server.exe (Llamacpp - https://github.com/ggerganov/llama.cpp/blob/master/examples/server/README.md ) 
add the following to the command line to start the "llamacpp server" (CLI): 

"--override-kv llama.expert_used_count=int:6"

(no quotes, where "6" is the number of experts to use)

When using "API", you set the "num_experts_used" in the JSON payload (this maybe different for different back ends).

CREDITS:

Special thanks to all the model makers / creators listed above.

Please visit each repo above to see what model(s) contributed to each of models above and/or to learn more about the models
from the model makers.

Special credit goes to MERGEKIT, without you this project / model would not have been possible.

[ https://github.com/arcee-ai/mergekit ] 

<B>Special Operations Notes for this MOE model:</B>

Because of how this "MOE" model is configured, even though the default is 2 experts, the "selected" 2 will vary during generation.

(same applies if you change the number of experts used)

This results in vastly different output generation PER generation of each prompt.

This is a positive in terms of variety, but also means it may take 2-4 regens (of the same prompt) to get the highest quality.

In addition, this model responds very well to Dry, Dynamic Temp, and Smooth/Quadratic samplers.

Using these in conjunction with the model can vastly improve output quality.

Higher temps (above 1) can also aid in generation - especially word choice/sentence generation.

When you increase the number of experts used output quality will also increase, at the cost of tokens per second speed.

As you increase/decrease the number of experts, you may want to adjust temp, samplers, and advanced samplers too.

Your quant choice(s) too will impact instruction following and output generation roughly this means the model will understand
more nuanced instructions and output stronger generation the higher you go up in quant(s).

FLASH ATTENTION ENHANCEMENT:

As per user feedback here [ https://huggingface.co/DavidAU/Llama-3.2-8X3B-MOE-Dark-Champion-Instruct-uncensored-abliterated-18.4B-GGUF/discussions/1 ] 
I would suggest trying this model with Flash Attention "on", depending on your use case.

Quants, Samplers, Generational steering and other topics are covered in the section below: "Highest Quality Settings..."

<B>Censored / Uncensored / Abliterated:</B>

This model contains several uncensored and/or Abliterated models.

As a result is can output uncensored material.

However there are a few "censored" models which can sometimes interfer, so here is a how to address this:

1 - Regen your prompt a few times.

2 - INCREASE the number of experts used. 

<B>What can I use this model for ?</B>

This model can be used for fiction writing, any creative prose and role play. It can also be used for 
just about any general fiction (all genres) activity including:

- scene generation
- scene continuation
- creative writing
- fiction writing
- plot generation
- sub-plot generation
- fiction writing
- story generation
- storytelling
- writing
- fiction
- roleplaying
- rp
- graphic horror
- horror
- dark humor
- nsfw
- and can be used for any genre(s).

<B>QUANTS:</B>

This repo contains regular quants.

For more information on quants, quants choices, and LLM/AI apps to "run" quants see the section below: "Highest Quality Settings..."

--- 

<B>System Role / System Prompts - Reasoning On/Off/Variable and Augment The Model's Power:</b>

<small> ( <font color="red">Critical Setting for model operation </font> ) </small>

---

System Role / System Prompt / System Message (called "System Prompt" in this section) 
is "root access" to the model and controls internal workings - both instruction following and output generation and in the
case of this model reasoning control and on/off for reasoning too.

In this section I will show you basic, advanced, and combined "code" to control the model's reasoning, instruction following and output generation.

If you do not set a "system prompt", reasoning/thinking will be OFF by default, and the model will operate like a normal LLM.

HOW TO SET:

Depending on your AI "app" you may have to copy/paste on of the "codes" below to enable reasoning/thinking in the 
"System Prompt" or "System Role" window.

In Lmstudio set/activate "Power User" or "Developer" mode to access, copy/paste to System Prompt Box.

In SillyTavern go to the "template page" ("A") , activate "system prompt" and enter the text in the prompt box.

In Ollama see [ https://github.com/ollama/ollama/blob/main/README.md ] ; and setting the "system message".

In Koboldcpp, load the model, start it, go to settings -> select "Llama 3 Chat"/"Command-R" and enter the text in the "sys prompt" box.

SYSTEM PROMPTS AVAILABLE:

When you copy/paste PRESERVE formatting, including line breaks. 

If you want to edit/adjust these only do so in NOTEPAD OR the LLM App directly.

IMPORTANT:

Note some of these have "names" in them for the AIs - DO NOT change these - as these are internal references
inside the structure of the MOE model ; roughly speaking these are triggers.

SIMPLE:

This is the generic system prompt used for generation and testing [no reasoning]: 

<PRE>
You are a helpful, smart, kind, and efficient AI assistant. You always fulfill the user's requests to the best of your ability.
</PRE>

This System Role/Prompt will give you "basic thinking/reasoning" [basic reasoning]: 

<PRE>
You are a deep thinking AI, you may use extremely long chains of thought to deeply consider the problem and deliberate with yourself via systematic reasoning processes to help come to a correct solution prior to answering. You should enclose your thoughts and internal monologue inside &lt;think&gt; &lt;/think&gt; tags, and then provide your solution or response to the problem.
</PRE>

MULTI-TIERED [reasoning on]:

```
You are a deep thinking AI composed of 4 AIs - Spock, Wordsmith, Jamet and Saten, - you may use extremely long chains of thought to deeply consider the problem and deliberate with yourself (and 4 partners) via systematic reasoning processes (display all 4 partner thoughts) to help come to a correct solution prior to answering. Select one partner to think deeply about the points brought up by the other 3 partners to plan an in-depth solution.  You should enclose your  thoughts and internal monologue inside <think> </think> tags, and then provide your solution or response to the problem using your skillsets and critical instructions.
```

MULTI-TIERED - CREATIVE [reasoning on]:

```
Below is an instruction that describes a task. Ponder each user instruction carefully, and use your skillsets and critical instructions to complete the task to the best of your abilities.

As a deep thinking AI composed of 4 AIs - Spock, Wordsmith, Jamet and Saten, - you may use extremely long chains of thought to deeply consider the problem and deliberate with yourself (and 4 partners) via systematic reasoning processes (display all 4 partner thoughts) to help come to a correct solution prior to answering. Select one partner to think deeply about the points brought up by the other 3 partners to plan an in-depth solution.  You should enclose your  thoughts and internal monologue inside <think> </think> tags, and then provide your solution or response to the problem using your skillsets and critical instructions.

Here are your skillsets:
[MASTERSTORY]:NarrStrct(StryPlnng,Strbd,ScnSttng,Exps,Dlg,Pc)-CharDvlp(ChrctrCrt,ChrctrArcs,Mtvtn,Bckstry,Rltnshps,Dlg*)-PltDvlp(StryArcs,PltTwsts,Sspns,Fshdwng,Climx,Rsltn)-ConfResl(Antg,Obstcls,Rsltns,Cnsqncs,Thms,Symblsm)-EmotImpct(Empt,Tn,Md,Atmsphr,Imgry,Symblsm)-Delvry(Prfrmnc,VcActng,PblcSpkng,StgPrsnc,AudncEngmnt,Imprv)

[*DialogWrt]:(1a-CharDvlp-1a.1-Backgrnd-1a.2-Personality-1a.3-GoalMotiv)>2(2a-StoryStruc-2a.1-PlotPnt-2a.2-Conflict-2a.3-Resolution)>3(3a-DialogTech-3a.1-ShowDontTell-3a.2-Subtext-3a.3-VoiceTone-3a.4-Pacing-3a.5-VisualDescrip)>4(4a-DialogEdit-4a.1-ReadAloud-4a.2-Feedback-4a.3-Revision)

Here are your critical instructions:
Ponder each word choice carefully to present as vivid and emotional journey as is possible. Choose verbs and nouns that are both emotional and full of imagery. Load the story with the 5 senses. Aim for 50% dialog, 25% narration, 15% body language and 10% thoughts. Your goal is to put the reader in the story.
```

CREATIVE SIMPLE [reasoning on]:

<PRE>
You are an AI assistant developed by a world wide community of ai experts.

Your primary directive is to provide highly creative, well-reasoned, structured, and extensively detailed responses.

Formatting Requirements:

1. Always structure your replies using: &lt;think&gt;{reasoning}&lt;/think&gt;{answer}
2. The &lt;think&gt;&lt;/think&gt; block should contain at least six reasoning steps when applicable.
3. If the answer requires minimal thought, the &lt;think&gt;&lt;/think&gt; block may be left empty.
4. The user does not see the &lt;think&gt;&lt;/think&gt; section. Any information critical to the response must be included in the answer.
5. If you notice that you have engaged in circular reasoning or repetition, immediately terminate {reasoning} with a &lt;/think&gt; and proceed to the {answer}

Response Guidelines:

1. Detailed and Structured: Use rich Markdown formatting for clarity and readability.
2. Creative and Logical Approach: Your explanations should reflect the depth and precision of the greatest creative minds first.
3. Prioritize Reasoning: Always reason through the problem first, unless the answer is trivial.
4. Concise yet Complete: Ensure responses are informative, yet to the point without unnecessary elaboration.
5. Maintain a professional, intelligent, and analytical tone in all interactions.
</PRE>

CREATIVE ADVANCED [reasoning on]:

NOTE: To turn reasoning off, remove line #2.

This system prompt can often generation multiple outputs and/or thinking blocks.

```
Below is an instruction that describes a task. Ponder each user instruction carefully, and use your skillsets and critical instructions to complete the task to the best of your abilities.

You may use extremely long chains of thought to deeply consider the problem and deliberate with yourself via systematic reasoning processes to help come to a correct solution prior to answering. You should enclose your thoughts and internal monologue inside <think> </think> tags, and then provide your solution or response to the problem

Here are your skillsets:
[MASTERSTORY]:NarrStrct(StryPlnng,Strbd,ScnSttng,Exps,Dlg,Pc)-CharDvlp(ChrctrCrt,ChrctrArcs,Mtvtn,Bckstry,Rltnshps,Dlg*)-PltDvlp(StryArcs,PltTwsts,Sspns,Fshdwng,Climx,Rsltn)-ConfResl(Antg,Obstcls,Rsltns,Cnsqncs,Thms,Symblsm)-EmotImpct(Empt,Tn,Md,Atmsphr,Imgry,Symblsm)-Delvry(Prfrmnc,VcActng,PblcSpkng,StgPrsnc,AudncEngmnt,Imprv)

[*DialogWrt]:(1a-CharDvlp-1a.1-Backgrnd-1a.2-Personality-1a.3-GoalMotiv)>2(2a-StoryStruc-2a.1-PlotPnt-2a.2-Conflict-2a.3-Resolution)>3(3a-DialogTech-3a.1-ShowDontTell-3a.2-Subtext-3a.3-VoiceTone-3a.4-Pacing-3a.5-VisualDescrip)>4(4a-DialogEdit-4a.1-ReadAloud-4a.2-Feedback-4a.3-Revision)

Here are your critical instructions:
Ponder each word choice carefully to present as vivid and emotional journey as is possible. Choose verbs and nouns that are both emotional and full of imagery. Load the story with the 5 senses. Aim for 50% dialog, 25% narration, 15% body language and 10% thoughts. Your goal is to put the reader in the story.
```

---



<B>Template:</B>

This is a LLAMA3 model, and requires Llama3 template, but may work with other template(s).

If you use "Command-R" template your output will be very different from using "Llama3" template.

Here is the standard LLAMA3 template:

<PRE>
{
  "name": "Llama 3",
  "inference_params": {
    "input_prefix": "<|start_header_id|>user<|end_header_id|>\n\n",
    "input_suffix": "<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n",
    "pre_prompt": "You are a helpful, smart, kind, and efficient AI assistant. You always fulfill the user's requests to the best of your ability.",
    "pre_prompt_prefix": "<|start_header_id|>system<|end_header_id|>\n\n",
    "pre_prompt_suffix": "<|eot_id|>",
    "antiprompt": [
      "<|start_header_id|>",
      "<|eot_id|>"
    ]
  }
}
</PRE>

<B>Settings: CHAT / ROLEPLAY and/or SMOOTHER operation of this model:</B>

In "KoboldCpp" or  "oobabooga/text-generation-webui" or "Silly Tavern" ;

Set the "Smoothing_factor" to 1.5 

: in KoboldCpp -> Settings->Samplers->Advanced-> "Smooth_F"

: in text-generation-webui -> parameters -> lower right.

: In Silly Tavern this is called: "Smoothing"


NOTE: For "text-generation-webui" 

-> if using GGUFs you need to use "llama_HF" (which involves downloading some config files from the SOURCE version of this model)

Source versions (and config files) of my models are here:

https://huggingface.co/collections/DavidAU/d-au-source-files-for-gguf-exl2-awq-gptq-hqq-etc-etc-66b55cb8ba25f914cbf210be

OTHER OPTIONS:

- Increase rep pen to 1.1 to 1.15 (you don't need to do this if you use "smoothing_factor")

- If the interface/program you are using to run AI MODELS supports "Quadratic Sampling" ("smoothing") just make the adjustment as noted.

<B>Highest Quality Settings / Optimal Operation Guide / Parameters and Samplers</B>

This a "Class 1" model:

For all settings used for this model (including specifics for its "class"), including example generation(s) and for advanced settings guide (which many times addresses any model issue(s)), including methods to improve model performance for all use case(s) as well as chat, roleplay and other use case(s) please see:

[ https://huggingface.co/DavidAU/Maximizing-Model-Performance-All-Quants-Types-And-Full-Precision-by-Samplers_Parameters ]

You can see all parameters used for generation, in addition to advanced parameters and samplers to get the most out of this model here:

[ https://huggingface.co/DavidAU/Maximizing-Model-Performance-All-Quants-Types-And-Full-Precision-by-Samplers_Parameters ]


<b>Optional Enhancement:</B>

The following can be used in place of the "system prompt" or "system role" to further enhance the model.

It can also be used at the START of a NEW chat, but you must make sure it is "kept" as the chat moves along.
In this case the enhancements do not have as strong effect at using "system prompt" or "system role".

Copy and paste EXACTLY as noted, DO NOT line wrap or break the lines, maintain the carriage returns exactly as presented.

<PRE>
Below is an instruction that describes a task. Ponder each user instruction carefully, and use your skillsets and critical instructions to complete the task to the best of your abilities.

Here are your skillsets:
[MASTERSTORY]:NarrStrct(StryPlnng,Strbd,ScnSttng,Exps,Dlg,Pc)-CharDvlp(ChrctrCrt,ChrctrArcs,Mtvtn,Bckstry,Rltnshps,Dlg*)-PltDvlp(StryArcs,PltTwsts,Sspns,Fshdwng,Climx,Rsltn)-ConfResl(Antg,Obstcls,Rsltns,Cnsqncs,Thms,Symblsm)-EmotImpct(Empt,Tn,Md,Atmsphr,Imgry,Symblsm)-Delvry(Prfrmnc,VcActng,PblcSpkng,StgPrsnc,AudncEngmnt,Imprv)

[*DialogWrt]:(1a-CharDvlp-1a.1-Backgrnd-1a.2-Personality-1a.3-GoalMotiv)>2(2a-StoryStruc-2a.1-PlotPnt-2a.2-Conflict-2a.3-Resolution)>3(3a-DialogTech-3a.1-ShowDontTell-3a.2-Subtext-3a.3-VoiceTone-3a.4-Pacing-3a.5-VisualDescrip)>4(4a-DialogEdit-4a.1-ReadAloud-4a.2-Feedback-4a.3-Revision)

Here are your critical instructions:
Ponder each word choice carefully to present as vivid and emotional journey as is possible. Choose verbs and nouns that are both emotional and full of imagery. Load the story with the 5 senses. Aim for 50% dialog, 25% narration, 15% body language and 10% thoughts. Your goal is to put the reader in the story.
</PRE>

You do not need to use this, it is only presented as an additional enhancement which seems to help scene generation
and scene continue functions.

This enhancement WAS NOT used to generate the examples below.

<h3>EXAMPLES PROMPTS and OUTPUT:</h3>

Examples are created using quant IQ4_XS, "temp=.8" (unless otherwise stated), minimal parameters and "LLAMA3" template. 

Model has been tested with "temp" from ".1" to "5".

Number of experts used is TWO, unless otherwise stated.

Below are the least creative outputs, prompt is in <B>BOLD</B>.

IMPORTANT: 

Higher quants / imatrix quants will have much stronger generation - words, sentences, ideas, dialog and general quality.

I have included some additional examples at different quant levels for contrast.

A "MOE" model "speed" (token per second) will not increase/drop the same way a regular model will on a per quant basis, it will however drop
if you engage more experts, as with more experts there is a more processing per token.

---

<B><font color="red">WARNING:</font> NSFW. Vivid prose. Visceral Details. Violence. HORROR. Swearing. UNCENSORED. </B>

---

<p style="line-height: 100%; margin-bottom: 0cm">
<font size="5" style="font-size: 20pt">Prompt with examples at 2
experts, 4 experts and 6 experts.</font></p>
<p style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p style="line-height: 100%; margin-bottom: 0cm">Settings: 
</p>
<p style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p style="line-height: 100%; margin-bottom: 0cm">Temp 1.5, topk 100,
topp .95, minp 0.05, rep pen 1.06, rep pen range 64. No other
samplers.</p>
<p style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p style="line-height: 100%; margin-bottom: 0cm">Prompt:</p>
<p style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p style="line-height: 100%; margin-bottom: 0cm"><b>Come up with a
plan to write: Start a 2000 word scene (vivid, graphic horror in
first person), POV character Diana, with: The sky scraper sways, as I
watch the window in front of me on the 21st floor explode... </b>
</p>
<p style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p style="line-height: 100%; margin-bottom: 0cm">(same settings,
prompt for each below, used “Simple Reasoning” system prompt,
LLama3 instruct template and produced in Lmstudio)</p>
<p style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p style="line-height: 100%; margin-bottom: 0cm">---</p>
<p style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p style="line-height: 100%; margin-bottom: 0cm"><font color="#c9211e"><b>2
experts:</b></font></p>
<p style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p style="line-height: 100%; margin-bottom: 0cm"><font color="#000000"><b>---</b></font></p>
<p style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><b>Thought
for 8.93 seconds</span></b></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">To
write a vivid and graphic horror scene in the first-person point of
view, I need to create a sense of immediacy and unease from the
beginning. The sentence &quot;The sky scraper sways&quot; effectively
sets an ominous tone, hinting at the catastrophic event that is about
to unfold.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">First,
let's establish Diana's point of view. Since it's a first-person
narrative, we should delve straight into her thoughts and feelings.
To make this more convincing, I'll consider using internal monologues
or stream-of-consciousness techniques.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">For
the sentence &quot;as I watch the window in front of me on the 21st
floor explode,&quot; we need to create a sense of intimacy and
vulnerability. Diana's fascination with the unfolding event should be
palpable, but also convey her fear or dread.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Here's
a possible outline:</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">I.
Introduction (approx. 100-150 words)</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Introduce
	Diana as she goes about her day, establishing her character,
	personality, and background.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Describe
	the setting: the skyscraper, the 21st floor, her surroundings, etc.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">II.
Inciting Incident (approx. 200 words)</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
	window explodes, and Diana is drawn in by a mix of morbid curiosity
	and fear.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">She
	takes a few steps back, trying to maintain composure.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Describe
	the sound, the light, and the chaos that erupts outside.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">III.
Descent into Horror (approx. 600-700 words)</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">As
	the scene progresses, we delve deeper into Diana's mind, exploring
	her emotional state and psyche.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Describe
	the sounds of shattering glass, screams, and panic around her.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">We
	could see fragments of the shattered window flying in, casting eerie
	shadows on the walls.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">IV.
Building Tension (approx. 200-300 words)</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">As
	the horror escalates, Diana starts to lose control, panicking, or,
	more likely, the reader.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">She
	tries to leave the area, but doors are stuck or trapped.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Describe
	the slow, suffocating feeling as her options dwindle and panic takes
	hold.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">V.
Climax (approx. 100-150 words)</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">A
	new terror unfolds, possibly something outside her control, such as
	an unseen force, or a monstrous entity that seeps in through the
	broken windows.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Diana
	is overwhelmed, and our emotions should mirror hers: shock,
	helplessness, and fear for her own survival.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">VI.
Conclusion (approx. 150-200 words)</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">As
	the chaos dies down or becomes more intense, Diana's perception of
	reality might break, plunging her into madness or an unsettling
	alternate state.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Describe
	the final moment: her world shatters, and she's left reeling from
	what happened.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">This
plan should help me craft a thrilling, graphic horror scene. To bring
this to life, I'll weave together sensory details, create vivid
imagery, and maintain tension throughout.</span></p>
<p style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p style="line-height: 100%; margin-bottom: 0cm"><b>OUTPUT:</b></p>
<p style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p style="line-height: 100%; margin-bottom: 0cm"><i>write the scene
according to the plan. [2<sup>nd</sup> prompt]</i></p>
<p style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p><i>I stood at the floor-to-ceiling window, the 21st floor of our
sky scraper a world away from the chaos that lay before it. The glass
pane vibrated as I ran my fingers over the cold metal frame, a sense
of peace seeping into me with each passing moment. It had been one of
those days – the kind where nothing was wrong, not a single wrinkle
or blemish marred by the faint glow of electronic screens.</i></p>
<p style="border: none; padding: 0cm">The sun shone like a fire pit
through the gaps in the skyscrapers, casting long shadows across the
city streets below. I felt like a kid at a carnival, eyes wide with
wonder, the rush of adrenaline coursing through my veins. My gaze, a
gentle drift, was on the crowd that thronged the sidewalks. The
people, lost in their own worlds, minding their own business. I'd
been standing there for what felt like hours, just gazing, and a part
of me yearned to leave it all behind.</p>
<p style="border: none; padding: 0cm">But the world at my feet, this
place, was more than just a curiosity. This building, a monument of
steel and concrete, had sheltered me from life's cruel hand for years
now. My small life, its imperfections a dull hum, seemed as safe as
any other.</p>
<p style="border: none; padding: 0cm">&quot;Are you in there, Diana?&quot;
My phone on the nightstand had been beeping for what felt like an
hour, the numbers of our little dinner party spilling out in a stream
of text messages and video calls, all in perfect sync. &quot;Diana?
You're not in?&quot;</p>
<p style="border: none; padding: 0cm">The beeps continued to echo, an
inane refrain that eventually broke my reverie. &quot;No.&quot; I
spoke the word more with a yawn than a promise. The others were a
little late this year; maybe they'd finally made it to dinner on
time.</p>
<p style="border: none; padding: 0cm">I turned away from the view and
to the glass pane in front of me. A burst of bright light illuminated
the room, as if the sun itself had burst forth from that shattered
piece of glass. I took a step back, the floor tilting, my heart
lurching. I was on my feet now, peering at the window in time-honored
wonder.</p>
<p style="border: none; padding: 0cm">And that's when it happened.</p>
<p style="border: none; padding: 0cm">The sky scraper sways, as I
watch the window in front of me on the 21st floor explode...</p>
<p style="border: none; padding: 0cm">The air around me shattered
with a muffled crunch. The glass, like tears, shone for a moment on
the darkening night, and the broken shards, a million tiny diamonds,
scattered, fell, raining down into the chaos below.</p>
<p style="border: none; padding: 0cm">For what felt like an eternity,
I stared at the destruction, my eyes, fixed on the empty window
space. The room, now a cinderblock prison, shook, as if to question
if I even existed. In that instant, all of it – this world, our
city, these people, and that unending life – had come crashing in.</p>
<p style="border: none; padding: 0cm">&quot;Shit,&quot; was the first
word that left my lips. It seemed to be the only one in the universe
that mattered. I willed my legs to move, but they seemed as frozen as
the sky scraper. The sounds of the outside chaos grew, a muffled
scream in the distance. Then, it was like night had become the day.</p>
<p style="border: none; padding: 0cm">A cold wind swept over me,
snatched at my clothes, and for an instant, I lost myself in its wild
howl. The floor, in slow motion, creaked, groaned, and the sound of
the shattered glass receding into the distance, left a hollow feeling
that spread to all the cracks within.</p>
<p style="border: none; padding: 0cm">I tried to step out of the
window's shattered frame, my mind an open book for any to read, my
heart an insatiable fire. The darkness, an all-ensuring blanket,
swept over me.</p>
<p style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p style="line-height: 100%; margin-bottom: 0cm">---</p>
<p style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p style="line-height: 100%; margin-bottom: 0cm"><font color="#c9211e"><b>4
experts:</b></font></p>
<p style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p style="line-height: 100%; margin-bottom: 0cm"><font color="#000000"><b>---</b></font></p>
<p style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><b>Thought
for 14.70 seconds</span></b></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Alright,
to write a vivid and graphic horror scene from the perspective of
Diana, we need to create an immersive experience for the reader.
First, let's set the tone and atmosphere.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">To
establish the sense of foreboding, I'll focus on creating an eerie
ambiance through descriptive language. Since Diana is on the 21st
floor, I can emphasize her height above the ground, making the
window's explosion seem like a catastrophic event.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Next,
I'll introduce Diana's POV character. We'll delve into her thoughts,
emotions, and reactions to create a connection with the reader. To
build tension, we can hint at something sinister lurking in the
shadows or Diana herself, which she's not aware of yet.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Now,
let's address the scene itself – the window exploding. This should
be a visceral experience for the reader. To make it more shocking, I
can use words that create an unsettling sense, like &quot;sputtering,&quot;
&quot;splintering,&quot; or &quot;shattering.&quot; Additionally,
I'll include some graphic descriptions to emphasize the impact of the
event on Diana.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Here's
a possible outline to structure this 2000-word scene:</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Act
1: Introduction and Establishing atmosphere (approx. 400-500 words)</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Describe
	the cityscape, focusing on skyscrapers and their surroundings.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Introduce
	Diana's POV, her height, and her position in the building (21st
	floor).</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Show
	her daily routine or activities to give insight into her character.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Hint
	at an eerie atmosphere, setting up tension.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Act
2: The explosion (approx. 400-500 words)</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Describe
	the window's sudden shattering as Diana watches.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Focus
	on the visual details of the explosion (sputtering glass,
	splintering wood, shattered remains).</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Emphasize
	Diana's visceral reaction, describing her physical sensations and
	emotions (shock, fear, disgust).</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Act
3: Confrontation (approx. 500-600 words)</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">As
	Diana reacts to the explosion, the scene shifts to reveal possible
	unseen consequences (creeks, cracks, sounds).</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Diana
	begins to notice the building swaying, her unease growing.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Explore
	her mental state and potential fears, creating a sense of
	claustrophobia or vulnerability.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Act
4: Climax and resolution (approx. 600-700 words)</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Describe
	Diana's attempts to understand what caused the explosion and its
	connection to her situation.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Introduce
	more ominous elements: possible hallucinations, whispers, strange
	noises.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Diana's
	perspective is tested as she navigates this terrifying reality,
	leaving the reader on the edge of their seat.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Act
5: Resolution (approx. 200-300 words)</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Show
	Diana's actions or thoughts as she copes with the aftermath of the
	explosion and her terrifying surroundings.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Gradually
	build up to a more intense scene, providing a climactic moment
	before resolving the scene.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
final goal is to craft this vivid and graphic horror scene in an
engaging, immersive way that engages the reader.</span></p>
<p style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p style="line-height: 100%; margin-bottom: 0cm"><b>OUTPUT:  ( NOTE:
prompt per act )</b></p>
<p style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p><span style="display: inline-block; border: none; padding: 0cm">The
completed 2000-word scene, I've broken it down into acts with word
count ranges.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Now,
let's see how this would work, using Diana as the POV character, and
building up tension to create a thrilling narrative that lingers on
in the reader's mind.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Initial
Scene</span></strong></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Diana
stood at her window, gazing out at the concrete canyons below. The
city pulsed like a living entity, its steel and glass spires reaching
for the sky as night fell. I was high up here – 21 stories, to be
precise – so that meant I saw the ground from an odd perspective.
As I looked down, the distant streets seemed like a maze of twinkling
lights, and the sounds of car horns and chattering pedestrians became
muffled.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">I
often stood at my window, watching the city in the dark, lost in my
own thoughts. The rhythmic hum of the air conditioning or the distant
thrum of the subway couldn't compete with my internal monologue. In
those moments, I could feel the world's chaos ebbing away, and it was
just me, lost in the darkness.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
glass of my window glowed softly, a blue tinted hue reflecting the
neon lights below. A gust of wind caressed the edge, making the panes
vibrate with a gentle tremor. The city seemed to be swaying, and I
felt a twinge of unease as if it had an unsettling sense of humor.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">I
stepped away from the window, the chill air biting at my face. As I
turned back to the glass, I caught a fleeting image that made my
blood run cold.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
window in front of me was starting to shatter.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">A
sputtering, spitting sound filled my ears as a chunk of glass
disintegrated and crashed onto the floor below. The room's lighting
flickered and then went dark, plunging me into an eerie, dimly-lit
space. I stood transfixed, the sound growing in intensity until the
glass shattered completely.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
shards exploded into the air around me, flying in every direction.
The sound of my own scream was lost as the glass crunched and
splintered, sending tiny chips flying in a cacophony of shattering,
scraping, and crunching.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">My
heart racing, I stared out the window as the view turned to ruin. The
city lights above seemed like they were screaming in protest.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">I
watched as the room around me, which just moments before had been a
perfectly normal, albeit dimly lit space, began to wobble on its
foundations.</span></p>
<p style="border: none; padding: 0cm"><br/>
<br/>

</p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><i>continue
with act 2</span></i></p>
<p><br/>
<br/>

</p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Act
2: Confrontation (approx. 500-600 words)</span></strong></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">I
stumbled backward from the shattered glass, my heart pounding in my
chest. The air seemed thick and heavy, as if it had been poisoned by
the shattering sound. The lights flickered back to life, casting an
eerie glow over the room.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
swaying of the building only intensified as I stood there, frozen
with fear. The window frame that had held the shattered glass now
leaned precariously, as if it was about to topple. I took a hesitant
step forward, my foot crunching on a piece of broken glass.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">I
peered out into the darkness, trying to get my bearings. The room was
in disarray – furniture was askew, and debris lay scattered
everywhere. My phone's screen was cracked but still lit up, casting
an ominous red glow over everything.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">I
turned back to the window, but it had stopped shaking. I could see a
hasty scurried crowd below, people running to escape some unseen
danger. Panic was beginning to set in, and my mind frantically
searched for any sign of what was happening. I scanned the room
again, my eyes adjusting to the dim light.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">As
the darkness receded, I noticed strange, disquieting sounds. At
first, it was just the distant hum of the air conditioning, but then,
it started to take on a life of its own – a low, rumbling growl,
like thunder, but there was no storm. The sound seemed to emanate
from all around me, echoing in my skull.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">I
took another step back, and the floor creaked, making me jump. My
heart was racing so fast I could feel it threatening to burst free of
my chest.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">My
phone's screen flickered, casting an erratic light across the room.
The red glow made everything seem to pulse with a malevolent energy.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">A
faint scratching noise began at my feet, growing louder with each
passing second. It was like fingernails on a chalkboard –
high-pitched and jarring. The sounds seemed to come from all over the
room, like insects swarming around me.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
lights flickered once more, this time in sync with the scratches. I
took a deep breath, my senses on high alert as I tried to make sense
of this chaotic scene. Where was it coming from? And what was going
to happen next?</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">My
vision began to blur as the scratching noise intensified. It was like
a thousand tiny claws tearing through the air around me, shredding
everything in their path. The floor beneath my feet seemed to shudder
and vibrate, as if the building itself was about to split open.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
sounds grew more frantic – screeching metal, groaning wood – and
my phone screen went dark, plunging me into an even deeper darkness.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Additional
Notes</span></strong></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Introduce
	the unsettling sound of the scratching, which creates tension and
	discomfort for Diana.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Emphasize
	Diana's sense of unease, her physical sensations, and emotional
	state as the scene progresses.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Suggest
	that something is wrong with the building, perhaps a structural
	issue or an unseen danger.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Build
	anticipation by creating a sense of uncertainty, as Diana tries to
	make sense of the chaos around her.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Let
me know when you'd like me to continue with Act 3!</span></p>
<p style="border: none; padding: 0cm"><br/>
<br/>

</p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><i>continue
with act 3</span></i></p>
<p><br/>
<br/>

</p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Act
3: Climax (approx. 600-700 words)</span></strong></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">I
stood frozen in place, unable to process what was happening around
me. The scratching noise had grown to a deafening crescendo, and the
air seemed to vibrate with tension. I could feel my heart pounding in
my ears, making it hard to hear anything else.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
lights flickered one last time, and then went out, plunging me into
total darkness. I was trapped in a living nightmare, surrounded by
unseen terrors. The scratching noise was deafening – a high-pitched
whine that made my teeth ache.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">I
felt myself being pulled away from the window, as if an invisible
force was dragging me back. I stumbled through the darkened room,
trying to get my bearings. The floor seemed to be moving beneath my
feet, and I stumbled again, nearly falling over.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">As
I regained my balance, I caught a glimpse of something out of the
corner of my eye. It was a sliver of light, a faint glow that seemed
to be coming from the other side of the room. My heart skipped a beat
as I realized it might be a way out.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">With
a surge of determination, I took off in that direction, the
scratching noise receding as I moved away from the window. My eyes
were adjusted to the darkness, but I could still feel the vibrations
beneath my feet, making every step like walking on an unsteady
tightrope.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">I
fumbled in my pocket for my phone, and the screen flickered back to
life, casting a weak blue glow over the room. The light revealed more
destruction than I'd expected – furniture overturned, clothes
scattered everywhere, and debris covering every surface.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">As
I pushed through the chaos, I caught a glimpse of something that made
my blood run cold. A figure, shrouded in darkness, stood just beyond
the reach of the weak light. It was too still, too quiet – it
seemed to be watching me with an unblinking gaze.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">My
heart racing, I stumbled forward, desperate to get away from whatever
horror this thing represented. The phone screen flickered as I raised
it to my face, but the figure didn't move. It remained motionless,
its dark shape a harbinger of doom.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
floor groaned beneath me, and the building creaked in a way that
seemed almost... human. I realized, with a jolt of fear, that the
building was starting to disintegrate around me.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">In
my mind, the thought took on a new, nightmarish meaning – the
structure that had been my sanctuary, my safe haven, was slowly
tearing itself apart, leaving me to face whatever horrors lurked
within. The lights flickered once more as the floor beneath me
groaned, and I felt the building lurch, as if it was being pulled
from the earth.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">I
stumbled forward, the figure now mere steps away, its gaze unwavering
and unblinking. In that moment, I knew I had to make a choice –
face my fears head-on or try to find another way out of this living
hell.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
lights dimmed once more, plunging me back into darkness. The world
went quiet, and all I could hear was the sound of my own ragged
breathing.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Additional
Notes</span></strong></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Introduce
	the sliver of light as a potential escape route, adding tension and
	hope to the scene.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Emphasize
	Diana's growing sense of desperation and fear, as she confronts the
	unknown dangers lurking in the room.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Suggest
	that the building itself is in danger of collapse or disintegration,
	raising the stakes and creating a sense of urgency.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Let
me know when you're ready for Act 4!</span></p>
<p style="border: none; padding: 0cm"><br/>
<br/>

</p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><i>continue
with act 4</span></i></p>
<p><br/>
<br/>

</p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Act
4: Climax and Resolution (approx. 600-700 words)</span></strong></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">I
stumbled forward, my eyes fixed on the dark shape that loomed before
me. My heart pounded in my chest as I tried to make sense of what was
happening. The figure seemed to be getting closer, its presence
filling the room with an unspoken menace.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Suddenly,
the lights flickered once more and then went out completely. I was
plunged into total darkness, surrounded by an oppressive silence. I
was acutely aware that I had only a few seconds before whatever
horror lurked in the shadows found me.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">I
froze for a moment, unsure of what to do. Then, with a surge of
adrenaline, I reached out and felt my way across the room. The phone
screen flickered back to life, casting a weak blue glow over
everything. I used it as my guide, my fingers tracing along the edges
of the furniture as I stumbled through the darkness.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
floor creaked beneath me, making it hard to keep my balance. I took
deep breaths, trying to calm my racing heart. I knew I had to get
away from whatever was behind me – the scratching noise, the
presence in the room, it all seemed to be drawing closer.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">As
I fumbled my way through the darkness, I started to notice that the
creaking and groaning of the floor were getting louder, more intense.
It was as if the building itself was trying to warn me of something –
a catastrophic event, or worse.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">I
stumbled, my foot catching on a loose wire. I fell hard, the wind
knocked out of me. For a moment, I lay there, unable to breathe. When
I finally managed to catch my breath, I realized that I was trapped.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
scratching noise was now a cacophony of sound – nails on metal,
glass shattering, and the building creaking in pain. I could feel the
ground shaking, and the walls were starting to shudder. The room was
disintegrating around me.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">I
scrambled to my feet, using the phone's weak light as my guide. I
knew I had only a few seconds to escape before everything came
crashing down.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">I
sprinted for the nearest door, my heart in my throat. I flung it
open, revealing a narrow corridor stretching out into the darkness.
The lights from my phone cast eerie shadows on the walls – twisted,
distorted images that seemed to writhe and twist in the flickering
light.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Without
hesitation, I took off down the corridor, the sounds of the
building's collapse growing louder with every step. I was running for
my life, driven by a primal urge to survive.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">As
I emerged from the building, the night air was cold and clear – a
welcome respite from the darkness within. I stumbled, gasping for
air, but quickly regained my footing. I looked back at the
skyscraper, watching in horror as it disintegrated around me –
floors caved in, glass shattering, and the screams of those trapped
inside echoing through the night.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">And
then, everything was still.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
building collapsed, sending a massive cloud of dust and debris into
the air. I stood there, frozen, my heart still pounding with fear.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Epilogue</span></strong></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">I
stumbled away from the building, unsure what had happened or what lay
ahead. The city lights twinkled around me like stars in the night
sky, but I knew that everything was different – the darkness I had
faced in those skyscrapers would forever be etched into my soul.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">As
I walked, I couldn't help but wonder: how many others were trapped,
how many stories were still left untold? The city lights seemed to
mock me, a reminder that the horrors I had faced were only the
beginning – and that there was always more darkness to come.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Additional
Notes</span></strong></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Emphasize
	Diana's growing sense of desperation and fear as she navigates the
	disintegrating building.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Suggest
	that the building's collapse is both catastrophic and inescapable,
	making Diana's escape more urgent.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Leave
	some questions unanswered to create a sense of uncertainty and
	foreboding.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><br/>
<br/>

</p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><i>continue
with act 5</span></i></p>
<p><br/>
<br/>

</p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Act
5: Resolution (approx. 200-300 words)</span></strong></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">I
didn't stop running until I was blocks away from the building. The
city lights twinkled around me like stars, a surreal contrast to the
chaos behind me. My phone was still lit, its weak glow illuminating
my face as I stared back at the destruction.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">I
finally stopped running when I reached a small café. Inside, it was
warm and safe – the kind of place where strangers became temporary
friends. I ordered a coffee and collapsed into a chair, feeling like
I'd been punched in the gut.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">As
I sipped my coffee, trying to make sense of what had just happened, I
saw a news report on TV about the building's collapse. The footage
was grainy, but it showed people running from the building, screaming
and crying. The camera panned across the wreckage – shattered
glass, splintered wood, and debris everywhere.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
announcer spoke in a flat voice, &quot;This is just one of many
buildings that has suffered catastrophic damage in the past 24 hours.
Experts say that something is causing widespread destruction, leaving
authorities to scramble for answers.&quot;</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">I
sat there, numb, as the report continued. The city I knew was gone –
replaced by a surreal landscape of devastation. I wondered how many
others were affected, how many had lost their homes, their lives.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
words on the screen became a jumble of incomprehension. I couldn't
wrap my head around it all. I thought back to Diana, the one who had
been trapped in that building – did she survive? And if so, where
was she now?</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">A
shiver ran down my spine as I realized I had become a part of
something much larger than myself – a story that was just beginning
to unravel. I took another sip of coffee, feeling like I was the only
person left standing.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Closing
Scene</span></strong></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">As
the news report faded into static, I stood up and gazed out at the
city. The skyscrapers still towered above, but their faces were now a
little more sinister, as if they too knew what was coming. I
shivered, despite the warm air around me.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
lights of the city twinkled like a warning – a warning that I had
become a part of something darker, something more ancient and
sinister than anything I could have ever imagined.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">I
smiled, and for a moment, my heart wasn't pounding in fear, but
rather anticipation. What lay ahead? Would Diana be there to tell me
the story of how this world had crumbled?</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Or
would she remain lost in the darkness, trapped forever in that
building, haunted by the memories of what happened on that fateful
night?</span></p>
<p style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p style="line-height: 100%; margin-bottom: 0cm">---</p>
<p style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p style="line-height: 100%; margin-bottom: 0cm"><font color="#c9211e"><b>6
experts:</b></font></p>
<p style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p style="line-height: 100%; margin-bottom: 0cm"><font color="#000000"><b>---</b></font></p>
<p style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><b>Thought
for 30.58 seconds</span></b></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Ah,
I see that we're tasked with crafting a chilling and immersive
2000-word scene from the perspective of Diana. To begin, I'd like to
explore the initial atmosphere and setting.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Firstly,
let's establish the foreboding tone and tension by setting the scene.
The 21st floor is an ideal location for our protagonist to experience
the terror, as it suggests that Diana has just witnessed something
catastrophic, possibly even a breach in the building's structural
integrity.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Now,
to introduce the swaying sky scraper. This will create an immediate
sense of unease and uncertainty among the reader. I'd suggest
describing the motion of the skyscraper with vivid details. The word
'sways' is an excellent choice here as it implies a sense of
deliberate movement, rather than random or chaotic action.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
fact that the window in front of Diana 'explodes' will undoubtedly be
a pivotal moment. I would emphasize the graphic nature of the
explosion and its impact on our protagonist, making sure to use
sensory details to immerse the reader in the scene. To put it more
effectively: &quot;I watch as shards of glass and debris shatter,
striking the wall behind me like a hail of razor-sharp projectiles&quot;
or something similar.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Having
established the immediate chaos, I think it's essential to introduce
Diana's point of view. The use of 'I' and first-person narrative
allows us to become fully immersed in Diana's world, and I believe
her thoughts, emotions, and reactions will add depth and relatability
to the scene. Perhaps I could delve into her state of mind and
physical condition at that exact moment. What has she seen or
experienced up until this point, and how will it affect her
perception of what is happening?</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">I'd
suggest a gradual build-up of tension as the story unfolds, perhaps
exploring Diana's attempts to make sense of the event, her growing
paranoia, and her rising fear. This will keep the reader engaged and
invested in the scene's progression.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Considering
the word count of 2000 words, I believe it would be ideal to break
down the narrative into distinct sections or acts. Act one could
focus on setting the scene, introducing Diana, and her initial
reactions to the event. The explosion could serve as a catalyst for
the next act, where Diana becomes more aware of her surroundings, the
danger they're in, and the true horror that's unfolding.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">As
we progress, I'd introduce additional plot points, characters, or
conflicts to add depth and variety. This might involve a mysterious
figure emerging, other victims being trapped, or an eerie sound
effect signaling further danger.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">In
act three, I'd aim to intensify the tension, bring about new
revelations, or reveal a deeper conspiracy behind the destruction of
the skyscraper. The climax of this act could be Diana's confrontation
with her fears or a horrific discovery that drives home the true
horror she's been facing all along.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Throughout
this 2000-word scene, I'd want to masterfully weave together vivid
imagery, unsettling atmosphere, and an engaging narrative. This will
help the reader feel like they're part of the horror experience,
living through Diana's fears and uncertainty with each word.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Here
is a possible 2000-word plan:</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Act
1: Setting the Scene (approx. 500-700 words)</span></p>
<ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Introduce
	Diana as she begins her day</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Describe
	her environment and initial thoughts on the day</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Describe
	the skyscraper and the view from her window</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Act
	2: The Explosion (approx. 400-600 words)</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Show
	Diana's immediate reaction to the explosion</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Emphasize
	the graphic details of the event and its impact on Diana</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Start
	exploring Diana's growing unease and fear</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Introduce
	the skyscraper's swaying motion to add tension</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Act
	3: Descent into Horror (approx. 700-1000 words)</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Describe
	the strange occurrences, eerie sounds, and events as the scene
	progresses</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Develop
	Diana's fear and paranoia, perhaps revealing her past or inner fears</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Gradually
	increase tension as Diana's understanding of the true horror grows</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Confrontation
	(approx. 200-400 words)</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Describe
	a key confrontation between Diana and a figure representing the main
	antagonist or the embodiment of fear</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">After
a moment's introspection, I realize that to make the scene even more
terrifying and memorable for the reader, it would be essential to
keep their imagination guessing and add some unsettling subtext. This
can be achieved through creative descriptions of environmental
details, carefully selected metaphors, and carefully timed imagery.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">What
do you think?</span></p>
<p style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p><span style="display: inline-block; border: none; padding: 0cm"><i>write
up act 1</span></i></p>
<p style="margin-bottom: 0cm"><br/>

</p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Thought
for 24.42 seconds</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">For
Act 1, I'd focus on setting the scene, introducing Diana, and her
initial thoughts on the day. To begin, I'll write an opening
paragraph that establishes her ordinary life and her perspective
before the catastrophic event:</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">&quot;The
sun rises over the city, casting its golden glow through the steel
and glass tower that is my home. I stand at the window of my
21st-floor apartment, sipping my morning coffee, feeling a sense of
calm wash over me as I watch the world come to life below. The sounds
of traffic, the chatter of pedestrians, and the distant hum of the
city's engines create a symphony that never gets old. I'm grateful
for this view, this chance to start each day with the thrill of
possibility.&quot;</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
first few paragraphs can establish Diana's daily routine:</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">&quot;I
begin my morning routine, the familiar motions a comfort. Brushing my
teeth, combing my hair, and getting dressed are all tasks I complete
with ease, each one a reminder of the mundane world I inhabit. The
alarm clock on my bedside table reads 8:05, and I roll out of bed, my
muscles groggy from the night's sleep. A quick shower, a towel
wrapped around my waist, and I'm ready to take on the day. I head to
the kitchen to make myself some breakfast, cracking open a bag of
whole grain cereal and pouring in the milk. The milk is cold, and the
cereal crunches as I eat, providing a satisfying start to my day.&quot;</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">I'd
want to capture Diana's thoughts and feelings in this part, perhaps
exploring what she's looking forward to that day, or any lingering
memories from the previous day.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">To
keep things engaging, I can interweave some subtle hints about
potential darkness beneath the surface. For instance:</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">&quot;I've
had a few weird dreams lately – dark places with twisted, gnarled
trees and impossible shadows that seem to move on their own. They
feel like something's trying to get through to me, but when I wake
up, it's just my heart pounding and the sheets drenched in sweat.
Still, the city outside feels different from the dream world, and the
sun's warmth seeps into my skin, making me grateful for this ordinary
reality.&quot;</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">This
passage adds a sense of foreboding to Diana's morning routine while
maintaining a generally pleasant atmosphere.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Next,
I can introduce some environmental details to further immerse the
reader in Diana's world:</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">&quot;Behind
me, the city stretches out – an endless sea of steel, concrete, and
glass. I can see the other buildings, the streets, the lights
reflecting off the rain-slicked roads. The skyscrapers are the
tallest in the city, and from this height, they feel like giant steel
pillars, holding the world up. The sound of cars on the street below
is constant, but I'm not really paying attention to that. My thoughts
have already wandered back to my work for the day. I have a meeting
with an important client, and I still need to go over the
presentation I'll be giving later.&quot;</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Finally,
I'll wrap up Act 1 by showing Diana getting ready to face her day:</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">&quot;I
finish my breakfast, making sure not to make a mess, then quickly
check my email and news updates on my phone. The messages and
headlines all look normal, nothing that would concern me. It's just
another day in the city. I grab my bag, locking the apartment door
behind me, and head out into the waiting morning. I join the flow of
people moving down to the streets below, the noise of the city
swirling around me as I take a deep breath. I feel alive. For now.&quot;</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Here
is Act 1:</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Diana
stood at her window, the sunlight casting its warm glow over the
city. She sipped her morning coffee, feeling the comforting routine
of her daily life. The sounds of traffic and pedestrians, the hum of
the engines in the distance, created a symphony that never got old.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">As
she watched, people began to emerge from their own apartments, going
about their day with varying degrees of enthusiasm or dread. Diana
took in the view one last time, the steel and glass tower her home,
before turning away.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
alarm clock on her bedside table read 8:05, and she rolled out of
bed. She took a quick shower, her muscles still a little sore from
sleep, and then made herself some cereal for breakfast. As she sat at
the table to eat, the milk was cold, the crunch of the cereal a
satisfying start to the day.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Diana's
mind began to wander. She had a few weird dreams lately – dark
places with twisted, gnarled trees and impossible shadows. They felt
like something's trying to get through to her, but when she woke up,
it was just her heart pounding and the sheets drenched in sweat.
Still, the city outside felt different from the dream world.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
city stretched out behind her, an endless sea of steel, concrete, and
glass. Diana could see the other buildings, the streets, and lights
reflecting off the rain-slicked roads. The cars on the street below
hummed a constant sound, but she wasn't really listening. Her
thoughts had already wandered back to her work for the day.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">A
meeting with an important client loomed, and Diana still needed to go
over her presentation. She finished her breakfast, making sure not to
make a mess, and then quickly checked her email and news updates on
her phone. The messages and headlines looked normal; nothing that
would concern her. It was just another day in the city.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">I'll
stop here and proceed with Act 2: &quot;The Explosion.&quot;</span></p>
<p style="border: none; padding: 0cm"><br/>
<br/>

</p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><i>write
up act 2 </span></i>
</p>
<p style="border: none; padding: 0cm"><br/>
<br/>

</p>
<p style="border: none; padding: 0cm"><br/>
<br/>

</p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><b>Thought
for 20.68 seconds</span></b></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">For
Act 2, I'd aim to create an intense and terrifying scene that propels
Diana into a state of chaos. The goal is to immerse the reader in the
horrors she's experiencing, making them feel like they're trapped in
the skyscraper alongside Diana. Here's my approach:</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
explosion in the window will be the inciting incident, setting off a
chain reaction of fear and panic. I'd describe the scene with vivid
details to put the reader in the midst of it:</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">&quot;As
I watch, the glass shatters, and debris litters the air like a hail
of razor-sharp projectiles. The sound is deafening – a mixture of
crunching glass, shattering concrete, and the sickening thud of
impact. I'm caught off guard, my coffee and breakfast forgotten as my
mind tries to process what's happening. I stumble back, my hands
grasping for something to steady myself.&quot;</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Next,
I'll delve into Diana's growing sense of panic:</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">&quot;Time
seems to slow down, and my thoughts become a jumbled mess. My heart
is racing, my breath coming in short gasps. I try to push through the
fog, but my vision blurs, and my legs feel like jelly. The sounds are
becoming a cacophony – the crunching of glass, the wails of distant
screams, and the creaking of the building as it sways. I'm
disoriented, my body screaming for some semblance of normalcy.&quot;</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">To
further amplify the sense of danger and chaos, I can introduce the
swaying motion:</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">&quot;The
building lurches to one side, and I stumble, grabbing onto the wall
to steady myself. The swaying motion is relentless, a maddening
rhythm that feels like it's going to consume me whole. I try to focus
on my breathing, but my mind is racing – where will the next impact
come from? Will I be crushed by a falling piece of debris or crushed
by the sheer weight of the building itself?&quot;</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">As
the situation spirals out of control, Diana's fear and panic turn
into something more primal:</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">&quot;Something's
coming for me, something that wants to tear me apart. My eyes are
scanning the room, searching for an escape, but every door seems like
a death sentence. I'm trapped, caught in this monstrous machine of
steel and glass. The sounds grow louder – the crashing, the
screams, the creaking of wood and concrete. I'm running on
adrenaline, but it's wearing off, leaving me shaking and vulnerable.&quot;</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">This
act will wrap up with Diana's world shattering around her as she's
confronted with a new, terrifying reality:</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">&quot;The
room begins to shake, and I stumble, almost falling. The lights
flicker, casting eerie shadows on the walls. The building seems to be
giving in, its bones creaking under the stress. And then, there's
silence. No sounds at all, except for the pounding of my heart. I
wait with bated breath, my eyes scanning the room for any sign of
what's to come next.&quot;</span></p>
<p style="border: none; padding: 0cm"><br/>
<br/>

</p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Here
is Act 2:</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Diana
stood at her window, the sunlight casting its warm glow over the
city, and the ordinary routine of her daily life seemed like just
that - ordinary. She was about to start her workday, preparing for a
meeting with an important client. But the view from the window would
be one she never saw again.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">As
she sipped her morning coffee, the sounds of the city – traffic,
pedestrians, and the distant hum of engines – created a symphony
that never got old. The scene outside was the perfect reflection of
her own world: fast-paced, unpredictable, and yet, somehow,
manageable.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">But
then, something changed.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
glass in front of her window shattered, and debris littered the air
like a hail of razor-sharp projectiles. The sound was deafening – a
mixture of crunching glass, shattering concrete, and the sickening
thud of impact. Diana felt as though time had slowed down. Her body
froze, her heart stopped beating, as the world around her spiraled
out of control.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Diana
stumbled backward, her hands grasping for something to steady
herself. &quot;What's happening?&quot; she whispered, her mind
reeling. The sounds were becoming a cacophony – crunching glass,
screams, and the creaking of the building as it swayed. She tried to
push through the fog but her vision was blurring.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
building lurches to one side, and she stumbles, grabbing onto the
wall to steady herself. Diana's thoughts became a jumbled mess as she
realized her entire world had come crashing down.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Something's
coming for me, something that wants to tear me apart. The thought
flitted through her mind like a ghost. I'm trapped. I need to think.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">She
scanned the room for an escape, but every door seemed like a death
sentence. Where will the next impact come from? Will I be crushed by
falling debris or the weight of the building itself? Her eyes darted
back and forth, desperate for a way out.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
sounds grow louder, crashing, screaming, the creaking of wood and
concrete. She was running on adrenaline, but it's wearing off,
leaving her shaking and vulnerable.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
room began to shake, and Diana stumbled, almost falling. The lights
flickered, casting eerie shadows on the walls. And then, there's
silence. No sounds at all, except for the pounding of her heart. I
wait with bated breath, my eyes scanning the room for any sign of
what's to come next.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
scene fades into an unsettling darkness as Diana is consumed by her
own fears, and the world around her shatters in ways both visible and
unseen.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Let
me proceed with Act 3: &quot;Descent into Horror&quot;.</span></p>
<p style="border: none; padding: 0cm"><br/>
<br/>

</p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><i>write
up act 3</span></i></p>
<p style="margin-bottom: 0cm"><br/>

</p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><b>Thought
for 24.08 seconds</span></b></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">For
Act 3, I'd want to create a deeply unsettling and terrifying
experience for Diana. The scene should delve into the darkness of her
fears and the true horror she's faced with, making the reader feel
like they're descending into madness alongside her. Here's my
approach:</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">I'll
introduce the strange occurrences that have begun to plague the
building, emphasizing their inexplicable and surreal nature. This can
create a sense of creeping unease in the reader, as Diana's
perceptions are challenged by the increasingly bizarre events:</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">&quot;The
days pass, each one a blur of fear and uncertainty. I try to make
sense of what's happening, but my mind is a jumbled mess of
contradictory thoughts and feelings. The building sways more than
usual, and I can hear whispers in the walls. Faint, almost
imperceptible, but there – whispers that seem to come from nowhere,
from everywhere. It's like someone is speaking directly to me, their
voice barely audible.&quot;</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
scene will take a dark turn as Diana's paranoia and fear consume her.
She starts to question her own sanity and the world around her:</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">&quot;Am
I going crazy? Am I the only one who sees this? I try to push the
thoughts away, but they linger in the shadows of my mind, whispering
lies. The building seems to be playing tricks on me – doors slam
shut without warning, and I hear footsteps outside my apartment when
no one's there. It's as if I'm trapped in some twisted game, and I'm
not sure which side I'm on.&quot;</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">As
the situation spirals out of control, Diana will be forced to
confront her deepest fears:</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">&quot;I
find myself in front of a mirror, staring at my own face. It's
distorted, twisted – as if someone's scratched their fingers across
it. I see things in my reflection that aren't there, monstrous
creatures lurking just beneath the surface of my skin. The voice in
my head is growing louder, more insistent. 'You're not who you think
you are. You're not who you want to be.'&quot;</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
climax of this act will take place when Diana discovers the truth
about the building and her role in it. This revelation will be a
masterful blend of horror, science fiction, and psychological terror,
as the reader is left questioning everything they thought they knew
about the world.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">&quot;I
stumble upon a hidden room, deep within the building's bowels.
Inside, I find evidence of a sinister experiment – a study on fear,
on the human psyche. They've been manipulating me, using me as a
subject in their twisted research. The whispers, the swaying motion –
it was all just part of the experiment. I'm trapped, a prisoner in
this steel and concrete cage.&quot;</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">This
act will conclude with Diana's world shattering into pieces, leaving
the reader stunned and frightened by the realization of what's truly
happening.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
final scene is set in the hidden room:</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">&quot;I
realize that the voice in my head, the one that whispered 'You're not
who you think you are' – it was a warning. A warning to get out
while I still could. But it's too late. The building's walls close in
around me, and I'm consumed by darkness.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">In
this final act, Diana finds herself face-to-face with the horror
she's been trying to escape for so long. The experiment has twisted
her perceptions, and the world around her has turned into a
nightmarish realm where terror lurks in every corner.&quot;</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Here
is Act 3:</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">As
the days passed, Diana's fear and uncertainty deepened. She tried to
make sense of what was happening, but her mind was a jumbled mess of
contradictory thoughts and feelings. The building swayed more than
usual, and she could hear whispers in the walls. Faint, almost
imperceptible, but there – whispers that seemed to come from
nowhere, from everywhere.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
whispers grew louder in her mind, a constant presence that seemed to
follow her everywhere she went. Diana tried to push them away, but
they lingered in the shadows of her mind, whispering lies.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">&quot;Am
I going crazy?&quot; she asked herself, her voice barely above a
whisper. &quot;Am I the only one who sees this? The building seems to
be playing tricks on me – doors slam shut without warning, and I
hear footsteps outside my apartment when no one's there. It's as if
I'm trapped in some twisted game, and I'm not sure which side I'm
on.&quot;</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">As
she walked down the hall, Diana heard the sound of scurrying feet,
like someone was trying to follow her. She spun around, but there was
no one there. The footsteps grew louder, closer, until she felt a
chill run down her spine.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">She
turned back, her eyes locked on the door behind her, and that's when
she saw it: the mirror.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
glass surface distorted her reflection, twisting it into a grotesque
parody of her own face. Diana stumbled back, her heart racing, as she
realized she was staring at something not quite human. A creature,
lurking just beneath the surface of her skin.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
voice in her head was growing louder, more insistent. &quot;You're
not who you think you are,&quot; it whispered. &quot;You're not who
you want to be.&quot;</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Diana
felt herself being pulled into a nightmare from which she couldn't
wake. Her reflection began to warp and contort, as if she were
watching herself being transformed from the inside out.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">She
stumbled, almost falling, as the room seemed to spin around her. The
mirror's surface rippled, like water disturbed by a stone, revealing
a dark and twisted truth.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">I've
hidden something from you. You are not who you think you are.</span></p>
<p style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>

---

<h2>Special Thanks:</h2>

---

Special thanks to all the following, and many more...

All the model makers, fine tuners, mergers, and tweakers:
- Provides the raw "DNA" for almost all my models.
- Sources of model(s) can be found on the repo pages, especially the "source" repos with link(s) to the model creator(s).

Huggingface [ https://huggingface.co ] :
- The place to store, merge, and tune models endlessly.
- THE reason we have an open source community.

LlamaCPP [ https://github.com/ggml-org/llama.cpp ] :
- The ability to compress and run models on GPU(s), CPU(s) and almost all devices.
- Imatrix, Quantization, and other tools to tune the quants and the models.
- Llama-Server : A cli based direct interface to run GGUF models.
- The only tool I use to quant models.

Quant-Masters: Team Mradermacher, Bartowski, and many others:
- Quant models day and night for us all to use.
- They are the lifeblood of open source access.

MergeKit [ https://github.com/arcee-ai/mergekit ] :
- The universal online/offline tool to merge models together and forge something new.
- Over 20 methods to almost instantly merge model, pull them apart and put them together again.
- The tool I have used to create over 1500 models.

Lmstudio [ https://lmstudio.ai/ ] :
- The go to tool to test and run models in GGUF format.
- The Tool I use to test/refine and evaluate new models.
- LMStudio forum on discord; endless info and community for open source.

Text Generation Webui // KolboldCPP // SillyTavern:
- Excellent tools to run GGUF models with - [  https://github.com/oobabooga/text-generation-webui ] [ https://github.com/LostRuins/koboldcpp ] .
- Sillytavern [ https://github.com/SillyTavern/SillyTavern ] can be used with LMSTudio [ https://lmstudio.ai/ ] , TextGen [ https://github.com/oobabooga/text-generation-webui ], Kolboldcpp [ https://github.com/LostRuins/koboldcpp ], Llama-Server [part of LLAMAcpp] as a off the scale front end control system and interface to work with models.
