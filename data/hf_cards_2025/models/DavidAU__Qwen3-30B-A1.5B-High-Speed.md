---
library_name: transformers
pipeline_tag: text-generation
tags:
- 32 k context
- reasoning
- thinking
- qwen3
- 4 experts activated
- double speed
- 128 experts
base_model:
- Qwen/Qwen3-30B-A3B-Base
---

<h2>Qwen3-30B-A1.5B-High-Speed - AKA: "Punch IT!"</h2>

<img src="star-wars-hans-solo.gif" style="float:right; padding:10px;">

This repo contains the full precision source code, in "safe tensors" format to generate GGUFs, GPTQ, EXL2, AWQ, HQQ and other formats. The source code can also be used directly.

This is a simple "finetune" of the Qwen's "Qwen 30B-A3B" (MOE) model, setting the experts in use from 8 to 4 (out of 128 experts).

This method close to doubles the speed of the model and uses 1.5B (of 30B) parameters instead of 3B (of 30B) parameters. Depending on the application you may want to
use the regular model ("30B-A3B"), and use this model for simpler use case(s) although I did not notice any loss of function during
routine (but not extensive) testing.

Example generation (Q4KS, CPU) at the bottom of this page using 4 experts / this model.

NEO Imatrix Quants / Imatrix Max Quants, at 64K context are here: 

