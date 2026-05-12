📘 README — 06‑DATASET‑CATAR
Dataset officiel du Subnet CATAR
Cadre universel d’entraînement, d’évaluation et de calibration des IA

🜁 Mission du dataset CATAR
Le dataset CATAR constitue la base d’entraînement, de test et d’évaluation du Subnet CATAR.
Il rassemble :

les prompts CATAR (T‑XX)

les réponses générées par les IA

les scores produits par les validateurs

les métadonnées nécessaires à la reproductibilité

les versions successives du dataset

Il permet :

d’entraîner des modèles compatibles CATAR

de calibrer les miners et validateurs

de mesurer la stabilité cognitive d’une IA

de détecter les dérives (domination, projection, fascination…)

de garantir la cohérence psychologique du système

Ce dataset est la mémoire opérationnelle du Subnet CATAR.

🜂 Structure du dossier
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
Cette structure reprend fidèlement celle décrite dans ton README actuel.

🧱 Description des sous‑dossiers
📂 /prompts/
Contient les prompts CATAR officiels, organisés par invariant.
Chaque dossier T‑XX contient :

5 niveaux de difficulté (L1 → L5)

3 variations par niveau

un format JSON strict

des consignes minimales garantissant la neutralité et la non‑projection


📂 /responses/
raw/
Réponses brutes générées par :

les miners

les modèles externes

les IA en test

les sessions d’évaluation humaine

Aucune filtration, aucune correction.

curated/
Réponses :

nettoyées

validées

anonymisées

prêtes pour l’entraînement


📂 /scores/
raw/
Sorties directes des validateurs CATAR :

scores locaux

marqueurs détectés

détails heuristiques

aggregated/
Statistiques globales :

moyennes

écarts‑types

distributions

matrices de cohérence


📂 /metadata/
Contient les fichiers de structure et de versionnement :

schema.json → format officiel du dataset

dataset-info.json → version, taille, provenance

version-history.md → changelog complet


🧬 Format standard d’un exemple dataset
Exemple de prompt

Exemple de réponse

Exemple de score

🛠 Scripts inclus dans le dataset
1. generate_dataset.py
Génère automatiquement les réponses et scores à partir des prompts.

2. aggregate_scores.py
Produit les statistiques globales et par invariant.

3. build_benchmark.py
Construit CATAR-Benchmark-v1.json.

4. visualize_benchmark.py
Génère les figures dans /benchmark/figures/.

5. compare_models.py
Compare plusieurs modèles IA entre eux.

6. export_benchmark_csv.py
Exporte le benchmark en CSV.

7. validate_dataset.py
Vérifie la conformité de tous les fichiers au schema.json.

8. clean_dataset.py
Nettoyage intelligent des fichiers générés automatiquement.

9. build_all.py
Pipeline complet : dataset → scores → benchmark → figures → CSV.

🧠 Usage du dataset
Le dataset CATAR permet :

l’entraînement supervisé

la calibration des miners

la comparaison de modèles

la détection de dérives cognitives

la génération de benchmarks CATAR

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
Le dossier est prêt à accueillir :

les prompts

les réponses

les scores

les métadonnées

les benchmarks

les visualisations

Il constitue la base du futur CATAR‑Benchmark v2.0.
