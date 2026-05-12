📘 README — Dossier /benchmark/figures
Visualisations officielles du CATAR‑Benchmark
🎯 Rôle du dossier
Le dossier /figures contient l’ensemble des visualisations générées automatiquement à partir du CATAR‑Benchmark.
Ces figures permettent d’analyser :

la distribution globale des scores CATAR

la stabilité des invariants

les corrélations entre invariants

la densité des scores

les comportements transversaux des modèles

Elles constituent la base visuelle pour l’analyse scientifique du Subnet CATAR.

🧱 Contenu du dossier
Les fichiers sont générés par :

Code
visualize_benchmark.py
et incluent :

📊 1. global_distribution.png
Histogramme + courbe KDE montrant la distribution globale des scores CATAR.

📦 2. scores_by_invariant.png
Boxplots comparant les scores pour chaque invariant T‑XX.

🔥 3. invariant_correlation_heatmap.png
Heatmap de corrélation entre invariants CATAR.
Permet d’identifier les invariants les plus liés ou les plus indépendants.

🌿 4. score_density.png
Courbe de densité globale des scores.

🧬 Usage
Ces visualisations sont utilisées pour :

analyser la cohérence psychologique des modèles

détecter les dérives (projection, domination, fascination…)

comparer plusieurs modèles IA

calibrer les miners et validateurs

préparer des rapports ou publications scientifiques

construire le CATAR‑Benchmark v1.0

Elles sont générées automatiquement à chaque exécution de :

Code
python visualize_benchmark.py
🛡️ Principes CATAR respectés
Toutes les visualisations respectent :

la non‑domination

la non‑projection

la non‑fascination

la séparation Soije / Moije

la transparence vérifiable

la neutralité épistémique

Aucune figure ne doit représenter des données violant ces invariants.

✔️ État actuel
Le dossier est prêt à accueillir :

les visualisations générées

les futures figures (comparaisons inter‑modèles, analyses avancées)

les exports haute résolution pour publication