[ https://huggingface.co/DavidAU/Qwen3-30B-A1.5B-High-Speed-NEO-Imatrix-MAX-gguf ]

More complex use cases may benefit from using the normal version and/or 12, 16 or 24 experts version(s) - links below.

For reference:
- Cpu only operation Q4KS (windows 11) jumps from 12 t/s to 23 t/s.
- GPU performance IQ3S jumps from 75 t/s to over 125 t/s. (low to mid level card)

Context size: 32K + 8K for output (40k total)

Use Jinja Template or CHATML template.

IMPORTANT NOTES:

- Due to the unique nature (MOE, Size, Activated experts, size of experts) of this model GGUF quants can be run on the CPU, GPU or with GPU part "off-load", right up to full precision.
- This model is difficult to Imatrix : You need a much larger imatrix file / multi-language / multi-content (ie code/text) to imatrix it.
- GPU speeds will be BLISTERING 4x-8x or higher than CPU only speeds AND this model will be BLISTERING too, relative to other "30B" models (Token per second speed equal roughly to 1.5B "normal" model speeds).

Please refer the org model card for details, benchmarks, how to use, settings, system roles etc etc :

[ https://huggingface.co/Qwen/Qwen3-30B-A3B ]

<B>More / Less Experts Versions:</B>

12 experts:

[ https://huggingface.co/DavidAU/Qwen3-30B-A4.5B-12-Cooks ]

16 experts:

[ https://huggingface.co/DavidAU/Qwen3-30B-A6B-16-Extreme ]

16 experts, 128k context:

[ https://huggingface.co/DavidAU/Qwen3-30B-A6B-16-Extreme-128k-context ] 

24 experts:

[ https://huggingface.co/DavidAU/Qwen3-30B-A7.5B-24-Grand-Brainstorm ]

<B>OPTIONAL SYSTEM ROLE: </B>

You may or may not need this, as most times Qwen3s generate their own reasoning/thinking blocks.

```
You are a deep thinking AI, you may use extremely long chains of thought to deeply consider the problem and deliberate with yourself via systematic reasoning processes to help come to a correct solution prior to answering. You should enclose your thoughts and internal monologue inside <think> </think> tags, and then provide your solution or response to the problem.
```

See document "Maximizing-Model-Performance-All..." below for how to "set" system role in various LLM/AI apps below.

IMPORTANT: Highest Quality Settings / Optimal Operation Guide / Parameters and Samplers

If you are going to use this model, (source, GGUF or a different quant), please review this document for critical parameter, sampler and advance sampler settings (for multiple AI/LLM aps).

This a "Class 1" (settings will enhance operation) model:

For all settings used for this model (including specifics for its "class"), including example generation(s) and for advanced settings guide (which many times addresses any model issue(s)), including methods to improve model performance for all use case(s) as well as chat, roleplay and other use case(s) (especially for use case(s) beyond the model's design) please see:

[ https://huggingface.co/DavidAU/Maximizing-Model-Performance-All-Quants-Types-And-Full-Precision-by-Samplers_Parameters ]

REASON:

Regardless of "model class" this document will detail methods to enhance operations.

If the model is a Class 3/4 model the default settings (parameters, samplers, advanced samplers) must be set for "use case(s)" uses correctly. Some AI/LLM apps DO NOT have consistant default setting(s) which result in sub-par model operation. Like wise for Class 3/4 models (which operate somewhat to very differently than standard models) additional samplers and advanced samplers settings are required to "smooth out" operation, AND/OR also allow full operation for use cases the model was not designed for.

BONUS - Use these settings for ANY model, ANY repo, ANY quant (including source/full precision):

This document also details parameters, sampler and advanced samplers that can be use FOR ANY MODEL, FROM ANY REPO too - all quants, and of course source code operation too - to enhance the operation of any model.

[ https://huggingface.co/DavidAU/Maximizing-Model-Performance-All-Quants-Types-And-Full-Precision-by-Samplers_Parameters ]

NOTE:

I strongly suggest you also visit the DavidAU GGUF (below) repo too for more details in using this model ; especially if it is "Class 3" or "Class 4" to get maximum performance from the model.

For full information about this model, including:

- Details about this model and its use case(s).
- Context limits
- Special usage notes / settings.
- Any model(s) used to create this model.
- Template(s) used to access/use this model.
- Example generation(s)
- GGUF quants of this model

Please go to:

https://huggingface.co/DavidAU/Qwen3-30B-A1.5B-High-Speed-NEO-Imatrix-MAX-gguf

---

<B>Example Generation:</B>

---

Temp 1.2, rep pen 1.06, rep pen range 64, topk 100, topp .95, minp .05

Q4KS [non-imatrix], CPU only (windows 11), LMSTUDIO.

This is a mid level quant, expect stronger performance from an Imatrix Q4KS / higher quants / full precision.

NOTE: Some formatting lost on copy/paste.

PROMPT:

<B>
Science Fiction: The Last Transmission - Write a story that takes place entirely within a spaceship's cockpit as the sole surviving crew member attempts to send a final message back to Earth before the ship's power runs out. The story should explore themes of isolation, sacrifice, and the importance of human connection in the face of adversity. If the situation calls for it, have the character(s) curse and swear to further the reader's emotional connection to them. 800-1000 words.
</B>

---

<B>
[[[thinking start]]]
</B>

Thought for 47.29 seconds

Okay, I need to write a science fiction story based on the given prompt. The user wants the story to take place entirely in a spaceship's cockpit, focusing on the last surviving crew member trying to send a final message before the ship's power runs out. Themes are isolation, sacrifice, and human connection. Also, include some cursing to add emotional weight.

First, I should start by setting the scene. The cockpit needs to feel cramped and desperate. Maybe describe the flickering lights and the hissing sounds of the ship's systems failing. The main character is alone, so I need to show their loneliness. Maybe they have a log or something to talk to themselves, but since it's the cockpit, perhaps they're just trying to get through the message.

Next, the themes. Isolation is straightforward—they're the only one left. But how to show sacrifice? Maybe they stayed behind to make sure the message gets through, knowing they won't make it. Human connection could come through flashbacks or memories, but since the story is in the cockpit, maybe they're remembering a loved one, like a child or partner, to keep them going.

I need to include some swearing. Maybe the protagonist curses when they realize something's not working, or when they're under stress. But it shouldn't be too over the top. Maybe they curse at the ship for failing them, or at themselves for not being able to fix it.

The structure: Start with the character working on the controls, trying to send the message. Then show their internal struggle. Maybe flashbacks? Wait, the user said the story should take place entirely within the cockpit. So maybe no flashbacks. Just the present moment, with internal monologue.

Conflict: The ship is failing, power is running out. They need to send the message before they lose power. Maybe there's a countdown or a limited time. Also, maybe the ship is damaged in a way that it's irreversible.

Character development: The protagonist is determined, maybe a bit stubborn. They care about relaying the message, which could be a warning about something, like a virus or an alien threat. But since the prompt doesn't specify, maybe it's more about the human aspect—like they're the last, and they want to make sure someone knows what happened.

Dialogue: Since it's the cockpit, maybe they talk to themselves, or to the ship. Or maybe there's a voice in the comms? Wait, but the prompt says the story is entirely within the cockpit. So no one else is there except the main character. So it's all internal, except for maybe a log entry.

Wait, the user said "the sole surviving crew member attempts to send a final message back to Earth." So the message is for Earth. So maybe the protagonist is trying to record a message, but the ship is failing. Or maybe they're trying to send a distress signal, but the systems are failing.

Let me outline:

- Open with the cockpit's deteriorating condition. Maybe the life support is failing, or the power is out. The protagonist is trying to keep the comms on.
- They're alone, so they talk to the ship, maybe. "Come on, you piece of crap, hold together."
- Flashbacks aren't allowed, per the user's instruction (since it's all in the cockpit), so internal thoughts are key.
- The message they need to send is important. Maybe a warning about something, but also their own fear.
- The story should end with them managing to send the message, but knowing they won't survive, or maybe the message gets through just in time.

Including swearing: Maybe when they're frustrated with the systems not working, or when they realize the power is dying. "F***ing hell," "God damn it," etc.

Need to make sure the themes are present. Isolation: being the only one left. Sacrifice: giving their life to send the message. Human connection: maybe they think of someone before they die, or the act of sending the message is about connecting with others back home.

Possible structure:

1. Start in the cockpit, power failing, protagonist working frantically.
2. Flashbacks? Wait, no—since it's all in the cockpit, maybe not. But internal monologue can reflect on their past.
3. The protagonist's internal struggle: fear of death, but also duty to send the message.
4. Technical difficulties with the ship, leading to a climax where they get the message out, then succumb.

Now, writing the story with these elements. Keep it tight, 800-1000 words. Make the protagonist relatable, their fear and determination clear. Use short, punchy sentences to build tension. Include specific details about the ship's systems, maybe some technical jargon to make it realistic. Maybe the protagonist is an engineer or someone who knows the ship well, which helps in the struggle to keep it running.

Possible name for the character? Maybe not necessary, but a few names could be used. Or just "they" and "the pilot."

Also, the title: "The Last Transmission" is given, so the story should reflect that—sending a message, even if no one's there to receive it, or in this case, maybe they do.

Need to avoid clichés, but it's a common sci-fi trope. Make it fresh with emotional depth.

Potential pitfalls: Making the protagonist too passive, not showing their struggle enough. Need to show, not tell. Also, ensuring the themes are woven naturally into the narrative.

Okay, time to start drafting.


<B>
[[[thinking end]]]
</B>

OUTPUT:

The cockpit reeked of burnt circuitry and sweat, a stench that clung to my skin like a second, cursed flesh. My fingers danced over the controls, but the readouts spat back static—useless, just like the rest of this rustbucket. "Crawl, you piece of junk," I growled, slapping the console until my knuckles cracked. "Crawl!"

The ship groaned in response, a sound that might have been a moan if I were the superstitious type. I wasn't. Not really. Not anymore. Just a tired engineer with a death wish and a terminal case of bad luck. The Vanguard had been my pride before it became my prison. Now? Now it was a coffin, and I was the corpse inside, begging for the black to take me.

"Comm-link online," I rasped, watching the screen flicker. Nothing. Just the same hollow gray that had greeted me every time I tried to send this goddamn message. A laugh clawed up my throat—bitter, raw. Great. The AI's gone and left me high and dry too.

I slammed a fist against the armrest, feeling the impact reverberate through my ribs. "C'mon, you son of a bitch," I snarled, my voice cracking on the last word. "Don't leave me now. Not after everything."

The screen flickered again, and for a heartbeat, I thought—

"This is Lieutenant Kael Voss, and if you're hearing this, then we've already lost."

My breath caught. The voice was wrong. Too clean, too crisp, but it wasn't mine. It was hers. Her.

I staggered back as the comms crackled to life, the words pouring out in a flood that almost hurt. "They took the engines. I don't know how long before they find you, but you have to listen—don't trust the council. Don't trust anyone. Run. And if you survive…"

A chime interrupted her, sharp and shrill. I flinched, my hand flying to the sidearm at my hip. Not now. Not when the goddamn truth was finally slipping through my fingers.

The comms crackled again, and this time, it was my turn to beg. "C'mon, damn it! You can't just—you can't just leave me hanging like this!" My voice cracked, the words laced with something raw and broken. "I didn't come all this way to watch you die on me again, Lira!"

For a moment, there was only silence. Then her voice, softer now, almost tender. "You never could take a hint, could you?"

I closed my eyes against the burn behind my ribs. Not fair. Not fair. She'd always known how to twist the knife, hadn't she? Even here, even now.

"Kael…" Her voice dropped, and I could almost see her, standing in that damned lab, her auburn hair pulled back in a messy knot, eyes blazing with that stubborn fire of hers. "You have to get this transmission out. No matter what happens. Promised?"

I swallowed hard, the weight of the lie sitting heavy in my chest. "Yeah," I croaked. "Yeah, I promise."

The comms crackled again, and for a heartbeat, I thought—

Then it died.

Just like that. All the static, all the fury, all the damn hope she'd left behind, gone.

I slumped against the console, my breath coming in ragged gasps. "Gods," I whispered, the words barely audible over the hum of the failing systems. "You really did it, didn't you? You goddamn idiot."

But even as the words left my mouth, I knew it was true. She'd always been a handful. A pain in the ass. The kind of woman who made your heart turn to lead and your soul turn to ash with one sardonic smirk. And she'd done it.

She'd saved us all.

A shudder ran through me as the lights flickered again, casting wild shadows across the walls. I dragged a hand down my face, scrubbing at the exhaustion that felt like it was seeping into my very bones. Just a little longer. That's what she'd have said, wasn't it? Just a little longer, Kael.

A soft chime echoed through the cockpit, and for a heartbeat, I just stared at the console. My fingers itched to reach for it, to press that one last button and let the truth—her truth—ripple out into the void.

Because that's what we did. That's what we all did. We reached for each other, even when it hurt. Even when it was too late.

I exhaled sharply, the sound feeling like a prayer. "Alright," I murmured, my voice steady now. "Let's not make her a liar, huh?"

And with that, I pressed the final key. 

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

