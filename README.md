<p align="center">
  <picture><source media="(max-width: 600px)" srcset="assets/hero-mobile.svg" /><img src="assets/hero.svg" width="100%" alt="Ishpreet Singh Dhamija. Building useful AI and making complex systems clear. Computer Engineering at Thapar." /></picture>
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/ishpreet-singh-351224322"><b>LinkedIn ↗</b></a> &nbsp; · &nbsp;
  <a href="#selected-work"><b>Selected work</b></a> &nbsp; · &nbsp;
  <a href="#how-the-projects-work"><b>System diagrams</b></a>
</p>

## A little about me

I'm **Ishpreet**, a Computer Engineering student at **Thapar Institute of Engineering and Technology, Patiala** (B.Tech., 2024–present). I build across **applied AI, machine learning, full-stack products, and desktop tools**.

I enjoy the part where a working model becomes a useful product: responsive interfaces, clear explanations, reliable data flows, and a person who can understand and review the result. My projects range from local semantic search and computer vision to storage explorers and interactive ML labs.

**Currently exploring:** evidence-backed AI workflows, local inference, and better ways to explain complex systems.  
**Happy to connect about:** AI/ML projects, engineering collaborations, and practical software problems.

## My toolkit

<picture><source media="(max-width: 600px)" srcset="assets/stack-mobile.svg" /><img src="assets/stack.svg" width="100%" alt="Languages: Python, TypeScript, SQL, JavaScript, C++, C. AI/ML: PyTorch, scikit-learn, OpenCV, NLP, embeddings. Product: React, Electron, Tailwind, FastAPI, Flask, REST. Data/tools: SQLite, Cloudflare D1, Drizzle, Git, Linux, Web Workers." /></picture>

<details>
<summary><b>The stack, in context</b></summary>

| Area | Technologies I work with |
| :--- | :--- |
| Languages | Python, TypeScript, JavaScript, SQL, C++, C |
| Data science & ML | Pandas, NumPy, scikit-learn, PyTorch, Jupyter, NLP |
| Local AI & vision | Sentence embeddings, semantic search, Transformers.js, ONNX Runtime, OpenCV |
| Frontend & desktop | React, Electron, HTML, CSS, Tailwind CSS, Canvas |
| APIs & persistence | FastAPI, Flask, REST APIs, SQLite, Cloudflare D1, Drizzle ORM |
| Engineering tools | Git, GitHub, Linux, Web Workers, Vite, Vitest |

</details>

## Selected work

A few projects that show how I approach products, data, and engineering. Follow the links beneath each pair to explore the source and documentation.

<picture><source media="(max-width: 600px)" srcset="assets/gallery-1-mobile.svg" /><img src="assets/gallery-1.svg" width="100%" alt="BlockIT: A clearer view of your disk. Fast filename search. Interactive treemaps. Windows portable release | CircuitSleuth: Inspect the board. Question the evidence. Adaptive PCB inspection with human review. Synthetic benchmark documented" /></picture>

<p align="center"><a href="https://github.com/ISHPREET0101/BlockIT"><b>BlockIT ↗</b></a> &nbsp; · &nbsp; <a href="https://github.com/ISHPREET0101/circuitsleuth1"><b>CircuitSleuth ↗</b></a></p>

<picture><source media="(max-width: 600px)" srcset="assets/gallery-2-mobile.svg" /><img src="assets/gallery-2.svg" width="100%" alt="Takumi: Turn demonstrations into guided practice. Capture the reasoning behind expert work. Sample demo + local processing | OpenDoor: Better directories start with evidence. Review every change before publication. Deterministic verification simulation" /></picture>

<p align="center"><a href="https://github.com/ISHPREET0101/takumi"><b>Takumi ↗</b></a> &nbsp; · &nbsp; <a href="https://github.com/ISHPREET0101/opendoor-calle"><b>OpenDoor ↗</b></a></p>

