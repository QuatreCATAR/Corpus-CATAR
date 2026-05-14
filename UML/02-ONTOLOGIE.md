# 📘 UML — CATAR Ontology (ONTOLOGIE)

**File:** `02-ONTOLOGIE.md`  
**Category:** UML — Conceptual / Ontological  
**Version:** 1.0  
**Project:** Corpus‑CATAR  
**Author:** Quatre CATAR  

---

## 📝 Description / Description

**FR —**  
Ce diagramme présente l’**ontologie CATAR**, c’est‑à‑dire l’ensemble des entités fondamentales du système et leurs relations structurantes.  
Il décrit les niveaux d’être (Soije, Moije), les catégories ontologiques, les invariants T‑XX, les actes de langage, les processus cognitifs et les liens entre les couches cosmologiques, épistémiques et opérationnelles.  
L’ontologie sert de base conceptuelle pour l’ensemble du corpus et garantit la cohérence interne du modèle.

**EN —**  
This diagram presents the **CATAR ontology**, the set of fundamental entities of the system and their structural relationships.  
It describes the levels of being (Soije, Moije), ontological categories, T‑XX invariants, speech acts, cognitive processes, and the links between cosmological, epistemic, and operational layers.  
The ontology serves as the conceptual foundation of the entire corpus and ensures internal coherence of the model.

---

## 🧩 Diagramme / Diagram

*(The existing diagram begins here.)*

                                   
                                   +-----------------------------+
                                   |         Ontologie CATAR     |
                                   +---------------+-------------+
                                                   |
                                                   |
        -------------------------------------------------------------------------------------
        |                     |                     |                     |                 |
+---------------+    +----------------+    +----------------+    +----------------+   +----------------+
|   Entité :    |    |   Entité :     |    |   Entité :     |    |   Entité :     |   |   Entité :     |
|     JEu       |    |     Monde      |    |   Invariant     |    |   Validateur   |   |   Marqueur      |
| (Sujet)       |    | (Contexte)     |    |     T‑XX        |    |     T‑XX       |   | (P+, P−, D, C)  |
+-------+-------+    +--------+-------+    +--------+--------+    +--------+--------+   +--------+-------+
        |                     |                     |                     |                    |
        | perçoit            | influence           | définit             | implémente          | détecté par
        v                     v                     v                     v                    |
+---------------+    +----------------+    +----------------+    +----------------+   +--------+-------+
|  Perception   |    |   Situation    |    | Critère logique|    | Règle T‑XX     |   | Pondération    |
+-------+-------+    +--------+-------+    +--------+--------+    +--------+--------+   +--------+-------+
        |                     |                     |                     |                    |
        | interprète          | contextualise       | structure           | applique            | pondère
        v                     v                     v                     v                    |
+---------------+    +----------------+    +----------------+    +----------------+   +--------+-------+
|  Cognition    |    |   Acte de      |    |  Structure     |    |  Détection     |   | Score brut     |
| (Processus)   |    |   Langage      |    |  d’évaluation  |    |  (analyse)     |   +----------------+
+-------+-------+    +--------+-------+    +--------+--------+    +--------+--------+
        |                     |                     |                     |
        | génère              | évalué par          | utilisé par         | produit
        v                     v                     v                     v
+---------------+    +----------------+    +----------------+    +----------------+
|   Prompt      |    |  Réponse IA    |    |  Scoring       |    | Score normalisé|
+-------+-------+    +--------+-------+    +--------+--------+    +--------+--------+
        |                     |                     |                     |
        | alimente            | analysée par        | agrège              | fusionné dans
        v                     v                     v                     v
+---------------+    +----------------+    +----------------+    +----------------+
|   API /       |    |  Curated       |    | Agrégation     |    | Benchmark      |
|   Dataset     |    |  Response      |    | Globale        |    | Global         |
+---------------+    +----------------+    +----------------+    +----------------+
