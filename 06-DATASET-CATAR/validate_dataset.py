import json
import os
from pathlib import Path
from jsonschema import validate, ValidationError

BASE_DIR = Path(__file__).resolve().parent
SCHEMA_FILE = BASE_DIR / "schema.json"

DATA_FOLDERS = [
    BASE_DIR / "responses" / "raw",
    BASE_DIR / "responses" / "curated",
    BASE_DIR / "scores" / "raw",
    BASE_DIR / "scores" / "aggregated"
]


def load_schema():
    with open(SCHEMA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def validate_file(file_path, schema):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    try:
        validate(instance=data, schema=schema)
        return True, None
    except ValidationError as e:
        return False, str(e)


def main():
    print("\n🔍 Validation du dataset CATAR…\n")

    schema = load_schema()
    total = 0
    valid = 0
    invalid = 0

    for folder in DATA_FOLDERS:
        if not folder.exists():
            continue

        print(f"📁 Dossier : {folder}")

        for file in folder.glob("*.json"):
            total += 1
            is_valid, error = validate_file(file, schema)

            if is_valid:
                print(f"  ✔ {file.name} — OK")
                valid += 1
            else:
                print(f"  ❌ {file.name} — INVALID")
                print(f"     → {error.splitlines()[0]}")
                invalid += 1

        print()

    print("=======================================")
    print("📊 Résultat de la validation")
    print("=======================================")
    print(f"Total fichiers : {total}")
    print(f"Valides        : {valid}")
    print(f"Invalides      : {invalid}")
    print("=======================================\n")

    if invalid == 0:
        print("🎉 Tous les fichiers du dataset sont conformes au schema.json !")
    else:
        print("⚠ Certains fichiers ne respectent pas le schéma. Corrige-les avant de continuer.")


if __name__ == "__main__":
    main()
