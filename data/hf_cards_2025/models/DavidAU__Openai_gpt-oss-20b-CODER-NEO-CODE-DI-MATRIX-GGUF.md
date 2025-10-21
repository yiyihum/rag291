---
license: apache-2.0
base_model:
- openai/gpt-oss-20b
language:
- en
pipeline_tag: text-generation
tags:
- gpt_oss
- gpt-oss
- openai
- mxfp4
- programming
- code generation
- code
- coding
- coder
- chat
- code
- chat
- reasoning
- thinking
- r1
- cot
- deepseek
- 128k context
- general usage
- problem solving
- brainstorming
- solve riddles
- general usage
- openai
- Neo
- MOE
- Mixture of Experts
- 24 experts
- NEO Imatrix
- Code Imatrix
- DI-Matrix
- Dual Imatrix
- Imatrix
---

<small><font color="red">Specialized quants (including "MXFP4_MOE.gguf") for new OpenAI 20B MOE - Mixture of Experts Model at 80+ t/s.</font></small>

<h2>Openai_gpt-oss-20b-CODER-NEO-CODE-DI-MATRIX-GGUF</h2>

<img src="matrix2.webp" style="float:right; width:300px; height:300px; padding:10px;"> 

These are DUEL NEO Imatrix / CODE IMATRIX GGUFs, NEO dataset by DavidAU with "Code" dataset compiled by DavidAU.

NEO dataset improves overall performance. 

CODER dataset is specifically for coding performance.

Example generation provided at bottom of this page.

DUEL ("DI")-> Separate Imatrix datasets ("NEO" and "CODER" - generated separately per model) are co-joined to create a new Imatrix dataset, which is then applied to the quants.

Model also passed "hard" coding test too (4 experts); no issues (IQ4_NL).

TEST: Forcing the model to create code with no dependencies and limits of coding short cuts, with multiple loops, and in real time with no blocking in a language that does not support it normally.

(example prompt, and generation below)

Due to quanting issues with this model (which result in oddball quant sizes / mixtures), only TESTED quants will be uploaded (at the moment).

Currently that means IQ4_NL, and <B>MXFP4_MOE</b> (a new OpenAI specific quant type) are available.

NEO/Coder datasets performance improvements will show the most in the IQ4_NL quants.

There are TWO "IQ4_NL" quants:
- OpenAI-20B-NEO-CODE-DIMAT-IQ4_NL.gguf : DI Imatrix applied.
- OpenAI-20B-NEO-CODE-DIMAT-2-IQ4_NL.gguf : DI Imatrix applied, including output tensor (also imatrixed), and embed tensor at IQ4_NL.

There are THREE NEO MXFP4_MOE quants:
- OpenAI-20B-NEO-CODE-DIMAT-MXFP4_MOE2.gguf : Output tensor Q5_1 (DI Imatrix applied)
- OpenAI-20B-NEO-CODE-DIMAT-MXFP4_MOE3.gguf : Output tensor IQ4_NL (DI Imatrix applied)
- OpenAI-20B-NEO-CODE-DIMAT-MXFP4_MOE4.gguf : Output tensor IQ4_NL (DI Imatrix applied) AND Embed at IQ4_NL - this makes this quant the smallest version.

MXFP4_MOE quants vastly outperform (at the moment) all other quants, except IQ4_NL, Q5_1 and Q8_0 due to odd
issues compressing OpenAI's 20B model due to odd "tensor" dimensions. 

