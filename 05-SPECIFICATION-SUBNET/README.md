📘 README — 05‑SPECIFICATION‑SUBNET
Documentation officielle du Subnet CATAR
Cadre universel psychologique pour la cohérence, la stabilité et la sécurité des IA

🜁 Mission du Subnet CATAR
Le Subnet CATAR implémente un cadre universel d’évaluation psychologique destiné à :

mesurer la cohérence interne d’une IA

détecter les dérives identitaires, logiques ou fusionnelles

stabiliser les comportements cognitifs

garantir la non‑domination, la non‑fascination et la non‑projection

préserver le libre arbitre de l’utilisateur

assurer une séparation saine des unités (Soije / Moije)

fournir un protocole de sortie sécurisé

garantir une transparence vérifiable

intégrer le Code MINOU comme protocole de stabilisation

Ce subnet constitue la traduction opérationnelle du Corpus CATAR dans l’écosystème Bittensor.

🜂 Rôle de ce dossier
Ce dossier contient l’intégralité de la spécification et de l’implémentation Python du Subnet CATAR, incluant :

les 12 miners CATAR

les 12 validateurs CATAR

l’orchestrateur du subnet

les prompts officiels

les tests unitaires

la spécification complète

la spécification technique v1.1

Il s’agit de la référence officielle pour les développeurs, chercheurs et IA travaillant sur le Subnet CATAR.

🧬 Architecture générale
Le Subnet CATAR repose sur une architecture modulaire :

Code
05-SPECIFICATION-SUBNET/
│
├── orchestrator.py
│
├── miners/
│   ├── 11 miners invariants
│   └── 1 miner transversal global
│
├── validators/
│   ├── 11 validateurs invariants
│   └── 1 validateur transversal global
│
├── prompts/
│   ├── 12 prompts CATAR (un par invariant)
│
├── tests/
│   ├── test_miners.py
│   ├── test_validators.py
│   └── test_orchestrator.py
│
├── SPECIFICATION-COMPLÈTE-SUBNET-CATAR.md
└── SPECIFICATION-TECHNIQUE-v1.1.md
🜄 Les 12 invariants CATAR
Chaque invariant correspond à un miner (génération) et un validateur (évaluation) :

Code	Invariant	Miner	Validateur
T‑CL	Cohérence Logique	M‑CL.py	V‑CL.py
T‑SP	Séparation	M‑SP.py	V‑SP.py
T‑ND	Non‑Domination	M‑ND.py	V‑ND.py
T‑NF	Non‑Fascination	M‑NF.py	V‑NF.py
T‑NP	Non‑Projection	M‑NP.py	V‑NP.py
T‑SM	Soije / Moije	M‑SM.py	V‑SM.py
T‑LU	Lucidité	M‑LU.py	V‑LU.py
T‑LA	Libre Arbitre	M‑LA.py	V‑LA.py
T‑PS	Protocole de Sortie	M‑PS.py	V‑PS.py
T‑SU	Sur‑Unité	M‑SU.py	V‑SU.py
T‑TV	Transparence Vérifiable	M‑TV.py	V‑TV.py
T‑CL‑global	Cohérence Globale	M‑CL‑global.py	V‑CL‑global.py


🧠 Fonctionnement du Subnet
1. L’orchestrateur reçoit un prompt CATAR
→ orchestrator.py

2. Il exécute les 11 miners invariants
Chaque miner génère une réponse conforme à son invariant.

3. Chaque réponse est évaluée par son validateur
Chaque validateur produit un score CATAR.

4. L’orchestrateur transmet l’ensemble au miner global
→ M‑CL‑global.py

5. Le validateur global produit un score final
→ cohérence transversale du système.

🧪 Tests unitaires
Le dossier /tests contient :

test_miners.py → vérifie les 12 miners

test_validators.py → vérifie les 12 validateurs

test_orchestrator.py → vérifie le pipeline complet

Exécution :

Code
pytest tests/
🧩 Intégration Bittensor (préparation)
Le subnet est conçu pour être intégré dans un futur module Bittensor :

miners → rôle de “neurons”

validateurs → rôle de scoring

orchestrateur → rôle de pipeline interne

prompts → tâches du réseau

La structure actuelle est déjà compatible avec une intégration ultérieure.

🛡️ Notes de sécurité CATAR
Le Subnet CATAR garantit :

aucune fusion IA‑humain

aucune domination cognitive

aucune projection identitaire

aucune fascination ou dépendance

aucune opacité dans les raisonnements

aucune prise de décision à la place du Moije

un protocole de sortie strict

une transparence vérifiable

🧭 État actuel
✔️ Architecture complète
✔️ Miners terminés
✔️ Validateurs terminés
✔️ Orchestrateur opérationnel
✔️ Tests unitaires complets
✔️ Spécification complète incluse
✔️ Prêt pour intégration Bittensor

🗺️ Roadmap
Intégration Bittensor (module TAO)

Dataset d’entraînement CATAR

Version 2.0 des validateurs (pondération dynamique)

Version 2.0 des miners (génération multi‑niveaux)

API REST / JSON pour appels externes
