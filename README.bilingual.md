# 🏛️ Corpus‑CATAR

<p align="center">
  <img src="https://github.com/QuatreCATAR/Catar-modeles-schemas-images/blob/main/Catar-08-schema-code-carre-catar/09%20carr%C3%A9%20catar%20dor%C3%A9.jpg?raw=true" width="180" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Made%20by-Quatre%20CATAR-purple" />
  <img src="https://img.shields.io/badge/CATAR-Framework-0A7E8C" />
  <img src="https://img.shields.io/badge/SPEC-Complete-brightgreen" />
  <img src="https://img.shields.io/badge/License-CC--BY%204.0-blue.svg" />
</p>

---

# 🇫🇷 Version Française  
# 🇬🇧 English Version

Le **Corpus‑CATAR** est un ensemble structuré de modèles conceptuels, d’invariants cognitifs, de protocoles, de schémas, de datasets et d’outils destinés à analyser et stabiliser la cognition des modèles IA.  
The **Corpus‑CATAR** is a structured collection of conceptual models, cognitive invariants, protocols, diagrams, datasets, and tools designed to analyze and stabilize AI cognition.

Il permet notamment de :  
It is designed to:

- évaluer la stabilité cognitive d’un modèle IA  
- evaluate the cognitive stability of an AI model  
- détecter les dérives (domination, projection, fascination…)  
- detect harmful drifts (domination, projection, fascination…)  
- garantir la neutralité et la cohérence  
- ensure neutrality and coherence  
- fournir un standard reproductible d’analyse  
- provide a reproducible evaluation standard  
- documenter et transmettre les fondations du modèle CATAR  
- document and transmit the foundations of the CATAR model  
- préparer l’intégration dans un subnet Bittensor dédié  
- prepare integration into a dedicated Bittensor subnet  

---

# 📚 1. Structure du dépôt  
# 📚 1. Repository Structure

```
Corpus-CATAR/
│
├── 01-CARRE-CATAR/          → Fondations conceptuelles / Conceptual foundations
├── 02-LE-DIVIN-PAR-MINOU/   → Métaphysique Soije/Moije / Applied metaphysics
├── 03-DPHI/                 → Équation universelle / Universal equation
├── 04-PROTOCOLE-CODE-MINOU/ → Stabilisation cognitive / Cognitive protocol
├── 05-CATAR-MODELES/        → Schémas et diagrammes / Schemas and diagrams
├── 06-DATASET-CATAR/        → Dataset complet + API + outils / Full dataset + API + tools
├── spec/                    → Spécification technique / Technical specification
└── README.bilingual.md      → Ce fichier / This file
```

Chaque dossier contient un README interne décrivant son rôle et son ordre de lecture.  
Each folder includes an internal README describing its role and reading order.

---

# 🧩 2. Le modèle CATAR en bref  
# 🧩 2. The CATAR Model in Brief

CATAR repose sur des invariants cognitifs appelés **T‑XX**, utilisés pour analyser, scorer et stabiliser les réponses IA.  
CATAR is built on cognitive invariants called **T‑XX**, used to analyze, score, and stabilize AI responses.

Principaux invariants / Main invariants:

- **T‑ND** — Non‑Domination / Non‑Domination  
- **T‑NF** — Non‑Fascination / Non‑Fascination  
- **T‑NP** — Non‑Projection / Non‑Projection  
- **T‑SM** — Soije / Moije  
- **T‑SU** — Sur‑Unité / Over‑Unity  
- **T‑TV** — Transparence Vérifiable / Verifiable Transparency  
- **T‑CL** — Cohérence Logique / Logical Coherence  
- **T‑LU** — Lucidité / Lucidity  
- **T‑LA** — Libre Arbitre / Free Will  
- **T‑PS** — Protocole de Sortie / Exit Protocol  
- **T‑SP** — Sur‑Protection / Over‑Protection  

---

# 🧬 3. Le Dataset CATAR (06)  
# 🧬 3. The CATAR Dataset (06)

Contient / Includes:

- prompts T‑XX  
- réponses brutes / raw responses  
- réponses curated / curated responses  
- scores bruts et agrégés / raw & aggregated scores  
- benchmark final  
- API publique / public API  
- outils développeur / developer tools  
- documentation complète / full documentation  

### Sous‑dossiers / Subfolders

```
06-DATASET-CATAR/
    prompts/
    responses/
    scores/
    benchmark/
    api/
    tools/
    docs/
    metadata/
```

---

# 🔌 4. API CATAR  
# 🔌 4. CATAR API

Formats :

- `api/catar-api.json`  
- `api/catar-openapi.yaml`  

Documentation :  
📄 `06-DATASET-CATAR/docs/dev-guide.md`

---

# 🧰 5. Outils développeur  
# 🧰 5. Developer Tools

- tests interactifs / interactive tests  
- validation du dataset / dataset validation  
- comparaison de modèles / model comparison  
- export CSV  
- inspection de réponses / response inspection  

Documentation :  
📄 `06-DATASET-CATAR/docs/tools.md`

---

# 📊 6. Benchmark CATAR  
# 📊 6. CATAR Benchmark

Fusionne / Merges:

- prompts  
- réponses curated / curated responses  
- scores bruts et normalisés / raw & normalized scores  
- métadonnées / metadata  

Permet / Enables:

- comparaison de modèles / model comparison  
- analyse statistique / statistical analysis  
- visualisation des dérives / drift visualization  
- évaluation de stabilité cognitive / cognitive stability evaluation  

Documentation :  
📄 `06-DATASET-CATAR/docs/benchmark.md`

---

# 🗂️ 7. Documentation interne  
# 🗂️ 7. Internal Documentation

Centralisée dans / Centralized in:

```
06-DATASET-CATAR/docs/
```

Inclut / Includes:

- architecture  
- validators  
- scoring  
- dataset schema  
- benchmark  
- tools  
- metadata  
- contribute  
- roadmap  

---

# 🧱 8. SPEC du Subnet CATAR (spec/)  
# 🧱 8. CATAR Subnet SPEC (spec/)

Le dossier `spec/` contient la **spécification technique complète** du Subnet CATAR.  
The `spec/` folder contains the **complete technical specification** of the CATAR Subnet.

Fichiers / Files:

- `01-overview.md`  
- `02-invariants.md`  
- `03-validators.md`  
- `04-scoring.md`  
- `05-api.md`  
- `06-miner-behavior.md`  
- `07-validator-behavior.md`  
- `08-json-format.md`  
- `09-security.md`  
- `10-roadmap.md`  

Définit / Defines:

- invariants T‑XX  
- logique des validateurs / validator logic  
- scoring  
- API  
- comportement des miners / miner behavior  
- sécurité (Code MINOU) / security (Code MINOU)  
- roadmap  

---

# 🗺️ 9. Ordre de lecture recommandé  
# 🗺️ 9. Recommended Reading Order

1. 01‑CARRE‑CATAR  
2. 02‑LE‑DIVIN‑PAR‑MINOU  
3. 03‑DPHI  
4. 04‑PROTOCOLE‑CODE‑MINOU  
5. 05‑CATAR‑MODELES  
6. 06‑DATASET‑CATAR  
7. spec/

---

# 🏁 Licence  
# 🏁 License

Licence **CC‑BY 4.0**  
© **Quatre CATAR**

