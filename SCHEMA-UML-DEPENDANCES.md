                           +----------------------+
                           |     Corpus-CATAR     |
                           +----------+-----------+
                                      |
                                      v
                         +--------------------------+
                         |   Fondations conceptuelles|
                         |  (01 → 05 : théorie)      |
                         +-------------+-------------+
                                       |
                                       |  Dépendances conceptuelles
                                       v
                         +--------------------------+
                         |   Invariants T‑XX        |
                         | (définis dans 01 → 05)   |
                         +-------------+-------------+
                                       |
                                       |  Dépendances fonctionnelles
                                       v
                         +--------------------------+
                         |     PROMPTS T‑XX         |
                         |  (prompts/T-XX/)         |
                         +-------------+-------------+
                                       |
                                       |  Dépendances IA
                                       v
                         +--------------------------+
                         |      Modèle IA           |
                         | (GPT, Mistral, etc.)     |
                         +-------------+-------------+
                                       |
                                       |  Dépendances pipeline
                                       v
                         +--------------------------+
                         |   RESPONSES RAW          |
                         +-------------+-------------+
                                       |
                                       |  Dépendances curation
                                       v
                         +--------------------------+
                         |  RESPONSES CURATED       |
                         +-------------+-------------+
                                       |
                                       |  Dépendances analyse
                                       v
                         +--------------------------+
                         |   VALIDATEURS T‑XX       |
                         | (validators/*.py)        |
                         +-------------+-------------+
                                       |
                                       |  Dépendances scoring
                                       v
                         +--------------------------+
                         |        SCORING           |
                         |   (scores/raw/)          |
                         +-------------+-------------+
                                       |
                                       |  Dépendances statistiques
                                       v
                         +--------------------------+
                         |   SCORES AGGREGATED      |
                         |  (scores/aggregated/)    |
                         +-------------+-------------+
                                       |
                                       |  Dépendances fusion
                                       v
                         +--------------------------+
                         |       BENCHMARK          |
                         | (benchmark/*.json)       |
                         +-------------+-------------+
                                       |
                                       |  Dépendances documentation
                                       v
                         +--------------------------+
                         |          DOCS            |
                         | (architecture, scoring…) |
                         +-------------+-------------+
                                       |
                                       |  Dépendances schéma
                                       v
                         +--------------------------+
                         |        METADATA          |
                         | (schema.json, info…)     |
                         +--------------------------+
