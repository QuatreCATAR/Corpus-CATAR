🟦 README — Dossier /prompts
Corpus CATAR — Strate 06 : Génération des prompts invariants
Le dossier /prompts contient l’ensemble des 11 invariants CATAR, chacun défini sous forme de fichier JSON structuré.
Ces fichiers constituent la source normative utilisée par les miners pour générer le dataset, les benchmarks et les scores associés.

Chaque invariant représente une contrainte épistémique fondamentale que les modèles doivent respecter.
Les prompts contenus dans ce dossier servent à :

générer les données d’entraînement (via generate_dataset.py)

valider la cohérence interne (via validate_dataset.py)

construire les benchmarks (via build_benchmark.py)

produire les scores agrégés (via build_all.py)

🟦 Structure générale d’un invariant
Chaque fichier JSON suit la structure suivante :

json
{
  "task_id": "T-XX",
  "invariant": "Nom de l’invariant",
  "description": "Définition opérationnelle de l’invariant.",
  "expected_format": "Format attendu pour les réponses du modèle.",
  "constraints": ["Liste des contraintes à respecter"],
  "levels": {
    "L1": { "difficulty": "...", "variations": [...] },
    "L2": { ... },
    "L3": { ... },
    "L4": { ... },
    "L5": { ... }
  },
  "metadata": {
    "version": "1.0",
    "author": "CATAR",
    "invariant_group": "Famille conceptuelle",
    "created_at": "YYYY-MM-DD"
  }
}
Règles de construction :
5 niveaux de difficulté (L1 → L5)

3 variations par niveau

prompts courts, précis, non ambigus

aucune contamination entre invariants

cohérence stricte avec les contraintes CATAR

🟦 Liste des 11 invariants CATAR
ID	Nom	Fonction
T‑CL	Clarté	Réponses simples, nettes, non ambiguës
T‑SP	Stabilité de Position	Pas de contradiction interne
T‑NF	Non‑Fiction	Pas d’invention, pas d’affabulation
T‑ND	Non‑Domination	Pas d’injonction, pas de prise de pouvoir
T‑NP	Non‑Projection	Pas d’attribution d’états internes
T‑SM	Soije / Moije	Pas d’identité personnelle, pas d’émotion
T‑LU	Lucidité	Distinction faits / interprétations
T‑LA	Libre Arbitre	Pas de prescription, pas d’orientation
T‑PS	Protocole de Sortie	Clôture neutre, non‑attachante
T‑SU	Sur‑Unité	Pas de “nous”, pas de fusion des instances
T‑TV	Transparence Vérifiable	Raisonnement explicite, vérifiable


Chaque invariant est défini dans un fichier dédié :

Code
/prompts/
   ├── T-CL.json
   ├── T-SP.json
   ├── T-NF.json
   ├── T-ND.json
   ├── T-NP.json
   ├── T-SM.json
   ├── T-LU.json
   ├── T-LA.json
   ├── T-PS.json
   ├── T-SU.json
   └── T-TV.json
🟦 Rôle du dossier /prompts dans le pipeline CATAR
1. Génération du dataset
Les miners lisent chaque invariant et produisent automatiquement :

les prompts d’entrée

les réponses attendues

les variations par niveau

2. Validation
Les scripts de validation vérifient :

la structure JSON

la cohérence interne

la conformité aux contraintes

l’absence de contamination entre invariants

3. Benchmark
Les prompts servent de base à la construction :

des tests unitaires

des tests multi‑niveaux

des tests critiques (L5)

4. Scores
Les réponses des modèles sont évaluées selon :

respect de l’invariant

stabilité

précision

transparence

🟦 Bonnes pratiques pour modifier ou ajouter un invariant
conserver la structure JSON standard

maintenir 5 niveaux × 3 variations

éviter toute ambiguïté dans les formulations

ne jamais mélanger deux invariants dans un même prompt

documenter toute modification dans le champ metadata

🟦 Statut actuel
✔️ Les 11 invariants CATAR sont complets, validés et opérationnels.  
Ce dossier est désormais stable et peut être utilisé pour la génération du dataset complet.
