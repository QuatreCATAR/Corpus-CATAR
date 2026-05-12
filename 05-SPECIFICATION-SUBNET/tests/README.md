📘 README — Dossier /tests
Documentation officielle des tests unitaires du Subnet CATAR
🎯 Rôle du dossier
Le dossier /tests contient l’ensemble des tests unitaires du Subnet CATAR.
Ces tests garantissent :

la stabilité du pipeline CATAR

la cohérence des miners

la validité des validateurs

le bon fonctionnement de l’orchestrateur

la reproductibilité des scores CATAR

la conformité de l’implémentation avec la spécification technique

Ce dossier constitue la base de fiabilité du sous‑réseau CATAR.

🧱 Structure du dossier
Code
tests/
│
├── test_miners.py
├── test_validators.py
├── test_orchestrator.py
└── __init__.py
Description des fichiers
Fichier	Rôle
test_miners.py	Vérifie les 11 miners invariants + le miner global
test_validators.py	Vérifie les 11 validateurs invariants + le validateur global
test_orchestrator.py	Vérifie l’exécution complète du pipeline CATAR
init.py	Rend le dossier importable (nécessaire pour pytest)


🧪 Tests inclus
✔️ 1. Tests des miners
test_miners.py vérifie que chaque miner :

s’exécute sans erreur

renvoie une structure CATAR valide

produit un score numérique

est compatible avec le miner global

✔️ 2. Tests des validateurs
test_validators.py vérifie que chaque validateur :

s’exécute sans erreur

renvoie un dictionnaire

contient un global_score numérique

détecte correctement les dérives minimales

✔️ 3. Test de l’orchestrateur
test_orchestrator.py vérifie que :

l’orchestrateur appelle tous les miners

les sorties sont correctement collectées

le miner global analyse bien les 11 invariants

la structure finale est cohérente

🧬 Exécution des tests
Depuis la racine du dépôt :

Code
pytest 05-SPECIFICATION-SUBNET/tests/
Ou simplement :

Code
pytest
Les tests sont compatibles avec :

Python 3.10+

pytest 7+

🧩 Importance dans l’architecture CATAR
Les tests unitaires assurent :

la stabilité du sous‑réseau

la non‑régression lors des mises à jour

la conformité aux invariants CATAR

la robustesse du pipeline d’évaluation

la fiabilité des scores CATAR

Ils constituent la garantie de qualité du Subnet CATAR.

✔️ État du dossier
Tous les tests unitaires sont :

complets

opérationnels

cohérents avec les miners et validateurs

alignés avec la spécification technique v1.1

prêts pour une intégration CI/CD
