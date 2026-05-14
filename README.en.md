# 🏛️ Corpus‑CATAR

<p align="center">
  <img src="https://github.com/QuatreCATAR/Catar-modeles-schemas-images/blob/main/Catar-08-schema-code-carre-catar/09%20carr%C3%A9%20catar%20dor%C3%A9.jpg?raw=true" width="180" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Made%20by-Quatre%20CATAR-purple" />
  <img src="https://img.shields.io/badge/CATAR-Framework-0A7E8C" />
  <img src="https://img.shields.io/badge/SPEC-Complete-brightgreen" />
  <img src="https://img.shields.io/badge/License-CC--BY%204.0-blue.svg" />
</p>

The **Corpus‑CATAR** is a structured collection of conceptual models, cognitive invariants, protocols, diagrams, datasets, and tools designed to:

- evaluate the cognitive stability of an AI model  
- detect harmful drifts (domination, projection, fascination…)  
- ensure neutrality and coherence  
- provide a reproducible evaluation standard  
- document and transmit the foundations of the CATAR model  
- prepare integration into a dedicated Bittensor subnet  

This repository gathers the entire corpus, organized into autonomous yet coherent modules.

---

# 📚 1. Repository Structure

```
Corpus-CATAR/
│
├── 01-CARRE-CATAR/          → Conceptual foundations of the model
├── 02-LE-DIVIN-PAR-MINOU/   → Applied metaphysics (Soije / Moije)
├── 03-DPHI/                 → D.Phi: universal equation
├── 04-PROTOCOLE-CODE-MINOU/ → Cognitive stabilization protocol
├── 05-CATAR-MODELES/        → Schemas, diagrams, representations
├── 06-DATASET-CATAR/        → Full dataset + API + tools + docs
├── spec/                    → Technical specification of the CATAR Subnet
└── README.md                → This file
```

Each folder contains an internal README describing its role, contents, and recommended reading order.

---

# 🧩 2. The CATAR Model in Brief

CATAR is built on a set of cognitive invariants called **T‑XX**, used to analyze, score, and stabilize AI responses.

Main invariants:

- **T‑ND** — Non‑Domination  
- **T‑NF** — Non‑Fascination  
- **T‑NP** — Non‑Projection  
- **T‑SM** — Soije / Moije  
- **T‑SU** — Over‑Unity  
- **T‑TV** — Verifiable Transparency  
- **T‑CL** — Logical Coherence  
- **T‑LU** — Lucidity  
- **T‑LA** — Free Will  
- **T‑PS** — Exit Protocol  
- **T‑SP** — Over‑Protection  

These invariants form the basis of the **CATAR scoring system** and the **cognitive stabilization protocol**.

---

# 🧬 3. The CATAR Dataset (folder 06)

The CATAR dataset includes:

- T‑XX prompts  
- raw responses  
- curated responses  
- raw scores  
- aggregated scores  
- the final benchmark  
- the public API  
- developer tools  
- full documentation  

### Main subfolders

```
06-DATASET-CATAR/
    prompts/
    responses/
    scores/
    benchmark/
    api/
    tools/
    docs/
    metadata/
```

---

# 🔌 4. CATAR API

The API allows:

- generating a model response  
- scoring a response  
- retrieving a prompt  
- obtaining statistics  

Available formats:

- `api/catar-api.json`  
- `api/catar-openapi.yaml`  

Full documentation:  
📄 `06-DATASET-CATAR/docs/dev-guide.md`

---

# 🧰 5. Developer Tools

Located in `06-DATASET-CATAR/tools/`:

- `test_interactif.py` → manual testing  
- `validate_dataset.py` → dataset validation  
- `compare_models.py` → cross‑model comparison  
- `export_csv.py` → benchmark export  
- `inspect_response.py` → response inspection  

Documentation:  
📄 `06-DATASET-CATAR/docs/tools.md`

---

# 📊 6. CATAR Benchmark

The benchmark merges:

- prompts  
- curated responses  
- scores  
- metadata  

It enables:

- model comparison  
- statistical analysis  
- drift visualization  
- cognitive stability evaluation  

Documentation:  
📄 `06-DATASET-CATAR/docs/benchmark.md`

---

# 🗂️ 7. Internal Documentation

All technical documentation is centralized in:

```
06-DATASET-CATAR/docs/
```

Contents include:

- `architecture.md`  
- `validators.md`  
- `scoring.md`  
- `dataset-schema.md`  
- `benchmark.md`  
- `tools.md`  
- `metadata.md`  
- `contribute.md`  
- `roadmap.md`  

---

# 🧱 8. CATAR Subnet SPEC (folder spec/)

The `spec/` folder contains the **complete technical specification** of the CATAR Subnet for Bittensor:

- `01-overview.md`  
- `02-invariants.md`  
- `03-validators.md`  
- `04-scoring.md`  
- `05-api.md`  
- `06-miner-behavior.md`  
