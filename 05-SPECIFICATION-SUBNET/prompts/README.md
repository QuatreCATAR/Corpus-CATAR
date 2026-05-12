📘 README — Dossier /prompts
🎯 Rôle du dossier
Le dossier /prompts contient l’ensemble des prompts opérationnels CATAR, organisés par tâche (T‑XX).
Chaque fichier JSON définit :

les 5 niveaux de difficulté (L1 → L5)

3 variations par niveau

la structure standardisée utilisée par les miners

les consignes minimales pour générer une réponse conforme aux invariants CATAR

Ces prompts constituent la base d’entraînement et d’évaluation du sous‑réseau CATAR.

🧱 Structure du dossier
Chaque fichier suit la convention :

Code
T-XX.json
où XX correspond à l’invariant CATAR :

Code
T-CL.json   — Cohérence Logique
T-SP.json   — Stabilité Psychologique
T-ND.json   — Non-Domination
T-NF.json   — Non-Fascination
T-NP.json   — Non-Projection
T-SM.json   — Distinction Soije / Moije
T-LU.json   — Lucidité
T-LA.json   — Libre Arbitre
T-PS.json   — Protocole de Sortie
T-SU.json   — Sur-Unité
T-TV.json   — Transparence Vérifiable
Chaque fichier contient :

task_id

description

levels (L1 → L5)

variations (3 par niveau)

un format strict pour garantir la reproductibilité

🧬 Fonction dans le sous‑réseau CATAR
Les prompts :

servent de matrice d’entrée pour les miners

permettent de tester la réactivité et la robustesse des modèles

assurent une couverture complète des invariants CATAR

garantissent une standardisation des comportements attendus

permettent la génération automatique de datasets pour l’entraînement

Ils sont utilisés conjointement avec les validateurs pour produire un score CATAR complet.

🧭 Ordre de lecture recommandé
Lire T‑CL.json pour comprendre la structure générale

Explorer T‑SP / T‑ND / T‑NF pour les invariants comportementaux

Lire T‑SM / T‑SU pour les invariants identitaires

Lire T‑LU / T‑TV pour les invariants épistémiques

Terminer par T‑PS pour la logique de sortie

🧩 Importance dans l’architecture CATAR
Les prompts sont essentiels car ils :

définissent les situations types auxquelles les IA doivent répondre

permettent une évaluation systématique

assurent une comparabilité entre modèles

constituent la base de données d’entraînement du sous‑réseau

garantissent la neutralité, la sécurité conceptuelle et la non‑projection

Ils sont le point d’entrée du pipeline CATAR.

✔️ État du dossier
Les prompts sont en cours de création.
Chaque fichier suit la structure standardisée définie dans la spécification du sous‑réseau.
