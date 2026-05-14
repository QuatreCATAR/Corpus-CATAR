# 📘 UML — Logical Process of T‑XX Validation (LOGIQUE)

**File:** `14-LOGIQUE.md`  
**Category:** UML — Logical / Validation Pipeline  
**Version:** 1.0  
**Project:** Corpus‑CATAR  
**Author:** Quatre CATAR  

---

## 📝 Description / Description

**FR —**  
Ce diagramme décrit la **logique interne du processus de validation T‑XX** dans le système CATAR.  
Il détaille la chaîne logique complète, telle qu’elle apparaît dans le fichier :  
1. **Invariants T‑XX** — ND, NF, NP, SM, etc.   
2. **Critères logiques** — règles, attentes, exigences de l’invariant   
3. **Validateur T‑XX** — implémenté dans `validators/T-XX.py`   
4. **Marqueurs détectés** — P+, P−, dérives cognitives, cohérence, neutralité   
5. **Pondérations T‑XX** — poids et coefficients associés à chaque marqueur   
6. **Score brut** — calculé à partir des marqueurs pondérés   
7. **Score normalisé** — exprimé sur une échelle 0→1 ou −1→+1   

Ce diagramme constitue la **représentation logique centrale** du fonctionnement des validateurs T‑XX : il montre comment les invariants se traduisent en critères, comment les critères alimentent le validateur, comment les marqueurs sont détectés, puis comment le score est produit et normalisé.

**EN —**  
This diagram describes the **internal logical process of T‑XX validation** within the CATAR system.  
It details the full logical chain, as shown in the file:  
1. **T‑XX Invariants** — ND, NF, NP, SM, etc.   
2. **Logical criteria** — rules, expectations, invariant requirements   
3. **T‑XX Validator** — implemented in `validators/T-XX.py`   
4. **Detected markers** — P+, P−, cognitive drifts, coherence, neutrality   
5. **T‑XX Weightings** — weights and coefficients for each marker   
6. **Raw score** — computed from weighted markers   
7. **Normalized score** — expressed on a 0→1 or −1→+1 scale   

This diagram provides the **core logical representation** of how T‑XX validators operate: how invariants become criteria, how criteria feed the validator, how markers are detected, and how the score is computed and normalized.

---

## 🧩 Diagramme / Diagram

*(The existing diagram begins here.)*

                          
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
