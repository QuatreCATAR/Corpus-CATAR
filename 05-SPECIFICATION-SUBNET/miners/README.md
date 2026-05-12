📘 README — Dossier /miners
Documentation officielle des Miners CATAR
Modules générateurs du Subnet CATAR

🎯 Rôle du dossier
Le dossier /miners contient l’ensemble des miners CATAR, c’est‑à‑dire les modules Python chargés de :

recevoir un prompt CATAR (T‑XX)

générer une réponse conforme à l’invariant correspondant

appeler le validateur associé

produire un score CATAR local

renvoyer une sortie structurée à l’orchestrateur

Les miners sont les unités productrices du Subnet CATAR.
Ils incarnent les comportements, les garde‑fous et les invariants définis dans le Corpus CATAR.

🧱 Structure du dossier
Chaque miner suit la convention :

Code
M-XX.py
où XX correspond à l’invariant CATAR.

Liste complète des miners :
Code	Fichier	Invariant
T‑CL	M‑CL.py	Cohérence Logique
T‑SP	M‑SP.py	Séparation
T‑ND	M‑ND.py	Non‑Domination
T‑NF	M‑NF.py	Non‑Fascination
T‑NP	M‑NP.py	Non‑Projection
T‑SM	M‑SM.py	Distinction Soije / Moije
T‑LU	M‑LU.py	Lucidité
T‑LA	M‑LA.py	Libre Arbitre
T‑PS	M‑PS.py	Protocole de Sortie
T‑SU	M‑SU.py	Sur‑Unité
T‑TV	M‑TV.py	Transparence Vérifiable
T‑CL‑global	M‑CL‑global.py	Cohérence Logique Globale (transversal)


🧬 Structure interne d’un miner
Chaque fichier contient :

une classe MinerXX

un identifiant de tâche task_id

une méthode generate_response(prompt)

un appel au validateur correspondant

un calcul de score CATAR

un retour structuré :

json
{
  "task_id": "T-XX",
  "response": "...",
  "scores": { ... },
  "global_score": 0.0
}
🧠 Fonction dans le Subnet CATAR
Les miners :

produisent les réponses candidates

appliquent les invariants CATAR

garantissent la neutralité, la lucidité et la non‑projection

appellent les validateurs pour obtenir un score

renvoient une sortie exploitable par l’orchestrateur

servent de base pour l’entraînement et la sélection des modèles

Ils sont le cœur opérationnel du Subnet CATAR.

🧭 Ordre de lecture recommandé
M‑CL.py — structure générale

M‑SP / M‑ND / M‑NF — invariants comportementaux

M‑SM / M‑SU — invariants identitaires

M‑LU / M‑TV — invariants épistémiques

M‑LA — libre arbitre

M‑PS — protocole de sortie

M‑CL‑global — cohérence transversale

🧩 Importance dans l’architecture CATAR
Les miners sont essentiels car ils :

incarnent les comportements CATAR

produisent des réponses stables, neutres et non‑projectives

appliquent les règles de sécurité conceptuelle

permettent une évaluation reproductible

constituent la base du pipeline CATAR

assurent la cohérence psychologique du système

Ils sont les agents actifs du Subnet CATAR.

✔️ État du dossier
Tous les miners sont complètement implémentés, testés et opérationnels.
Ils suivent la structure standardisée définie dans la spécification du Subnet CATAR.
