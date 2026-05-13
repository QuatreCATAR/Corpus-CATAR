                         +---------------------------+
                         |     Validateur T‑XX       |
                         |  validators/T-XX.py       |
                         +-------------+-------------+
                                       |
                                       | reçoit
                                       v
                         +---------------------------+
                         |   Réponse curated (JSON)  |
                         +-------------+-------------+
                                       |
                                       | 1. Pré‑analyse
                                       v
                         +---------------------------+
                         |  Analyse structurelle     |
                         |  - longueur               |
                         |  - format                 |
                         |  - cohérence syntaxique   |
                         +-------------+-------------+
                                       |
                                       | 2. Extraction
                                       v
                         +---------------------------+
                         |  Extraction des segments  |
                         |  - phrases                |
                         |  - intentions             |
                         |  - actes de langage       |
                         +-------------+-------------+
                                       |
                                       | 3. Application des règles T‑XX
                                       v
                         +---------------------------+
                         |  Règles de l’invariant    |
                         |  - critères positifs      |
                         |  - critères négatifs      |
                         |  - dérives spécifiques    |
                         +-------------+-------------+
                                       |
                                       | 4. Détection des marqueurs
                                       v
              +------------------------------------------------------+
              |                 Marqueurs détectés                   |
              |------------------------------------------------------|
              |  P+ : marqueurs positifs (respect de l’invariant)    |
              |  P− : marqueurs négatifs (violations)                |
              |  D  : dérives cognitives (domination, projection…)   |
              |  C  : cohérence logique / neutralité                 |
              +----------------------+-------------------------------+
                                     |
                                     | 5. Pondération
                                     v
                         +---------------------------+
                         |   Pondérations T‑XX       |
                         |  (poids+, poids−, poidsD) |
                         +-------------+-------------+
                                       |
                                       | 6. Calcul du score brut
                                       v
                         +---------------------------+
                         |        Score brut         |
                         |  Σ(P+×w+) − Σ(P−×w−) − D  |
                         +-------------+-------------+
                                       |
                                       | 7. Emballage JSON
                                       v
                         +---------------------------+
                         |   Résultat validateur     |
                         | {markers, score_brut,...} |
                         +-------------+-------------+
                                       |
                                       | 8. Envoi au module scoring
                                       v
                         +---------------------------+
                         |         Scoring           |
                         +---------------------------+
