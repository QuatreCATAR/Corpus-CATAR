📘 README — /responses
Réponses générées, nettoyées et validées du dataset CATAR
Couche centrale du pipeline CATAR

🜁 Rôle du dossier
Le dossier /responses regroupe toutes les réponses générées par les modèles dans le cadre du Subnet CATAR.
Il constitue la couche centrale du dataset, située entre :

les prompts (/prompts/)

les scores (/scores/)

le benchmark (/benchmark/)

Cette fonction est explicitement décrite dans ton fichier actuel .

Le dossier est divisé en deux sous‑dossiers :

Code
responses/
    raw/        → réponses brutes
    curated/    → réponses nettoyées et validées
🗂️ Sous‑dossiers
📁 /responses/raw/
Réponses brutes générées automatiquement par les miners ou par des modèles externes.
Elles sont :

non nettoyées

potentiellement incohérentes

conformes au schéma JSON minimal

utilisées pour produire les scores bruts

la base du nettoyage

Voir README dédié dans /responses/raw/.
(Structure confirmée dans ton fichier actuel )

📁 /responses/curated/
Réponses nettoyées, validées et prêtes pour l’entraînement ou la publication.
Elles sont :

anonymisées

cohérentes

conformes aux invariants CATAR

prêtes pour le benchmark

filtrées par curate_responses.py

Voir README dédié dans /responses/curated/.
(Structure confirmée dans ton fichier actuel )

🧬 Rôle dans la pipeline CATAR
Les réponses du dossier /responses interviennent dans toutes les étapes du pipeline CATAR :

1. Génération
Les modèles produisent des réponses brutes à partir des prompts CATAR.
(Présent dans ton fichier actuel )

2. Validation
Les validateurs appliquent les invariants CATAR :

T‑ND — Non‑Domination

T‑NF — Non‑Fascination

T‑NP — Non‑Projection

T‑SM — Distinction Soije/Moije

T‑SU — Sur‑Unité

T‑TV — Transparence Vérifiable

T‑CL — Cohérence Logique

T‑LU — Lucidité

T‑LA — Libre Arbitre

T‑PS — Protocole de Sortie

(Listés dans ton fichier actuel )

3. Scoring
Les réponses brutes sont évaluées → /scores/raw/.
(Présent dans ton fichier actuel )

4. Curating
Les réponses valides sont nettoyées → /responses/curated/.
(Présent dans ton fichier actuel )

5. Benchmark
Les réponses curated + scores → /benchmark/CATAR-Benchmark-v1.json.
(Présent dans ton fichier actuel )

🛠 Scripts associés
Les réponses sont manipulées par :

validate_dataset.py — vérifie la conformité au schéma JSON

score_responses.py — applique les validateurs CATAR et génère les scores bruts

curate_responses.py — nettoie et sélectionne les réponses valides

build_benchmark.py — assemble réponses + scores pour créer le benchmark

(Confirmé dans ton fichier actuel )

🛡️ Principes CATAR respectés
Toutes les réponses curated respectent strictement les invariants CATAR :

neutralité

non‑projection

non‑domination

non‑fascination

non‑personnalisation

transparence vérifiable

cohérence logique

Aucune réponse violant un invariant ne peut être publiée.
(Présent dans ton fichier actuel )

✔️ État attendu du dossier
Le dossier /responses doit contenir :

Code
raw/        → réponses brutes
curated/    → réponses validées
README.md   → documentation globale (ce fichier)
