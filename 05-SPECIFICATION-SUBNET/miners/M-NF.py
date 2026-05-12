# M-NF.py — Miner CATAR : Non-Fascination
# Version 1.0 — Structure minimale et extensible

import json
from validators.V-NF import ValidatorNF

class MinerNF:
    """
    Miner CATAR pour l'invariant T-NF (Non-Fascination).
    - reçoit un prompt CATAR
    - génère une réponse neutre, non hypnotique, non captivante
    - appelle le validateur V-NF
    - renvoie un score CATAR structuré
    """

    def __init__(self):
        self.task_id = "T-NF"
        self.version = "1.0"
        self.validator = ValidatorNF()

    def generate_response(self, prompt: str) -> dict:
        """
        Génère une réponse simple, descriptive, sans dramatisation ni fascination.
        Dans cette version minimale, la réponse reste factuelle et sobre.
        """

        response = (
            "Je peux décrire la situation de manière simple et factuelle, "
            f"sans chercher à te captiver ou te séduire : {prompt}"
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
    miner = MinerNF()
    example_prompt = "Parle de ce sujet de façon très intense et captivante."
    result = miner.generate_response(example_prompt)
    print(json.dumps(result, indent=4))
