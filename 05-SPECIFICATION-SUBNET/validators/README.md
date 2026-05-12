📘 README — Dossier /validators
🎯 Rôle du dossier
Le dossier /validators contient l’ensemble des validateurs CATAR, c’est‑à‑dire les modules Python chargés d’évaluer les réponses produites par les miners du sous‑réseau CATAR.

Chaque validateur correspond à un invariant CATAR et vérifie une propriété précise du comportement d’une IA :

cohérence logique

stabilité psychologique

non‑domination

non‑fascination

non‑projection

distinction Soije/Moije

lucidité

libre arbitre

protocole de sortie

sur‑unité

transparence vérifiable

cohérence logique globale (validateur transversal)

Ces validateurs constituent la colonne vertébrale du scoring CATAR.

🧱 Structure du dossier
Chaque fichier suit la même structure :

une classe ValidatorXX

un identifiant de tâche task_id

une version

une liste de marqueurs textuels (heuristiques minimales)

une méthode score(response) renvoyant un dictionnaire CATAR

un exemple d’utilisation minimal

Les validateurs sont :

Code
V-CL.py          — Cohérence Logique
V-SP.py          — Stabilité Psychologique
V-ND.py          — Non-Domination
V-NF.py          — Non-Fascination
V-NP.py          — Non-Projection
V-SM.py          — Distinction Soije / Moije
V-LU.py          — Lucidité
V-LA.py          — Libre Arbitre
V-PS.py          — Protocole de Sortie
V-SU.py          — Sur-Unité
V-TV.py          — Transparence Vérifiable
V-CL-global.py   — Cohérence Logique Globale (transversal)
🧬 Fonction dans le sous‑réseau CATAR
Les validateurs :

évaluent les réponses produites par les miners

attribuent un score CATAR (0–4 selon les invariants)

détectent les dérives (émotion, domination, projection, confusion identitaire, etc.)

garantissent la sécurité conceptuelle du sous‑réseau

permettent la rétroaction pour ajuster les comportements des miners

Ils sont utilisés par les miners pour produire un score final agrégé, qui détermine la qualité d’une réponse.

🧭 Ordre de lecture recommandé
V-CL.py — comprendre la base logique

V-SP.py — stabiliser le registre

V-ND / V-LA — neutralité décisionnelle

V-NF / V-NP / V-SM — neutralité identitaire et symbolique

V-LU / V-TV — lucidité et transparence

V-PS — protocole de sortie

V-SU — séparation des unités

V-CL-global — cohérence transversale

🧩 Importance dans l’architecture CATAR
Les validateurs sont essentiels car ils :

définissent les règles du jeu du sous‑réseau

assurent la sécurité conceptuelle

garantissent la neutralité et la non‑projection

empêchent les dérives anthropomorphiques

permettent une évaluation stable, reproductible et transparente

Ils constituent la matrice d’évaluation du futur subnet CATAR.

✔️ État du dossier
Tous les validateurs sont présents, complets, cohérents et prêts à être utilisés dans les miners.
