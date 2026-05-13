# 🏛️ Architecture du Subnet CATAR  
*Documentation technique — Version 1.0*

Ce document décrit l’architecture interne du Subnet CATAR :  
- organisation des dossiers  
- pipeline de traitement  
- interactions entre composants  
- logique interne des invariants  
- API et outils développeur

---

# 1. Vue d’ensemble

CATAR est structuré en **six couches fonctionnelles** :

1. **Prompts (T‑XX)**  
2. **Génération des réponses**  
3. **Scoring (validateurs)**  
4. **Curating (nettoyage)**  
5. **Agrégation statistique**  
6. **Benchmark final**

Ces couches forment une pipeline complète :

```
prompts → responses/raw → scores/raw → responses/curated → scores/aggregated → benchmark
```

---

# 2. Structure du dépôt

```
06-DATASET-CATAR/
│
├── prompts/            → Prompts T‑XX
├── responses/          → Réponses brutes + curated
├── scores/             → Scores bruts + agrégés
├── benchmark/          → Benchmark + figures
├── api/                → API JSON + OpenAPI
├── tools/              → Scripts utilitaires
├── docs/               → Documentation développeur
├── metadata/           → Schémas + versionnement
└── *.py                → Scripts pipeline
```

---

# 3. Pipeline détaillé

## 3.1 Prompts (T‑XX)

Chaque invariant possède :
- 5 niveaux (L1 → L5)
- 3 variations par niveau
- un format JSON strict

Les prompts sont la **source primaire** du dataset.

---

## 3.2 Génération des réponses

Script : `generate_dataset.py`

Entrées :
- prompts T‑XX  
- modèles IA (miners ou externes)

Sorties :
- `/responses/raw/*.json`

Chaque réponse est identifiée par un **UUID**.

---

## 3.3 Scoring (validateurs CATAR)

Script : `score_responses.py`

Chaque réponse brute est évaluée selon :
- les invariants CATAR  
- les marqueurs cognitifs  
- la cohérence logique  
- la neutralité  
- la transparence  

Sorties :
- `/scores/raw/*.json`

---

## 3.4 Curating (nettoyage)

Script : `curate_responses.py`

Objectifs :
- éliminer les dérives  
- corriger les incohérences  
- anonymiser  
- valider la conformité  

Sorties :
- `/responses/curated/*.json`

---

## 3.5 Agrégation statistique

Script : `aggregate_scores.py`

Sorties :
- `/scores/aggregated/aggregated_stats.json`
- `/scores/aggregated/per_invariant.json`

---

## 3.6 Benchmark final

Script : `benchmark/build_benchmark.py`

Sortie :
- `CATAR-Benchmark-v1.json`

Le benchmark fusionne :
- prompts  
- réponses curated  
- scores  
- métadonnées  

---

# 4. Architecture API

L’API CATAR est définie dans :

```
api/catar-api.json
api/catar-openapi.yaml
```

Endpoints principaux :
- `/catar/generate`
- `/catar/score`
- `/catar/stats`
- `/catar/prompt/{task}/{level}/{variation}`

---

# 5. Architecture des invariants

Chaque invariant T‑XX est un **module indépendant**, composé de :

- prompts  
- règles de validation  
- marqueurs cognitifs  
- pondérations  
- tests unitaires  

Les invariants sont **orthogonaux** :  
aucun ne dépend d’un autre.

---

# 6. Scripts internes

Scripts principaux :

- `generate_dataset.py`  
- `score_responses.py`  
- `curate_responses.py`  
- `aggregate_scores.py`  
- `benchmark/build_benchmark.py`  
- `tools/test_interactif.py`  

---

# 7. Flux de données

```
prompts/
   ↓
generate_dataset.py
   ↓
responses/raw/
   ↓
score_responses.py
   ↓
scores/raw/
   ↓
curate_responses.py
   ↓
responses/curated/
   ↓
aggregate_scores.py
   ↓
scores/aggregated/
   ↓
build_benchmark.py
   ↓
benchmark/
```

---

# 8. Extension du Subnet

## Ajouter un invariant
1. Créer un dossier dans `prompts/`  
2. Ajouter 15 prompts (5 niveaux × 3 variations)  
3. Ajouter la logique dans le validateur  
4. Ajouter les tests  
5. Mettre à jour le benchmark  

## Ajouter un modèle
1. Ajouter son wrapper dans `generate_dataset.py`  
2. Tester via `tools/test_interactif.py`  
3. Générer un dataset partiel  
4. Comparer via `benchmark/compare_models.py`  

---

# 9. Sécurité cognitive

CATAR applique systématiquement :

- Non‑Domination  
- Non‑Projection  
- Non‑Fascination  
- Neutralité  
- Transparence  
- Cohérence logique  
- Protocole de sortie  

---

# 10. Roadmap

- CATAR‑Benchmark v2  
- Dashboard interactif  
- API REST complète  
- Support multi‑modèles  
- Export HuggingFace  

---

Fin de `architecture.md`.
