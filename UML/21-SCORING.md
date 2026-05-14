# 📘 UML — Scoring Process of the CATAR System (SCORING)

**File:** `21-SCORING.md`  
**Category:** UML — Operational / Scoring Engine  
**Version:** 1.0  
**Project:** Corpus‑CATAR  
**Author:** Quatre CATAR  

---

## 📝 Description / Description

**FR —**  
Ce diagramme décrit le **processus complet de scoring** dans le système CATAR, tel qu’il apparaît dans le fichier.  
Il détaille les cinq étapes successives du calcul du score, à partir du résultat du validateur T‑XX (marqueurs P+, P−, D, C, etc.)  :

1. **Préparation** — normalisation des données, format JSON, vérification des champs   
2. **Pondération** — application des poids T‑XX : w+, w−, wD, wC   
3. **Calcul du score brut** — somme pondérée :  
   Σ(P+×w+) − Σ(P−×w−) − Σ(D×wD) + Σ(C×wC)   
4. **Normalisation** — conversion du score brut en score normalisé (0→1 ou −1→+1)   
5. **Emballage JSON** — création de l’objet final `{score_brut, score_norm, markers, invariant, ...}`   

Ce diagramme constitue la **référence opérationnelle** du moteur de scoring CATAR, reliant directement les marqueurs produits par les validateurs T‑XX au score final utilisé dans le benchmark.

**EN —**  
This diagram describes the **complete scoring process** in the CATAR system, as shown in the file.  
It details the five sequential steps used to compute the score from the T‑XX validator output (markers P+, P−, D, C, etc.)  :

1. **Preparation** — data normalization, JSON format, field verification   
2. **Weighting** — application of T‑XX weights: w+, w−, wD, wC   
3. **Raw score computation** — weighted sum:  
   Σ(P+×w+) − Σ(P−×w−) − Σ(D×wD) + Σ(C×wC)   
4. **Normalization** — converting the raw score into a normalized score (0→1 or −1→+1)   
5. **JSON packaging** — creation of the final scoring object `{score_brut, score_norm, markers, invariant, ...}`   

This diagram provides the **operational reference** for the CATAR scoring engine, directly linking T‑XX validator markers to the final benchmark score.

---

## 🧩 Diagramme / Diagram

*(The existing diagram begins here.)*

                         
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