( IQ4_NL, Q5_1 and Q8_0 quants are compatible with OpenAI's tensor structure as of this writing. )

MXFP4_MOE quant was specifically designed for (what appears to be) loss less quantization relative to source model. Jury still out on this.

Suggested Settings (tested in Lmstudio, Beta Branch 0.3.21 ; 4 ):

- Context: 8k min.
- Temp 1.2+ for creative. Temp .6 (or so) for coding/general.
- Rep pen 1.1, topk 40, topp .95, min p 0.05
- Experts 4-8 depending on use case. (higher than 8 MAY lower quality)

Model Supports:
- 128k context
- up to 24 experts
- Tools use, browsing, etc 

For my help docs, SETTING NUMBER OF EXPERTS, and other see below.

See more about this model here:

https://huggingface.co/openai/gpt-oss-20b

Please refer to their model card, especially to control "thinking" levels.

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

<h2>Example Generation</h2>

Using default settings (coder), 4 experts and no system prompt.

---

Prompt:

<b>

Write a JavaScript for fetch api using 4 ais, all using streaming that does NOT use "promise.all", and processes all streams separately but in real time - that means all streams need to be processed at the same time and not interrupt each other.

Also include sending a payload to each of the 4 ais with content, system prompt, temp, topk, topp, minp, repeat penalty ; all of these parameters will be in an array for each of the four ais.

Record the entire response - chunks - from each AI in an array - text.

Also, send the chunks in real time to 4 separate text boxes on an HTML page so real time readout from each AI can be seen by the user.

IMPORTANT: All streams must be processed at the same time, not in sequence. IMPORTANT: Do not use any dependencies, nor import any module(s).

</b>

OUTPUT: 

(note: Pretty print, color and some formatting lost on copy/paste)

<p style="border: none; padding: 0cm">
<span style="display: inline-block; border: none; padding: 0cm"><font color="#ff0000"><b>Thought
for 11.81 seconds</b></font></span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">We
need to write JavaScript code that uses fetch API with streaming
responses (likely using ReadableStream from
Response.body.getReader()). We have 4 AI endpoints; each will be
called with a payload containing content, system prompt, temp, topk,
topp, minp, repeat penalty. These parameters are in an array for each
of the four AIs.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">We
need to process all streams concurrently, not sequentially, and not
using Promise.all. So we can start fetch calls, get readers, then
read from each reader in separate async functions that run
concurrently (like starting them but not awaiting). We need to send
chunks in real time to 4 separate text boxes on an HTML page.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">We
cannot use dependencies or import modules; just plain JS.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">We
need to record entire response chunks per AI into arrays. So we
maintain array of strings for each AI, push each chunk as it arrives.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Also
we need to send the payload to each AI with content, system prompt,
temp, topk, topp, minp, repeat penalty. These parameters will be in
an array for each of the four AIs. So maybe we have a config array
like:</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">const
aiConfigs = [ {url: '', params: {...}}, ... ];</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">But
they said &quot;parameters will be in an array for each of the four
ais.&quot; So we can define arrays.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">We
need to send payload as JSON body. Use fetch with method POST,
headers: Content-Type: application/json, body:
JSON.stringify(payload).</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Then
handle streaming: Response.body is a ReadableStream; getReader();
read loop reading chunks (Uint8Array). Convert to string using
TextDecoder. Append to array and update UI.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">We
need to run all four concurrently but not use Promise.all. We can
just start them sequentially but not await each before starting next.
For example:</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">function
startAI(index) { ... } Then call for i=0..3: startAI(i); That will
kick off fetch calls; inside we handle reading and UI updates.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">We
need to ensure they run concurrently, so no blocking.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Also
record entire response chunks in an array per AI.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">We
also need to send the chunks in real time to 4 separate text boxes on
an HTML page. So we need to have &lt;textarea id=&quot;ai1&quot;&gt;
etc. Then update innerText or value as new chunk arrives.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">We
must not use dependencies, so no external libs.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Also
we need to handle errors.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Let's
produce code snippet with explanation.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">We'll
create a function fetchAndStream(aiIndex) that returns nothing but
handles reading and UI updates.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">We
also need to define arrays for each AI's parameters. For example:</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">const
aiParams = [ {url: '', content: 'Hello', systemPrompt: 'You are ...',
temp: 0.7, topk: 50, topp: 0.95, minp: 0.01, repeatPenalty: 2}, ...
];</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">But
they said &quot;parameters will be in an array for each of the four
ais.&quot; So we can define arrays like:</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">const
aiConfigs = [ {url: '', payload: {...}}, ... ];</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">We
need to send content, system prompt, temp, topk, topp, minp, repeat
penalty. So we can create payload object accordingly.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Also
we need to record entire response chunks in an array per AI. We'll
have const responses = [[], [], [], []]; Then push each chunk string
into responses[aiIndex].</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">We
also need to update UI: document.getElementById('output'+(i+1)).value
+= chunk; or innerText.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Let's
produce final code with comments and explanation.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Also
we need to ensure no Promise.all. So just call startAI for each
index.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Also
we need to handle fetch errors gracefully.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Also
we need to use async/await inside each function but not block others.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">We
can do:</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">async
function streamFromAi(index) { ... }</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Then
call streamFromAi(0); streamFromAi(1); etc. Since they are async
functions, calling them without await will start them concurrently.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Alternatively
we can wrap in IIFE: (async () =&gt; {...})(); But simpler: just call
them.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">We
need to ensure that the fetch calls happen concurrently; but if we
use await inside each function, it won't block others because each
function runs independently. So it's fine.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Also
we need to record entire response chunks from each AI in an array -
we can push chunk string into responses[index].</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Now
produce final code snippet with HTML skeleton and JS script.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">We
also need to mention that the fetch API must support streaming; some
browsers may not support reading body as stream? But modern ones do.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">We'll
provide fallback for older browsers maybe but not necessary.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Also
we need to ensure no dependencies, so just plain JS.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Let's
craft final answer: Provide explanation then code snippet.</span></p>
<p style="border: none; padding: 0cm"><br/>
<br/>

</p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><font color="#ff0000"><b>OUTPUT:</b></font></span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Below
is a <strong>stand&#8209;alone</strong> example that fulfils every
requirement you listed:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">4
	independent AI calls</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">All
	four streams are read&nbsp;<em>concurrently</em>&nbsp;(no&nbsp;</span><span style="display: inline-block; border: 1px solid #3b3b3b; padding: 0.05cm"><code class="western">Promise.all</code></span><span style="display: inline-block; border: none; padding: 0cm">&nbsp;or
	any other blocking construct)</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Each
	call receives its own payload
	(</span><span style="display: inline-block; border: 1px solid #3b3b3b; padding: 0.05cm"><code class="western">content</code></span><span style="display: inline-block; border: none; padding: 0cm">,&nbsp;</span><span style="display: inline-block; border: 1px solid #3b3b3b; padding: 0.05cm"><code class="western">systemPrompt</code></span><span style="display: inline-block; border: none; padding: 0cm">,&nbsp;</span><span style="display: inline-block; border: 1px solid #3b3b3b; padding: 0.05cm"><code class="western">temp</code></span><span style="display: inline-block; border: none; padding: 0cm">,&nbsp;</span><span style="display: inline-block; border: 1px solid #3b3b3b; padding: 0.05cm"><code class="western">topk</code></span><span style="display: inline-block; border: none; padding: 0cm">,&nbsp;</span><span style="display: inline-block; border: 1px solid #3b3b3b; padding: 0.05cm"><code class="western">topp</code></span><span style="display: inline-block; border: none; padding: 0cm">,&nbsp;</span><span style="display: inline-block; border: 1px solid #3b3b3b; padding: 0.05cm"><code class="western">minp</code></span><span style="display: inline-block; border: none; padding: 0cm">,&nbsp;</span><span style="display: inline-block; border: 1px solid #3b3b3b; padding: 0.05cm"><code class="western">repeatPenalty</code></span><span style="display: inline-block; border: none; padding: 0cm">)
	– the values are stored in an array of objects.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Every
	chunk that arrives is pushed into a per&#8209;AI array and written
	immediately to a dedicated&nbsp;</span><span style="display: inline-block; border: 1px solid #3b3b3b; padding: 0.05cm"><code class="western">&lt;textarea&gt;</code></span><span style="display: inline-block; border: none; padding: 0cm">&nbsp;so
	the user can see the output live.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">No
	external libraries or imports – pure vanilla JavaScript.</span></p></li>
</ul>
<hr/>

<h2 class="western" style="border-top: none; border-bottom: 1px solid #3b3b3b; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm">
<span style="display: inline-block; border: none; padding: 0cm">1️⃣
HTML skeleton</span></h2>
<pre class="western" style="border: 1px solid #3b3b3b; padding: 0.05cm"><span style="display: inline-block; border: none; padding: 0cm"><code class="western">&lt;!DOCTYPE html&gt;</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">&lt;html lang=&quot;en&quot;&gt;</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">&lt;head&gt;</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">&lt;meta charset=&quot;utf-8&quot;&gt;</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">&lt;title&gt;Concurrent AI Streaming Demo&lt;/title&gt;</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">&lt;style&gt;</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">        </code><code class="western">textarea { width:100%; height:150px; margin-bottom:10px;}</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">&lt;/style&gt;</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">&lt;/head&gt;</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">&lt;body&gt;</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">&lt;!-- Four output boxes --&gt;</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">&lt;textarea id=&quot;output0&quot; placeholder=&quot;AI #1 …&quot;&gt;&lt;/textarea&gt;</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">&lt;textarea id=&quot;output1&quot; placeholder=&quot;AI #2 …&quot;&gt;&lt;/textarea&gt;</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">&lt;textarea id=&quot;output2&quot; placeholder=&quot;AI #3 …&quot;&gt;&lt;/textarea&gt;</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">&lt;textarea id=&quot;output3&quot; placeholder=&quot;AI #4 …&quot;&gt;&lt;/textarea&gt;</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">&lt;!-- Start button --&gt;</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">&lt;button id=&quot;startBtn&quot;&gt;Start All 4 AIs&lt;/button&gt;</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">&lt;script src=&quot;ai-stream.js&quot;&gt;&lt;/script&gt;   &lt;!-- the script below --&gt;</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">&lt;/body&gt;</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">&lt;/html&gt;</code></span></pre>
<hr/>

<h2 class="western" style="border-top: none; border-bottom: 1px solid #3b3b3b; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm">
<span style="display: inline-block; border: none; padding: 0cm">2️⃣
JavaScript (</span><span style="display: inline-block; border: 1px solid #3b3b3b; padding: 0.05cm"><code class="western">ai-stream.js</code></span><span style="display: inline-block; border: none; padding: 0cm">)</span></h2>
<pre class="western" style="border: 1px solid #3b3b3b; padding: 0.05cm"><span style="display: inline-block; border: none; padding: 0cm"><code class="western">/* -------------------------------------------------------------</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western"> </code><code class="western">* 1.  Configuration – one object per AI</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western"> </code><code class="western">* ------------------------------------------------------------- */</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">const aiConfigs = [</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">{</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">        </code><code class="western">// URL of the first AI endpoint</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">        </code><code class="western">url: 'https://api.example.com/v1/chat',</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">        </code><code class="western">payload: {</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">            </code><code class="western">content:      &quot;Hello, what can you do?&quot;,</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">            </code><code class="western">systemPrompt: &quot;You are a helpful assistant.&quot;,</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">            </code><code class="western">temp:         0.7,</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">            </code><code class="western">topk:         50,</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">            </code><code class="western">topp:         0.95,</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">            </code><code class="western">minp:         0.01,</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">            </code><code class="western">repeatPenalty: 2</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">        </code><code class="western">}</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">},</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">{</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">        </code><code class="western">url: 'https://api.example.com/v1/chat',</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">        </code><code class="western">payload: {</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">            </code><code class="western">content:      &quot;Tell me a joke.&quot;,</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">            </code><code class="western">systemPrompt: &quot;You are a funny chatbot.&quot;,</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">            </code><code class="western">temp:         0.8,</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">            </code><code class="western">topk:         40,</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">            </code><code class="western">topp:         0.9,</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">            </code><code class="western">minp:         0.02,</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">            </code><code class="western">repeatPenalty: 1</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">        </code><code class="western">}</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">},</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">{</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">        </code><code class="western">url: 'https://api.example.com/v1/chat',</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">        </code><code class="western">payload: {</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">            </code><code class="western">content:      &quot;Explain relativity.&quot;,</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">            </code><code class="western">systemPrompt: &quot;You are a physics teacher.&quot;,</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">            </code><code class="western">temp:         0.6,</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">            </code><code class="western">topk:         60,</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">            </code><code class="western">topp:         0.97,</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">            </code><code class="western">minp:         0.01,</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">            </code><code class="western">repeatPenalty: 3</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">        </code><code class="western">}</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">},</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">{</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">        </code><code class="western">url: 'https://api.example.com/v1/chat',</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">        </code><code class="western">payload: {</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">            </code><code class="western">content:      &quot;Give me a recipe for pancakes.&quot;,</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">            </code><code class="western">systemPrompt: &quot;You are a cooking expert.&quot;,</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">            </code><code class="western">temp:         0.5,</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">            </code><code class="western">topk:         30,</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">            </code><code class="western">topp:         0.85,</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">            </code><code class="western">minp:         0.02,</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">            </code><code class="western">repeatPenalty: 2</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">        </code><code class="western">}</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">}</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">];</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western">/* -------------------------------------------------------------</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western"> </code><code class="western">* 2.  Storage for the full responses (array of strings)</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western"> </code><code class="western">* ------------------------------------------------------------- */</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">const allResponses = [[], [], [], []];   // one array per AI</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western">/* -------------------------------------------------------------</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western"> </code><code class="western">* 3.  Helper – read a stream and push chunks to UI &amp; storage</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western"> </code><code class="western">* ------------------------------------------------------------- */</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">async function streamFromAi(aiIndex) {</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">const cfg = aiConfigs[aiIndex];</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">const outputBox = document.getElementById(`output${aiIndex}`);</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">const decoder = new TextDecoder('utf-8');</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">try {</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">        </code><code class="western">// 3.1  Send the request</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">        </code><code class="western">const response = await fetch(cfg.url, {</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">            </code><code class="western">method: 'POST',</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">            </code><code class="western">headers: { 'Content-Type': 'application/json' },</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">            </code><code class="western">body: JSON.stringify(cfg.payload)</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">        </code><code class="western">});</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western">        </code><code class="western">if (!response.ok) {</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">            </code><code class="western">throw new Error(`HTTP ${response.status} – ${response.statusText}`);</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">        </code><code class="western">}</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western">        </code><code class="western">// 3.2  Get the reader</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">        </code><code class="western">const reader = response.body.getReader();</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western">        </code><code class="western">// 3.3  Read loop – runs until stream ends</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">        </code><code class="western">while (true) {</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">            </code><code class="western">const { value, done } = await reader.read();</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">            </code><code class="western">if (done) break;          // no more data</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western">            </code><code class="western">// Convert Uint8Array to string</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">            </code><code class="western">const chunkText = decoder.decode(value, { stream: true });</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western">            </code><code class="western">// Store the chunk in the array</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">            </code><code class="western">allResponses[aiIndex].push(chunkText);</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western">            </code><code class="western">// Push it live into the textarea</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">            </code><code class="western">outputBox.value += chunkText;</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">        </code><code class="western">}</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western">        </code><code class="western">// Finalise – flush any remaining buffered text</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">        </code><code class="western">outputBox.value += decoder.decode();   // empty decode to flush</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">} catch (err) {</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">        </code><code class="western">console.error(`AI #${aiIndex+1} error:`, err);</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">        </code><code class="western">outputBox.value += `\n[Error] ${err.message}\n`;</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">}</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">}</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western">/* -------------------------------------------------------------</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western"> </code><code class="western">* 4.  Kick&#8209;off – start all four streams concurrently</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western"> </code><code class="western">* ------------------------------------------------------------- */</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">function startAllAIs() {</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">// Reset UI and storage</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">for (let i = 0; i &lt; 4; ++i) {</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">        </code><code class="western">document.getElementById(`output${i}`).value = '';</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">        </code><code class="western">allResponses[i] = [];</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">}</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">// Start each stream – the async function is *called* but not awaited,</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">// so they run in parallel.</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">for (let i = 0; i &lt; 4; ++i) {</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">        </code><code class="western">streamFromAi(i);   // &lt;-- no await</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">    </code><code class="western">}</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">}</code></span>

