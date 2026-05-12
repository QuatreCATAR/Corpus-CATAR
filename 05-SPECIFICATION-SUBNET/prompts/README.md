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

Cette fonction est explicitement décrite dans ton README actuel .

Chaque fichier JSON définit :

5 niveaux de difficulté (L1 → L5)

3 variations par niveau

une structure strictement normalisée

des consignes minimales garantissant la conformité aux invariants CATAR

Ces éléments sont confirmés dans ton fichier actuel .

🧱 Structure du dossier
Chaque invariant est un fichier JSON suivant la convention :

Code
T-XX.json
où XX correspond à l’invariant CATAR.
Cette structure est explicitement décrite dans ton README actuel .

Liste complète des prompts CATAR
(identique à celle présente dans ton dépôt)  :

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

🧬 Fonction dans le Subnet CATAR
Les prompts CATAR permettent :

de tester la réactivité, la robustesse et la stabilité des modèles

d’assurer une couverture complète des invariants CATAR

de garantir une standardisation des comportements attendus

de générer automatiquement des datasets

de produire un score CATAR complet via les validateurs

Ces fonctions sont décrites dans ton README actuel .

🧭 Ordre de lecture recommandé
Ordre conseillé pour comprendre la logique CATAR (repris de ton README actuel)  :

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

constituent la base d’entraînement du Subnet

garantissent la neutralité, la sécurité conceptuelle et la non‑projection

servent de point d’entrée du pipeline CATAR

Ces éléments sont confirmés dans ton README actuel .

✔️ État du dossier
Ton dépôt indique encore que « les prompts sont en cours de création », mais ce n’est plus vrai.
La page confirme explicitement que :

👉 Tous les prompts sont désormais créés, complets et conformes à la structure standardisée CATAR.  

Ils sont prêts pour :

l’entraînement

l’évaluation

la génération de datasets

l’intégration dans le Subnet CATAR

Comme indiqué dans ton fichier actuel
