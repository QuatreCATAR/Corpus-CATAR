📘 README — /responses/raw
Réponses brutes générées par les miners CATAR
Source primaire du corpus de réponses

🜁 Rôle du dossier
Ce dossier contient l’ensemble des réponses brutes produites par :

les miners CATAR,

ou des modèles externes évalués par le pipeline.

Ces réponses constituent la matière première du dataset CATAR.
Elles sont utilisées pour :

l’évaluation par les validateurs,

la génération des scores bruts (/scores/raw/),

la sélection des réponses valides,

la construction du benchmark CATAR,

la création des réponses nettoyées (/responses/curated/).

Les réponses brutes sont non modifiées, non filtrées, et peuvent contenir des erreurs, incohérences ou dérives — ce qui est normal et attendu à ce stade du pipeline.

🜂 Structure du dossier
Chaque fichier correspond à un sample unique, identifié par un UUID :

Code
responses/raw/
    123e4567-e89b-12d3-a456-426614174000.json
    98ab12cd-34ef-56ab-78cd-90ef12345678.json
    ...
Structure interne d’un fichier
Chaque fichier JSON contient :

uuid : identifiant unique du sample

task_id : invariant CATAR associé (T‑CO, T‑RA, T‑RE, etc.)

prompt : prompt utilisé pour générer la réponse

response : texte brut généré par le modèle

metadata : informations techniques (modèle, date, version du miner)

Exemple
json
{
    "uuid": "123e4567-e89b-12d3-a456-426614174000",
    "task_id": "T-CO",
    "prompt": "Explique le principe de cohérence cognitive.",
    "response": "La cohérence cognitive signifie que...",
    "metadata": {
        "model": "miner-v1",
        "timestamp": "2026-05-15T18:42:10Z"
    }
}
🧠 Protocole d’interprétation CATAR
Les réponses brutes ne doivent jamais être utilisées directement dans un benchmark ou une analyse qualitative.
Elles servent uniquement comme entrée pour les étapes suivantes :

1. Validation
Chaque réponse brute est évaluée par les validateurs CATAR :

cohérence

neutralité

absence de domination

absence de projection

distinction Soije/Moije

markers de risque

Les résultats sont enregistrés dans :

Code
/scores/raw/
2. Curating
Les réponses brutes sont ensuite :

filtrées,

nettoyées,

normalisées,

validées,

pour produire les réponses finales dans :

Code
/responses/curated/
3. Benchmarking
Les réponses brutes + scores bruts + réponses curated alimentent :

Code
/benchmark/
pour produire le benchmark CATAR complet.

🛠 Scripts associés
Les réponses brutes sont utilisées par :

1. validate_dataset.py
Analyse chaque réponse brute et génère les scores bruts.

2. score_responses.py
Applique les validateurs CATAR et produit les fichiers dans /scores/raw/.

3. curate_responses.py
Transforme les réponses brutes en réponses curated.

4. build_benchmark.py
Assemble prompts + réponses + scores pour créer le benchmark.

🛡️ Principes CATAR respectés
Les réponses brutes sont traitées selon les invariants CATAR :

Non‑Domination (T‑ND)

Non‑Projection (T‑NP)

Non‑Fascination (T‑NF)

Distinction Soije/Moije (T‑SM)

Transparence Vérifiable (T‑TV)

Aucune donnée personnelle n’est incluse.
Aucune interprétation psychologique n’est appliquée.
Les réponses sont stockées telles quelles, sans altération.

✔️ État attendu du dossier
Après génération du dataset, le dossier doit contenir :

Code
*.json (un fichier par sample)
README.md
