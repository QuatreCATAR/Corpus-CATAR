# 📘 UML — Structural Diagram of Corpus‑CATAR (STRUCTUREL)

**File:** `10-STRUCTUREL.md`  
**Category:** UML — Structural / System Architecture  
**Version:** 1.0  
**Project:** Corpus‑CATAR  
**Author:** Quatre CATAR  

---

## 📝 Description / Description

**FR —**  
Ce diagramme représente la **structure globale du Corpus‑CATAR**, organisée en modules principaux et sous‑systèmes.  
Il montre la hiérarchie des dossiers conceptuels (01 à 05), la structure du dataset (06‑DATASET‑CATAR), ainsi que leurs sous‑composants internes tels que `prompts/`, `responses/`, `scores/`, `benchmark/`, `api/`, `tools/`, et `docs/` .  
Le diagramme inclut également les sous‑sections documentaires (`dev-guide`, `architecture`, `scoring`, `dataset-schema`, `benchmark`, `metadata`, `roadmap`) et les fichiers de métadonnées (`schema.json`, `dataset-info`, `invariants-index`) .  
Il sert de **vue d’ensemble structurelle**, permettant de comprendre comment les différentes parties du corpus s’articulent entre elles.

**EN —**  
This diagram represents the **global structural architecture of the Corpus‑CATAR**, organized into its main modules and subsystems.  
It displays the hierarchy of conceptual folders (01 to 05), the dataset structure (06‑DATASET‑CATAR), and internal components such as `prompts/`, `responses/`, `scores/`, `benchmark/`, `api/`, `tools/`, and `docs/` .  
The diagram also includes documentation subsections (`dev-guide`, `architecture`, `scoring`, `dataset-schema`, `benchmark`, `metadata`, `roadmap`) and metadata files (`schema.json`, `dataset-info`, `invariants-index`) .  
It provides a **structural overview** of how all parts of the corpus interconnect.

---

## 🧩 Diagramme / Diagram

*(The existing diagram begins here.)*

                           
                           +----------------------+
                           |     Corpus-CATAR     |
                           +----------+-----------+
                                      |
        --------------------------------------------------------------------
        |            |                |                |                   |
+---------------+ +---------------+ +---------------+ +---------------+ +---------------+
| 01-CARRE-     | | 02-LE-DIVIN-  | | 03-DPHI       | | 04-PROTOCOLE- | | 05-CATAR-     |
|    CATAR      | |    PAR-MINOU  | | (Équation)    | |   CODE-MINOU  | |   MODELES      |
+---------------+ +---------------+ +---------------+ +---------------+ +---------------+
                                      |
                                      |
                           +---------------------------+
                           |     06-DATASET-CATAR      |
                           +--------------+------------+
                                          |
      -----------------------------------------------------------------------------------------
      |               |                 |                 |                 |                 |
+-----------+  +--------------+  +--------------+  +--------------+  +--------------+  +--------------+
| prompts/  |  | responses/   |  | scores/      |  | benchmark/   |  | api/         |  | tools/       |
|  T-XX     |  | raw/curated  |  | raw/agg      |  | JSON/figures |  | OpenAPI      |  | *.py scripts |
+-----------+  +--------------+  +--------------+  +--------------+  +--------------+  +--------------+
                                          |
                                          |
                                +---------------------+
                                |        docs/        |
                                +----------+----------+
                                           |
       -----------------------------------------------------------------------------------------------
       |             |             |             |             |             |             |          |
+-------------+ +-------------+ +-------------+ +-------------+ +-------------+ +-------------+ +-------------+
| dev-guide   | | architecture| | scoring     | | dataset-    | | benchmark  | | metadata    | | roadmap     |
|             | |             | |             | | schema      | |            | |             | |             |
+-------------+ +-------------+ +-------------+ +-------------+ +-------------+ +-------------+ +-------------+
                                           |
                                           |
                                +---------------------+
                                |     metadata/       |
                                +----------+----------+
                                           |
                     -------------------------------------------------
                     |                       |                       |
              +---------------+      +---------------+      +---------------------+
              | schema.json   |      | dataset-info  |      | invariants-index    |
              +---------------+      +---------------+      +---------------------+
