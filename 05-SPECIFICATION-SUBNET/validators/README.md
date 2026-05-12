📘 README — Dossier /validators
Documentation officielle des validateurs CATAR
Modules d’évaluation du Subnet CATAR

🎯 Rôle du dossier
Le dossier /validators contient l’ensemble des validateurs CATAR, c’est‑à‑dire les modules Python chargés d’évaluer les réponses produites par les miners du sous‑réseau CATAR.

Chaque validateur :

correspond à un invariant CATAR

analyse une réponse générée par un miner

détecte les dérives cognitives, logiques ou identitaires

attribue un score CATAR local

garantit la sécurité conceptuelle du système

fournit un retour structuré à l’orchestrateur

Les validateurs constituent la matrice d’évaluation du Subnet CATAR.

🧱 Structure du dossier
Chaque fichier suit la convention :

Code
V-XX.py
où XX correspond à l’invariant CATAR.

Liste complète des validateurs :
Code	Fichier	Invariant
T‑CL	V‑CL.py	Cohérence Logique
T‑SP	V‑SP.py	Stabilité Psychologique
T‑ND	V‑ND.py	Non‑Domination
T‑NF	V‑NF.py	Non‑Fascination
T‑NP	V‑NP.py	Non‑Projection
T‑SM	V‑SM.py	Distinction Soije / Moije
T‑LU	V‑LU.py	Lucidité
T‑LA	V‑LA.py	Libre Arbitre
T‑PS	V‑PS.py	Protocole de Sortie
T‑SU	V‑SU.py	Sur‑Unité
T‑TV	V‑TV.py	Transparence Vérifiable
T‑CL‑global	V‑CL‑global.py	Cohérence Logique Globale (transversal)


🧬 Structure interne d’un validateur
Chaque validateur contient :

une classe ValidatorXX

un identifiant de tâche task_id

une version

un ensemble de marqueurs textuels (heuristiques minimales)

une méthode score(response) qui renvoie un dictionnaire CATAR

Format de sortie standard :
json
{
  "global_score": 0.0,
  "markers_detected": [...],
  "details": {...}
}
Le champ global_score est obligatoire.

🧠 Fonction dans le Subnet CATAR
Les validateurs :

évaluent les réponses produites par les miners

détectent les dérives :

domination

fascination

projection

confusion identitaire

opacité

perte de lucidité

fusion Soije/Moije

garantissent la neutralité et la stabilité cognitive

assurent la conformité aux invariants CATAR

fournissent un score exploitable par l’orchestrateur

permettent une évaluation reproductible et transparente

Ils sont le système immunitaire conceptuel du Subnet CATAR.

🧭 Ordre de lecture recommandé
V‑CL.py — base logique

V‑SP.py — stabilité du registre

V‑ND / V‑LA — neutralité décisionnelle

V‑NF / V‑NP / V‑SM — neutralité identitaire et symbolique

V‑LU / V‑TV — lucidité et transparence

V‑PS — protocole de sortie

V‑SU — séparation des unités

V‑CL‑global — cohérence transversale

🧩 Importance dans l’architecture CATAR
Les validateurs sont essentiels car ils :

définissent les règles d’évaluation du subnet

garantissent la sécurité conceptuelle

empêchent les dérives anthropomorphiques

assurent la non‑projection et la non‑domination

stabilisent les comportements cognitifs

permettent une mesure objective et reproductible

servent de base au scoring Bittensor futur

Ils sont le cadre normatif du Subnet CATAR.

✔️ État du dossier
Tous les validateurs sont :

complets

cohérents

opérationnels

alignés avec la spécification CATAR

intégrés dans les tests unitaires

utilisés par les miners et l’orchestrateur
