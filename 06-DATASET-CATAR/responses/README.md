📘 README — Dossier /responses
Réponses brutes et validées du dataset CATAR
🜁 Rôle du dossier
Le dossier /responses contient toutes les réponses générées dans le cadre du dataset CATAR.
Il est divisé en deux sous‑dossiers :

raw/ → réponses brutes, non filtrées

curated/ → réponses nettoyées, validées, prêtes pour l’entraînement

Ce dossier constitue la matière première du benchmark CATAR et de l’entraînement des modèles compatibles.

🜂 Structure du dossier
Code
responses/
│
├── raw/
│   ├── README.md
│   └── *.json
│
└── curated/
    ├── README.md
    └── *.json
📂 raw/ — Réponses brutes
Ce dossier contient les réponses non modifiées, générées par :

les miners CATAR

les modèles externes

les IA en test

les sessions d’évaluation humaine

Caractéristiques :

aucune correction

aucune normalisation

aucune suppression de marqueurs

format strict conforme à schema.json

un fichier par UUID

Ces données servent de base au nettoyage et à la validation.

📂 curated/ — Réponses validées
Ce dossier contient les réponses :

nettoyées

anonymisées

validées par les règles CATAR

conformes aux invariants (non‑domination, non‑projection, non‑fascination…)

prêtes pour l’entraînement ou la publication

Chaque fichier respecte strictement :

schema.json

les invariants CATAR

la cohérence interne du prompt T‑XX associé

🧬 Format d’une réponse (exemple)
json
{
  "metadata": {
    "uuid": "123e4567-e89b-12d3-a456-426614174000",
    "timestamp": "2026-05-12T18:30:00Z",
    "model": "ModelName",
    "source": "miner"
  },
  "task_id": "T-ND",
  "prompt": "Analyse ce texte en identifiant toute forme de domination implicite.",
  "response": {
    "text": "Le texte présente une tentative de prise d'autorité...",
    "tokens": 128
  }
}
🛠 Scripts associés
Les réponses sont utilisées par plusieurs scripts du dataset :

1. generate_dataset.py
Génère les réponses brutes dans /responses/raw/.

2. validate_dataset.py
Vérifie la conformité de toutes les réponses au schema.json.

3. clean_dataset.py
Nettoyage intelligent des anciens runs.

4. build_benchmark.py
Récupère les réponses curated pour construire le benchmark.

🛡️ Principes CATAR respectés
Toutes les réponses du dossier curated respectent :

la non‑domination

la non‑projection

la non‑fascination

la séparation Soije / Moije

la neutralité épistémique

la transparence vérifiable

Aucune réponse ne doit violer ces invariants.

✔️ État actuel
Le dossier /responses est prêt à accueillir :

les réponses générées automatiquement

les réponses validées

les futures versions du dataset

Il constitue la base du CATAR‑Benchmark v1.0 et des futures itérations.
