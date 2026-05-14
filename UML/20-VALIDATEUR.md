# 📘 UML — Internal Structure of a T‑XX Validator (VALIDATEUR)

**File:** `20-VALIDATEUR.md`  
**Category:** UML — Operational / Validation Engine  
**Version:** 1.0  
**Project:** Corpus‑CATAR  
**Author:** Quatre CATAR  

---

## 📝 Description / Description

**FR —**  
Ce diagramme décrit la **structure interne d’un validateur T‑XX**, tel qu’implémenté dans `validators/T-XX.py` .  
Il détaille les quatre étapes principales du processus de validation, telles qu’elles apparaissent dans le fichier :

1. **Pré‑analyse** — vérification structurelle de la réponse curated : longueur, format, cohérence syntaxique   
2. **Extraction** — segmentation de la réponse : phrases, intentions, actes de langage   
3. **Application des règles T‑XX** — critères positifs, critères négatifs, dérives spécifiques à l’invariant   
4. **Détection des marqueurs** — P+, P−, D (dérives cognitives), C (cohérence / neutralité)   

Ce diagramme constitue la **référence opérationnelle** pour comprendre comment chaque invariant T‑XX est appliqué à une réponse curated afin de produire les marqueurs nécessaires au scoring.

**EN —**  
This diagram describes the **internal structure of a T‑XX validator**, as implemented in `validators/T-XX.py` .  
It details the four main stages of the validation process, as shown in the file:

1. **Pre‑analysis** — structural checks on the curated response: length, format, syntactic coherence   
2. **Extraction** — segmentation of the response: sentences, intentions, speech acts   
3. **Application of T‑XX rules** — positive criteria, negative criteria, invariant‑specific drifts   
4. **Marker detection** — P+, P−, D (cognitive drifts), C (coherence / neutrality)   

This diagram serves as the **operational reference** for understanding how each T‑XX invariant is applied to a curated response to produce the markers required for scoring.

---

## 🧩 Diagramme / Diagram

*(The existing diagram begins here.)*

                         
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
