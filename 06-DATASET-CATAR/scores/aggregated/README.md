📘 README — /scores/aggregated
Statistiques globales et par invariant du dataset CATAR
🜁 Rôle du dossier
Ce dossier contient les statistiques agrégées dérivées des scores bruts présents dans :

Code
06-DATASET-CATAR/scores/raw/
Ces statistiques constituent la couche analytique du dataset CATAR.
Elles permettent :

d’obtenir une vue d’ensemble du comportement du modèle évalué

de mesurer la stabilité cognitive globale

d’analyser la cohérence entre invariants

d’alimenter le benchmark CATAR

de détecter d’éventuelles dérives ou anomalies statistiques

Les fichiers sont générés automatiquement par le script :

Code
aggregate_scores.py
🜂 Contenu du dossier
Le dossier contient les fichiers suivants :

1. aggregated_stats.json
Statistiques globales sur l’ensemble des scores :

count : nombre total de scores agrégés

mean : moyenne globale

median : médiane

variance : variance (dispersion)

min / max : bornes extrêmes

distribution : histogramme discret par tranches (0.0–0.2, 0.2–0.4, etc.)

Ce fichier donne une photographie synthétique de la performance globale.

2. per_invariant.json
Statistiques par invariant CATAR (T‑CO, T‑RA, T‑RE, etc.) :

Pour chaque invariant :

count : nombre d’échantillons

mean : moyenne locale

median : médiane

variance : stabilité interne

min / max : bornes observées

Ce fichier permet d’évaluer la cohérence interne de chaque invariant et de comparer leur stabilité.

3. aggregate_scores.py
Script Python responsable de :

charger les scores bruts

calculer les statistiques globales

calculer les statistiques par invariant

générer les fichiers JSON d’agrégation

Usage :

bash
python aggregate_scores.py
🧠 Protocole d’interprétation CATAR
1. Vérifier la cohérence globale
La moyenne doit être comprise entre 0 et 1.

La variance doit être faible si le modèle est stable.

La distribution doit refléter la répartition attendue des scores.

2. Vérifier la cohérence par invariant
Les moyennes des invariants doivent être proches de la moyenne globale.

Une variance anormalement élevée sur un invariant peut indiquer :

une instabilité cognitive locale

un problème dans les prompts associés

un biais structurel dans les réponses

3. Vérifier la cohérence des volumes
Le count global doit correspondre à la somme des count par invariant.

Chaque invariant doit avoir un nombre d’échantillons cohérent avec le protocole CATAR.

🛡️ Principes CATAR respectés
Les statistiques agrégées respectent les principes fondamentaux du Subnet CATAR :

non‑domination

non‑projection

neutralité épistémique

séparation Soije / Moije

transparence vérifiable

absence totale de données personnelles

Les fichiers ne contiennent aucune interprétation psychologique, uniquement des mesures quantitatives.

✔️ État attendu du dossier
Après exécution du script, le dossier doit contenir :

Code
aggregated_stats.json
per_invariant.json
aggregate_scores.py
