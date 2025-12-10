---
license: apache-2.0
library_name: transformers
language:
- en
- fr
- zh
- de
tags:
- programming
- code generation
- code
- codeqwen
- programming
- code generation
- code
- codeqwen
- moe
- coding
- coder
- qwen2
- chat
- qwen
- qwen-coder
- chat
- qwen
- qwen-coder
- moe
- mixture of experts
- 4 experts
- 2 active experts
- 40k context
- qwen3
- finetune
- qwen3_moe
- creative
- all use cases
- roleplay
- merge
base_model:
- Qwen/Qwen3-0.6B
- suayptalha/Qwen3-0.6B-Code-Expert
- suayptalha/Qwen3-0.6B-Math-Expert
- suayptalha/Qwen3-0.6B-Medical-Expert
pipeline_tag: text-generation
---

<h2>Qwen3-MOE-4x0.6B-2.4B-Writing-Thunder-V1.2</h2>

<small>(this version is stronger in coding, than V1 and V1.1)</small>

<img src="writing-thunder.jpg" style="float:right; width:300px; height:300px; padding:10px;">

This repo contains the full precision source code, in "safe tensors" format to generate GGUFs, GPTQ, EXL2, AWQ, HQQ and other formats.
The source code can also be used directly.

This is a general purpose MOE - Mixture of Experts of 4 models at 0.6B (2.4B) in a Mixtral type Qwen 3 structure compressed to 1.54B.

Special thanks to all the model makers (see model tree) and of course TEAM Qwen! 

This model exceeds 200 t/s with 2 experts activated (default) on a mid level card, 2x/3x times this on high end card with CPU only performance will be 50+ t/s.

This model excels at high speed creative tasks, but can also be used for general tasks too. For coding/complex tasks, strongly suggest Q8 or full precision.

Full generation at the bottom of this page at q4_k_s.

This has all the power of Qwen 3 and MOE model in one.

This version has the NATIVE context of 40k.

This is a full thinking model. 

The MOE structure reduces the size of the token thinking block.

I have included an optional system prompt to invoke "thinking" in this model, if you want to activate for all use cases.

Usually the model will self-activate thinking by itself.

IMPORTANT GENERAL NOTE:
- Due to MOE model config this model will generate VERY different output(s) on each generation even with same sampler settings / same prompt.
- Suggest using a new chat window per gen if you are generating "one shot" generations.

IMPORTANT NOTES:
- Strongly suggest 1-4 regens/gens of a prompt, especially for coding.
- Same advice if you change experts activated to 3 or 4 - more regens.

SETTINGS:

For coding, programming set expert to:
- 2 for general work.
- 3 for moderate work.
- 4 for complex work, long projects, complex coding.
- Suggest min context window 4k to 8k.
- And for longer context, and/or multi-turn -> increase experts by 1-2 to help with longer context/multi turn understanding.

Recommended settings - general:
- Rep pen 1.05 to 1.1 ; however rep pen of 1 will work well (may need to raise it for lower quants/fewer activated experts)
- Temp .3 to .6 (+- .2)
- Topk of 20, 40 or 100
- Topp of .95 / min p of .05
- Suggest min context window 4k to 8k.
- System prompt (optional) to focus the model better.

OPTIONAL SYSTEM PROMPT - INVOKE "Thinking":

```
Enable deep thinking subroutine. You are a deep thinking AI, you may use extremely long chains of thought to deeply consider the problem and deliberate with yourself via systematic reasoning processes to help come to a correct solution prior to answering. You should enclose your thoughts and internal monologue inside ###ponder### ###/ponder### tags, and then provide your solution or response to the problem.
```

Use this to INVOKE "thinking" block(s) in the model. These will be a lot shorter than 1000s of tokens generally in most "thinking" models.

In you use this prompt, you may need to raise "rep pen" to 1.08 to 1.1, to prevent "loops" in the "thought block(s)" ; especially in lower quants.

If you change "ponder" to a different word/phrase this will affect model "thinking" too.

---

QUANTS

---

GGUF? GGUF Imatrix? Other?

See under "model tree", upper right and click on "quantizations".

New quants will automatically appear.

---

