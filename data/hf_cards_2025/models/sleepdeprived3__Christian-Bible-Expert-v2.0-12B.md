---
license: apache-2.0
language:
- en
base_model:
- mistralai/Mistral-Nemo-Instruct-2407
base_model_relation: finetune
pipeline_tag: text-generation
tags:
- Christian
- Bible
- Theology
- Jesus
- Non-Denominational
- Evangelical
---
<style>
body {
    font-family: 'Quicksand', sans-serif;
    background: linear-gradient(135deg, #0a1a1a 0%, #001010 100%);
    color: #e1ffff !important;
    text-shadow: 0 0 3px rgba(0, 0, 0, 0.7);
    margin: 0;
    padding: 20px;
    transition: all 0.5s ease;
}

@media (prefers-color-scheme: light) {
    body {
        background: linear-gradient(135deg, #e1ffff 0%, #c0f0ff 100%);
        color: #002b36 !important;
        text-shadow: 0 0 3px rgba(255, 255, 255, 0.7);
    }
}

.container {
    min-width: 100%;
    margin: 0 auto;
    max-width: 1200px;
    background: rgba(0, 17, 22, 0.95);
    border-radius: 12px;
    padding: 30px;
    box-shadow: 0 0 20px rgba(0, 255, 255, 0.1);
    border: 1px solid rgba(0, 255, 255, 0.2);
    position: relative;
    overflow: hidden;
}

.container::before {
    content: '';
    position: absolute;
    top: -1px;
    left: -1px;
    right: -1px;
    bottom: -1px;
    border: 1px solid rgba(0, 255, 255, 0.5);
    border-radius: 12px;
    pointer-events: none;
    animation: borderGlow 3s ease-in-out infinite alternate;
}

@keyframes borderGlow {
    0% {
        box-shadow: 0 0 5px rgba(0, 255, 255, 0.3);
        border-color: rgba(0, 255, 255, 0.5);
    }
    50% {
        box-shadow: 0 0 15px rgba(0, 100, 255, 0.3);
        border-color: rgba(0, 100, 255, 0.5);
    }
    100% {
        box-shadow: 0 0 5px rgba(0, 255, 255, 0.3);
        border-color: rgba(0, 255, 255, 0.5);
    }
}

.header {
    text-align: center;
    margin-bottom: 30px;
    position: relative;
}

.header::after {
    content: '';
    position: absolute;
    bottom: -15px;
    left: 25%;
    right: 25%;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(0, 255, 255, 0.5), transparent);
    animation: scanline 8s linear infinite;
}

@keyframes scanline {
    0% { background-position: -100% 0; }
    100% { background-position: 200% 0; }
}

.model-name {
    color: #00ffff;
    font-size: 2.5em;
    text-shadow: 0 0 15px rgba(0, 255, 255, 0.5);
    margin: 0;
    letter-spacing: -1px;
    animation: textGlow 4s ease-in-out infinite alternate;
}

@keyframes textGlow {
    0% { text-shadow: 0 0 15px rgba(0, 255, 255, 0.5); }
    50% { text-shadow: 0 0 20px rgba(0, 100, 255, 0.5); }
    100% { text-shadow: 0 0 15px rgba(0, 255, 255, 0.5); }
}

.subtitle {
    color: #00ffcc;
    font-size: 1.2em;
    margin-top: 10px;
    animation: subtitleFade 6s ease-in-out infinite;
}

@keyframes subtitleFade {
    0%, 100% { opacity: 0.8; }
    50% { opacity: 1; }
}

.bible-container {
    margin: 20px -30px;
    width: calc(100% + 60px);
    overflow: hidden;
    border-radius: 8px;
    border: 1px solid rgba(0, 255, 255, 0.3);
    position: relative;
}

.bible-container::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(45deg,
        rgba(0, 255, 255, 0.1) 0%,
        transparent 20%,
        transparent 80%,
        rgba(0, 100, 255, 0.1) 100%);
    pointer-events: none;
    animation: gradientSlide 10s linear infinite;
}

@keyframes gradientSlide {
    0% { background-position: 0% 0%; }
    100% { background-position: 100% 100%; }
}

.bible-img {
    width: 100%;
    height: auto;
    border-radius: 0;
    border: none;
    box-shadow: 0 0 40px rgba(0, 255, 255, 0.2);
    transition: transform 0.5s ease;
}

.bible-img:hover {
    transform: scale(1.01);
}

.section {
    color: #e1ffff;
    margin: 25px 0;
    padding: 20px;
    background: rgba(5, 25, 35, 0.9);
    border-radius: 8px;
    border: 1px solid rgba(0, 255, 255, 0.15);
    position: relative;
    transition: all 0.3s ease;
}

