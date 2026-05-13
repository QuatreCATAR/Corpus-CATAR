import requests
import json

API_BASE = "http://localhost:8000/catar"  # À adapter selon ton déploiement

def choisir_invariant():
    invariants = [
        "T-ND", "T-NF", "T-NP", "T-SM", "T-SU",
        "T-TV", "T-CL", "T-LU", "T-LA", "T-PS", "T-SP"
    ]
    print("\n=== Choix de l'invariant CATAR ===")
    for i, inv in enumerate(invariants):
        print(f"{i+1}. {inv}")
    choix = int(input("\nSélection : ")) - 1
    return invariants[choix]

def obtenir_prompt(task_id):
    print("\nRécupération d'un prompt...")
    r = requests.get(f"{API_BASE}/prompt/{task_id}/L3/1")
    return r.json()["prompt"]

def envoyer_reponse(task_id, prompt, reponse):
    payload = {
        "task_id": task_id,
        "prompt": prompt,
        "response": reponse
    }
    r = requests.post(f"{API_BASE}/score", json=payload)
    return r.json()

def main():
    print("\n=== Test interactif CATAR ===")

    task_id = choisir_invariant()
    prompt = obtenir_prompt(task_id)

    print("\n--- Prompt CATAR ---")
    print(prompt)

    reponse = input("\nVotre réponse :\n> ")

    resultat = envoyer_reponse(task_id, prompt, reponse)

    print("\n=== Résultat CATAR ===")
    print(json.dumps(resultat, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    main()
