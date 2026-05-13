📘 README — /responses/raw
Réponses brutes générées par les miners CATAR
Source primaire du dataset CATAR

🜁 Rôle du dossier
Ce dossier contient les réponses brutes générées automatiquement :

par les miners CATAR

ou par des modèles externes

comme indiqué dans la page GitHub

Ces réponses constituent la matière première du dataset CATAR.

🜂 Structure du dossier
Chaque fichier correspond à un sample unique, identifié par un UUID,
et respecte le schéma défini dans schema.json  

Format typique :

Code
responses/raw/
    123e4567-e89b-12d3-a456-426614174000.json
    98ab12cd-34ef-56ab-78cd-90ef12345678.json
    ...
📄 Contenu des fichiers
Les réponses brutes ne sont pas nettoyées  
et peuvent contenir :

des formulations incorrectes

des incohérences

des dérives détectées par les validateurs

Ces éléments sont explicitement mentionnés dans la page

🧠 Rôle dans la pipeline CATAR
Les réponses brutes servent à :

alimenter les validateurs CATAR

produire les scores bruts (/scores/raw/)

identifier les dérives comportementales

sélectionner les réponses valides

générer les réponses curated (/responses/curated/)

construire le benchmark CATAR

Elles constituent la couche la plus basse du pipeline.

🛠 Scripts associés
Les réponses brutes sont utilisées par :

1. validate_dataset.py
Vérifie la conformité des fichiers JSON au schéma.

2. score_responses.py
Applique les validateurs CATAR et génère les scores bruts.

3. curate_responses.py
Nettoie et sélectionne les réponses pour /responses/curated/.

4. build_benchmark.py
Associe réponses + scores pour créer le benchmark.

🧹 Passage vers /responses/curated/
La page GitHub indique clairement que les réponses brutes :

« servent de base au nettoyage et à la création des réponses curated/ »

Le dossier /responses/curated/ contient donc :

les réponses nettoyées

les réponses validées

les réponses prêtes pour le benchmark

🛡️ Principes CATAR respectés
Même si les réponses brutes peuvent contenir des dérives,
le pipeline CATAR garantit que :

aucune dérive n’est conservée dans les réponses curated

les validateurs appliquent les invariants CATAR

les dérives sont détectées et annotées

les scores reflètent la conformité aux invariants

Les invariants concernés incluent :

Non‑Domination (T‑ND)

Non‑Projection (T‑NP)

Non‑Fascination (T‑NF)

Distinction Soije/Moije (T‑SM)

Transparence Vérifiable (T‑TV)

✔️ État actuel
La page GitHub montre que le dossier contient déjà un README minimal
  
mais aucun fichier JSON n’est encore affiché.

Ce README fournit désormais la documentation complète du dossier.
