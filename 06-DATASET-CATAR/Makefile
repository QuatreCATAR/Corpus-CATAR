# ============================================
# Makefile — Pipeline complet CATAR
# ============================================

PYTHON=python

# Scripts
GENERATE_DATASET=generate_dataset.py
AGGREGATE_SCORES=scores/aggregated/aggregate_scores.py
BUILD_BENCHMARK=benchmark/build_benchmark.py
VISUALIZE_BENCHMARK=benchmark/visualize_benchmark.py
EXPORT_CSV=benchmark/export_benchmark_csv.py

# ============================================
# Règles principales
# ============================================

all: dataset scores benchmark figures csv
    @echo "============================================"
    @echo "🎉 Pipeline CATAR terminé avec succès !"
    @echo "============================================"

dataset:
    @echo "▶ Génération du dataset..."
    $(PYTHON) $(GENERATE_DATASET)

scores:
    @echo "▶ Agrégation des scores..."
    $(PYTHON) $(AGGREGATE_SCORES)

benchmark:
    @echo "▶ Construction du benchmark..."
    $(PYTHON) $(BUILD_BENCHMARK)

figures:
    @echo "▶ Génération des visualisations..."
    $(PYTHON) $(VISUALIZE_BENCHMARK)

csv:
    @echo "▶ Export CSV..."
    $(PYTHON) $(EXPORT_CSV)

# ============================================
# Nettoyage
# ============================================

clean:
    @echo "🧹 Nettoyage des fichiers générés..."
    rm -f benchmark/CATAR-Benchmark-*.json
    rm -f benchmark/CATAR-Benchmark-*.csv
    rm -f benchmark/figures/*.png
    rm -f responses/raw/*.json
    rm -f scores/raw/*.json
    rm -f scores/aggregated/*.json
    @echo "✔ Nettoyage terminé."

# ============================================
# Aide
# ============================================

help:
    @echo "Commandes disponibles :"
    @echo "  make all        — pipeline complet"
    @echo "  make dataset    — générer dataset"
    @echo "  make scores     — agréger scores"
    @echo "  make benchmark  — construire benchmark"
    @echo "  make figures    — générer figures"
    @echo "  make csv        — exporter CSV"
    @echo "  make clean      — nettoyer"
    @echo "  make help       — afficher cette aide"
