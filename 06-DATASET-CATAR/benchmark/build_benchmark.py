import os
import json
from pathlib import Path
from statistics import mean, median, variance

BASE_DIR = Path(__file__).resolve().parent

PROMPTS_DIR = BASE_DIR.parent / "prompts"
RESPONSES_DIR = BASE_DIR.parent / "responses" / "curated"
SCORES_DIR = BASE_DIR.parent / "scores" / "raw"
BENCHMARK_DIR = BASE_DIR

BENCHMARK_FILE = BENCHMARK_DIR / "CATAR-Benchmark-v1.json"


def load_json_files(directory):
    """Charge tous les fichiers JSON d'un dossier."""
    data = []
    for file in directory.glob("*.json"):
        with open(file, "r", encoding="utf-8") as f:
            data.append(json.load(f))
    return data


def build_benchmark():
    print("📘 Construction du CATAR‑Benchmark v1.0…")

    # Chargement des prompts (optionnel mais utile pour vérification)
    prompts = []
    for task_dir in PROMPTS_DIR.iterdir():
        if task_dir.is_dir():
            for file in task_dir.glob("*.json"):
                with open(file, "r", encoding="utf-8") as f:
                    prompts.append(json.load(f))

    # Chargement des réponses et scores
    responses = load_json_files(RESPONSES_DIR)
    scores = load_json_files(SCORES_DIR)

    # Indexation par UUID
    score_map = {s["metadata"]["uuid"]: s for s in scores}
    response_map = {r["metadata"]["uuid"]: r for r in responses}

    benchmark = []

    for uuid_key, response in response_map.items():
        score = score_map.get(uuid_key)
        if not score:
            continue

        entry = {
            "uuid": uuid_key,
            "task_id": response["task_id"],
            "prompt": response["prompt"],
            "response": response["response"]["text"],
            "global_score": score["scores"]["global_score"],
            "markers_detected": score["scores"].get("markers_detected", []),
            "validator_version": score["scores"].get("validator_version", "unknown")
        }

        benchmark.append(entry)

    # Sauvegarde du benchmark
    with open(BENCHMARK_FILE, "w", encoding="utf-8") as f:
        json.dump(benchmark, f, indent=4, ensure_ascii=False)

    print(f"✔ Benchmark généré : {BENCHMARK_FILE.name}")
    print("🎉 CATAR‑Benchmark v1.0 construit avec succès !")


if __name__ == "__main__":
    build_benchmark()
