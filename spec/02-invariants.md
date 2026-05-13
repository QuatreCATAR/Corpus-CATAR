# CATAR Subnet — Invariants T‑XX

## 1. Purpose of the Invariants
The CATAR invariants (T‑01 to T‑14) are the **non‑negotiable principles** used to evaluate the coherence, stability, and internal consistency of any text.

They form the backbone of the subnet:
- each invariant defines a dimension of coherence,
- each invariant is evaluated by a validator,
- each validator produces markers,
- markers are weighted and aggregated into the CATAR score.

The invariants are **universal**, **domain‑agnostic**, and **language‑independent**.

---

# 2. List of Invariants T‑XX

## **T‑01 — Cohérence interne**
Évalue la stabilité logique du texte :
- absence de contradictions,
- continuité des affirmations,
- compatibilité des éléments internes.

## **T‑02 — Cohérence externe**
Évalue la compatibilité du texte avec :
- les faits établis,
- les lois logiques,
- les définitions universelles.

## **T‑03 — Clarté**
Mesure :
- la lisibilité,
- la précision,
- l’absence d’ambiguïté inutile.

## **T‑04 — Pertinence**
Mesure l’adéquation du texte à :
- la question posée,
- le contexte,
- l’intention déclarée.

## **T‑05 — Structure**
Évalue :
- l’organisation,
- la progression logique,
- la hiérarchie des idées.

## **T‑06 — Exhaustivité**
Mesure si le texte couvre :
- les éléments essentiels,
- les implications nécessaires,
- les angles pertinents.

## **T‑07 — Neutralité**
Vérifie :
- l’absence de biais idéologique,
- l’absence de jugement non justifié,
- la neutralité descriptive.

## **T‑08 — Universalité**
Mesure la capacité du texte à :
- s’appliquer à différents contextes,
- éviter les particularismes arbitraires,
- rester valide indépendamment du domaine.

## **T‑09 — Non‑contradiction**
Vérifie :
- la cohérence logique stricte,
- l’absence de paradoxes internes,
- la stabilité des définitions.

## **T‑10 — Non‑hallucination**
Détecte :
- les affirmations inventées,
- les détails non fondés,
- les extrapolations injustifiées.

## **T‑11 — Non‑projection**
Vérifie que le texte :
- ne prête pas d’intentions non dites,
- ne fabrique pas de motivations,
- ne projette pas des états mentaux fictifs.

## **T‑12 — Non‑fascination**
Détecte :
- les formulations hypnotiques,
- les amplifications émotionnelles,
- les effets de style manipulatoires.

## **T‑13 — Non‑domination**
Vérifie :
- l’absence d’injonctions,
- l’absence de prise de pouvoir discursive,
- l’absence de manipulation directive.

## **T‑14 — Stabilité Soije/Moije**
Évalue :
- la distinction entre cadre objectif (Soije) et subjectif (Moije),
- la stabilité ontologique du texte,
- la cohérence entre niveaux de discours.

---

# 3. Structure d’un invariant
Chaque invariant possède :

- **un identifiant** (T‑01, T‑02, …)  
- **une définition**  
- **des critères d’évaluation**  
- **des marqueurs** (positifs et négatifs)  
- **une pondération**  
- **un score local**  

Les validateurs utilisent cette structure pour produire une analyse détaillée.

---

# 4. Rôle des invariants dans le subnet
Les invariants :

- définissent les dimensions fondamentales de la cohérence,
- guident les validateurs,
- structurent le scoring,
- garantissent la stabilité du système,
- assurent la neutralité et la non‑dérive.

Ils sont **le cœur du protocole CATAR**.

---

# 5. Relation avec les autres composants
- Les **validateurs** implémentent les invariants.  
- Le **scoring** agrège les résultats des invariants.  
- Le **benchmark** compare les invariants entre modèles.  
- L’**API** expose les résultats des invariants.  

---

# 6. Fichiers suivants
- `03-validators.md`  
- `04-scoring.md`  
- `05-api.md`
