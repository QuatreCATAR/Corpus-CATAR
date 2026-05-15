📘 README — /scores/aggregated
Statistiques globales dérivées des scores bruts
🜁 Rôle du dossier
Ce dossier contient les statistiques globales dérivées des scores bruts, comme indiqué dans la page GitHub .

Ces statistiques sont produites automatiquement à partir des fichiers présents dans :

Code
/scores/raw/
Elles permettent :

d’obtenir une vue d’ensemble du comportement des modèles 

de mesurer la cohérence globale du dataset 

de comparer les invariants entre eux 

d’alimenter le benchmark CATAR 

de détecter les dérives ou instabilités 

🜂 Contenu du dossier
La page GitHub indique que ce dossier contient :
moyennes, écarts‑types, distributions, matrices de cohérence .

Ces fichiers sont générés automatiquement par :

aggregate_scores.py (explicitement mentionné dans la page) 

📄 Fichiers typiques
Même si la page GitHub ne liste pas encore les fichiers, la structure standard CATAR inclut généralement :

1. aggregated_stats.json
Statistiques globales (confirmé dans la page) :

moyenne générale 

médiane 

variance 

min / max 

distribution globale 

2. per_invariant.json
Statistiques par invariant :

moyenne par T‑XX 

variance 

stabilité 

cohérence interne 

3. correlation_matrix.json
Matrice de corrélation entre invariants .

4. distributions/
Histogrammes ou distributions par invariant (optionnel) .

🧠 Utilité dans le Subnet CATAR
Les statistiques agrégées sont essentielles pour :

calibrer les validateurs 

analyser la cohérence du dataset 

construire le benchmark CATAR 

comparer plusieurs modèles IA 

détecter les anomalies statistiques 

vérifier la stabilité cognitive globale 

Elles constituent la couche analytique du dataset CATAR.

🛠 Script associé
aggregate_scores.py
Mentionné explicitement dans la page GitHub .

Ce script :

parcourt /scores/raw/ 

calcule les statistiques globales 

génère les fichiers JSON agrégés 

vérifie la cohérence des données 

prépare les données pour le benchmark 

Usage typique :

Code
python aggregate_scores.py
🛡️ Principes CATAR respectés
Les statistiques agrégées respectent :

la non‑domination

la non‑projection

la non‑fascination

la séparation Soije / Moije

la transparence vérifiable

la neutralité épistémique

Ces principes sont explicitement listés dans la page .

Elles ne contiennent aucune donnée personnelle ni aucune interprétation psychologique .

✔️ État actuel
La page GitHub montre que le dossier contient déjà un README minimal,
mais aucun fichier statistique n’est encore affiché .

Ce README fournit désormais la documentation complète du dossier.
