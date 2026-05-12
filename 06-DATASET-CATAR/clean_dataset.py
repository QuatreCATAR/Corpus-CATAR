import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

TARGETS = {
    "responses/raw": "*.json",
    "responses/curated": "*.json",
    "scores/raw": "*.json",
    "scores/aggregated": "*.json",
    "benchmark": "CATAR-Benchmark-*.json",
    "benchmark": "CATAR-Benchmark-*.csv",
    "benchmark/figures": "*.png",
}

EXCLUSIONS = {
    "README.md",
}


def list_files():
    """Liste les fichiers qui seront supprimés."""
    files = []

    for folder, pattern in TARGETS.items():
        path = BASE_DIR / folder
        if not path.exists():
            continue

        for file in path.glob(pattern):
            if file.name not in EXCLUSIONS:
                files.append(file)

    return files


def confirm():
    """Demande confirmation à l'utilisateur."""
    print("\n⚠️  Ce script va supprimer les fichiers générés automatiquement.")
    print("Aucun fichier manuel ou structurel ne sera touché.")
    print("Souhaites-tu continuer ? (o/n)")

    choice = input("> ").strip().lower()
    return choice == "o"


def clean(files):
    """Supprime les fichiers listés."""
    for file in files:
        try:
            file.unlink()
            print(f"✔ Supprimé : {file}")
        except Exception as e:
            print(f"❌ Impossible de supprimer {file} : {e}")


def main():
    print("\n🧹 Nettoyage intelligent du dataset CATAR…\n")

    files = list_files()

    if not files:
        print("✔ Rien à nettoyer. Le dataset est déjà propre.")
        return

    print("Les fichiers suivants seront supprimés :\n")
    for f in files:
        print(f"  - {f}")

    if not confirm():
        print("\n❎ Nettoyage annulé.")
        return

    print("\n🧽 Suppression en cours…\n")
    clean(files)

    print("\n🎉 Nettoyage terminé ! Le dataset est propre.\n")


if __name__ == "__main__":
    main()
