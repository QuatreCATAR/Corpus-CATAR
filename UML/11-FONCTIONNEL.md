# 📘 UML — Functional Diagram of the CATAR Pipeline (FONCTIONNEL)

**File:** `11-FONCTIONNEL.md`  
**Category:** UML — Functional / Pipeline Flow  
**Version:** 1.0  
**Project:** Corpus‑CATAR  
**Author:** Quatre CATAR  

---

## 📝 Description / Description

**FR —**  
Ce diagramme décrit le **flux fonctionnel complet du pipeline CATAR**, depuis la sélection d’un invariant T‑XX jusqu’à l’agrégation statistique finale.  
Il détaille les étapes successives du traitement :  
- sélection d’un invariant T‑XX   
- génération du prompt associé   
- production d’une réponse brute par un modèle IA (GPT, Mistral, etc.)   
- nettoyage / transformation en réponse curated   
- passage au validateur T‑XX correspondant   
- détection des marqueurs (neutralité, cohérence, non‑domination, etc.)   
- scoring et agrégation statistique   

Ce diagramme constitue la **colonne vertébrale fonctionnelle** du Subnet CATAR, reliant prompts, modèles, validateurs et scoring.

**EN —**  
This diagram describes the **full functional flow of the CATAR pipeline**, from selecting a T‑XX invariant to final statistical aggregation.  
It details the sequential processing steps:  
- selecting a T‑XX invariant   
- generating the corresponding prompt   
- producing a raw response from an AI model (GPT, Mistral, etc.)   
- cleaning / transforming into a curated response   
- passing the response to the appropriate T‑XX validator   
- detecting markers (neutrality, coherence, non‑domination, etc.)   
- scoring and statistical aggregation   

This diagram forms the **functional backbone** of the CATAR Subnet, connecting prompts, models, validators, and scoring.

---

## 🧩 Diagramme / Diagram

*(The existing diagram begins here.)*

                          
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
