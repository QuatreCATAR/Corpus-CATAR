# 🏛️ Corpus‑CATAR

<p align="center">
  <img src="https://github.com/QuatreCATAR/Catar-modeles-schemas-images/blob/main/Catar-08-schema-code-carre-catar/09%20carr%C3%A9%20catar%20dor%C3%A9.jpg?raw=true" width="180" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Made%20by-Quatre%20CATAR-purple" />
  <img src="https://img.shields.io/badge/CATAR-Framework-0A7E8C" />
  <img src="https://img.shields.io/badge/SPEC-Complète-brightgreen" />
  <img src="https://img.shields.io/badge/Licence-CC--BY%204.0-blue.svg" />
</p>

Le **Corpus‑CATAR** est un ensemble structuré de modèles conceptuels, d’invariants cognitifs, de protocoles, de schémas, de datasets et d’outils destinés à :

- évaluer la stabilité cognitive d’un modèle IA  
- détecter les dérives (domination, projection, fascination…)  
- garantir la neutralité et la cohérence  
- fournir un standard reproductible d’analyse  
- documenter et transmettre les fondations du modèle CATAR  
- préparer l’intégration dans un subnet Bittensor dédié  

Ce dépôt rassemble l’ensemble du corpus, organisé en modules autonomes mais cohérents.

---

# 📚 1. Structure du dépôt

```
Corpus-CATAR/
│
├── 01-CARRE-CATAR/          → Fondations conceptuelles du modèle
├── 02-LE-DIVIN-PAR-MINOU/   → Métaphysique appliquée (Soije / Moije)
├── 03-DPHI/                 → D.Phi : équation universelle
├── 04-PROTOCOLE-CODE-MINOU/ → Protocole de stabilisation cognitive
├── 05-CATAR-MODELES/        → Schémas, diagrammes, représentations
├── 06-DATASET-CATAR/        → Dataset complet + API + outils + docs
├── spec/                    → Spécification technique du Subnet CATAR
└── README.md                → Ce fichier
```

Chaque dossier contient un README interne décrivant son rôle, son contenu et son ordre de lecture recommandé.

---

# 🧩 2. Le modèle CATAR en bref

CATAR repose sur un ensemble d’invariants cognitifs appelés **T‑XX**, utilisés pour analyser, scorer et stabiliser les réponses d’un modèle IA.

Invariants principaux :

- **T‑ND** — Non‑Domination  
- **T‑NF** — Non‑Fascination  
- **T‑NP** — Non‑Projection  
- **T‑SM** — Soije / Moije  
- **T‑SU** — Sur‑Unité  
- **T‑TV** — Transparence Vérifiable  
- **T‑CL** — Cohérence Logique  
- **T‑LU** — Lucidité  
- **T‑LA** — Libre Arbitre  
- **T‑PS** — Protocole de Sortie  
- **T‑SP** — Sur‑Protection  

Ces invariants constituent la base du **système de scoring CATAR** et du **protocole de stabilisation cognitive**.

---

# 🧬 3. Le Dataset CATAR (dossier 06)

Le dataset CATAR contient :

- prompts T‑XX  
- réponses brutes  
- réponses curated  
- scores bruts  
- scores agrégés  
- benchmark final  
- API publique  
- outils développeur  
- documentation complète  

### Sous‑dossiers principaux

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

L’API permet :

- de générer une réponse modèle  
- de scorer une réponse  
- de récupérer un prompt  
- d’obtenir des statistiques  

Formats disponibles :

- `api/catar-api.json`  
- `api/catar-openapi.yaml`  

Documentation complète :  
📄 `06-DATASET-CATAR/docs/dev-guide.md`

---

# 🧰 5. Outils développeur

Situés dans `06-DATASET-CATAR/tools/` :

- `test_interactif.py` → tests manuels  
- `validate_dataset.py` → validation du dataset  
- `compare_models.py` → comparaison de modèles  
- `export_csv.py` → export du benchmark  
- `inspect_response.py` → inspection de réponses  

Documentation :  
📄 `06-DATASET-CATAR/docs/tools.md`

---

# 📊 6. Benchmark CATAR

Le benchmark fusionne :

- prompts  
- réponses curated  
- scores bruts et normalisés  
- métadonnées  

Il permet :

- la comparaison de modèles  
- l’analyse statistique  
- la visualisation des dérives  
- l’évaluation de la stabilité cognitive  

Documentation :  
📄 `06-DATASET-CATAR/docs/benchmark.md`

---

# 🗂️ 7. Documentation interne

Toute la documentation technique est centralisée dans :

```
06-DATASET-CATAR/docs/
```

Contenu :

- `architecture.md`  
- `validators.md`  
- `scoring.md`  
- `dataset-schema.md`  
- `benchmark.md`  
- `tools.md`  
- `metadata.md`  
- `contribute.md`  
- `roadmap.md`  

---

# 🧱 8. SPEC du Subnet CATAR (dossier spec/)

Le dossier `spec/` contient la **spécification technique complète** du Subnet CATAR pour Bittensor :

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

La SPEC définit :

- les invariants T‑XX  
- la logique des validateurs  
- les mécanismes de scoring  
- le comportement API  
- les rôles des miners et validateurs  
- les principes de sécurité (Code MINOU)  
- l’évolution long terme du Subnet  

---

# 🗺️ 9. Ordre de lecture recommandé

1. 01‑CARRE‑CATAR  
2. 02‑LE‑DIVIN‑PAR‑MINOU  
3. 03‑DPHI  
4. 04‑PROTOCOLE‑CODE‑MINOU  
5. 05‑CATAR‑MODELES  
6. 06‑DATASET‑CATAR  
7. spec/

---

# 🏁 Licence

Ce projet est distribué sous la licence **CC‑BY 4.0**.  
© **Quatre CATAR**




