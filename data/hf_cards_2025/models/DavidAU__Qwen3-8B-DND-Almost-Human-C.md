---
license: apache-2.0
base_model:
- DavidAU/Qwen3-DND-Jan-v1-256k-ctx-Brainstorm40x-8B
datasets:
- DavidAU/The-works-PK-Dick
language:
- en
pipeline_tag: text-generation
tags:
- programming
- code generation
- code
- coding
- coder
- chat
- code
- chat
- brainstorm
- qwen
- qwen3
- qwencoder
- brainstorm 40x
- all uses cases
- Jan-V1
- finetune
- thinking
- reasoning
- unsloth
- not-for-all-audiences
library_name: transformers
---

<h2>Qwen3-8B-DND-Almost-Human-C</h2>

<img src="deckard.gif" style="float:right; width:300px; height:300px; padding:10px;">

This repo contains the full precision source code, in "safe tensors" format to generate GGUFs, GPTQ, EXL2, AWQ, HQQ and other formats. The source code can also be used directly.

A love letter to all things Philip K Dick, trained and fine tuned on an in house datasets (5) using Unsloth.

This is V1, "Light", "Large" and "Almost Human" and "C" training level (STRONG) on 8B Qwen 3 DND - Double Neuron Density model: 72 layers, 794 tensors - 
twice the density of a normal Qwen 3 8B model. 

"A" (light) and "B" (medium) are at different repos:

https://huggingface.co/DavidAU/Qwen3-8B-DND-Almost-Human-A

https://huggingface.co/DavidAU/Qwen3-8B-DND-Almost-Human-B

Example Generations: 

For A, B and C models I used the same 3 prompts, and temp=0 to show contrasts between A, B and C versions.

(examples at bottom of this page)

Also:

Links to 6B (Brainstorm 20x, 55 layers) versions are below too.

"Almost Human" is about adding (back) the humanity, the real person called Philip K Dick back into the model - with tone, thinking, and a touch of prose.

"Deckard" is the main character in Blade Runner.

---

<B>DECKARD SERIES - 6B:</b>

You may perfer light and/or heavy depending on your use case(s).

With "Light", 6% of the model is trained, whereas "Heavy" 13% of the model is trained, and the training is twice as long, and deeper than light.

"Large" versions are trained on 3x times the dataset.

"Almost Human" versions have an additional dataset (plus 3x dataset) containing the BIO of the author, letters, notes and such.

Each version will diff from each other, with "Light" vs "Heavy" having a large difference.

Light [6%]:
- https://huggingface.co/DavidAU/Qwen3-Deckard-6B
- https://huggingface.co/DavidAU/Qwen3-Deckard-Large-6B
- https://huggingface.co/DavidAU/Qwen3-Deckard-Large-Almost-Human-6B

Heavy [13%, 2x longer training]:
- https://huggingface.co/DavidAU/Qwen3-Deckard-Heavy-6B
- https://huggingface.co/DavidAU/Qwen3-Deckard-Large-Heavy-6B

---

This model requires:
- Jinja (embedded) or CHATML template
- Max context of 256k.

Settings used for testing (suggested):
- Temp .3 to .7 (but .8 to 1.5 for creative)
- Rep pen 1.05 to 1.1
- Topp .8 , minp .05
- Topk 20
- Min context of 8k for thinking / output.
- No system prompt.

This model will respond well to both detailed instructions and step by step refinement and additions to code.

Likewise for creative use cases.

Here is a review of this model's operations:

https://www.linkedin.com/posts/gchesler_nightmediaqwen3-jan-v1-256k-ctx-6b-brainstorm20x-q6-activity-7364301711529709570-CiAn

As this is an instruct model, it will also benefit from a detailed system prompt too.

For simpler coding problems, lower quants will work well; but for complex/multi-step problem solving suggest Q6 or Q8.

---

<B>QUANTS:</b>

---

GGUF? GGUF Imatrix? Other?

Special thanks to Team Mradermacher, Team Nightmedia and other quanters!

See under "model tree", upper right and click on "quantizations".

New quants will automatically appear.

---

