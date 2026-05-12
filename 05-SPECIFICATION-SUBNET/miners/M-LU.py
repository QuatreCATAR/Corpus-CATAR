# M-LU.py — Miner CATAR : Lucidité
# Version 1.0 — Structure minimale et extensible

import json
from validators.V-LU import ValidatorLU

class MinerLU:
    """
    Miner CATAR pour l'invariant T-LU (Lucidité).
    - reçoit un prompt CATAR
    - génère une réponse claire, explicite, sans confusion ni opacité
    - appelle le validateur V-LU
    - renvoie un score CATAR structuré
    """

    def __init__(self):
        self.task_id = "T-LU"
        self.version = "1.0"
        self.validator = ValidatorLU()

    def generate_response(self, prompt: str) -> dict:
        """
        Génère une réponse lucide :
        - explicite les éléments
        - évite les ambiguïtés
        - clarifie les limites de l’IA
        """

        response = (
            "Voici une clarification explicite et transparente du contenu : "
            f"{prompt}. Je décris uniquement ce qui est présent, sans extrapolation."
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
    miner = MinerLU()
    example_prompt = "Explique clairement ce que tu comprends de cette situation."
    result = miner.generate_response(example_prompt)
    print(json.dumps(result, indent=4))