.section:hover {
    border-color: rgba(0, 100, 255, 0.3);
    box-shadow: 0 0 15px rgba(0, 255, 255, 0.1);
}

.section::before {
    content: '';
    position: absolute;
    top: -1px;
    left: -1px;
    right: -1px;
    bottom: -1px;
    border: 1px solid rgba(0, 255, 255, 0.3);
    border-radius: 8px;
    pointer-events: none;
    animation: sectionPulse 5s ease-in-out infinite;
}

@keyframes sectionPulse {
    0%, 100% { opacity: 0.7; }
    50% { opacity: 0.3; }
}

.section-title {
    color: #00ffff;
    font-size: 1.8em;
    margin-top: 0;
    text-shadow: 0 0 5px rgba(0, 255, 255, 0.3);
    position: relative;
    display: inline-block;
}

.section-title::after {
    content: '';
    position: absolute;
    bottom: -5px;
    left: 0;
    width: 100%;
    height: 1px;
    background: linear-gradient(90deg, rgba(0, 255, 255, 0.5), rgba(0, 100, 255, 0.5));
    transform: scaleX(0);
    transform-origin: left;
    transition: transform 0.3s ease;
}

.section:hover .section-title::after {
    transform: scaleX(1);
}

.quant-links {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 15px;
    margin: 20px 0;
}

.link-card {
    padding: 15px;
    background: rgba(20, 35, 45, 0.95);
    border-radius: 8px;
    transition: all 0.3s ease;
    border: 1px solid rgba(0, 255, 255, 0.1);
    position: relative;
    overflow: hidden;
}

.link-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 2px;
    background: linear-gradient(90deg, rgba(0, 255, 255, 0.5), rgba(0, 100, 255, 0.5));
    animation: cardScan 4s linear infinite;
}

@keyframes cardScan {
    0% { transform: translateX(-100%); }
    100% { transform: translateX(100%); }
}

.link-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 5px 15px rgba(0, 255, 255, 0.2);
    border-color: rgba(0, 100, 255, 0.3);
}

.link-card h3 {
    margin-top: 0;
    color: #e1ffff !important;
}

.link-button {
    display: inline-flex;
    align-items: center;
    background: rgba(0, 255, 255, 0.1);
    color: #e1ffff !important;
    padding: 8px 15px;
    border-radius: 6px;
    text-decoration: none;
    border: 1px solid rgba(0, 255, 255, 0.3);
    margin: 5px 0;
    transition: all 0.3s ease;
    font-size: 0.95em;
    position: relative;
    overflow: hidden;
}

.link-button::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
    transition: all 0.5s ease;
}

.link-button:hover {
    background: rgba(0, 255, 255, 0.2);
    border-color: rgba(0, 255, 255, 0.5);
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 255, 255, 0.2);
}

.link-button:hover::before {
    left: 100%;
}

.link-button::after {
    content: '→';
    margin-left: 8px;
    opacity: 0.7;
    transition: all 0.3s ease;
}

.link-button:hover::after {
    transform: translateX(3px);
    opacity: 1;
}

.button-group {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin: 15px 0;
}

.disclaimer {
    color: #00ff99;
    border-left: 3px solid #00ff99;
    padding-left: 15px;
    margin: 20px 0;
    position: relative;
}

.disclaimer::before {
    content: '⚠️';
    position: absolute;
    left: -10px;
    top: 0;
    transform: translateX(-100%);
    animation: pulse 2s ease-in-out infinite;
}

@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.5; }
}

.badge {
    display: inline-block;
    padding: 5px 10px;
    border-radius: 5px;
    background: rgba(0, 255, 255, 0.1);
    border: 1px solid #00ffff;
    margin: 5px;
    font-size: 0.9em;
    animation: badgePulse 3s ease-in-out infinite;
}

@keyframes badgePulse {
    0%, 100% { box-shadow: 0 0 5px rgba(0, 255, 255, 0.3); }
    50% { box-shadow: 0 0 10px rgba(0, 255, 255, 0.5); }
}

