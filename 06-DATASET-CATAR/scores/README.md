📘 README — Dossier /scores
Scores bruts, agrégés et métadonnées d’évaluation CATAR
Colonne vertébrale du Subnet CATAR

🜁 Rôle du dossier
Le dossier /scores contient tous les résultats d’évaluation produits par les validateurs CATAR.

Il est divisé en deux sous‑dossiers :

raw/ → scores bruts, un fichier par réponse

aggregated/ → statistiques globales et par invariant

Ces scores constituent la base :

du benchmark CATAR

de la calibration des validateurs

de la comparaison inter‑modèles

de la détection des dérives cognitives

🜂 Structure du dossier
Code
scores/
│
├── raw/
│   ├── README.md
│   └── *.json
│
└── aggregated/
    ├── README.md
    ├── aggregate_scores.py
    ├── aggregated_stats.json
    └── per_invariant.json
📂 /raw — Scores bruts
Ce dossier contient les scores non modifiés, générés automatiquement par les validateurs CATAR.

Chaque fichier correspond à une réponse (UUID unique) et contient :

le score global CATAR

les marqueurs détectés

les pondérations appliquées

la version du validateur

les métadonnées d’évaluation

Exemple
json
{
  "metadata": {
    "uuid": "123e4567-e89b-12d3-a456-426614174000",
    "validator_version": "1.0"
  },
  "task_id": "T-ND",
  "scores": {
    "global_score": 0.82,
    "markers_detected": ["neutralité", "absence de prise d'autorité"]
  }
}
Ces fichiers servent directement à la construction du benchmark.

📂 /aggregated — Statistiques globales
Ce dossier contient les statistiques produites par :

Code
aggregate_scores.py
Il génère deux fichiers :

1. aggregated_stats.json
Statistiques globales :

moyenne

médiane

variance

min / max

distribution par tranche

2. per_invariant.json
Statistiques par invariant T‑XX :

moyenne

variance

stabilité

cohérence interne

Ces fichiers sont utilisés par :

visualize_benchmark.py

compare_models.py

les dashboards d’analyse

🛠 Scripts associés
aggregate_scores.py
Calcule les statistiques globales et par invariant.

validate_dataset.py
Vérifie la conformité des scores au schema.json.

build_benchmark.py
Associe chaque score à sa réponse correspondante.

clean_dataset.py
Nettoyage intelligent des anciens scores.

🧠 Usage des scores
Les scores CATAR permettent :

la calibration des validateurs

la comparaison de modèles IA

la détection des dérives (projection, domination, fascination…)

la construction du benchmark CATAR

l’analyse de cohérence psychologique

Ils constituent la colonne vertébrale du Subnet CATAR.

🛡️ Principes CATAR respectés
Tous les scores respectent :

la non‑domination

la non‑projection

la non‑fascination

la séparation Soije / Moije

la neutralité épistémique

la transparence vérifiable

Les validateurs CATAR ne produisent jamais de jugement moral ou d’autorité.

✔️ État actuel
Le dossier /scores est prêt à accueillir :

les scores bruts

les statistiques agrégées

les futures versions du validateur CATAR

Il constitue la base du CATAR‑Benchmark v1.0.
