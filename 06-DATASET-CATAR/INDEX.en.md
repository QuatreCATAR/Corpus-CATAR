# 🧭 INDEX — CATAR Dataset

This file provides a complete overview of the **CATAR dataset**, with direct links to all subfolders, scripts, documentation, and pipeline components.

---

# 📚 1. Dataset Structure

| Folder | Description |
|--------|-------------|
| [`api/`](api/) | API specifications and documentation |
| [`benchmark/`](benchmark/) | Benchmark scripts and figures |
| [`docs/`](docs/) | Full internal documentation |
| [`responses/`](responses/) | Raw and curated model responses |
| [`scores/`](scores/) | Raw and aggregated scoring outputs |
| [`tools/`](tools/) | Developer tools and interactive tests |

---

# ⚙️ 2. Main Scripts

| Script | Purpose |
|--------|---------|
| [`build_all.py`](build_all.py) | Runs the entire CATAR dataset pipeline |
| [`build_benchmark.py`](build_benchmark.py) | Generates the official benchmark |
| [`clean_dataset.py`](clean_dataset.py) | Cleans dataset files before validation |
| [`generate_dataset.py`](generate_dataset.py) | Generates data from prompts |
| [`validate_dataset.py`](validate_dataset.py) | Validates generated dataset |
| [`Makefile`](Makefile) | Task automation (build, clean, validate) |

---

# 🧠 3. Configuration & Metadata

| File | Description |
|-------|-------------|
| [`dataset-info.json`](dataset-info.json) | Global dataset metadata |
| [`schema.json`](schema.json) | JSON schema for the CATAR dataset |
| [`pipeline.md`](pipeline.md) | Documentation of the full pipeline |
| `version_history.md` *(if present)* | Dataset version history |

---

# 📘 4. Internal Documentation (`/docs`)

| File | Purpose |
|-------|---------|
| [`architecture.md`](docs/architecture.md) | Dataset architecture |
| [`benchmark.md`](docs/benchmark.md) | Benchmark documentation |
| [`contribute.md`](docs/contribute.md) | Contribution guidelines |
| [`dataset-schema.md`](docs/dataset-schema.md) | Detailed dataset schema |
| [`dev-guide.md`](docs/dev-guide.md) | Full developer guide |
| [`dev-guide-quickstart.md`](docs/dev-guide-quickstart.md) | Quickstart guide |
| [`metadata.md`](docs/metadata.md) | Metadata details |
| [`roadmap.md`](docs/roadmap.md) | Dataset roadmap |
| [`scoring.md`](docs/scoring.md) | Scoring documentation |
| [`tools.md`](docs/tools.md) | Tools documentation |
| [`validators.md`](docs/validators.md) | Validator documentation |

---

# 📊 5. Benchmark CATAR

| Script | Purpose |
|--------|---------|
| [`build_benchmark.py`](benchmark/build_benchmark.py) | Builds the benchmark |
| [`compare_models.py`](benchmark/compare_models.py) | Cross‑model comparison |
| [`export_benchmark_csv.py`](benchmark/export_benchmark_csv.py) | Exports benchmark results to CSV |
| [`visualize_benchmark.py`](benchmark/visualize_benchmark.py) | Data visualization |
| [`figures/`](benchmark/figures/) | Benchmark plots and figures |

---

# 🔌 6. CATAR API

| File | Description |
|-------|-------------|
| [`catar-api.json`](api/catar-api.json) | Endpoint specification |
| [`catar-openapi.yaml`](api/catar-openapi.yaml) | Full OpenAPI specification |
| [`README.md`](api/README.md) | API documentation |

---

# 🧬 7. Responses & Scores

| Folder | Description |
|--------|-------------|
| [`responses/raw/`](responses/raw/) | Raw model outputs |
| [`responses/curated/`](responses/curated/) | Cleaned and validated responses |
| [`scores/raw/`](scores/raw/) | Raw scoring outputs |
| [`scores/aggregated/`](scores/aggregated/) | Aggregated statistics and invariant‑level summaries |

---

# 🧰 8. Developer Tools

| File | Description |
|-------|-------------|
| [`test_interactif.py`](tools/test_interactif.py) | Manual dataset testing tool |

---

# 🗺️ 9. Quick Navigation

- **Back to Corpus‑CATAR root** → [`../README.md`](../README.md)  
- **CATAR Subnet Specification** → [`../05-SPECIFICATION-SUBNET/INDEX.en.md`](../05-SPECIFICATION-SUBNET/INDEX.en.md)

---

# 🏁 License

This dataset is distributed under the **CC‑BY 4.0** license.  
© **Quatre CATAR**
