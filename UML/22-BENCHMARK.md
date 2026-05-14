# 📘 UML — Benchmark Construction Process (BENCHMARK)

**File:** `22-BENCHMARK.md`  
**Category:** UML — Operational / Benchmark Engine  
**Version:** 1.0  
**Project:** Corpus‑CATAR  
**Author:** Quatre CATAR  

---

## 📝 Description / Description

**FR —**  
Ce diagramme décrit le **processus complet de construction du Benchmark CATAR**, tel qu’il apparaît dans le fichier.  
Il détaille les cinq étapes successives permettant de transformer les scores agrégés en un benchmark structuré et visualisable :

1. **Préparation** — chargement des données : prompts, réponses curated, scores agrégés, métadonnées   
2. **Fusion logique** — regroupement par invariant T‑XX, niveaux L1→L5, variations 1→3   
3. **Construction des objets** — création des objets `BenchmarkEntry` contenant `{prompt, response, score, invariant, niveau, meta}`   
4. **Agrégation globale** — constitution du benchmark global sous forme de liste d’entrées   
5. **Génération des figures** — production des visualisations finales (figures, graphiques, etc.)   

Ce diagramme constitue la **référence opérationnelle** pour comprendre comment les données brutes et les scores T‑XX sont transformés en un benchmark exploitable pour l’analyse comparative des modèles IA.

**EN —**  
This diagram describes the **complete construction process of the CATAR Benchmark**, as shown in the file.  
It details the five sequential steps that transform aggregated scores into a structured and visualizable benchmark:

1. **Preparation** — loading data: prompts, curated responses, aggregated scores, metadata   
2. **Logical fusion** — grouping by T‑XX invariant, levels L1→L5, variations 1→3   
3. **Object construction** — creation of `BenchmarkEntry` objects containing `{prompt, response, score, invariant, level, meta}`   
4. **Global aggregation** — building the global benchmark as a list of entries   
5. **Figure generation** — producing final visualizations (figures, charts, etc.)   

This diagram provides the **operational reference** for understanding how raw data and T‑XX scores are transformed into a benchmark suitable for comparative analysis of AI models.

---

## 🧩 Diagramme / Diagram

*(The existing diagram begins here.)*

                         
                         +-----------------------------+
                         |         Benchmark           |
                         |     benchmark/*.py          |
                         +-------------+---------------+
                                       |
                                       | reçoit
                                       v
                         +-----------------------------+
                         |   Scores agrégés (JSON)     |
                         | scores/aggregated/*.json    |
                         +-------------+---------------+
                                       |
                                       | 1. Préparation
                                       v
                         +-----------------------------+
                         |   Chargement des données    |
                         |   - prompts                 |
                         |   - réponses curated        |
                         |   - scores agrégés          |
                         |   - métadonnées             |
                         +-------------+---------------+
                                       |
                                       | 2. Fusion logique
                                       v
                         +-----------------------------+
                         |   Fusion par invariant      |
                         |   - T‑XX                    |
                         |   - niveaux L1→L5           |
                         |   - variations 1→3          |
                         +-------------+---------------+
                                       |
                                       | 3. Construction des objets
                                       v
                         +-----------------------------+
                         |   Objet BenchmarkEntry      |
                         | {prompt, response, score,   |
                         |  invariant, niveau, meta}   |
                         +-------------+---------------+
                                       |
                                       | 4. Agrégation globale
                                       v
                         +-----------------------------+
                         |   Benchmark global          |
                         |  liste de BenchmarkEntry    |
                         +-------------+---------------+
                                       |
                                       | 5. Génération des figures
                                       v
                         +-----------------------------+
                         |   Figures / Visualisations  |
                         | benchmark/figures/*.png     |
                         +-------------+---------------+
                                       |
                                       | 6. Export final
                                       v
                         +-----------------------------+
                         | CATAR-Benchmark-v1.json     |
                         | (benchmark complet)         |
                         +-----------------------------+