<span style="display: inline-block; border: none; padding: 0cm"><code class="western">/* -------------------------------------------------------------</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western"> </code><code class="western">* 5.  Wire up the button</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western"> </code><code class="western">* ------------------------------------------------------------- */</code></span>
<span style="display: inline-block; border: none; padding: 0cm"><code class="western">document.getElementById('startBtn').addEventListener('click', startAllAIs);</code></span></pre>
<hr/>

<h3 class="western" style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">How
it works</span></h3>
<ol>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Configuration</strong>
	– </span><span style="display: inline-block; border: 1px solid #3b3b3b; padding: 0.05cm"><code class="western">aiConfigs</code></span><span style="display: inline-block; border: none; padding: 0cm">
	holds one object per AI, each with its own payload (</span><span style="display: inline-block; border: 1px solid #3b3b3b; padding: 0.05cm"><code class="western">content</code></span><span style="display: inline-block; border: none; padding: 0cm">,
	</span><span style="display: inline-block; border: 1px solid #3b3b3b; padding: 0.05cm"><code class="western">systemPrompt</code></span><span style="display: inline-block; border: none; padding: 0cm">,
	etc.).</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Storage</strong>
	– </span><span style="display: inline-block; border: 1px solid #3b3b3b; padding: 0.05cm"><code class="western">allResponses</code></span><span style="display: inline-block; border: none; padding: 0cm">
	is an array of four arrays; every chunk that arrives for a given AI
	is pushed into the corresponding sub&#8209;array.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Streaming</strong>
	– Inside </span><span style="display: inline-block; border: 1px solid #3b3b3b; padding: 0.05cm"><code class="western">streamFromAi()</code></span><span style="display: inline-block; border: none; padding: 0cm">
	we:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Send
		a POST request with the JSON payload.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Grab
		the&nbsp;</span><span style="display: inline-block; border: 1px solid #3b3b3b; padding: 0.05cm"><code class="western">ReadableStream</code></span><span style="display: inline-block; border: none; padding: 0cm">&nbsp;from&nbsp;</span><span style="display: inline-block; border: 1px solid #3b3b3b; padding: 0.05cm"><code class="western">response.body</code></span><span style="display: inline-block; border: none; padding: 0cm">.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Use
		its&nbsp;</span><span style="display: inline-block; border: 1px solid #3b3b3b; padding: 0.05cm"><code class="western">getReader()</code></span><span style="display: inline-block; border: none; padding: 0cm">&nbsp;and
		read in a loop (</span><span style="display: inline-block; border: 1px solid #3b3b3b; padding: 0.05cm"><code class="western">reader.read()</code></span><span style="display: inline-block; border: none; padding: 0cm">).</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Each
		chunk (a&nbsp;</span><span style="display: inline-block; border: 1px solid #3b3b3b; padding: 0.05cm"><code class="western">Uint8Array</code></span><span style="display: inline-block; border: none; padding: 0cm">)
		is decoded to text, appended to the per&#8209;AI array&nbsp;<strong>and</strong>&nbsp;written
		immediately into the dedicated&nbsp;</span><span style="display: inline-block; border: 1px solid #3b3b3b; padding: 0.05cm"><code class="western">&lt;textarea&gt;</code></span><span style="display: inline-block; border: none; padding: 0cm">.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
		loop ends when&nbsp;</span><span style="display: inline-block; border: 1px solid #3b3b3b; padding: 0.05cm"><code class="western">done</code></span><span style="display: inline-block; border: none; padding: 0cm">&nbsp;becomes
		true.</span></p></li>
	</ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Concurrent
	start</strong> – In </span><span style="display: inline-block; border: 1px solid #3b3b3b; padding: 0.05cm"><code class="western">startAllAIs()</code></span><span style="display: inline-block; border: none; padding: 0cm">
	we simply call </span><span style="display: inline-block; border: 1px solid #3b3b3b; padding: 0.05cm"><code class="western">streamFromAi(i)</code></span><span style="display: inline-block; border: none; padding: 0cm">
	for each index without awaiting them. Because each function is
	async, calling it starts its own fetch and read loop immediately;
	all four loops run in parallel, so the streams are processed
	<em>simultaneously</em>.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>No
	external dependencies</strong> – everything uses only standard
	browser APIs (</span><span style="display: inline-block; border: 1px solid #3b3b3b; padding: 0.05cm"><code class="western">fetch</code></span><span style="display: inline-block; border: none; padding: 0cm">,
	</span><span style="display: inline-block; border: 1px solid #3b3b3b; padding: 0.05cm"><code class="western">ReadableStream</code></span><span style="display: inline-block; border: none; padding: 0cm">,
	</span><span style="display: inline-block; border: 1px solid #3b3b3b; padding: 0.05cm"><code class="western">TextDecoder</code></span><span style="display: inline-block; border: none; padding: 0cm">,
	DOM methods).</span></p></li>
</ol>
<hr/>

<h3 class="western" style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">What
you’ll see</span></h3>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">When
you click <strong>Start All 4 AIs</strong>, each </span><span style="display: inline-block; border: 1px solid #3b3b3b; padding: 0.05cm"><code class="western">&lt;textarea&gt;</code></span><span style="display: inline-block; border: none; padding: 0cm">
will start filling up in real time as the corresponding AI streams
its response. The full text of every AI is also kept in memory (the
</span><span style="display: inline-block; border: 1px solid #3b3b3b; padding: 0.05cm"><code class="western">allResponses</code></span><span style="display: inline-block; border: none; padding: 0cm">
arrays) so you can later inspect or export it if needed.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Feel
free to adapt the URLs, payloads, and UI layout to match your own
environment. Happy streaming!</span></p>
<p style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>