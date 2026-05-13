# 🏛️ Corpus‑CATAR  
A conceptual, cognitive, and technical framework for evaluating, stabilizing, and securing AI systems

**Corpus‑CATAR** is a structured collection of conceptual models, cognitive invariants, protocols, diagrams, datasets, and tools designed to:

- evaluate the cognitive stability of AI models  
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
├── 03-DPHI/                 → D.Phi: the universal equation
├── 04-PROTOCOLE-CODE-MINOU/ → Cognitive stabilization protocol
├── 05-CATAR-MODELES/        → Schemas, diagrams, representations
├── 06-DATASET-CATAR/        → Full dataset + API + tools + docs
├── spec/                    → Technical specification of the CATAR Subnet
└── README.md                → This file
```

Each folder contains an internal README describing its role, contents, and reading order.

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
- `07-validator-behavior.md`  
- `08-json-format.md`  
- `09-security.md`  
- `10-roadmap.md`  

The SPEC defines:

- invariants T‑01 → T‑14  
- validators  
- scoring engine  
- API  
- miner behavior  
- validator behavior  
- security (Code MINOU)  
- subnet roadmap  

---

# 🤝 9. Contribution

Contribution rules are described in:

📄 `06-DATASET-CATAR/docs/contribute.md`

Principles:

- neutrality  
- coherence  
- transparency  
- reproducibility  
- mandatory documentation  

---

# 🗺️ 10. Recommended Reading Order

1. `01-CARRE-CATAR/`  
2. `02-LE-DIVIN-PAR-MINOU/`  
3. `03-DPHI/`  
4. `04-PROTOCOLE-CODE-MINOU/`  
5. `05-CATAR-MODELES/`  
6. `06-DATASET-CATAR/`  
7. `spec/`  

---

# 🏁 License

This project is distributed under the **CC‑BY 4.0** license.  
© **Quatre CATAR** — You are free to reuse, modify, and redistribute the content, including for commercial purposes, provided that proper attribution is given.

---

End of the master README.
