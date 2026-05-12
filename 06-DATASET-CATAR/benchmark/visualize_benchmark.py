import json
import os
from pathlib import Path

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
BENCHMARK_FILE = BASE_DIR / "CATAR-Benchmark-v1.json"
FIGURES_DIR = BASE_DIR / "figures"

FIGURES_DIR.mkdir(exist_ok=True)


def load_benchmark():
    """Charge le benchmark CATAR."""
    with open(BENCHMARK_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return pd.DataFrame(data)


def plot_global_distribution(df):
    """Histogramme global des scores."""
    plt.figure(figsize=(8, 5))
    sns.histplot(df["global_score"], bins=20, kde=True, color="royalblue")
    plt.title("Distribution globale des scores CATAR")
    plt.xlabel("Score global")
    plt.ylabel("Fréquence")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "global_distribution.png")
    plt.close()


def plot_scores_by_invariant(df):
    """Distribution des scores par invariant."""
    plt.figure(figsize=(10, 6))
    sns.boxplot(x="task_id", y="global_score", data=df)
    plt.title("Scores par invariant CATAR")
    plt.xlabel("Invariant (T-XX)")
    plt.ylabel("Score global")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "scores_by_invariant.png")
    plt.close()


def plot_heatmap(df):
    """Heatmap de corrélation entre invariants."""
    pivot = df.pivot_table(
        index="uuid",
        columns="task_id",
        values="global_score"
    )

    plt.figure(figsize=(12, 8))
    sns.heatmap(pivot.corr(), annot=True, cmap="coolwarm", vmin=-1, vmax=1)
    plt.title("Corrélation entre invariants CATAR")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "invariant_correlation_heatmap.png")
    plt.close()


def plot_density(df):
    """Courbe de densité globale."""
    plt.figure(figsize=(8, 5))
    sns.kdeplot(df["global_score"], fill=True, color="darkgreen")
    plt.title("Densité des scores CATAR")
    plt.xlabel("Score global")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "score_density.png")
    plt.close()


def main():
    print("📊 Visualisation du CATAR‑Benchmark…")

    df = load_benchmark()

    plot_global_distribution(df)
    print("✔ global_distribution.png généré")

    plot_scores_by_invariant(df)
    print("✔ scores_by_invariant.png généré")

    plot_heatmap(df)
    print("✔ invariant_correlation_heatmap.png généré")

    plot_density(df)
    print("✔ score_density.png généré")

    print("\n🎉 Visualisations générées dans le dossier /figures/")


if __name__ == "__main__":
    main()
