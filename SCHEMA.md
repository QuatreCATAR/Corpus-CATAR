🜁 Schéma global — Pipeline CATAR
Code
                         ┌───────────────────────────┐
                         │       /prompts/ T‑XX       │
                         │  (11 invariants CATAR)     │
                         └──────────────┬────────────┘
                                        │
                                        ▼
                         ┌───────────────────────────┐
                         │   generate_dataset.py      │
                         │ Génération des réponses    │
                         └──────────────┬────────────┘
                                        │
                                        ▼
                    ┌────────────────────────────────────────┐
                    │          /responses/raw/                │
                    │ Réponses brutes (non nettoyées)        │
                    └──────────────┬─────────────────────────┘
                                   │
                                   ▼
                    ┌────────────────────────────────────────┐
                    │         score_responses.py              │
                    │ Application des invariants T‑XX         │
                    │ (validateurs CATAR)                     │
                    └──────────────┬─────────────────────────┘
                                   │
                                   ▼
                    ┌────────────────────────────────────────┐
                    │            /scores/raw/                 │
                    │ Scores bruts + marqueurs détectés       │
                    └──────────────┬─────────────────────────┘
                                   │
                                   ▼
                    ┌────────────────────────────────────────┐
                    │         curate_responses.py             │
                    │ Nettoyage + filtrage + validation       │
                    └──────────────┬─────────────────────────┘
                                   │
                                   ▼
                    ┌────────────────────────────────────────┐
                    │        /responses/curated/              │
                    │ Réponses validées (propres)             │
                    └──────────────┬─────────────────────────┘
                                   │
                                   ▼
                    ┌────────────────────────────────────────┐
                    │        aggregate_scores.py              │
                    │ Statistiques globales + invariants      │
                    └──────────────┬─────────────────────────┘
                                   │
                                   ▼
                    ┌────────────────────────────────────────┐
                    │        /scores/aggregated/              │
                    │ Moyennes, variances, matrices           │
                    └──────────────┬─────────────────────────┘
                                   │
                                   ▼
                    ┌────────────────────────────────────────┐
                    │         build_benchmark.py              │
                    │ Fusion réponses + scores                │
                    └──────────────┬─────────────────────────┘
                                   │
                                   ▼
                    ┌────────────────────────────────────────┐
                    │           /benchmark/                   │
                    │ CATAR‑Benchmark‑v1.json                 │
                    │ figures/ + comparaisons                 │
                    └────────────────────────────────────────┘
🜂 Description synthétique des étapes
1. Prompts → Génération
Les invariants T‑XX définis dans /prompts/ sont utilisés pour générer les réponses brutes.
(Structure confirmée dans la section Dataset du dépôt )

2. Réponses brutes → Scoring
Les validateurs CATAR appliquent les invariants cognitifs T‑ND, T‑NP, T‑NF, T‑SM, T‑SU, T‑TV, etc.
(Section Invariants du dépôt )

3. Scores bruts → Curating
Les réponses incohérentes ou violant un invariant sont filtrées.
Les réponses valides sont nettoyées et normalisées.

4. Réponses validées → Statistiques
Les scores sont agrégés pour produire :

moyennes

variances

matrices de cohérence

distributions

(Section Benchmark et Tools du dépôt )

5. Dataset complet → Benchmark
Fusion des réponses curated + scores agrégés → CATAR-Benchmark-v1.json.

6. Benchmark → API / Analyse / Comparaison
Le benchmark sert à :

comparer des modèles

analyser la stabilité cognitive

détecter les dérives

alimenter l’API CATAR
(Section API du dépôt )

🜄 Version ultra‑compacte
Code
prompts
   → raw responses
      → raw scores
         → curated responses
            → aggregated scores
               → benchmark
🜇 Version conceptuelle (haute lisibilité)
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