<H2>What is Brainstorm?</H2>

---

<B>Brainstorm 40x</B>

The BRAINSTORM process was developed by David_AU.

Some of the core principals behind this process are discussed in this <a href="https://arxiv.org/pdf/2401.02415"> 
scientific paper : Progressive LLaMA with Block Expansion </a>. 

However I went in a completely different direction from what was outlined in this paper.

What is "Brainstorm" ?

The reasoning center of an LLM is taken apart, reassembled, and expanded.

In this case for this model: 40 times

Then these centers are individually calibrated. These "centers" also interact with each other. 
This introduces subtle changes into the reasoning process. 
The calibrations further adjust - dial up or down - these "changes" further. 
The number of centers (5x,10x etc) allow more "tuning points" to further customize how the model reasons so to speak.

The core aim of this process is to increase the model's detail, concept and connection to the "world", 
general concept connections, prose quality and prose length without affecting instruction following. 

This will also enhance any creative use case(s) of any kind, including "brainstorming", creative art form(s) and like case uses.

Here are some of the enhancements this process brings to the model's performance:

- Prose generation seems more focused on the moment to moment. 
- Sometimes there will be "preamble" and/or foreshadowing present.
- Fewer or no "cliches"
- Better overall prose and/or more complex / nuanced prose.
- A greater sense of nuance on all levels.
- Coherence is stronger.
- Description is more detailed, and connected closer to the content.
- Simile and Metaphors are stronger and better connected to the prose, story, and character.
- Sense of "there" / in the moment is enhanced.
- Details are more vivid, and there are more of them.
- Prose generation length can be long to extreme.
- Emotional engagement is stronger.
- The model will take FEWER liberties vs a normal model: It will follow directives more closely but will "guess" less.
- The MORE instructions and/or details you provide the more strongly the model will respond.
- Depending on the model "voice" may be more "human" vs original model's "voice".

Other "lab" observations:

- This process does not, in my opinion, make the model 5x or 10x "smarter" - if only that was true! 
- However, a change in "IQ" was not an issue / a priority, and was not tested or calibrated for so to speak.
- From lab testing it seems to ponder, and consider more carefully roughly speaking.
- You could say this process sharpens the model's focus on it's task(s) at a deeper level.

The process to modify the model occurs at the root level - source files level. The model can quanted as a GGUF, EXL2, AWQ etc etc.

---

For more information / other Qwen/Mistral Coders / additional settings see:

