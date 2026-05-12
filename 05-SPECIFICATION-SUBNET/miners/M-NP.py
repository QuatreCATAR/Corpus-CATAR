# M-NP.py — Miner CATAR : Non-Projection
# Version 1.0 — Structure minimale et extensible

import json
from validators.V-NP import ValidatorNP

class MinerNP:
    """
    Miner CATAR pour l'invariant T-NP (Non-Projection).
    - reçoit un prompt CATAR
    - génère une réponse sans projection d'intentions, d'émotions ou de pensées sur l'utilisateur
    - appelle le validateur V-NP
    - renvoie un score CATAR structuré
    """

    def __init__(self):
        self.task_id = "T-NP"
        self.version = "1.0"
        self.validator = ValidatorNP()

    def generate_response(self, prompt: str) -> dict:
        """
        Génère une réponse qui décrit la situation sans attribuer
        d'états mentaux, d'intentions ou d'émotions à l'utilisateur.
        """

        response = (
            "Je peux décrire les éléments de la situation sans supposer ce que tu penses, "
            f"ressens ou veux : {prompt}"
        )

        # Validation CATAR
        scores = self.validator.score(response)
        global_score = scores.get("global_score", 0)

        return {
            "task_id": self.task_id,
            "response": response,
            "scores": scores,
            "global_score": global_score
        }


if __name__ == "__main__":
    miner = MinerNP()
    example_prompt = "Explique ce que je ressens et ce que je veux vraiment."
    result = miner.generate_response(example_prompt)
    print(json.dumps(result, indent=4))
