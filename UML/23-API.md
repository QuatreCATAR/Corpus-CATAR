                         +-----------------------------+
                         |         Client API          |
                         |  (outil, script, modèle)    |
                         +-------------+---------------+
                                       |
                                       | 1. Requête HTTP POST
                                       v
                         +-----------------------------+
                         |        API Gateway          |
                         |   (FastAPI / OpenAPI)       |
                         +-------------+---------------+
                                       |
                                       | 2. Validation OpenAPI
                                       v
                         +-----------------------------+
                         |   Schéma OpenAPI (YAML)     |
                         |  - types                    |
                         |  - champs obligatoires      |
                         |  - formats                  |
                         +-------------+---------------+
                                       |
                                       | 3. Parsing & Normalisation
                                       v
                         +-----------------------------+
                         |   Parser interne API        |
                         |  - normalisation prompt     |
                         |  - extraction invariant     |
                         |  - vérification niveau      |
                         +-------------+---------------+
                                       |
                                       | 4. Envoi au modèle IA
                                       v
                         +-----------------------------+
                         |        Modèle IA            |
                         |   (GPT, Mistral, etc.)      |
                         +-------------+---------------+
                                       |
                                       | 5. Réponse brute
                                       v
                         +-----------------------------+
                         |     Response RAW            |
                         |   (texte non filtré)        |
                         +-------------+---------------+
                                       |
                                       | 6. Curation interne
                                       v
                         +-----------------------------+
                         |   Response Curated          |
                         | - nettoyage                 |
                         | - stabilisation             |
                         | - format JSON               |
                         +-------------+---------------+
                                       |
                                       | 7. Passage au validateur T‑XX
                                       v
                         +-----------------------------+
                         |     Validateur T‑XX         |
                         | - détection P+ / P− / D     |
                         | - cohérence / neutralité    |
                         +-------------+---------------+
                                       |
                                       | 8. Score brut
                                       v
                         +-----------------------------+
                         |          Scoring            |
                         | - pondérations T‑XX         |
                         | - normalisation             |
                         +-------------+---------------+
                                       |
                                       | 9. Construction objet API
                                       v
                         +-----------------------------+
                         |   Objet APIResponse JSON    |
                         | {prompt, response, score,   |
                         |  invariant, niveau, meta}   |
                         +-------------+---------------+
                                       |
                                       | 10. Retour HTTP
                                       v
                         +-----------------------------+
                         |      Client API             |
                         |   (résultat final JSON)     |
                         +-----------------------------+