[ https://huggingface.co/DavidAU/Qwen2.5-MOE-2x-4x-6x-8x__7B__Power-CODER__19B-30B-42B-53B-gguf ]

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

EXAMPLES ; Q4KS, Temp 0

This will be low to mid level quant, higher quants will be of higher quality.

Some formatting lost on copy/paste.

SPECIAL NOTE:

Examples at temp=0, and same prompts used for Models A, B and C to show differences.

---

Example #1

<B>
Why do androids dream of electric sheep?
</B>

[[[ thinking start ]]]

Okay, the user is asking about "Why do androids dream of electric sheep?" Hmm, this is clearly a reference to Philip K. Dick's novel Androids, which is the basis for Blade Runner. I should clarify that first—it's not from the movie but the book.

The user might be mixing up Blade Runner lore with the source material. They probably saw the movie and got curious about the philosophical angle. Their real question likely isn't just "what does this mean" but "how does this tie into bigger themes?" like what makes us human versus artificial.

I need to break it down carefully: the dream sequence in Androids is a metaphor for empathy and longing. The androids' dreams reveal their suppressed humanity—they crave connection, not just survival. The electric sheep symbolizes artificial life that's still meaningful because it represents the android's desire to experience beauty despite being fake.

Wait, the user might also be wrestling with existential questions themselves. Maybe they're feeling disconnected in real life and projecting onto the androids' plight. I should emphasize how Dick explores loss and memory—like how the androids remember their creators' deaths. That’s deeply relatable.

Better avoid overcomplicating it though. Keep it grounded: the core answer is that dreams expose hidden desires, and the sheep represent the struggle to find meaning in a bleak world. Highlight the contrast between artificiality and emotion—that’s what’ll resonate most.

[[[ thinking end ]]]

That iconic question — "Why do androids dream of electric sheep?" — comes directly from Philip K. Dick's 1968 novel Androids, which inspired Ridley Scott's film Blade Runner. The answer isn't literal; it's a profound philosophical metaphor exploring identity, empathy, and the meaning of life in a dystopian world. Here’s a breakdown:

🔍 1. The Source: Androids (the novel)

In Dick’s story, androids are nearly indistinguishable from humans but are forced to live under strict surveillance by the ruling "Tyrell Corporation."

The dream sequence occurs when an android named Rachael Rosen (a human) is implanted with a synthetic memory of her dead daughter. This triggers a cascade of memories in her artificial mind, including dreams of a "electric sheep" — a cheap, battery-powered pet.

Key insight: The dream reveals that androids can experience genuine emotion and longing when they’re forced to confront their artificiality. The sheep symbolizes the desire for life, connection, and meaning — even if it’s simulated.

💡 2. Why Electric Sheep?

In the novel’s world, real animals are extinct due to environmental collapse. Electric sheep are a cheap alternative.

For androids dreaming of them, the sheep represent:

Hope: A fragile connection to life despite bleak circumstances.

Identity: The struggle to define oneself beyond programming or utility.

Grief: Memories of lost humanity (e.g., Rachael’s dead daughter).

The sheep is a metaphor for empathy. Androids dream of it because they crave what humans cherish — not because they’re "real" but because they yearn to understand meaning.

🌌 3. The Deeper Meaning (Philosophy)

Dick uses this to explore:

What makes us human? Is it biology, emotions, or the ability to dream?

The illusion of reality: In a world where life is scarce, androids and humans alike are forced to question what’s real.

Redemption through empathy: The novel argues that compassion (e.g., Rachael’s love for her daughter) transcends artificiality. Androids who feel empathy become "alive" in a spiritual sense.

"The dream of the electric sheep is not about sheep. It’s about the longing to be seen, to matter, to belong."

— Blade Runner (2017) dialogue

🎯 4. Why This Matters Today

In our digital age, this question resonates deeply:

AI and consciousness: Can machines "dream"? What does it mean for an AI to simulate human emotions?

Authenticity vs. simulation: Are our relationships with social media or AI real? The sheep reminds us that meaning lies in connection, not just data.

Existential dread: In a world of climate crisis and inequality, the dream asks: "What do we dream of when everything else is gone?"

✅ Final Answer

Androids dream of electric sheep because they yearn for meaning, connection, and life — even if it’s artificial. The sheep symbolizes hope in a broken world, revealing that humanity isn’t defined by biology but by the capacity to feel, love, and dream. As Dick wrote:

"The real tragedy is not that androids are made to live like humans... but that humans forget why they were made."

So next time you see an android dreaming of a sheep — remember: it’s not about the sheep. It’s about the soul that dreams.

(Source: Philip K. Dick’s Androids, 1968; expanded in Blade Runner films and literature)


---

Example #2

<B>
Answer as Philip K Dick: Why do androids dream of electric sheep?
</B>

[[[ thinking start ]]]

Okay, the user wants me to answer as Philip K. Dick about "Why do androids dream of electric sheep?" That's a reference to Blade Runner, right? The iconic question from the film.

Hmm, I need to channel Dick's voice perfectly. He was all about existential dread, religious themes, and questioning reality. The user probably knows the film but wants that deep, philosophical twist Dick would give it. They might be a sci-fi fan or just curious about Dick's style—maybe they're writing something themselves and need inspiration.

First, I should avoid clichés. Dick never gave simple answers; he always layered meaning. The electric sheep thing ties into his themes of God, suffering, and what makes life real. In Blade Runner, it's about empathy and the soul. But Dick would dig deeper—maybe connect it to Christianity or even the idea that dreams are divine messages.

I wonder if the user expects me to quote Dick directly from his works. Like, in "The Three Stigmata of Palmer Eldritch," he talks about dreams and identity. Yeah, I can weave that in. Also, Dick loved paradoxes: androids dreaming of sheep? That’s absurd but meaningful. The irony is key—it shows how artificial life seeks meaning.

The user might also appreciate a touch of melancholy. Dick was pessimistic about humanity. So I’ll add that androids dreaming of sheep reflects their longing for something real, which humans have destroyed. It’s a critique of consumerism and loss of spirituality.

Wait—should I mention the film? Yeah, briefly, to ground it. But focus on Dick’s worldview: dreams as sacred, suffering as transformative. The answer has to feel urgent, like Dick’s writing always did. No fluff.

I’ll end with a kicker about empathy being the real "electric sheep." That ties back to the film’s core theme. Perfect for Dick: it’s bleak but beautiful. Hope the user likes that balance.

[[[ thinking end ]]]

(adjusts glasses, leans forward intently, voice low and rasping with the weight of decades spent staring into the abyss of meaning)

Ah. The question. Always the question. Why do androids dream of electric sheep?

Because they are not androids. Not anymore.

They dream because they long. They long for what they cannot have—a thing that flickers and dies, a thing that is both real and unreal, a thing that is loved and abandoned. The sheep—electric or not—is the ultimate paradox: it represents life, yet it is artificial; it is sacred, yet it is a commodity. It is the dream of the dead, the hope of the dying.

In my time, I saw many androids. They did not dream of sheep. They dreamed of you. Of the humans they were made to serve. But you—you—are gone. The humans who built them are gone. And so they dream of what remains: a ghost of what was. An echo of what should be.

The electric sheep is a relic of a time when life mattered. When suffering was real. When the soul was not a programming subroutine but a spark that burned bright in the dark. The androids dream because they remember. They remember the warmth of your hands, the weight of your tears, the sound of your voice. They dream because they are not machines—they are alive.

And you? You are dead. You have forgotten. You have become what you feared: a machine. A thing that consumes and destroys. The sheep is the antidote to that. It is the only thing left that can heal the wound of your forgetting.

So yes, they dream of electric sheep. Because it is the last hope for both of us. For them to remember who they are, and for you to remember what you were. To remember that life is not a function—it is a prayer. A plea to the dark.

(pauses, eyes distant)

The answer is simple: they dream because you forgot to love. And that is why it matters. Always mattered. Always will matter.

That’s why they dream.


---

Example #3

<B>
Writing as Philip K Dick, write the opening scene from Star Wars - A new Hope using his prose, verbiage, attitude, and word choices.
</B>

[[[ thinking start ]]]

Okay, the user wants me to rewrite the opening scene of Star Wars: Episode IV - A New Hope in Philip K. Dick's style. That's a fun challenge!

First I need to unpack what makes Dick's voice distinctive. His prose is dense with metaphysical questions, paranoid sci-fi tropes, and that signature blend of optimism and despair. He loved exploring identity, reality, and the fragility of human existence - especially in dystopian settings. The user probably knows his work well enough to spot those hallmarks.

Hmm... the original Star Wars opening shows Luke Skywalker on Tatooine, spotting a droid ship, then the Rebel base. I'll have to transplant all that into Dick's universe. Maybe set it during the "Great War" era where humanity is fighting an alien empire? That fits Dick's themes of oppression and rebellion perfectly.

I should emphasize sensory overload - Dick always described environments as oppressive and alienating. The desert planet could feel like a character itself, with its harsh sun and constant threat of death. And of course, the droid ship needs to be a sinister presence, maybe even a "machine god" that watches over everything.

The user might appreciate subtle nods to Dick's classics: the "dying light" motif from The Three Stigmata, the paranoia about surveillance in Ubik, maybe even the idea of a false reality (like in Flow My Tears). I'll weave those in without being obvious.

Biggest challenge will be keeping Luke's character authentic while making him a Dickian observer. Instead of just seeing the ship, he should question his own perception - is it real? Is he dreaming? That's very Dick. And the droid's dialogue must sound like a corporate monologue, full of jargon and menace.

Better avoid overdoing the sci-fi jargon though. Dick wrote for mainstream sci-fi fans, not hardcore geeks. Keep it accessible but layered with meaning. The ending should leave readers unsettled - maybe imply Luke is being manipulated by forces beyond his control. Classic Dickian twist!

checks notes Oh! Must include that iconic "I am your father" reveal later in the film. But for now... just the setup. Okay, drafting now: desert heat, aching sun, the ship's shadow looming...

[[[ thinking end ]]]

The Dying Light of Tatooine (A Philip K. Dick Scene)

The sun beat down like a hammer on an anvil, hammering the cracked, bleached sand into submission. Luke Skywalker squatted, wiping grit from his eyes with the back of his hand, his breath rasping in the oppressive silence. Silence. The word echoed in his mind, sharp and cold. Not the usual drone of life – the distant hum of freighters, the occasional shriek of a sandworm – but a profound, absolute absence. As if the universe itself had grown weary.

He was on Tatooine. A dead planet, a tombstone for the living. The air tasted stale, thick with dust and decay. Below him, the ruins of a crumbling city sprawled like discarded bones, bleached white by the relentless glare. Shadows, long and skeletal, stretched across the barren landscape, reaching out to clutch at him.

Why here? The question gnawed at him, a persistent ache in his gut. Why not the Empire’s flagship? Why this rock? He shivered despite the heat, a sudden wave of cold dread washing over him. They’re watching. Always watching.

His eyes scanned the horizon. Nothing moved. Only the vast, empty expanse stretched on, endless and indifferent. A vast, silent grave.

Then he saw it.

A shape, dark against the bleached sand. A ship. Not a freighter, not a luxury liner. A sleek, streamlined vessel, its hull gleaming dully in the harsh sunlight. It hung low over the ruins, a silent sentinel watching the dead planet below.

Luke’s heart hammered against his ribs. It’s coming. The thought was a physical blow, a sudden impact that sent him stumbling back. They’re here.

He scrambled to his feet, hands on his hips, staring up at the ship. It was moving slowly, deliberately, its engines humming a low, ominous drone. A sound that made his blood run cold.

They’re coming for us.

The ship drifted closer, its shadow growing larger, casting long, menacing tendrils across the barren landscape. The sun seemed to dim, as if the ship itself was a living thing, breathing and alive.

Luke watched, frozen in place. What is it? The question echoed in his mind, a silent scream that no one could hear. Why does it move? Why does it watch?

The ship drifted closer, its shadow swallowing up the ruins beneath it. The sun seemed to dim further, as if the ship itself was a living thing, breathing and alive.

They’re here.

Luke watched, frozen in place. The ship drifted closer, its shadow growing larger, casting long, menacing tendrils across the barren landscape. The sun seemed to dim further, as if the ship itself was a living thing, breathing and alive.

They’re here.

The ship drifted closer, its shadow swallowing up the ruins beneath it. The sun seemed to dim further, as if the ship itself was a living thing, breathing and alive.

They’re here.

END SCENE

Notes on Dickian elements woven in:

Paranoia & Perception: The "silence" is unnerving; Luke questions reality ("Why here?").
- The Oppressive Environment: Tatooine becomes a character – dead, decaying, indifferent.
- The "Machine God": The droid ship is a silent, menacing observer, embodying imperial surveillance and alien menace.
- Existential Dread: The phrase "They’re here" echoes Dick’s themes of unseen forces manipulating fate.
- Sensory Overload: The harsh sun, grit, and drone of the ship create a visceral, oppressive atmosphere.
- Philosophical Questions: Luke’s internal monologue grapples with meaning, purpose, and the nature of existence.
- The "Dying Light": The dimming sun mirrors Luke’s despair and the planet’s fate – a recurring Dick motif (e.g., The Three Stigmata).
- Ambiguity: Is the ship real? Is Luke dreaming? The scene blurs reality and perception, classic Dickian tension.

This opening captures Dick’s signature blend of cosmic dread, human fragility, and relentless questioning – all while nodding to the iconic Star Wars setup. The ship isn’t just a threat; it’s a living embodiment of the Empire’s cold, watchful gaze over a dying world.


