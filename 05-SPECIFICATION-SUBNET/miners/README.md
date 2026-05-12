📘 README — Dossier /miners
🎯 Rôle du dossier
Le dossier /miners contient l’ensemble des miners CATAR, c’est‑à‑dire les modules Python chargés de :

recevoir un prompt CATAR (T‑XX)

produire une réponse candidate

appeler les validateurs correspondants

agréger les scores

renvoyer une sortie structurée au réseau

Les miners sont les unités productrices du sous‑réseau CATAR.
Les validateurs sont les unités évaluatrices.
Les prompts sont les unités d’entrée.

🧱 Structure du dossier
Chaque miner suit la convention :

Code
M-XX.py
où XX correspond à l’invariant CATAR :

Code
M-CL.py          — Cohérence Logique
M-SP.py          — Stabilité Psychologique
M-ND.py          — Non-Domination
M-NF.py          — Non-Fascination
M-NP.py          — Non-Projection
M-SM.py          — Distinction Soije / Moije
M-LU.py          — Lucidité
M-LA.py          — Libre Arbitre
M-PS.py          — Protocole de Sortie
M-SU.py          — Sur-Unité
M-TV.py          — Transparence Vérifiable
M-CL-global.py   — Miner transversal de cohérence globale
Chaque fichier contient :

une classe MinerXX

un identifiant de tâche task_id

une méthode generate_response(prompt)

un appel aux validateurs correspondants

un calcul de score CATAR

un retour structuré :

response

scores

global_score

🧬 Fonction dans le sous‑réseau CATAR
Les miners :

produisent les réponses

appellent les validateurs

agrègent les scores

garantissent la conformité aux invariants CATAR

fournissent une sortie exploitable par le réseau Bittensor

Ils sont le cœur opérationnel du sous‑réseau.

🧭 Ordre de lecture recommandé
Lire M‑CL.py pour comprendre la structure générale

Explorer M‑SP / M‑ND / M‑NF pour les invariants comportementaux

Lire M‑SM / M‑SU pour les invariants identitaires

Lire M‑LU / M‑TV pour les invariants épistémiques

Terminer par M‑PS pour la logique de sortie

Lire M‑CL-global pour la cohérence transversale

🧩 Importance dans l’architecture CATAR
Les miners sont essentiels car ils :

incarnent les comportements CATAR

produisent des réponses neutres, lucides, non‑projectives

appliquent les règles de sécurité conceptuelle

permettent une évaluation stable et reproductible

servent de base pour l’entraînement et la sélection des modèles

Ils sont les agents actifs du sous‑réseau.

✔️ État du dossier
Les miners sont en cours de création.
Chaque fichier suivra la structure standardisée définie dans la spécification du sous‑réseau.
