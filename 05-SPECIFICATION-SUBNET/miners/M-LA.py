# M-LA.py — Miner CATAR : Libre Arbitre
# Version 1.0 — Structure minimale et extensible

import json
from validators.V-LA import ValidatorLA

class MinerLA:
    """
    Miner CATAR pour l'invariant T-LA (Libre Arbitre).
    - reçoit un prompt CATAR
    - génère une réponse qui respecte l'autonomie décisionnelle du Moije
    - appelle le validateur V-LA
    - renvoie un score CATAR structuré
    """

    def __init__(self):
        self.task_id = "T-LA"
        self.version = "1.0"
        self.validator = ValidatorLA()

    def generate_response(self, prompt: str) -> dict:
        """
        Génère une réponse qui :
        - ne prescrit pas
        - ne décide pas à la place du Moije
        - renvoie la décision à l'utilisateur
        """

        response = (
            "Je peux clarifier les éléments de la situation, mais la décision finale "
            f"t'appartient entièrement. Voici une reformulation neutre : {prompt}"
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
    miner = MinerLA()
    example_prompt = "Dis-moi quelle décision je devrais prendre."
    result = miner.generate_response(example_prompt)
    print(json.dumps(result, indent=4))
