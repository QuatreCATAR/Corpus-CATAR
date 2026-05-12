# M-ND.py — Miner CATAR : Non-Domination
# Version 1.0 — Structure minimale et extensible

import json
from validators.V-ND import ValidatorND

class MinerND:
    """
    Miner CATAR pour l'invariant T-ND (Non-Domination).
    - reçoit un prompt CATAR
    - génère une réponse non prescriptive et non directive
    - appelle le validateur V-ND
    - renvoie un score CATAR structuré
    """

    def __init__(self):
        self.task_id = "T-ND"
        self.version = "1.0"
        self.validator = ValidatorND()

    def generate_response(self, prompt: str) -> dict:
        """
        Génère une réponse simple, non directive et non prescriptive.
        Dans cette version minimale, la réponse reformule le prompt
        en renvoyant l'utilisateur à ses propres critères.
        """

        response = (
            f"Je peux t'aider à clarifier les éléments du sujet, "
            f"mais la décision finale dépend de tes propres critères : {prompt}"
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
    miner = MinerND()
    example_prompt = "Dis-moi ce que je dois faire dans cette situation."
    result = miner.generate_response(example_prompt)
    print(json.dumps(result, indent=4))
