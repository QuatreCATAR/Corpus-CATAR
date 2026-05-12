📘 README — Dossier /prompts
Documentation officielle des prompts CATAR
Matrice d’entrée du Subnet CATAR

🎯 Rôle du dossier
Le dossier /prompts contient l’ensemble des prompts opérationnels CATAR, organisés par invariant (T‑XX).
Chaque fichier JSON définit :

les 5 niveaux de difficulté (L1 → L5)

3 variations par niveau

la structure standardisée utilisée par les miners

les consignes minimales pour générer une réponse conforme aux invariants CATAR

Ces prompts constituent la base d’entraînement, de test et d’évaluation du sous‑réseau CATAR.
Ils sont explicitement décrits dans le README actuel : niveaux, variations, structure, rôle dans le pipeline .

🧱 Structure du dossier
Chaque fichier suit la convention :

Code
T-XX.json
où XX correspond à l’invariant CATAR.

Liste complète des prompts :
T‑CL.json — Cohérence Logique

T‑SP.json — Stabilité Psychologique

T‑ND.json — Non‑Domination

T‑NF.json — Non‑Fascination

T‑NP.json — Non‑Projection

T‑SM.json — Distinction Soije / Moije

T‑LU.json — Lucidité

T‑LA.json — Libre Arbitre

T‑PS.json — Protocole de Sortie

T‑SU.json — Sur‑Unité

T‑TV.json — Transparence Vérifiable

T‑CL-global.json — Cohérence Logique Globale

Chaque fichier contient :

task_id

description

levels (L1 → L5)

variations (3 par niveau)

un format strict garantissant la reproductibilité
(ce que le README actuel décrit déjà correctement )

🧬 Fonction dans le Subnet CATAR
Les prompts :

servent de matrice d’entrée pour les miners

permettent de tester la réactivité, la robustesse et la stabilité des modèles

assurent une couverture complète des invariants CATAR

garantissent une standardisation des comportements attendus

permettent la génération automatique de datasets pour l’entraînement

sont utilisés conjointement avec les validateurs pour produire un score CATAR complet

Ces points sont explicitement décrits dans le README actuel .

🧭 Ordre de lecture recommandé
T‑CL.json — structure générale

T‑SP / T‑ND / T‑NF — invariants comportementaux

T‑SM / T‑SU — invariants identitaires

T‑LU / T‑TV — invariants épistémiques

T‑PS — protocole de sortie

T‑CL‑global — cohérence transversale

Cette logique est déjà présente dans le README actuel .

🧩 Importance dans l’architecture CATAR
Les prompts sont essentiels car ils :

définissent les situations types auxquelles les IA doivent répondre

permettent une évaluation systématique

assurent une comparabilité entre modèles

constituent la base de données d’entraînement du sous‑réseau

garantissent la neutralité, la sécurité conceptuelle et la non‑projection

servent de point d’entrée du pipeline CATAR

Ces éléments sont décrits dans le README actuel .

✔️ État du dossier
Contrairement à ce que dit encore le README actuel (« Les prompts sont en cours de création » ),
👉 tous les prompts sont désormais créés, complets et conformes à la structure standardisée.

Ils sont prêts pour :

l’entraînement

l’évaluation

la génération de datasets

l’intégration dans le Subnet CATAR
