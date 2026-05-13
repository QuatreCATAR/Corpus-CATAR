                         +---------------------------+
                         |         Scoring           |
                         |     scoring/*.py          |
                         +-------------+-------------+
                                       |
                                       | reçoit
                                       v
                         +---------------------------+
                         | Résultat validateur T‑XX  |
                         | {P+, P−, D, C, ...}       |
                         +-------------+-------------+
                                       |
                                       | 1. Préparation
                                       v
                         +---------------------------+
                         |  Normalisation des données|
                         |  - format JSON            |
                         |  - vérification champs    |
                         +-------------+-------------+
                                       |
                                       | 2. Pondération
                                       v
                         +---------------------------+
                         |  Pondérations T‑XX        |
                         |  w+, w−, wD, wC           |
                         +-------------+-------------+
                                       |
                                       | 3. Calcul du score brut
                                       v
                         +---------------------------+
                         |       Score brut          |
                         | Σ(P+×w+) − Σ(P−×w−) −     |
                         | Σ(D×wD) + Σ(C×wC)         |
                         +-------------+-------------+
                                       |
                                       | 4. Normalisation
                                       v
                         +---------------------------+
                         |   Score normalisé         |
                         |   (0→1 ou -1→+1)          |
                         +-------------+-------------+
                                       |
                                       | 5. Emballage JSON
                                       v
                         +---------------------------+
                         |  Objet scoring final      |
                         | {score_brut, score_norm,  |
                         |  markers, invariant, ...} |
                         +-------------+-------------+
                                       |
                                       | 6. Transmission
                                       v
                         +---------------------------+
                         |   Agrégateur de scores    |
                         |  scores/aggregated/*.json |
                         +---------------------------+
