📘 README — Dossier /prompts
Documentation officielle des prompts CATAR
Matrice d’entrée du Subnet CATAR

🎯 Rôle du dossier
Le dossier /prompts contient l’ensemble des prompts opérationnels CATAR, organisés par invariant T‑XX.
Ils constituent la matrice d’entrée standardisée utilisée par :

les miners

les validateurs

les générateurs de dataset

les benchmarks

les comparaisons inter‑modèles

Chaque fichier JSON définit :

les 5 niveaux de difficulté (L1 → L5)

3 variations par niveau

une structure strictement normalisée

les consignes minimales garantissant la conformité aux invariants CATAR

Ces éléments sont explicitement décrits dans ton README actuel .

🧱 Structure du dossier
Chaque fichier suit la convention :

Code
T-XX.json
où XX correspond à l’invariant CATAR.

Liste complète des prompts (confirmée dans ton README actuel)  :

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

🧬 Fonction dans le Subnet CATAR
Les prompts :

servent de matrice d’entrée pour les miners

permettent de tester la réactivité, la robustesse et la stabilité des modèles

assurent une couverture complète des invariants CATAR

garantissent une standardisation des comportements attendus

permettent la génération automatique de datasets

sont utilisés conjointement avec les validateurs pour produire un score CATAR complet

Ces points sont explicitement décrits dans ton README actuel .

🧭 Ordre de lecture recommandé
Ordre conseillé pour comprendre la logique CATAR (déjà présent dans ton README actuel)  :

T‑CL.json — structure générale

T‑SP / T‑ND / T‑NF — invariants comportementaux

T‑SM / T‑SU — invariants identitaires

T‑LU / T‑TV — invariants épistémiques

T‑PS — protocole de sortie

T‑CL‑global — cohérence transversale

🧩 Importance dans l’architecture CATAR
Les prompts sont essentiels car ils :

définissent les situations types auxquelles les IA doivent répondre

permettent une évaluation systématique

assurent une comparabilité entre modèles

constituent la base de données d’entraînement du sous‑réseau

garantissent la neutralité, la sécurité conceptuelle et la non‑projection

servent de point d’entrée du pipeline CATAR

Ces éléments sont décrits dans ton README actuel .

✔️ État du dossier
Ton README actuel indique encore que « les prompts sont en cours de création », mais ce n’est plus vrai.
La page confirme explicitement que :

👉 Tous les prompts sont désormais créés, complets et conformes à la structure standardisée .

Ils sont prêts pour :

l’entraînement

l’évaluation

la génération de datasets

l’intégration dans le Subnet CATAR
