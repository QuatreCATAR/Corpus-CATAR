📘 README — /responses
Réponses générées, nettoyées et validées du dataset CATAR
Couche centrale du pipeline CATAR

🜁 Rôle du dossier
Le dossier /responses regroupe toutes les réponses générées par les modèles dans le cadre du Subnet CATAR.
Il constitue la couche centrale du dataset, entre :

les prompts (/prompts/)

les scores (/scores/)

le benchmark (/benchmark/)

Cette fonction est explicitement décrite dans ton fichier actuel .

Le dossier est divisé en deux sous‑dossiers :

Code
responses/
   raw/      → réponses brutes
   curated/  → réponses nettoyées et validées
🗂️ Sous‑dossiers
📁 /responses/raw/
Réponses brutes générées automatiquement par les miners ou par des modèles externes .

Caractéristiques :

non nettoyées

peuvent contenir des dérives

conformes au schéma JSON minimal

utilisées pour produire les scores bruts

servent de base au nettoyage

Voir README dédié dans /responses/raw/.

📁 /responses/curated/
Réponses nettoyées, validées et prêtes pour l’entraînement ou la publication .

Caractéristiques :

anonymisées

cohérentes

conformes aux invariants CATAR

prêtes pour le benchmark

filtrées par curate_responses.py

Voir README dédié dans /responses/curated/.

🧬 Rôle dans la pipeline CATAR
Les réponses du dossier /responses interviennent dans toutes les étapes du pipeline CATAR  :

1. Génération
Les modèles produisent des réponses brutes à partir des prompts CATAR.

2. Validation
Les validateurs appliquent les invariants CATAR  :

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

3. Scoring
Les réponses brutes sont évaluées → /scores/raw/ .

4. Curating
Les réponses valides sont nettoyées → /responses/curated/ .

5. Benchmark
Les réponses curated + scores → /benchmark/CATAR-Benchmark-v1.json .

🛠 Scripts associés
Les réponses sont manipulées par les scripts suivants  :

validate_dataset.py  
Vérifie la conformité au schéma JSON.

score_responses.py  
Applique les validateurs CATAR et génère les scores bruts.

curate_responses.py  
Nettoie et sélectionne les réponses valides.

build_benchmark.py  
Assemble réponses + scores pour créer le benchmark.

🛡️ Principes CATAR respectés
Toutes les réponses curated respectent strictement les invariants CATAR  :

neutralité

non‑projection

non‑domination

non‑fascination

non‑personnalisation

transparence vérifiable

cohérence logique

Aucune réponse violant un invariant ne peut être publiée.

✔️ État actuel
Ton dépôt contient déjà :

un README minimal

les dossiers raw/ et curated/

la structure complète du dataset

Ce README fournit désormais la documentation globale et finale du dossier /responses .
