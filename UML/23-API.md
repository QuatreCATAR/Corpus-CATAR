# 📘 UML — API Flow for the CATAR System (API)

**File:** `23-API.md`  
**Category:** UML — Operational / API Flow  
**Version:** 1.0  
**Project:** Corpus‑CATAR  
**Author:** Quatre CATAR  

---

## 📝 Description / Description

**FR —**  
Ce diagramme décrit le **flux complet de l’API CATAR**, depuis la requête HTTP initiale jusqu’à la production d’une réponse curated.  
Il détaille les étapes successives visibles dans le fichier :

1. **Requête HTTP POST** — envoi d’un prompt, d’un invariant et d’un niveau via un client API  
2. **Validation OpenAPI** — contrôle du schéma : types, champs obligatoires, formats  
3. **Parsing & normalisation** — extraction de l’invariant, normalisation du prompt, vérification du niveau  
4. **Envoi au modèle IA** — appel au modèle (GPT, Mistral, etc.)  
5. **Réponse brute (RAW)** — texte non filtré renvoyé par le modèle  
6. **Curation interne** — nettoyage, stabilisation, préparation pour la validation T‑XX  

Ce diagramme constitue la **référence opérationnelle** du fonctionnement de l’API CATAR, reliant le client, la passerelle API, le schéma OpenAPI, le modèle IA et la curation interne.

**EN —**  
This diagram describes the **full flow of the CATAR API**, from the initial HTTP request to the production of a curated response.  
It details the sequential steps shown in the file:

1. **HTTP POST request** — sending a prompt, invariant, and level through an API client  
2. **OpenAPI validation** — schema checking: types, required fields, formats  
3. **Parsing & normalization** — extracting the invariant, normalizing the prompt, verifying the level  
4. **Sending to the AI model** — calling the model (GPT, Mistral, etc.)  
5. **RAW response** — unfiltered text returned by the model  
6. **Internal curation** — cleaning, stabilizing, preparing for T‑XX validation  

This diagram provides the **operational reference** for how the CATAR API works, connecting the client, the API gateway, the OpenAPI schema, the AI model, and the internal curation layer.

---

## 🧩 Diagramme / Diagram

*(The existing diagram begins here.)*

                         
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
