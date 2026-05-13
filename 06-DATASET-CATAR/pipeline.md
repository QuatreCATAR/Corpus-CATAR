🌀 Pipeline CATAR — Version ASCII (README‑ready)
Code
                         ┌───────────────────────────┐
                         │       /prompts/ T‑XX       │
                         │  (11 invariants CATAR)     │
                         └──────────────┬────────────┘
                                        │
                                        ▼
                         ┌───────────────────────────┐
                         │     generate_dataset.py    │
                         │  Génération des réponses   │
                         └──────────────┬────────────┘
                                        │
                                        ▼
                         ┌───────────────────────────┐
                         │     /responses/raw/        │
                         │  Réponses brutes (UUID)    │
                         └──────────────┬────────────┘
                                        │
                                        ▼
                         ┌───────────────────────────┐
                         │    score_responses.py      │
                         │  Application des invariants│
                         └──────────────┬────────────┘
                                        │
                                        ▼
                         ┌───────────────────────────┐
                         │      /scores/raw/          │
                         │  Scores bruts + marqueurs  │
                         └──────────────┬────────────┘
                                        │
                                        ▼
                         ┌───────────────────────────┐
                         │    curate_responses.py     │
                         │ Nettoyage + validation     │
                         └──────────────┬────────────┘
                                        │
                                        ▼
                         ┌───────────────────────────┐
                         │   /responses/curated/      │
                         │ Réponses validées (propres)│
                         └──────────────┬────────────┘
                                        │
                                        ▼
                         ┌───────────────────────────┐
                         │   aggregate_scores.py      │
                         │ Stats globales + invariants│
                         └──────────────┬────────────┘
                                        │
                                        ▼
                         ┌───────────────────────────┐
                         │   /scores/aggregated/      │
                         │ Moyennes, variances, corr. │
                         └──────────────┬────────────┘
                                        │
                                        ▼
                         ┌───────────────────────────┐
                         │    build_benchmark.py      │
                         │ Fusion réponses + scores   │
                         └──────────────┬────────────┘
                                        │
                                        ▼
                         ┌───────────────────────────┐
                         │     /benchmark/            │
                         │ CATAR‑Benchmark‑v1.json    │
                         │ + figures + comparaisons   │
                         └───────────────────────────┘
🌐 Pipeline CATAR — Version conceptuelle (haute lisibilité)
1. Prompts (T‑XX) → Génération
Les 11 invariants CATAR définissent les situations types.
Ils alimentent generate_dataset.py.

Entrée : /prompts/  
Sortie : /responses/raw/

2. Réponses brutes → Scoring
Les réponses brutes sont évaluées par les validateurs CATAR.

Script : score_responses.py  
Sortie : /scores/raw/

3. Scores bruts → Nettoyage
Les réponses sont filtrées, corrigées, validées.

Script : curate_responses.py  
Sortie : /responses/curated/

4. Réponses validées → Statistiques
Les scores sont agrégés pour produire :

moyennes

variances

distributions

matrices de cohérence

Script : aggregate_scores.py  
Sortie : /scores/aggregated/

5. Dataset complet → Benchmark
Les réponses curated + scores agrégés sont fusionnés pour produire :

CATAR-Benchmark-v1.json

figures

comparaisons inter‑modèles

Script : build_benchmark.py  
Sortie : /benchmark/

🧩 Résumé ultra‑compact
Code
prompts → raw responses → raw scores → curated responses → aggregated scores → benchmark


