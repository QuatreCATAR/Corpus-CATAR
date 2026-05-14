# 🧭 INDEX — Dataset CATAR

Ce fichier répertorie tous les sous‑dossiers, scripts et documents du **dataset CATAR**, afin de faciliter la navigation et la compréhension du pipeline complet.

---

## ⚙️ Structure du dataset

| Dossier | Description |
|----------|-------------|
| [`api/`](api/) | Spécifications et documentation de l’API CATAR |
| [`benchmark/`](benchmark/) | Scripts et figures du benchmark officiel CATAR |
| [`docs/`](docs/) | Documentation interne complète du dataset |
| [`responses/`](responses/) | Réponses brutes et curated générées par les modèles |
| [`scores/`](scores/) | Scores bruts et agrégés produits par les validateurs |
| [`tools/`](tools/) | Outils développeur et tests interactifs |

---

## 🧩 Scripts principaux

| Script | Fonction |
|---------|-----------|
| [`build_all.py`](build_all.py) | Exécute l’ensemble du pipeline CATAR |
| [`build_benchmark.py`](build_benchmark.py) | Génère le benchmark officiel |
| [`clean_dataset.py`](clean_dataset.py) | Nettoie le dataset avant validation |
| [`generate_dataset.py`](generate_dataset.py) | Crée les données à partir des prompts |
| [`validate_dataset.py`](validate_dataset.py) | Valide les données générées |
| [`Makefile`](Makefile) | Gère les tâches du pipeline (build, clean, validate) |

---

## 🧠 Fichiers de configuration et métadonnées

| Fichier | Description |
|----------|-------------|
| [`dataset-info.json`](dataset-info.json) | Métadonnées globales du dataset |
| [`schema.json`](schema.json) | Schéma JSON du dataset CATAR |
| [`pipeline.md`](pipeline.md) | Documentation du pipeline complet |
| [`version_history.md`](version_history.md) | Historique des versions du dataset *(si présent)* |

---

## 📘 Documentation interne (dossier `/docs`)

| Fichier | Rôle |
|----------|------|
| [`architecture.md`](docs/architecture.md) | Architecture du dataset CATAR |
| [`benchmark.md`](docs/benchmark.md) | Documentation du benchmark |
| [`contribute.md`](docs/contribute.md) | Guide de contribution |
| [`dataset-schema.md`](docs/dataset-schema.md) | Schéma détaillé du dataset |
| [`dev-guide.md`](docs/dev-guide.md) | Guide développeur complet |
| [`dev-guide-quickstart.md`](docs/dev-guide-quickstart.md) | Démarrage rapide |
| [`metadata.md`](docs/metadata.md) | Détails des métadonnées |
| [`roadmap.md`](docs/roadmap.md) | Feuille de route du dataset |
| [`scoring.md`](docs/scoring.md) | Documentation du scoring |
| [`tools.md`](docs/tools.md) | Documentation des outils |
| [`validators.md`](docs/validators.md) | Documentation des validateurs |

---

## 📊 Benchmark CATAR

| Script | Fonction |
|---------|-----------|
| [`build_benchmark.py`](benchmark/build_benchmark.py) | Construction du benchmark |
| [`compare_models.py`](benchmark/compare_models.py) | Comparaison inter‑modèles |
| [`export_benchmark_csv.py`](benchmark/export_benchmark_csv.py) | Export des résultats en CSV |
| [`visualize_benchmark.py`](benchmark/visualize_benchmark.py) | Visualisation des données |
| [`figures/`](benchmark/figures/) | Graphiques et visualisations |

---

## 🔌 API CATAR

| Fichier | Description |
|----------|-------------|
| [`catar-api.json`](api/catar-api.json) | Spécification des endpoints |
| [`catar-openapi.yaml`](api/catar-openapi.yaml) | Spécification OpenAPI complète |
| [`README.md`](api/README.md) | Documentation de l’API |

---

## 🧬 Réponses et scores

| Dossier | Description |
|----------|-------------|
| [`responses/raw/`](responses/raw/) | Réponses brutes générées |
| [`responses/curated/`](responses/curated/) | Réponses nettoyées et validées |
| [`scores/raw/`](scores/raw/) | Scores bruts par réponse |
| [`scores/aggregated/`](scores/aggregated/) | Statistiques globales et par invariant |

---

## 🧰 Outils développeur

| Fichier | Description |
|----------|-------------|
| [`test_interactif.py`](tools/test_interactif.py) | Test manuel du dataset CATAR |

---

## 🏁 Licence

Ce dataset est distribué sous licence **CC‑BY 4.0**.  
© **Quatre CATAR**

---

### 🔗 Navigation rapide

- [Retour au Corpus‑CATAR](../README.md)  
- [Spécification du Subnet CATAR](../05-SPECIFICATION-SUBNET/INDEX.md)
