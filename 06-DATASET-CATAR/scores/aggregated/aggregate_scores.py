import os
import json
import statistics
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RAW_SCORES_DIR = BASE_DIR.parent / "raw"
OUTPUT_STATS = BASE_DIR / "aggregated_stats.json"
OUTPUT_INVARIANTS = BASE_DIR / "per_invariant.json"


def load_scores():
    """Charge tous les scores bruts depuis /scores/raw/."""
    scores = []
    for file in RAW_SCORES_DIR.glob("*.json"):
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
            scores.append(data)
    return scores


def aggregate_global_scores(scores):
    """Calcule les statistiques globales sur tous les scores."""
    global_scores = [s["scores"]["global_score"] for s in scores]

    return {
        "count": len(global_scores),
        "mean": statistics.mean(global_scores) if global_scores else 0,
        "median": statistics.median(global_scores) if global_scores else 0,
        "variance": statistics.variance(global_scores) if len(global_scores) > 1 else 0,
        "min": min(global_scores) if global_scores else 0,
        "max": max(global_scores) if global_scores else 0,
        "distribution": {
            "0.0-0.2": sum(1 for x in global_scores if 0.0 <= x < 0.2),
            "0.2-0.4": sum(1 for x in global_scores if 0.2 <= x < 0.4),
            "0.4-0.6": sum(1 for x in global_scores if 0.4 <= x < 0.6),
            "0.6-0.8": sum(1 for x in global_scores if 0.6 <= x < 0.8),
            "0.8-1.0": sum(1 for x in global_scores if 0.8 <= x <= 1.0),
        }
    }


def aggregate_by_invariant(scores):
    """Calcule les statistiques par invariant CATAR."""
    invariants = {}

    for s in scores:
        task_id = s["task_id"]
        score = s["scores"]["global_score"]

        invariants.setdefault(task_id, []).append(score)

    stats = {}
    for task_id, values in invariants.items():
        stats[task_id] = {
            "count": len(values),
            "mean": statistics.mean(values),
            "median": statistics.median(values),
            "variance": statistics.variance(values) if len(values) > 1 else 0,
            "min": min(values),
            "max": max(values)
        }

    return stats


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def main():
    print("📊 Agrégation des scores CATAR…")

    scores = load_scores()

    if not scores:
        print("⚠ Aucun score trouvé dans /scores/raw/.")
        return

    global_stats = aggregate_global_scores(scores)
    per_invariant_stats = aggregate_by_invariant(scores)

    save_json(OUTPUT_STATS, global_stats)
    save_json(OUTPUT_INVARIANTS, per_invariant_stats)

    print(f"✔ Statistiques globales enregistrées dans : {OUTPUT_STATS.name}")
    print(f"✔ Statistiques par invariant enregistrées dans : {OUTPUT_INVARIANTS.name}")
    print("\n🎉 Agrégation terminée avec succès !")


if __name__ == "__main__":
    main()
