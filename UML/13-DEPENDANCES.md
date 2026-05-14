# 📘 UML — Dependency Diagram of the CATAR System (DEPENDANCES)

**File:** `13-DEPENDANCES.md`  
**Category:** UML — Structural / Dependency Graph  
**Version:** 1.0  
**Project:** Corpus‑CATAR  
**Author:** Quatre CATAR  

---

## 📝 Description / Description

**FR —**  
Ce diagramme représente l’ensemble des **dépendances internes du système CATAR**, organisées en couches successives depuis les fondations conceptuelles jusqu’au benchmark final.  
Chaque bloc du diagramme correspond à une dépendance explicite, telle qu’elle apparaît dans le fichier :  
- **Fondations conceptuelles** (dossiers 01 → 05)   
- **Invariants T‑XX** (définis dans 01 → 05)   
- **Prompts T‑XX** (`prompts/T-XX/`)   
- **Modèle IA** (GPT, Mistral, etc.)   
- **Responses RAW** → **Responses Curated**   
- **Validateurs T‑XX** (`validators/*.py`)   
- **Scoring** (`scores/raw/`) → **Scores Aggregated** (`scores/aggregated/`)   
- **Benchmark** (`benchmark/*.json`)   
- **Documentation** (architecture, scoring…)   
- **Metadata** (`schema.json`, info…)   

Le diagramme montre clairement la **chaîne de dépendances verticales**, depuis la théorie jusqu’aux artefacts finaux, ce qui permet de comprendre comment chaque module du corpus repose sur les précédents.

**EN —**  
This diagram represents the full set of **internal dependencies of the CATAR system**, organized as a vertical chain from conceptual foundations to the final benchmark.  
Each block corresponds to an explicit dependency shown in the file:  
- **Conceptual foundations** (folders 01 → 05)   
- **T‑XX Invariants** (defined in 01 → 05)   
- **T‑XX Prompts** (`prompts/T-XX/`)   
- **AI Model** (GPT, Mistral, etc.)   
- **RAW Responses** → **Curated Responses**   
- **T‑XX Validators** (`validators/*.py`)   
- **Scoring** (`scores/raw/`) → **Aggregated Scores** (`scores/aggregated/`)   
- **Benchmark** (`benchmark/*.json`)   
- **Documentation** (architecture, scoring…)   
- **Metadata** (`schema.json`, info…)   

This diagram provides a clear view of the **vertical dependency chain**, showing how each module of the corpus relies on the previous ones.

---

## 🧩 Diagramme / Diagram

*(The existing diagram begins here.)*

                           
                           +----------------------+
                           |     Corpus-CATAR     |
                           +----------+-----------+
                                      |
                                      v
                         +--------------------------+
                         |   Fondations conceptuelles|
                         |  (01 → 05 : théorie)      |
                         +-------------+-------------+
                                       |
                                       |  Dépendances conceptuelles
                                       v
                         +--------------------------+
                         |   Invariants T‑XX        |
                         | (définis dans 01 → 05)   |
                         +-------------+-------------+
                                       |
                                       |  Dépendances fonctionnelles
                                       v
                         +--------------------------+
                         |     PROMPTS T‑XX         |
                         |  (prompts/T-XX/)         |
                         +-------------+-------------+
                                       |
                                       |  Dépendances IA
                                       v
                         +--------------------------+
                         |      Modèle IA           |
                         | (GPT, Mistral, etc.)     |
                         +-------------+-------------+
                                       |
                                       |  Dépendances pipeline
                                       v
                         +--------------------------+
                         |   RESPONSES RAW          |
                         +-------------+-------------+
                                       |
                                       |  Dépendances curation
                                       v
                         +--------------------------+
                         |  RESPONSES CURATED       |
                         +-------------+-------------+
                                       |
                                       |  Dépendances analyse
                                       v
                         +--------------------------+
                         |   VALIDATEURS T‑XX       |
                         | (validators/*.py)        |
                         +-------------+-------------+
                                       |
                                       |  Dépendances scoring
                                       v
                         +--------------------------+
                         |        SCORING           |
                         |   (scores/raw/)          |
                         +-------------+-------------+
                                       |
                                       |  Dépendances statistiques
                                       v
                         +--------------------------+
                         |   SCORES AGGREGATED      |
                         |  (scores/aggregated/)    |
                         +-------------+-------------+
                                       |
                                       |  Dépendances fusion
                                       v
                         +--------------------------+
                         |       BENCHMARK          |
                         | (benchmark/*.json)       |
                         +-------------+-------------+
                                       |
                                       |  Dépendances documentation
                                       v
                         +--------------------------+
                         |          DOCS            |
                         | (architecture, scoring…) |
                         +-------------+-------------+
                                       |
                                       |  Dépendances schéma
                                       v
                         +--------------------------+
                         |        METADATA          |
                         | (schema.json, info…)     |
                         +--------------------------+
