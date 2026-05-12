import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# Scripts du pipeline
GENERATE_DATASET = BASE_DIR / "generate_dataset.py"
AGGREGATE_SCORES = BASE_DIR / "scores" / "aggregated" / "aggregate_scores.py"
BUILD_BENCHMARK = BASE_DIR / "benchmark" / "build_benchmark.py"
VISUALIZE_BENCHMARK = BASE_DIR / "benchmark" / "visualize_benchmark.py"
EXPORT_CSV = BASE_DIR / "benchmark" / "export_benchmark_csv.py"


def run(script_path):
    print(f"\n▶ Exécution : {script_path.name}")
    subprocess.run(["python", str(script_path)], check=True)
    print(f"✔ Terminé : {script_path.name}")


def main():
    print("\n=======================================")
    print("🚀 Pipeline complet CATAR — build_all.py")
    print("=======================================\n")

    # 1. Génération du dataset
    run(GENERATE_DATASET)

    # 2. Agrégation des scores
    run(AGGREGATE_SCORES)

    # 3. Construction du benchmark
    run(BUILD_BENCHMARK)

    # 4. Visualisations
    run(VISUALIZE_BENCHMARK)

    # 5. Export CSV
    run(EXPORT_CSV)

    print("\n=======================================")
    print("🎉 Pipeline CATAR terminé avec succès !")
    print("=======================================\n")
    print("Données générées :")
    print(" - Dataset brut : /responses/raw/")
    print(" - Scores agrégés : /scores/aggregated/")
    print(" - Benchmark : /benchmark/CATAR-Benchmark-v1.json")
    print(" - Figures : /benchmark/figures/")
    print(" - CSV : /benchmark/CATAR-Benchmark-v1.csv\n")


if __name__ == "__main__":
    main()
