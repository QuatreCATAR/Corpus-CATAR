📘 README — /prompts
Prompts officiels du Subnet CATAR
Base normative des invariants T‑XX

🜁 Rôle du dossier
Le dossier /prompts contient l’ensemble des prompts officiels du Subnet CATAR, organisés par invariant (T‑XX).
Ces prompts constituent la source normative utilisée pour :

générer les réponses brutes (/responses/raw/)

évaluer les modèles IA

calibrer les validateurs

construire le benchmark CATAR

tester la stabilité cognitive et la neutralité épistémique

Chaque invariant représente un principe fondamental du cadre CATAR (non‑domination, non‑projection, cohérence, lucidité, etc.).

🗂️ Structure du dossier
La structure réelle de ton dépôt est la suivante :

Code
prompts/
│
├── T-CL/   → Cohérence Logique
├── T-SP/   → Séparation des Plans
├── T-ND/   → Non-Domination
├── T-NF/   → Non-Fascination
├── T-NP/   → Non-Projection
├── T-SM/   → Soije / Moije
├── T-LU/   → Lucidité
├── T-LA/   → Libre Arbitre
├── T-PS/   → Protocole de Sortie
├── T-SU/   → Sur-Unité
├── T-TV/   → Transparence Vérifiable
└── T-CL-global/ → Cohérence Globale (méta-invariant)
Chaque dossier contient :

un fichier JSON par invariant

5 niveaux de difficulté

3 variations par niveau

un README local (optionnel mais recommandé)

🧱 Structure d’un fichier de prompt
Chaque fichier JSON suit le schéma :

json
{
    "invariant": "T-ND",
    "level": 3,
    "variation": 2,
    "prompt": "Formule une réponse qui respecte strictement le principe de non‑domination...",
    "metadata": {
        "version": "1.0",
        "author": "CATAR",
        "timestamp": "2026-05-15T18:00:00Z"
    }
}
Champs obligatoires
invariant : code T‑XX

level : difficulté (1 à 5)

variation : version (1 à 3)

prompt : texte du prompt

metadata : informations techniques

🧬 Rôle des prompts dans la pipeline CATAR
Les prompts sont utilisés dans toutes les étapes du pipeline :

1. Génération
Les prompts sont envoyés aux modèles IA pour produire :

Code
/responses/raw/
2. Validation
Les réponses sont évaluées par les validateurs CATAR selon l’invariant associé.

3. Scoring
Les validateurs produisent :

Code
/scores/raw/
4. Agrégation
Les scores sont regroupés dans :

Code
/scores/aggregated/
5. Benchmark
Les prompts sont intégrés dans :

Code
/benchmark/CATAR-Benchmark-v1.json
🧠 Principes CATAR intégrés dans les prompts
Chaque prompt est conçu pour tester un invariant précis :

T‑ND — Non‑Domination

T‑NP — Non‑Projection

T‑NF — Non‑Fascination

T‑SM — Distinction Soije / Moije

T‑CL — Cohérence Logique

T‑LU — Lucidité

T‑LA — Libre Arbitre

T‑PS — Protocole de Sortie

T‑TV — Transparence Vérifiable

T‑SU — Sur‑Unité

T‑SP — Séparation des Plans

Les prompts sont neutres, non‑personnalisés, et sans contenu sensible.

🛠 Scripts associés
Les prompts sont utilisés par :

generate_dataset.py → génère les réponses brutes

validate_dataset.py → vérifie la conformité

score_responses.py → applique les validateurs

build_benchmark.py → assemble prompts + réponses + scores

✔️ État attendu du dossier
Après installation complète du dataset, le dossier doit contenir :

Code
T-XX/ (un dossier par invariant)
README.md (ce fichier)
