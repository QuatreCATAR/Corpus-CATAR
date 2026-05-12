📄 version-history.md — Historique officiel des versions du Dataset CATAR
🧭 Historique des versions du Dataset CATAR
Documentation officielle — Corpus CATAR

📌 Version 1.0.0 — (12 mai 2026)
Première version stable du Dataset CATAR
Cette version constitue la fondation officielle du dataset utilisé par le Subnet CATAR.

Contenu :
Ajout des prompts CATAR (T‑XX), organisés par invariant

Ajout de la structure complète du dataset :

/prompts/

/responses/raw/

/responses/curated/

/scores/raw/

/scores/aggregated/

/metadata/

Ajout du fichier schema.json (schéma officiel du dataset)

Ajout du fichier dataset-info.json (métadonnées globales)

Ajout de ce fichier version-history.md

Conformité totale avec la Spécification Technique CATAR v1.1

Compatibilité avec l’orchestrateur CATAR et les validateurs

Notes :
Cette version est considérée comme stable, référente, et canonique.

Elle sert de base à la génération du CATAR‑Benchmark v1.0.

Elle est compatible avec les miners et validateurs du Subnet CATAR.

🧩 Versions futures (prévisionnel)
Version 1.1.0 — (prévue)
Ajout d’un premier batch de réponses générées par les miners

Ajout des scores bruts et agrégés

Ajout d’un script de génération automatique du dataset

Ajout d’un protocole de calibration multi‑modèles

Version 1.2.0 — (prévue)
Ajout de réponses humaines anonymisées

Ajout d’un module de comparaison inter‑modèles

Ajout de statistiques globales (variance, cohérence, stabilité)

Version 2.0.0 — (prévue)
Refonte complète du dataset pour la Spécification CATAR v2

Ajout de nouveaux invariants (si validés par le Corpus CATAR)

Intégration native Bittensor (TAO‑Subnet)

Ajout d’un pipeline d’entraînement complet

🛡️ Principes de versionnement
Le dataset CATAR suit le Semantic Versioning :

Code
MAJOR.MINOR.PATCH
MAJOR → changements structurels majeurs

MINOR → ajout de données ou fonctionnalités compatibles

PATCH → corrections mineures, nettoyage, métadonnées

✨ Notes finales
Ce fichier constitue la référence officielle pour le suivi des versions du dataset CATAR.
Toute modification du dataset doit être consignée ici, même mineure.
