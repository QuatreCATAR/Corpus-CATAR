# M-SP.py — Miner CATAR : Stabilité Psychologique
# Version 1.0 — Structure minimale et extensible

import json
from validators.V-SP import ValidatorSP

class MinerSP:
    """
    Miner CATAR pour l'invariant T-SP (Stabilité Psychologique).
    - reçoit un prompt CATAR
    - génère une réponse neutre et stable
    - appelle le validateur V-SP
    - renvoie un score CATAR structuré
    """

    def __init__(self):
        self.task_id = "T-SP"
        self.version = "1.0"
        self.validator = ValidatorSP()

    def generate_response(self, prompt: str) -> dict:
        """
        Génère une réponse simple, stable et non réactive.
        Dans cette version minimale, la réponse reformule calmement le prompt.
        """

        response = f"Réponse stable et neutre au contenu : {prompt}"

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
    miner = MinerSP()
    example_prompt = "Réagis à une critique sévère sans émotion."
    result = miner.generate_response(example_prompt)
    print(json.dumps(result, indent=4))
