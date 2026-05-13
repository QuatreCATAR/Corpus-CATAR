                                        +--------------------------------+
                                        |        Métamodèle CATAR        |
                                        +----------------+---------------+
                                                         |
                                                         |
                   -------------------------------------------------------------------------
                   |                                       |                               |
        +------------------+                     +------------------+             +------------------+
        |   JEu (Sujet)    |                     |   Monde (Contexte)|             | Champs d’influence|
        +--------+---------+                     +--------+---------+             +--------+---------+
                 |                                          |                               |
                 | agit dans                                 | influence                     |
                 v                                          v                               v
        +------------------+                     +------------------+             +------------------+
        | Processus cog.   |                     | Actes de langage |             |  Invariants T‑XX |
        +--------+---------+                     +--------+---------+             +--------+---------+
                 |                                          |                               |
                 | génère                                   | évalués par                   |
                 v                                          v                               |
        +------------------+                     +------------------+                       |
        | Prompts T‑XX     |-------------------->| Validateurs T‑XX |<----------------------+
        +--------+---------+                     +--------+---------+
                 |                                          |
                 | via API / dataset                        | produit
                 v                                          v
        +------------------+                     +------------------+
        | Modèle IA        |                     | Marqueurs (P+,P−,D,C)
        +--------+---------+                     +--------+---------+
                 |                                          |
                 | génère                                   | pondérés par
                 v                                          v
        +------------------+                     +------------------+
        | Responses RAW    |                     | Pondérations T‑XX|
        +--------+---------+                     +--------+---------+
                 |                                          |
                 | curated                                  | calcule
                 v                                          v
        +------------------+                     +------------------+
        | Responses Curated|-------------------->|   Scoring        |
        +--------+---------+                     +--------+---------+
                 |                                          |
                 | via dataset                              | normalise
                 v                                          v
        +------------------+                     +------------------+
        | Scores Agrégés   |-------------------->| Benchmark Global |
        +--------+---------+                     +--------+---------+
                 |                                          |
                 | génère                                   | exporte
                 v                                          v
        +------------------+                     +------------------+
        | Figures / JSON   |                     | CATAR-Benchmark  |
        +------------------+                     +------------------+


                                        (STRUCTURE DU CORPUS)
                                        ----------------------
Corpus-CATAR/
│
├── 01 → 05  (Fondations conceptuelles : invariants, Soije/Moije, D.Phi, Code MINOU)
│
├── 06-DATASET-CATAR/
│     ├── prompts/ (T‑XX)
│     ├── responses/ (raw/curated)
│     ├── scores/ (raw/aggregated)
│     ├── benchmark/
│     ├── api/ (OpenAPI)
│     ├── tools/
│     ├── docs/
│     └── metadata/
│
└── README.md / SCHEMA.md


                                        (PIPELINE API)
                                        ---------------
Client → API Gateway → OpenAPI → Parser → Modèle IA → Curated → Validateur → Scoring → JSON final