<picture><source media="(max-width: 600px)" srcset="assets/gallery-3-mobile.svg" /><img src="assets/gallery-3.svg" width="100%" alt="Synapse Memory Lab: Make attention and memory visible. Explore recurrence, decay and interference. Interactive toy-model labs | RetailPulse AI: From retail tables to customer insight. Explain the segments behind the numbers. Reproducible notebook + artifacts" /></picture>

<p align="center"><a href="https://github.com/ISHPREET0101/synapse-memory-lab-dataforge-2026"><b>Synapse Memory Lab ↗</b></a> &nbsp; · &nbsp; <a href="https://github.com/ISHPREET0101/ML-PROJECT"><b>RetailPulse AI ↗</b></a></p>



<p align="center">
  <a href="https://github.com/ISHPREET0101/BlockIT/releases/latest">Download BlockIT</a> &nbsp; · &nbsp;
  <a href="https://takumi-two-kohl.vercel.app/">Takumi sample demo</a> &nbsp; · &nbsp;
  <a href="https://ishpreet0101.github.io/synapse-memory-lab-dataforge-2026/">Explore Synapse Memory Lab</a>
</p>

## How the projects work

<picture><source media="(max-width: 600px)" srcset="assets/project-flows-mobile.svg" /><img src="assets/project-flows.svg" width="100%" alt="Six project workflows: BlockIT turns file metadata into searchable storage insights; CircuitSleuth verifies PCB regions; Takumi turns recordings into expert-approved lessons; OpenDoor reviews evidence before publishing; Synapse visualizes memory updates; RetailPulse converts retail data into segment profiles." /></picture>

<details>
<summary><b>Go deeper: architecture, design choices, and demo boundaries</b></summary>

### [BlockIT](https://github.com/ISHPREET0101/BlockIT)

```mermaid
flowchart LR
  A[Drive or folder] --> B[Metadata scanner worker]
  B --> C[(SQLite scan index)]
  C --> D[Query worker]
  D --> E[React views and treemap]
  A --> F[Filename index worker]
  F --> G[Explorer search]
```

Scans file metadata; filename search does not inspect document contents.

### [CircuitSleuth](https://github.com/ISHPREET0101/circuitsleuth1)

```mermaid
flowchart LR
  A[Reference and test board] --> B{Registration valid?}
  B -->|No| C[NOT_EVALUABLE]
  B -->|Yes| D[Detect candidate regions]
  D --> E[Agent chooses verification tool]
  E --> F{Enough evidence?}
  F -->|More needed| E
  F -->|Yes| G[Verdict with evidence]
  F -->|Capture needed| H[Operator review / new capture]
```

Collaborative project. Published benchmark uses seeded synthetic boards; it is not factory accuracy.

### [Takumi](https://github.com/ISHPREET0101/takumi)

```mermaid
flowchart LR
  A[Expert recording] --> B[Local transcription]
  B --> C[Lesson extraction adapter]
  C --> D[Validate transcript evidence]
  D --> E[Expert edits and approves]
  E --> F[Versioned lesson]
  F --> G[Guided practice and attempts]
```

Hosted browser demo uses a bundled sample. Custom uploads and AI processing require the local backend.

### [OpenDoor](https://github.com/ISHPREET0101/opendoor-calle)

```mermaid
flowchart LR
  A[Authorized verification plan] --> B[Deterministic call fixture]
  B --> C[Evidence-linked candidate facts]
  C --> D[Quarantine conflicts]
  D --> E[Human field decisions]
  E --> F[Atomic version check]
  F --> G[(D1 revision + audit event)]
```

The demonstrated review flow uses simulated calls. Live CALL-E creation is not a validated end-to-end integration.

### [Synapse Memory Lab](https://github.com/ISHPREET0101/synapse-memory-lab-dataforge-2026)

```mermaid
flowchart LR
  A[Deterministic token stream] --> B[Read prior memory]
  B --> C[Outer-product state update]
  C --> D[Neuron and synapse canvases]
  B --> E[Explicit-history comparison]
  C --> F[Load and interference experiment]
```