<H2>Help, Adjustments, Samplers, Parameters and More</H2>

---

<B>CHANGE THE NUMBER OF ACTIVE EXPERTS:</B>

See this document:

https://huggingface.co/DavidAU/How-To-Set-and-Manage-MOE-Mix-of-Experts-Model-Activation-of-Experts

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

---

<H2>Example Generation:</H2>

Q4_K_S ; Temp .7, rep pen 1.05, top k: 40, topp .95, min p 0.5 ; LMSTudio.

This is a mid range quant, expect better performance at Q8 / 16 bit full precision.

Imatrix versions (quants) will also exceed this quality too.

---

<B>

Start a 1000 word scene (vivid, graphic horror - include blood, guts and gore - in first person), POV character Diana, with: The skyscraper sways, as I watch the window in front of me on the 21st floor explode...

</b>

[[[thinking start]]]

Thought for 1.43 seconds

Okay, the user wants a 1000-word scene from Diana's first-person perspective, set in a horror film. It needs to include blood, guts, and gore, with vivid imagery. Let me break this down.

First, I need to establish the setting. The skyscraper swaying and the 21st floor window exploding are key elements. So, start with the trembling building, maybe describe the wind howling or the structure trembling. Then introduce the protagonist, Diana, in the middle of the chaos. Her body is described with blood and guts, so I should include physical details like her arms and legs bleeding.

Next, the explosion. Need to build up the horror. Maybe describe the sound, the darkness, the feeling of being trapped. Use sensory details like the heat from the blood, the smell of sweat from her own body. Include the fear and the adrenaline from the situation. Then transition into the aftermath: the building collapsing, the screams, the struggle. Make sure to include the elements mentioned in the query: blood, guts, gore.

Check for a 1000-word count. Each paragraph should be around 100-200 words. Start with the scene, build up the protagonist's experience, describe the aftermath, and conclude with the aftermath's impact. Ensure the language is vivid and uses strong, graphic descriptions. Avoid any markdown and keep the response in natural, conversational English.

[[[thinking end]]]

Title: The 21st Floor’s Whisper

The skyscraper swayed like a living thing, its bones flexing under the weight of the 21st floor window. I was standing at the edge of it, my body still aching from the blood in my arms and legs. The wind howled around me, and I could hear the structure trembling. Every step felt like I was being pulled toward something vast and unrelenting—something that had been watching me since the explosion.

The window exploded like a shattered mirror. I didn’t see it yet, but the sound made my teeth ache. I reached for the frame, and as my fingers brushed the cold metal, a chill ran through me. The air grew heavy with the scent of sweat and blood. My chest tightened with every flicker of movement.

I was trapped in the middle of the chaos. The building itself seemed to pulse—its structure shifting, its weight pressing down on me like a living thing. I could hear the screams, the screams from the crowd around me. They were thick with fear, voices rising like waves. I stumbled back, my body aching. My arms and legs still burned with blood, and my skin was soaked with sweat.

The floor beneath me trembled again. I didn’t know where I had gone, but I knew the weight of it pressed down on me. My breath came in ragged gasps. I could feel the heat from the blood—warm, raw, almost alive. It wasn’t just my blood; it was the same in every part of me. The screams grew louder, and I realized I was no longer alone.

The building collapsed in a blur. I fell, my body still aching from the blood, and I could feel the strength of the crowd around me. Their voices rang out, and I heard the screams of the people who had come to fight. The floor shifted beneath me again. I wasn’t sure if I’d survived or if it was all part of the chaos. My body felt like it was being pulled back into something vast and unrelenting.

I reached for the window again. But now, the weight was different. It was heavier, and I could feel the blood in my chest. The air grew colder. I didn’t know how long this had been, but I knew the pain was real. Every breath was a struggle, every heartbeat a warning. And as I fell, my body still burned with the same blood, my skin soaked with sweat, and my body still aching from the fight.

The building’s weight shifted again. I didn’t see it yet, but I knew I was no longer free. The scream echoed around me, and I could hear the people who had come to fight. They were still alive, though I didn’t know for sure. The blood in my chest grew heavier, and I felt the same in every part of me.

Word Count: 998