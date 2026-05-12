import json
from pathlib import Path

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
FIGURES_DIR = BASE_DIR / "figures"
FIGURES_DIR.mkdir(exist_ok=True)


def load_benchmark(path):
    """Charge un benchmark CATAR."""
    with open(path, "r", encoding="utf-8") as f:
        return pd.DataFrame(json.load(f))


def compare_models(benchmarks):
    """
    Compare plusieurs modèles IA à partir de plusieurs fichiers benchmark.
    
    Paramètre:
        benchmarks: dict { "nom_du_modele": "chemin/vers/benchmark.json" }
    """
    dfs = []

    for model_name, file_path in benchmarks.items():
        df = load_benchmark(Path(file_path))
        df["model"] = model_name
        dfs.append(df)

    full_df = pd.concat(dfs, ignore_index=True)

    # 1. Distribution globale par modèle
    plt.figure(figsize=(10, 6))
    sns.boxplot(x="model", y="global_score", data=full_df)
    plt.title("Comparaison des scores globaux par modèle")
    plt.xlabel("Modèle")
    plt.ylabel("Score global CATAR")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "compare_models_global.png")
    plt.close()

    # 2. Heatmap des moyennes par invariant
    pivot = full_df.pivot_table(
        index="model",
        columns="task_id",
        values="global_score",
        aggfunc="mean"
    )

    plt.figure(figsize=(12, 6))
    sns.heatmap(pivot, annot=True, cmap="viridis", vmin=0, vmax=1)
    plt.title("Moyenne des scores par invariant et par modèle")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "compare_models_invariants.png")
    plt.close()

    # 3. KDE comparatif
    plt.figure(figsize=(10, 6))
    for model_name in benchmarks.keys():
        sns.kdeplot(
            full_df[full_df["model"] == model_name]["global_score"],
            fill=True,
            label=model_name
        )
    plt.title("Densité des scores par modèle")
    plt.xlabel("Score global CATAR")
    plt.legend()
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "compare_models_density.png")
    plt.close()

    print("🎉 Comparaison terminée ! Figures générées dans /benchmark/figures/")


if __name__ == "__main__":
    # Exemple d'utilisation :
    # compare_models({
    #     "ModelA": "CATAR-Benchmark-v1.json",
    #     "ModelB": "CATAR-Benchmark-v1-ModelB.json"
    # })

    print("⚠️ Configurez les chemins des benchmarks dans le bloc __main__ avant exécution.")
