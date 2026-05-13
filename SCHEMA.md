# Schéma global — Corpus‑CATAR (ASCII)

Corpus-CATAR/
│
├── 01-CARRE-CATAR/              # Fondations conceptuelles du modèle CATAR
│   ├── README.md                # Présentation du Carré CATAR
│   └── ...                      # Textes, schémas, notes
│
├── 02-LE-DIVIN-PAR-MINOU/       # Métaphysique appliquée (Soije / Moije)
│   ├── README.md
│   └── ...
│
├── 03-DPHI/                     # D.Phi : équation universelle
│   ├── README.md
│   └── ...
│
├── 04-PROTOCOLE-CODE-MINOU/     # Protocole de stabilisation cognitive (Code MINOU)
│   ├── README.md
│   └── ...
│
├── 05-CATAR-MODELES/            # Schémas, diagrammes, représentations du modèle CATAR
│   ├── README.md
│   └── ...
│
├── 06-DATASET-CATAR/            # Subnet CATAR : dataset, API, outils, docs
│   │
│   ├── prompts/                 # Prompts T‑XX (invariants, niveaux, variations)
│   │   └── T-XX/...
│   │
│   ├── responses/               # Réponses brutes + curated
│   │   ├── raw/
│   │   └── curated/
│   │
│   ├── scores/                  # Scores bruts + agrégés
│   │   ├── raw/
│   │   └── aggregated/
│   │
│   ├── benchmark/               # Benchmark CATAR (JSON + figures + scripts)
│   │   ├── CATAR-Benchmark-v1.json
│   │   ├── figures/
│   │   └── *.py
│   │
│   ├── api/                     # Spécifications API CATAR
│   │   ├── catar-api.json
│   │   └── catar-openapi.yaml
│   │
│   ├── tools/                   # Outils développeur
│   │   ├── test_interactif.py
│   │   ├── validate_dataset.py
│   │   ├── compare_models.py
│   │   └── export_csv.py
│   │
│   ├── docs/                    # Documentation technique complète
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
│   ├── metadata/                # Schémas & métadonnées globales
│   │   ├── schema.json
│   │   ├── dataset-info.json
│   │   └── invariants-index.json
│   │
│   └── *.py                     # Scripts pipeline (generate, score, aggregate, etc.)
│
├── README.md                    # README maître (vue globale du Corpus‑CATAR)
└── SCHEMA.md                    # Présent schéma ASCII global
