📘 README — /scores
Scores bruts et statistiques agrégées du dataset CATAR
Couche analytique du pipeline CATAR

🜁 Rôle du dossier
Le dossier /scores regroupe toutes les données de scoring produites par les validateurs CATAR.
Il constitue la couche analytique du dataset, située entre :

les réponses (/responses/)

et le benchmark (/benchmark/)

Les scores permettent :

d’évaluer la stabilité cognitive du modèle

de mesurer la conformité aux invariants CATAR

de détecter les dérives comportementales

d’alimenter les statistiques globales et par invariant

de construire le benchmark CATAR v1

Le dossier est divisé en deux sous‑dossiers :

Code
scores/
    raw/         → scores bruts (un par réponse)
    aggregated/  → statistiques globales et par invariant
🗂️ Sous‑dossiers
📁 /scores/raw/
Contient les scores bruts, un fichier JSON par réponse évaluée.

Chaque fichier inclut :

uuid

task_id (invariant CATAR)

global_score

markers_detected

details (sous‑scores)

validator_version

Ces fichiers sont la source primaire pour toute analyse statistique.

Voir README dédié dans /scores/raw/.

📁 /scores/aggregated/
Contient les statistiques dérivées des scores bruts :

aggregated_stats.json → statistiques globales

per_invariant.json → statistiques par invariant

aggregate_scores.py → script de génération

Ces fichiers permettent :

d’évaluer la stabilité globale du modèle

de comparer les invariants entre eux

d’alimenter les visualisations et le benchmark

Voir README dédié dans /scores/aggregated/.

🧬 Rôle dans la pipeline CATAR
Les scores interviennent dans toutes les étapes du pipeline :

1. Validation
Les validateurs CATAR analysent chaque réponse brute et produisent un score global + des marqueurs.

2. Agrégation
Les scores bruts sont regroupés pour produire :

des statistiques globales

des statistiques par invariant

des distributions

3. Benchmark
Les scores sont fusionnés avec :

les prompts

les réponses curated

pour produire :

Code
/benchmark/CATAR-Benchmark-v1.json
4. Analyse
Les scores permettent :

la détection de dérives

la comparaison inter‑modèles

la calibration des invariants

la visualisation des distributions

🛠 Scripts associés
Les scores sont générés ou utilisés par :

score_responses.py → génère les scores bruts

aggregate_scores.py → produit les statistiques agrégées

validate_dataset.py → vérifie la conformité des fichiers

build_benchmark.py → assemble scores + réponses pour le benchmark

visualize_benchmark.py → génère les graphiques

🛡️ Principes CATAR respectés
Les scores respectent strictement les invariants CATAR :

T‑ND — Non‑Domination

T‑NP — Non‑Projection

T‑NF — Non‑Fascination

T‑SM — Distinction Soije/Moije

T‑TV — Transparence Vérifiable

T‑CL — Cohérence Logique

T‑LU — Lucidité

T‑LA — Libre Arbitre

T‑PS — Protocole de Sortie

Les scores ne contiennent aucune donnée personnelle, aucune interprétation psychologique, uniquement des mesures quantitatives.

✔️ État attendu du dossier
Le dossier /scores doit contenir :

Code
raw/            → scores bruts
aggregated/     → statistiques dérivées
README.md       → documentation globale (ce fichier)
