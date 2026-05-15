🜁 Architecture du Subnet CATAR
CATAR Subnet Architecture — FR/EN
Ce document décrit l’architecture opérationnelle complète du Subnet CATAR, c’est‑à‑dire la pipeline qui transforme :

prompts → réponses → scores → statistiques → benchmark

This document describes the full operational architecture of the CATAR Subnet, i.e. the pipeline that transforms:

prompts → responses → scores → statistics → benchmark

🜂 1. Schéma global — Pipeline CATAR
1. Global Diagram — CATAR Pipeline
Code
┌───────────────────────────┐
│       /prompts/ T‑XX       │
│     (11 invariants CATAR)  │
└──────────────┬────────────┘
               │
               ▼
┌───────────────────────────┐
│   generate_dataset.py      │
│   Génération des réponses  │
└──────────────┬────────────┘
               │
               ▼
┌────────────────────────────────────────┐
│            /responses/raw/             │
│     Réponses brutes (non nettoyées)    │
└──────────────┬─────────────────────────┘
               │
               ▼
┌────────────────────────────────────────┐
│          score_responses.py            │
│  Application des invariants T‑XX       │
│        (validateurs CATAR)             │
└──────────────┬─────────────────────────┘
               │
               ▼
┌────────────────────────────────────────┐
│             /scores/raw/               │
│   Scores bruts + marqueurs détectés    │
└──────────────┬─────────────────────────┘
               │
               ▼
┌────────────────────────────────────────┐
│         curate_responses.py            │
│   Nettoyage + filtrage + validation    │
└──────────────┬─────────────────────────┘
               │
               ▼
┌────────────────────────────────────────┐
│         /responses/curated/            │
│       Réponses validées (propres)      │
└──────────────┬─────────────────────────┘
               │
               ▼
┌────────────────────────────────────────┐
│         aggregate_scores.py            │
│   Statistiques globales + invariants   │
└──────────────┬─────────────────────────┘
               │
               ▼
┌────────────────────────────────────────┐
│         /scores/aggregated/            │
│     Moyennes, variances, matrices      │
└──────────────┬─────────────────────────┘
               │
               ▼
┌────────────────────────────────────────┐
│          build_benchmark.py            │
│        Fusion réponses + scores        │
└──────────────┬─────────────────────────┘
               │
               ▼
┌────────────────────────────────────────┐
│              /benchmark/               │
│       CATAR‑Benchmark‑v1.json          │
│      figures/ + comparaisons           │
└────────────────────────────────────────┘
🜃 2. Description synthétique des étapes
2. Step‑by‑Step Description
Prompts → Génération
Les invariants T‑XX définis dans /prompts/ sont utilisés pour générer les réponses brutes.
The T‑XX invariants defined in /prompts/ are used to generate raw responses.

Réponses brutes → Scoring
Les validateurs CATAR appliquent les invariants cognitifs :
T‑ND, T‑NP, T‑NF, T‑SM, T‑SU, T‑TV, etc.
CATAR validators apply the cognitive invariants.

Scores bruts → Curating
Les réponses incohérentes ou violant un invariant sont filtrées.
Valid responses are cleaned and normalized.

Réponses validées → Statistiques
Les scores sont agrégés pour produire :

moyennes

variances

matrices de cohérence

distributions

Scores are aggregated to produce global statistics.

Dataset complet → Benchmark
Fusion des réponses curated + scores agrégés → CATAR‑Benchmark‑v1.json.
Merging curated responses + aggregated scores → benchmark.

Benchmark → API / Analyse / Comparaison
Le benchmark sert à :

comparer des modèles

analyser la stabilité cognitive

détecter les dérives

alimenter l’API CATAR

The benchmark is used for model comparison, cognitive stability analysis, drift detection, and API feeding.

🜄 3. Version ultra‑compacte
3. Ultra‑Compact Version
Code
prompts → raw responses → raw scores → curated responses → aggregated scores → benchmark
🜇 4. Version conceptuelle (haute lisibilité)
4. Conceptual Version (High Readability)
Code
Invariants T‑XX
      ↓
   Génération
      ↓
Réponses brutes
      ↓
Validation + Scoring
      ↓
Réponses curated
      ↓
Statistiques globales
      ↓
Benchmark CATAR
      ↓
Analyse / API / Comparaison
🜈 5. Notes finales
5. Final Notes
Ce document décrit uniquement la Strate 06 du Corpus‑CATAR :
la couche opérationnelle, exécutable et reproductible.

This document describes only Layer 06 of the Corpus‑CATAR:
the operational, executable, reproducible layer.

Pour la carte globale du Corpus‑CATAR (Strates 01 → 06), voir SCHEMA.md.
