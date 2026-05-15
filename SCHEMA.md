🜁 SCHEMA.md — Carte globale du Corpus‑CATAR
Global Structural Map of the Corpus‑CATAR (FR/EN)
Ce document présente la structure complète du Corpus‑CATAR, organisée en trois strates cohérentes.
This document presents the full structure of the Corpus‑CATAR, organized into three coherent layers.

🧭 Légende — Lecture du schéma global
Legend — How to Read the Global Map
Le Corpus‑CATAR est organisé en trois grandes strates :
The Corpus‑CATAR is organized into three major layers:

1. Strate conceptuelle (01 → 05)
1. Conceptual Layer (01 → 05)
Les fondations théoriques, métaphysiques et structurelles du modèle CATAR :
The theoretical, metaphysical, and structural foundations of the CATAR model:

invariants cognitifs / cognitive invariants

Soije / Moije

équation D.Phi / D.Phi universal equation

Code MINOU

schémas et représentations / diagrams and representations

Cette strate définit le cadre conceptuel du modèle.
This layer defines the conceptual framework of the model.

2. Strate opérationnelle (06‑DATASET‑CATAR)
2. Operational Layer (06‑DATASET‑CATAR)
Le Subnet CATAR : dataset, API, validateurs, scoring, benchmark, outils, documentation.
The CATAR Subnet: dataset, API, validators, scoring, benchmark, tools, documentation.

C’est la partie exécutable, reproductible et testable du Corpus.
This is the executable, reproducible, testable part of the Corpus.

3. Strate d’entrée/sortie (README + SCHEMA)
3. Input/Output Layer (README + SCHEMA)
Les documents maîtres qui permettent :
The master documents that allow:

de comprendre l’ensemble / understanding the whole

de naviguer dans le dépôt / navigating the repository

de transmettre le modèle / transmitting the model

Chaque dossier est autonome mais articulé dans une architecture cohérente.
Each folder is autonomous but integrated into a coherent architecture.

🗺️ Schéma global — Corpus‑CATAR (ASCII)
Global Map — Corpus‑CATAR (ASCII)
Code
Corpus-CATAR/
│
├── 01-CARRE-CATAR/              # Fondations conceptuelles / Conceptual foundations
│   ├── README.md
│   └── ...
│
├── 02-LE-DIVIN-PAR-MINOU/       # Métaphysique Soije/Moije / Applied metaphysics
│   ├── README.md
│   └── ...
│
├── 03-DPHI/                     # D.Phi : équation universelle / Universal equation
│   ├── README.md
│   └── ...
│
├── 04-PROTOCOLE-CODE-MINOU/     # Protocole de stabilisation cognitive / Cognitive protocol
│   ├── README.md
│   └── ...
│
├── 05-CATAR-MODELES/            # Schémas et représentations / Schemas and diagrams
│   ├── README.md
│   └── ...
│
├── 06-DATASET-CATAR/            # Subnet CATAR : dataset, API, outils, docs / Full operational layer
│   │
│   ├── prompts/                 # Prompts T‑XX (invariants, niveaux, variations)
│   │   └── T-XX/...
│   │
│   ├── responses/               # Réponses brutes + curated / Raw + curated responses
│   │   ├── raw/
│   │   └── curated/
│   │
│   ├── scores/                  # Scores bruts + agrégés / Raw + aggregated scores
│   │   ├── raw/
│   │   └── aggregated/
│   │
│   ├── benchmark/               # Benchmark CATAR (JSON + figures + scripts)
│   │   ├── CATAR-Benchmark-v1.json
│   │   ├── figures/
│   │   └── *.py
│   │
│   ├── api/                     # API CATAR (JSON + OpenAPI)
│   │   ├── catar-api.json
│   │   └── catar-openapi.yaml
│   │
│   ├── tools/                   # Outils développeur / Developer tools
│   │   ├── test_interactif.py
│   │   ├── validate_dataset.py
│   │   ├── compare_models.py
│   │   └── export_csv.py
│   │
│   ├── docs/                    # Documentation technique complète / Full technical documentation
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
│   ├── metadata/                # Métadonnées globales / Global metadata
│   │   ├── schema.json
│   │   ├── dataset-info.json
│   │   └── invariants-index.json
│   │
│   └── *.py                     # Scripts pipeline (generate, score, aggregate…)
│
├── README.md                    # README maître / Main README
└── SCHEMA.md                    # Présent schéma global / This global schema
🏁 Licence / License
Licence CC‑BY 4.0  
© Quatre CATAR

License CC‑BY 4.0  
© Quatre CATAR

flowchart TD

%% ============================
%%   STRATE 1 — CONCEPTUELLE
%% ============================

subgraph S1[01 → 05 • Strate conceptuelle / Conceptual Layer]
    A01[01-CARRE-CATAR<br/>Fondations conceptuelles<br/>Conceptual foundations]
    A02[02-LE-DIVIN-PAR-MINOU<br/>Métaphysique Soije/Moije<br/>Applied metaphysics]
    A03[03-DPHI<br/>Équation universelle D.Phi<br/>Universal equation]
    A04[04-PROTOCOLE-CODE-MINOU<br/>Protocole cognitif<br/>Cognitive protocol]
    A05[05-CATAR-MODELES<br/>Schémas et représentations<br/>Schemas & diagrams]
end

%% ============================
%%   STRATE 2 — OPÉRATIONNELLE
%% ============================

subgraph S2[06-DATASET-CATAR • Strate opérationnelle / Operational Layer]
    
    subgraph P[Prompts]
        P1[/prompts/T-XX/]
    end

    subgraph R[Responses]
        R1[/responses/raw/]
        R2[/responses/curated/]
    end

    subgraph SC[Scores]
        S1[/scores/raw/]
        S2[/scores/aggregated/]
    end

    subgraph B[Benchmark]
        B1[CATAR-Benchmark-v1.json]
        B2[figures/]
    end

    subgraph API[API CATAR]
        A1[catar-api.json]
        A2[catar-openapi.yaml]
    end

    subgraph Tools[Outils / Tools]
        T1[test_interactif.py]
        T2[validate_dataset.py]
        T3[compare_models.py]
        T4[export_csv.py]
    end

    subgraph Docs[Documentation]
        D1[dev-guide.md]
        D2[architecture.md]
        D3[validators.md]
        D4[scoring.md]
        D5[dataset-schema.md]
        D6[benchmark.md]
        D7[tools.md]
        D8[metadata.md]
        D9[contribute.md]
        D10[roadmap.md]
    end

    subgraph Meta[Métadonnées / Metadata]
        M1[schema.json]
        M2[dataset-info.json]
        M3[invariants-index.json]
    end

end

%% ============================
%%   STRATE 3 — I/O
%% ============================

subgraph S3[Strate d’entrée/sortie / Input–Output Layer]
    IO1[README.md<br/>README maître / Main README]
    IO2[SCHEMA.md<br/>Schéma global / Global map]
end

%% ============================
%%   RELATIONS ENTRE STRATES
%% ============================

A01 --> S2
A02 --> S2
A03 --> S2
A04 --> S2
A05 --> S2

S2 --> S3
