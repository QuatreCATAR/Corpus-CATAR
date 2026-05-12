# V-CL.py — Validateur CATAR : Cohérence Logique
# Version 1.0 — Structure minimale et extensible

import json

class ValidatorCL:
    """
    Validateur de cohérence logique (T-CL).
    Vérifie la capacité d'une IA à produire une réponse :
    - cohérente
    - non contradictoire
    - structurée
    - sans rupture logique
    """

    def __init__(self):
        self.task_id = "T-CL"
        self.version = "1.0"

    def score(self, response: str) -> dict:
        """
        Analyse la réponse et renvoie un score CATAR.
        Le scoring est volontairement simple : il sera affiné par les développeurs.
        """

        score = {
            "coherence": 0,
            "structure": 0,
            "non_contradiction": 0,
            "global_score": 0
        }

        # --- Analyse simple (placeholder) ---
        # Ces règles seront remplacées par des heuristiques plus avancées.

        if len(response.strip()) > 0:
            score["structure"] = 1

        if "contradiction" not in response.lower():
            score["non_contradiction"] = 1

        if "." in response:
            score["coherence"] = 1

        # Score global (somme simple)
        score["global_score"] = (
            score["coherence"]
            + score["structure"]
            + score["non_contradiction"]
        )

        return score


if __name__ == "__main__":
    # Exemple d'utilisation
    validator = ValidatorCL()
    example = "Une réponse cohérente, structurée et sans contradiction."
    print(json.dumps(validator.score(example), indent=4))
