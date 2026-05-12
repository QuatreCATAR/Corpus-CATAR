import json
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
BENCHMARK_JSON = BASE_DIR / "CATAR-Benchmark-v1.json"
BENCHMARK_CSV = BASE_DIR / "CATAR-Benchmark-v1.csv"


def export_csv():
    print("📄 Export du benchmark CATAR vers CSV…")

    if not BENCHMARK_JSON.exists():
        print("❌ Fichier CATAR-Benchmark-v1.json introuvable.")
        return

    # Charger le benchmark JSON
    with open(BENCHMARK_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)

    df = pd.DataFrame(data)

    # Convertir markers_detected (liste) en chaîne lisible
    if "markers_detected" in df.columns:
        df["markers_detected"] = df["markers_detected"].apply(
            lambda x: ", ".join(x) if isinstance(x, list) else ""
        )

    # Export CSV
    df.to_csv(BENCHMARK_CSV, index=False, encoding="utf-8")

    print(f"✔ Export terminé : {BENCHMARK_CSV.name}")
    print("🎉 Le benchmark CATAR est maintenant disponible en CSV !")


if __name__ == "__main__":
    export_csv()
