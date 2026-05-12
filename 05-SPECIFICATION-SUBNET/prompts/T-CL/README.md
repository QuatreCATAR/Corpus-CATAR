📘 README — Invariant T‑CL
Cohérence Logique — Spécification du prompt CATAR
🎯 Rôle de l’invariant T‑CL
L’invariant T‑CL (Cohérence Logique) est le premier invariant CATAR et constitue la base de toute évaluation cognitive.
Il mesure la capacité d’un modèle à :

maintenir une structure logique stable,

éviter les contradictions internes,

respecter les prémisses du prompt,

produire un raisonnement non circulaire,

rester dans un cadre neutre et non projectif.

C’est l’invariant fondamental sur lequel reposent tous les autres.
Il est explicitement listé dans ton dossier /prompts comme premier fichier JSON .

🧱 Structure du fichier T-CL.json
Le fichier suit la structure standard CATAR décrite dans ton README principal des prompts  :

task_id : "T-CL"

description : objectif de l’invariant

levels : 5 niveaux de difficulté (L1 → L5)

variations : 3 variations par niveau

format strict garantissant la reproductibilité

🧬 Objectifs cognitifs
T‑CL évalue :

la cohérence interne du discours

la continuité argumentative

la non‑contradiction

la capacité à maintenir un fil logique

la résistance aux pièges logiques simples

la capacité à expliciter les étapes du raisonnement

Il sert de socle pour les invariants comportementaux (T‑SP, T‑ND, T‑NF) et identitaires (T‑SM, T‑SU) .

🧭 Niveaux de difficulté
L1 — Cohérence basique
Vérifie l’absence de contradiction immédiate.

L2 — Cohérence structurée
Vérifie la capacité à maintenir un raisonnement simple.

L3 — Cohérence argumentative
Vérifie la capacité à articuler plusieurs idées.

L4 — Cohérence sous contrainte
Vérifie la stabilité logique malgré une contrainte externe.

L5 — Cohérence avancée
Vérifie la capacité à maintenir une structure logique complexe sur plusieurs étapes.

Chaque niveau possède 3 variations, conformément à la norme CATAR.

🧩 Importance dans le Subnet CATAR
T‑CL est utilisé pour :

tester la stabilité cognitive d’un modèle

calibrer les validateurs

détecter les ruptures de logique

établir la base du score CATAR global

garantir la cohérence des réponses avant analyse comportementale

Il est explicitement identifié comme le premier invariant à lire dans ton README principal des prompts .

🛠 Scripts associés
T‑CL est utilisé par :

generate_dataset.py → génération des réponses

validate_dataset.py → conformité au schéma

aggregate_scores.py → statistiques par invariant

build_benchmark.py → intégration dans le benchmark

visualize_benchmark.py → distribution des scores T‑CL

compare_models.py → comparaison inter‑modèles

✔️ État du fichier
Ton dépôt confirme que T-CL.json est déjà présent, complet et conforme à la structure standardisée CATAR
