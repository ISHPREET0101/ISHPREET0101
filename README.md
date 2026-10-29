# Hi, I'm Ishpreet

I'm a Computer Engineering student at **Thapar Institute of Engineering and Technology, Patiala**. I work with Python and TypeScript, mostly on machine learning projects, web apps, and desktop software.

This is a mix of coursework, hackathon projects, and apps I've worked on. Some are team projects; the linked repositories have the contributors and setup details.

[LinkedIn](https://www.linkedin.com/in/ishpreet-singh-351224322)

## Projects

- **[2D Metaverse](https://2d-metaverse-se.vercel.app/)** — A shared virtual office where you choose an avatar and walk around with teammates. Move close to someone and a video call starts. The link opens the demo; the source is private.

- **[BlockIT](https://github.com/ISHPREET0101/BlockIT)** — A Windows storage explorer for finding files and seeing what's taking up disk space. Built with Electron, React, TypeScript and SQLite. [Download](https://github.com/ISHPREET0101/BlockIT/releases/latest).

- **[Takumi](https://github.com/ISHPREET0101/takumi)** — Turns a recorded demonstration into a lesson that an expert can edit and approve, with guided practice for the learner. React frontend, Python/FastAPI backend. [Try the sample](https://takumi-two-kohl.vercel.app/); processing your own recordings needs the local backend.

- **[CircuitSleuth](https://github.com/ISHPREET0101/circuitsleuth1)** — A team project for PCB inspection using OpenCV. It compares a board against a reference, checks suspicious regions, and keeps the evidence for review. The documented benchmark uses synthetic boards.

- **[Synapse Memory Lab](https://github.com/ISHPREET0101/synapse-memory-lab-dataforge-2026)** — An interactive explanation of attention and memory, built as a team project for DataForge. Change decay or memory load and watch what happens in the toy simulations. [Open the labs](https://ishpreet0101.github.io/synapse-memory-lab-dataforge-2026/).

- **[RetailPulse AI](https://github.com/ISHPREET0101/ML-PROJECT)** — Retail customer segmentation using RFM features and clustering. The notebook covers data checks, model comparisons, and customer segment profiles.

<details>
<summary>A couple of screenshots</summary>

**Takumi:** the oscilloscope practice screen in the sample lesson.

![Takumi practice screen](https://raw.githubusercontent.com/ISHPREET0101/takumi/main/docs/screenshots/refined/practice-1440.png)

**CircuitSleuth:** the inspection workspace, with board regions and the agent's evidence trail.

![CircuitSleuth inspection workspace](https://raw.githubusercontent.com/ISHPREET0101/circuitsleuth1/main/docs/screenshots/workspace.png)

</details>

## Tools I use

- **Languages:** Python, TypeScript, JavaScript, SQL, C++, C
- **ML and data:** pandas, NumPy, scikit-learn, PyTorch, OpenCV, Jupyter
- **Apps and APIs:** React, Electron, FastAPI, Flask, HTML/CSS, Tailwind
- **Storage and tooling:** SQLite, Cloudflare D1, Git, Linux, Vite, Vitest

I've also used Transformers.js and ONNX Runtime for local sentence embeddings and semantic search.

## Other projects I've worked on

- [DeltaProof](https://github.com/sgoel2be24-cyber/deltaproof) — team project for reviewing scope changes using local embeddings, source citations, and a cost/schedule simulator.
- [Teachable Voice](https://github.com/ISHPREET0101/prism-teachable-voice) — team project for teaching an Android task by demonstration and replaying it with a spoken command.
- [JOY PITWALL](https://github.com/ISHPREET0101/joy-pitwall) — an offline app for race-weekend plans, stint logs, and setup sheets.
- [Aegis Alpha](https://github.com/ISHPREET0101/alpaca-AI-Hackathon) — an options-agent project with risk checks and an audit log, built for paper trading.

[More repositories](https://github.com/ISHPREET0101?tab=repositories&type=public)

## Education and courses

**B.Tech. Computer Engineering, Thapar** · 2024–present<br/>
**Finalist, DATA FORGE, IIT Kharagpur** · [Project](https://github.com/ISHPREET0101/synapse-memory-lab-dataforge-2026)

Completed these courses from DeepLearning.AI and Stanford Online on Coursera:

- [Supervised Machine Learning: Regression and Classification](https://coursera.org/verify/PYVPJPP6KXGL)
- [Advanced Learning Algorithms](https://coursera.org/verify/LYUZK160D8N7)
- [Unsupervised Learning, Recommenders, Reinforcement Learning](https://coursera.org/verify/PBVJQMLLHWXM)

<details>
<summary>Project diagrams</summary>

### BlockIT

```mermaid
flowchart LR
  A[Drive or folder] --> B[Metadata scanner worker]
  B --> C[(SQLite scan index)]
  C --> D[Query worker]
  D --> E[React views and treemap]
  A --> F[Filename index worker]
  F --> G[Explorer search]
```

### CircuitSleuth

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

### Takumi

```mermaid
flowchart LR
  A[Expert recording] --> B[Local transcription]
  B --> C[Lesson extraction adapter]
  C --> D[Validate transcript evidence]
  D --> E[Expert edits and approves]
  E --> F[Versioned lesson]
  F --> G[Guided practice and attempts]
```

### 2D Metaverse

```mermaid
flowchart LR
  A[Enter a name and choose an avatar] --> B[Join the shared world]
  B --> C[Walk around and meet teammates]
  C --> D[Move close to another player]
  D --> E[Automatic proximity video call]
```

### Synapse Memory Lab

```mermaid
flowchart LR
  A[Deterministic token stream] --> B[Read prior memory]
  B --> C[Outer-product state update]
  C --> D[Neuron and synapse canvases]
  B --> E[Explicit-history comparison]
  C --> F[Load and interference experiment]
```

### RetailPulse AI

```mermaid
flowchart LR
  A[Customers / products / sales] --> B[Validate relational data]
  B --> C[RFM and behavioral features]
  C --> D[Compare clustering models]
  D --> E[Interpretable segment profiles]
  D --> F[Segment-assignment classifier]
  E --> G[Export analysis artifacts]
```

</details>
