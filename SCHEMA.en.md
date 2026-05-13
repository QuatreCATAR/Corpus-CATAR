🧭 Legend — How to read the global schema
The Corpus‑CATAR is organized into three major layers:

1. Conceptual Layer (01 → 05)
The theoretical, metaphysical, and structural foundations of the CATAR model:

cognitive invariants

Soije/Moije

D.Phi universal equation

Code MINOU

diagrams and conceptual models

2. Operational Layer (06‑DATASET‑CATAR)
The CATAR Subnet: dataset, API, validators, scoring, benchmark, tools, documentation.
This is the executable, reproducible, testable part of the Corpus.

3. Entry/Output Layer (README + SCHEMA)
The master documents that allow:

understanding the whole system

navigating the repository

transmitting the model

Each folder is autonomous but articulated within a coherent architecture.

🗺️ Global Schema — Corpus‑CATAR (ASCII)

Corpus-CATAR/
│
├── 01-CARRE-CATAR/              # Conceptual foundations of the CATAR model
│   ├── README.md                # Presentation of the CATAR Square
│   └── ...                      # Texts, diagrams, notes
│
├── 02-LE-DIVIN-PAR-MINOU/       # Applied metaphysics (Soije / Moije)
│   ├── README.md
│   └── ...
│
├── 03-DPHI/                     # D.Phi: the universal equation
│   ├── README.md
│   └── ...
│
├── 04-PROTOCOLE-CODE-MINOU/     # Cognitive stabilization protocol (Code MINOU)
│   ├── README.md
│   └── ...
│
├── 05-CATAR-MODELES/            # Diagrams, models, visual representations
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
│   ├── api/                     # CATAR API specifications
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
│   ├── metadata/                # Global schemas & metadata
│   │   ├── schema.json
│   │   ├── dataset-info.json
│   │   └── invariants-index.json
│   │
│   └── *.py                     # Pipeline scripts (generate, score, aggregate, etc.)
│
├── README.md                    # Master README (global overview of Corpus‑CATAR)
└── SCHEMA.md                    # Global ASCII schema (this document)
