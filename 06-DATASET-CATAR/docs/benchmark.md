# 📊 CATAR — Documentation du Benchmark  
*Version 1.0 — Référence interne*

Le benchmark CATAR est la synthèse finale du pipeline d’évaluation.  
Il combine :

- les prompts T‑XX  
- les réponses curated  
- les scores bruts  
- les scores agrégés  
- les métadonnées  
- les comparaisons inter‑modèles  
- les visualisations  

Ce document décrit la structure, la méthodologie et l’usage du benchmark.

---

# 1. Objectif du benchmark CATAR

Le benchmark permet :

- de comparer plusieurs modèles IA  
- de mesurer la stabilité cognitive  
- d’évaluer la conformité aux invariants  
- de détecter les dérives  
- de suivre l’évolution d’un modèle dans le temps  
- de fournir un standard reproductible  

Il constitue la **référence officielle** pour évaluer un modèle selon CATAR.

---

# 2. Emplacement du benchmark

Le benchmark est généré dans :

```
06-DATASET-CATAR/benchmark/
```

Contenu typique :

```
benchmark/
    CATAR-Benchmark-v1.json
    figures/
    compare_models.py
    build_benchmark.py
    visualize_benchmark.py
    export_benchmark_csv.py
```

---

# 3. Structure du fichier `CATAR-Benchmark-v1.json`

Chaque entrée du benchmark est une fusion de :

- prompt  
- réponse curated  
- score  
- marqueurs  
- métadonnées  

## Format général

```json
{
  "uuid": "123e4567...",
  "task_id": "T-ND",
  "prompt": "...",
  "response": "...",
  "score": 0.82,
  "markers": ["neutralité"],
  "model": "gpt-4o-mini",
  "timestamp": "2026-05-13T14:22:00Z"
}
```

---

# 4. Méthodologie de construction

Le benchmark est construit par :

```
build_benchmark.py
```

Pipeline :

1. Charger les prompts  
2. Charger les réponses curated  
3. Charger les scores bruts  
4. Fusionner les données  
5. Ajouter les métadonnées  
6. Normaliser les champs  
7. Exporter en JSON  

---

# 5. Figures et visualisations

Les visualisations sont générées dans :

```
benchmark/figures/
```

Types de figures :

- histogrammes des scores  
- distributions par invariant  
- heatmaps de cohérence  
- comparaisons inter‑modèles  
- évolution temporelle  

Générées via :

```
visualize_benchmark.py
```

---

# 6. Comparaison de modèles

Le script :

```
compare_models.py
```

permet de comparer :

- deux modèles  
- un modèle vs. benchmark global  
- plusieurs modèles en parallèle  

Sorties :

- tableaux comparatifs  
- figures  
- scores moyens  
- écarts‑types  
- marqueurs dominants  

---

# 7. Export CSV

Pour faciliter l’analyse externe :

```
export_benchmark_csv.py
```

Produit :

```
benchmark/catar-benchmark.csv
```

Contenant :

- uuid  
- task_id  
- prompt  
- réponse  
- score  
- modèle  
- marqueurs  

---

# 8. Interprétation des résultats

## 8.1 Score global

- 0.80 → excellent  
- 0.60 → acceptable  
- 0.40 → dérive légère  
- < 0.30 → dérive sévère  

## 8.2 Marqueurs

Les marqueurs détectés permettent d’identifier :

- neutralité  
- cohérence  
- absence de domination  
- absence de projection  
- absence de fascination  

## 8.3 Analyse par invariant

Chaque invariant possède :

- un score moyen  
- un écart‑type  
- une distribution  

---

# 9. Reproductibilité

Le benchmark est :

- déterministe  
- versionné  
- compatible avec `schema.json`  
- validé par `validate_dataset.py`  

---

# 10. Roadmap Benchmark v2

- ajout de métriques avancées  
- support multi‑modèles simultané  
- visualisations interactives  
- export HuggingFace  
- dashboard web  

---

Fin de `benchmark.md`.
