# 🧭 Global Schema — Corpus‑CATAR  
*(EN — Structural Map)*

This document presents the full structure of the **Corpus‑CATAR**, organized into three coherent layers.

---

# 🧭 Legend — How to Read the Global Map

The Corpus‑CATAR is organized into three major layers:

---

## 1. Conceptual Layer (01 → 05)

The theoretical, metaphysical, and structural foundations of the CATAR model:

- cognitive invariants  
- Soije / Moije  
- D.Phi universal equation  
- Code MINOU  
- diagrams and representations  

---

## 2. Operational Layer (06-DATASET-CATAR)

The CATAR Subnet: dataset, API, validators, scoring, benchmark, tools, documentation.

This is the **executable**, reproducible, and testable part of the Corpus.

---

## 3. Input/Output Layer (README + SCHEMA)

The master documents that allow:

- understanding the whole  
- navigating the repository  
- transmitting the model  

Each folder is autonomous but integrated into a coherent architecture.

---

# 🗺️ Global Map — Corpus‑CATAR (ASCII)

```
Corpus-CATAR/
│
├── 01-CARRE-CATAR/              # Conceptual foundations of the CATAR model
│   ├── README.md
│   └── ...
│
├── 02-LE-DIVIN-PAR-MINOU/       # Applied metaphysics (Soije / Moije)
│   ├── README.md
│   └── ...
│
├── 03-DPHI/                     # D.Phi: universal equation
│   ├── README.md
│   └── ...
│
├── 04-PROTOCOLE-CODE-MINOU/     # Cognitive stabilization protocol (Code MINOU)
│   ├── README.md
│   └── ...
│
├── 05-CATAR-MODELES/            # Schemas, diagrams, representations
│   ├── README.md
│   └── ...
│
├── 06-DATASET-CATAR/            # CATAR Subnet: dataset, API, tools, docs
│   │
│   ├── prompts/                 # T‑XX prompts (invariants, levels, variations)
│   │   └── T-XX/...
│   │
│   ├── responses/               # Raw + curated responses
│   │   ├── raw/
│   │   └── curated/
│   │
│   ├── scores/                  # Raw + aggregated scores
│   │   ├── raw/
│   │   └── aggregated/
│   │
│   ├── benchmark/               # CATAR Benchmark (JSON + figures + scripts)
│   │   ├── CATAR-Benchmark-v1.json
│   │   ├── figures/
│   │   └── *.py
│   │
│   ├── api/                     # CATAR API (JSON + OpenAPI)
│   │   ├── catar-api.json
│   │   └── catar-openapi.yaml
│   │
│   ├── tools/                   # Developer tools
│   │   ├── test_interactif.py
│   │   ├── validate_dataset.py
│   │   ├── compare_models.py
│   │   └── export_csv.py
│   │
│   ├── docs/                    # Full technical documentation
│   │   ├── dev-guide.md
│   │   ├── dev-guide-quickstart.md
│   │   ├── architecture.md
│   │   ├── validators.md
│   │   ├── scoring.md
│   │   ├── dataset-schema.md
│   │   ├── benchmark.md
│   │   ├── tools.md
│   │   ├── metadata.md
│   │   ├── contribute.md
│   │   └── roadmap.md
│   │
│   ├── metadata/                # Global metadata
│   │   ├── schema.json
│   │   ├── dataset-info.json
│   │   └── invariants-index.json
│   │
│   └── *.py                     # Pipeline scripts (generate, score, aggregate…)
│
├── README.md                    # Main README
└── SCHEMA.en.md                 # This global schema (English version)
```

---

# 🏁 License

This corpus is distributed under the **CC‑BY 4.0** license.  
© **Quatre CATAR**
