                         +-----------------------------+
                         |         Benchmark           |
                         |     benchmark/*.py          |
                         +-------------+---------------+
                                       |
                                       | reçoit
                                       v
                         +-----------------------------+
                         |   Scores agrégés (JSON)     |
                         | scores/aggregated/*.json    |
                         +-------------+---------------+
                                       |
                                       | 1. Préparation
                                       v
                         +-----------------------------+
                         |   Chargement des données    |
                         |   - prompts                 |
                         |   - réponses curated        |
                         |   - scores agrégés          |
                         |   - métadonnées             |
                         +-------------+---------------+
                                       |
                                       | 2. Fusion logique
                                       v
                         +-----------------------------+
                         |   Fusion par invariant      |
                         |   - T‑XX                    |
                         |   - niveaux L1→L5           |
                         |   - variations 1→3          |
                         +-------------+---------------+
                                       |
                                       | 3. Construction des objets
                                       v
                         +-----------------------------+
                         |   Objet BenchmarkEntry      |
                         | {prompt, response, score,   |
                         |  invariant, niveau, meta}   |
                         +-------------+---------------+
                                       |
                                       | 4. Agrégation globale
                                       v
                         +-----------------------------+
                         |   Benchmark global          |
                         |  liste de BenchmarkEntry    |
                         +-------------+---------------+
                                       |
                                       | 5. Génération des figures
                                       v
                         +-----------------------------+
                         |   Figures / Visualisations  |
                         | benchmark/figures/*.png     |
                         +-------------+---------------+
                                       |
                                       | 6. Export final
                                       v
                         +-----------------------------+
                         | CATAR-Benchmark-v1.json     |
                         | (benchmark complet)         |
                         +-----------------------------+