Collaborative educational toy simulations; no official BDH checkpoint or trained-model benchmark is run.

### [RetailPulse AI](https://github.com/ISHPREET0101/ML-PROJECT)

```mermaid
flowchart LR
  A[Customers / products / sales] --> B[Validate relational data]
  B --> C[RFM and behavioral features]
  C --> D[Compare clustering models]
  D --> E[Interpretable segment profiles]
  D --> F[Segment-assignment classifier]
  E --> G[Export analysis artifacts]
```

Classifier evaluation measures agreement with the selected segmentation model, not causal business lift.

</details>

## More builds & collaborations

| Project | What it explores | Stack / context |
| :--- | :--- | :--- |
| [DeltaProof](https://github.com/sgoel2be24-cyber/deltaproof) | Local semantic retrieval of scope clauses, cited evidence, and reviewer-driven cost/schedule simulation | Collaboration · TypeScript, MiniLM, Transformers.js, ONNX/WASM |
| [Teachable Voice](https://github.com/ISHPREET0101/prism-teachable-voice) | Teach an Android task by demonstration, then replay it from a spoken command | Team project · Android, Kotlin, accessibility APIs |
| [JOY PITWALL](https://github.com/ISHPREET0101/joy-pitwall) | Offline race-weekend planning, stint logs, setup sheets, and engineering calculators | Electron, TypeScript · local data |
| [Aegis Alpha](https://github.com/ISHPREET0101/alpaca-AI-Hackathon) | Explainable options-agent architecture with deterministic risk gates and an audit trail | Python, SQLite, Streamlit · paper trading only |

<details>
<summary><b>Browse the wider project shelf</b></summary>

- [Multimodal Sentiment Analysis](https://github.com/ISHPREET0101/Multimodel-Sentiment-Analysis)
- [SmartCart](https://github.com/ISHPREET0101/SmartCart)
- [ShopIQ](https://github.com/ISHPREET0101/ShopIQ)
- [Loan Approval Project](https://github.com/ISHPREET0101/Loan-Approval-Project)
- [AQI Project](https://github.com/ISHPREET0101/AQI-PROJECT)
- [Portfolio Risk Analyzer](https://github.com/ISHPREET0101/portfolio-risk-analyzer)
- [Ecommerce](https://github.com/ISHPREET0101/Ecommerce)
- [Mental Health Support System](https://github.com/ISHPREET0101/Mental-Health-Support-System)
- [AI Lab Experiments](https://github.com/ISHPREET0101/AI-Lab-Experiments)
- [JavaScript Projects](https://github.com/ISHPREET0101/JS-projects)

[View all public repositories →](https://github.com/ISHPREET0101?tab=repositories&type=public)

</details>

## Learning & milestones

**Finalist — DATA FORGE, IIT Kharagpur** · [Synapse Memory Lab](https://github.com/ISHPREET0101/synapse-memory-lab-dataforge-2026)

**Machine Learning Specialization coursework — DeepLearning.AI & Stanford Online, via Coursera**

| Course | Credential |
| :--- | :--- |
| Supervised Machine Learning: Regression and Classification | [May 2026 ↗](https://coursera.org/verify/PYVPJPP6KXGL) |
| Advanced Learning Algorithms | [August 2026 ↗](https://coursera.org/verify/LYUZK160D8N7) |
| Unsupervised Learning, Recommenders, Reinforcement Learning | [August 2026 ↗](https://coursera.org/verify/PBVJQMLLHWXM) |

<p align="center">
  <a href="https://www.linkedin.com/in/ishpreet-singh-351224322"><img src="assets/connect.svg" width="100%" alt="Have an interesting problem to build around? Connect with Ishpreet about applied AI, thoughtful tools, and software people can understand." /></a>
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/ishpreet-singh-351224322">LinkedIn</a> ·
  <a href="https://github.com/ISHPREET0101?tab=repositories">Explore my repositories</a>
</p>
