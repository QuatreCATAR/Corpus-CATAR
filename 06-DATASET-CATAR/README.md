📘 README — 06‑DATASET‑CATAR
Dataset officiel du Subnet CATAR
Cadre universel d’entraînement, d’évaluation et de calibration des IA

🜁 Mission du dataset CATAR
Le dataset CATAR constitue la base d’entraînement, de test et d’évaluation du Subnet CATAR.
Il rassemble l’ensemble des éléments nécessaires à la stabilité cognitive, à la neutralité épistémique et à la calibration comportementale des IA.

Selon la structure affichée dans ton dépôt, il inclut :

les prompts CATAR (T‑XX)

les réponses générées

les scores produits par les validateurs

les statistiques agrégées

les benchmarks

les métadonnées (schéma, version, historique) 

Ce dataset est la mémoire opérationnelle du Subnet CATAR.

🜂 Structure du dossier
La structure complète du dataset, telle qu’affichée dans ton dépôt, est la suivante  :

Code
06-DATASET-CATAR/
│
├── README.md
│
├── prompts/
│   ├── T-CL/
│   ├── T-SP/
│   ├── T-ND/
│   ├── T-NF/
│   ├── T-NP/
│   ├── T-SM/
│   ├── T-LU/
│   ├── T-LA/
│   ├── T-PS/
│   ├── T-SU/
│   ├── T-TV/
│   └── T-CL-global/
│
├── responses/
│   ├── raw/
│   └── curated/
│
├── scores/
│   ├── raw/
│   └── aggregated/
│
├── benchmark/
│   ├── CATAR-Benchmark-v1.json
│   ├── build_benchmark.py
│   ├── visualize_benchmark.py
│   ├── compare_models.py
│   ├── export_benchmark_csv.py
│   └── figures/
│
├── schema.json
├── dataset-info.json
├── version-history.md
│
├── generate_dataset.py
├── validate_dataset.py
├── clean_dataset.py
└── build_all.py
🧱 Description des sous‑dossiers
📂 /prompts/
Contient les prompts CATAR officiels, organisés par invariant.
Chaque dossier T‑XX contient :

5 niveaux de difficulté

3 variations par niveau

un format JSON strict

des consignes minimales garantissant la neutralité 

📂 /responses/
Deux sous‑dossiers :

raw/ → réponses brutes (non filtrées)

curated/ → réponses nettoyées, validées, prêtes pour l’entraînement 

📂 /scores/
Deux sous‑dossiers :

raw/ → scores bruts (sorties directes des validateurs)

aggregated/ → statistiques globales, distributions, matrices de cohérence 

📂 /metadata/
Contient les fichiers de structure et de versionnement :

schema.json → format officiel du dataset

dataset-info.json → version, taille, provenance

version-history.md → changelog complet 

📂 /benchmark/
Contient :

CATAR-Benchmark-v1.json

scripts d’analyse

visualisations dans /figures/ 

🛠 Scripts inclus
La page GitHub liste explicitement les scripts suivants  :

generate_dataset.py — génère réponses + scores

aggregate_scores.py — statistiques globales

build_benchmark.py — construit CATAR‑Benchmark‑v1

visualize_benchmark.py — figures dans /benchmark/figures/

compare_models.py — comparaison inter‑modèles

export_benchmark_csv.py — export CSV

validate_dataset.py — conformité au schéma

clean_dataset.py — nettoyage intelligent

build_all.py — pipeline complet : dataset → scores → benchmark → figures → CSV

🧬 Format standard d’un exemple dataset
Le dataset inclut :

un exemple de prompt

un exemple de réponse

un exemple de score

Ces exemples sont fournis dans les README des sous‑dossiers correspondants .

🧠 Usage du dataset
Le dataset CATAR permet :

l’entraînement supervisé

la calibration des miners

la comparaison de modèles

la détection de dérives cognitives

la génération de benchmarks

la validation de cohérence globale 

🛡️ Principes de sécurité CATAR
Le dataset respecte strictement :

la non‑domination

la non‑projection

la non‑fascination

la séparation Soije / Moije

la transparence vérifiable

la neutralité épistémique

le protocole de sortie 

✔️ État actuel
La page GitHub indique que :

« Le dossier est prêt à accueillir les prompts, les réponses, les scores, les métadonnées, les benchmarks et les visualisations. » 

Il constitue la base du futur :

CATAR‑Benchmark v2.0 


