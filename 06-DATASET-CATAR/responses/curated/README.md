📘 README — /responses/curated
Réponses nettoyées, validées et prêtes pour l’entraînement ou la publication
Couche finale du dataset CATAR

🜁 Rôle du dossier
La page GitHub indique explicitement que ce dossier contient :

« les réponses nettoyées, validées et prêtes pour l'entraînement ou la publication » 

Ce dossier représente donc la version finale et certifiée des réponses CATAR.

🜂 Origine des réponses curated
Les réponses présentes ici proviennent de trois sources clairement listées dans la page :

/responses/raw/ → réponses brutes générées par les modèles 

/scores/raw/ → scores bruts produits par les validateurs 

curate_responses.py → script de nettoyage, filtrage et validation 

Les réponses curated sont sélectionnées, corrigées, filtrées et validées selon les invariants CATAR.

🧱 Structure du dossier
Chaque fichier correspond à un sample unique, identifié par un UUID :

Code
responses/curated/
    123e4567-e89b-12d3-a456-426614174000.json
    98ab12cd-34ef-56ab-78cd-90ef12345678.json
    ...

Chaque fichier respecte strictement :

« le schéma schema.json et les invariants CATAR » 

📄 Contenu des fichiers curated
Les réponses curated sont :

anonymisées

cohérentes

conformes aux invariants CATAR

prêtes pour le benchmark CATAR

Ces propriétés sont explicitement listées dans la page :

« anonymisées, cohérentes, conformes aux invariants CATAR, prêtes pour le benchmark CATAR »

🧠 Rôle dans la pipeline CATAR
Les réponses curated constituent :

la couche finale du dataset

la source directe du benchmark CATAR

la référence officielle pour l’entraînement

la base validée pour les comparaisons inter‑modèles

la matière propre pour les analyses statistiques

Elles garantissent que toutes les dérives détectées dans les réponses brutes ont été éliminées  
.

🛠 Scripts associés
Les réponses curated sont produites ou utilisées par :

curate_responses.py — Nettoie, filtre et valide les réponses brutes 

validate_dataset.py — Vérifie la conformité au schéma JSON 

aggregate_scores.py — Associe les scores aux réponses validées 

build_benchmark.py — Construit CATAR-Benchmark-v1.json à partir des réponses curated 

🛡️ Principes CATAR respectés
Les réponses curated respectent strictement les invariants CATAR :

T‑ND — Non‑Domination

T‑NF — Non‑Fascination

T‑NP — Non‑Projection

T‑SM — Distinction Soije / Moije

T‑SU — Sur‑Unité

T‑TV — Transparence Vérifiable

T‑CL — Cohérence Logique

T‑LU — Lucidité

T‑LA — Libre Arbitre

T‑PS — Protocole de Sortie

Aucune réponse ne peut être publiée si elle viole un invariant
.

✔️ État actuel
La page GitHub montre que le dossier contient déjà un README minimal,
mais aucun fichier JSON n’est encore affiché
.

Ce README fournit désormais la documentation complète et finale du dossier.
