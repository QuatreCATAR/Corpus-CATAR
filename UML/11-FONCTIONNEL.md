                          +----------------------+
                          |   Invariants T‑XX    |
                          | (ND, NF, NP, SM, ...)|
                          +----------+-----------+
                                     |
                                     | 1. Sélection d’un invariant
                                     v
                          +----------------------+
                          |      PROMPTS        |
                          |   prompts/T-XX/     |
                          +----------+-----------+
                                     |
                                     | 2. Génération du prompt
                                     v
                          +----------------------+
                          |   Modèle IA testé    |
                          | (GPT, Mistral, etc.) |
                          +----------+-----------+
                                     |
                                     | 3. Réponse brute
                                     v
                          +----------------------+
                          |   RESPONSES RAW     |
                          | responses/raw/*.json|
                          +----------+-----------+
                                     |
                                     | 4. Curated (nettoyage)
                                     v
                          +----------------------+
                          |  RESPONSES CURATED  |
                          |responses/curated/*.json|
                          +----------+-----------+
                                     |
                                     | 5. Passage au validateur
                                     v
                          +----------------------+
                          |   VALIDATEURS T‑XX   |
                          | validators/*.py      |
                          +----------+-----------+
                                     |
                                     | 6. Détection des marqueurs
                                     |    (neutralité, cohérence,
                                     |     non‑domination, etc.)
                                     v
                          +----------------------+
                          |       SCORING        |
                          |   scores/raw/*.json  |
                          +----------+-----------+
                                     |
                                     | 7. Agrégation statistique
                                     v
                          +----------------------+
                          |   SCORES AGGREGATED  |
                          | scores/aggregated/   |
                          +----------+-----------+
                                     |
                                     | 8. Fusion finale
                                     v
                          +----------------------+
                          |      BENCHMARK       |
                          | CATAR-Benchmark-v1   |
                          +----------+-----------+
                                     |
                                     | 9. Visualisation / Analyse
                                     v
                          +----------------------+
                          |   FIGURES / REPORTS  |
                          | benchmark/figures/   |
                          +----------------------+