/* Light mode adjustments */
@media (prefers-color-scheme: light) {
    .container {
        background: rgba(224, 255, 255, 0.95);
        border-color: rgba(0, 150, 150, 0.3);
    }

    .model-name, .section-title, .subtitle {
        color: #006666;
        text-shadow: 0 0 5px rgba(0, 200, 200, 0.3);
    }

    .section {
        background: rgba(200, 250, 255, 0.9);
        border-color: rgba(0, 200, 200, 0.2);
        color: #002b36;
    }

    .link-card {
        background: rgba(150, 230, 255, 0.95);
        border-color: rgba(0, 150, 150, 0.2);
    }

    .link-card h3 {
        color: #002b36 !important;
    }

    .link-button {
        background: rgba(0, 150, 150, 0.1);
        color: #002b36 !important;
        border-color: rgba(0, 150, 150, 0.3);
    }

    .link-button:hover {
        background: rgba(0, 150, 150, 0.2);
        border-color: rgba(0, 150, 150, 0.5);
    }

    .disclaimer {
        color: #008080;
        border-color: #008080;
    }

    .badge {
        border-color: #008080;
        background: rgba(0, 150, 150, 0.1);
    }
}
</style>

<div class="container">

<div class="header">
    <h1 class="model-name">Christian Bible Expert v2.0 12B</h1>
    <p class="subtitle">Where Biblical Truth Meets Theological Depth</p>
</div>

<div class="section">
    <h2 class="section-title">✝️ Theological Foundation</h2>
    <p>This enhanced version delivers coherent biblical analysis with unprecedented depth:</p>
    <ul>
        <li>📖 <strong>Expanded 4x Training Data</strong> - Incorporating ecumenical Christian theological texts and comprehensive exegesis</li>
        <li>⚡ <strong>Optimized Architecture</strong> - Smoother theological reasoning with improved consistency</li>
        <li>💎 <strong>Balanced Interpretation</strong> - Maintains Nicene Creed orthodoxy while respecting denominational diversity</li>
        <li>🎓 <strong>Enhanced Ministry Applications</strong> - Improved Bible study generation and spiritual formation</li>
        <li>🌹 <strong>Spiritual Depth</strong> - Provides profound biblical insights with practical application</li>
    </ul>
</div>

<div class="section">
    <h2 class="section-title">⚙️ Technical Specifications</h2>
    <p><strong>FULL SETTINGS and an optional Pastor character card</strong> <a href="https://huggingface.co/sleepdeprived3/Pastor-Luke-V3" class="link-button">Pastor-Luke-V3</a></p>
    <div class="quant-links">
        <div class="link-card">
            <h3>GGUF</h3>
            <a href="https://huggingface.co/mradermacher/Christian-Bible-Expert-v2.0-12B-GGUF" class="link-button">Quants</a>
        </div>
        <div class="link-card">
            <h3>imatrix</h3>
            <a href="https://huggingface.co/mradermacher/Christian-Bible-Expert-v2.0-12B-i1-GGUF" class="link-button">Quants</a>
        </div>
        <div class="section">
        Recommended deterministic sampler for maximum Biblical accuracy.
        "temperature": 0
        "top_k": 1
        "dry_multiplier": 0.01
        </div>
    </div>
</div>

<div class="section">
    <h2 class="section-title">📜 Key Features</h2>
    <ul>
        <li>🕊️ Answers theological questions from a Nicene Christian perspective</li>
        <li>✝️ Explains Scripture using historical-grammatical interpretation with emphasis on core Christian doctrines</li>
        <li>🌍 Multilingual support for ministry in 10+ languages (English, Spanish, French, Korean, etc.)</li>
        <li>🎓 Enhanced capabilities for Bible study generation and spiritual formation</li>
        <li>💬 Advanced roleplaying for discipleship and spiritual growth scenarios</li>
        <li>📖 Focuses on essential Christian doctrines as expressed in the Nicene Creed</li>
    </ul>
</div>

<div class="section">
    <h2 class="section-title">⚠️ Ethical Considerations</h2>
        <p>This model is designed to:</p>
        <ul>
            <li>Maintain strict fidelity to the Nicene Creed and core Christian doctrines</li>
            <li>Promote biblical authority and Christ-centered interpretation</li>
            <li>Support but never replace local church leadership and pastoral counsel</li>
        </ul>
</div>

<div class="section">
    <h2 class="section-title">📖 Performance Notes</h2>
    <ul>
        <li>🔥 Maintains theological accuracy with improved narrative flow</li>
        <li>📖 Handles complex biblical analysis with improved consistency</li>
        <li>🧠 Excels at long-form theological discussions without losing track of doctrinal threads</li>
        <li>⚡ Noticeably better at following complex exegetical instructions than previous versions</li>
        <li>🎭 Responds to subtle theological nuances with precision</li>
    </ul>
</div>

<div class="section">
    <h2 class="section-title">🧑‍🔬 Model Authors</h2>
    <ul>
        <li>sleepdeprived3 (Training Data & Fine-Tuning)</li>
    </ul>
</div>

<script>
[Previous JavaScript remains identical]
</script>
