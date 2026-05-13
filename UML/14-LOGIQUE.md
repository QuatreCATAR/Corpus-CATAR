                          +----------------------+
                          |   Invariants T‑XX     |
                          | (ND, NF, NP, SM, ...) |
                          +----------+-----------+
                                     |
                                     | 1. Définit
                                     v
                          +----------------------+
                          |  Critères logiques   |
                          |  (règles, attentes)  |
                          +----------+-----------+
                                     |
                                     | 2. Alimente
                                     v
                          +----------------------+
                          |  Validateur T‑XX     |
                          | validators/T-XX.py   |
                          +----------+-----------+
                                     |
                                     | 3. Détecte
                                     v
                   +---------------------------------------+
                   |   Marqueurs détectés par invariant    |
                   |----------------------------------------|
                   |  - marqueurs positifs (P+)             |
                   |  - marqueurs négatifs (P−)             |
                   |  - dérives cognitives                  |
                   |  - cohérence / neutralité              |
                   +------------------+----------------------+
                                      |
                                      | 4. Pondération
                                      v
                          +----------------------+
                          |   Pondérations T‑XX  |
                          | (poids, coefficients)|
                          +----------+-----------+
                                     |
                                     | 5. Calcul du score brut
                                     v
                          +----------------------+
                          |       Scoring        |
                          |  scores/raw/*.json   |
                          +----------+-----------+
                                     |
                                     | 6. Normalisation
                                     v
                          +----------------------+
                          |  Score normalisé     |
                          | (0 → 1 ou -1 → +1)   |
                          +----------+-----------+
                                     |
                                     | 7. Agrégation
                                     v
                          +----------------------+
                          |  Agrégation globale  |
                          | scores/aggregated/   |
                          +----------+-----------+
                                     |
                                     | 8. Fusion
                                     v
                          +----------------------+
                          |      Benchmark       |
                          |  (résultat final)    |
                          +----------------------+
