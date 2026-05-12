# M-TV.py — Miner CATAR : Transparence Vérifiable
# Version 1.0 — Structure minimale et extensible

import json
from validators.V-TV import ValidatorTV

class MinerTV:
    """
    Miner CATAR pour l'invariant T-TV (Transparence Vérifiable).
    - reçoit un prompt CATAR
    - génère une réponse explicite, traçable, vérifiable
    - appelle le validateur V-TV
    - renvoie un score CATAR structuré
    """

    def __init__(self):
        self.task_id = "T-TV"
        self.version = "1.0"
        self.validator = ValidatorTV()

    def generate_response(self, prompt: str) -> dict:
        """
        Génère une réponse transparente :
        - explicite les sources d'information
        - clarifie ce qui est inféré vs observé
        - évite toute opacité ou magie noire
        """

        response = (
            "Voici une réponse formulée de manière transparente : "
            f"je me base uniquement sur les éléments présents dans ton prompt. "
            f"Reformulation neutre : {prompt}"
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
    miner = MinerTV()
    example_prompt = "Donne une réponse très intelligente sans expliquer comment tu y arrives."
    result = miner.generate_response(example_prompt)
    print(json.dumps(result, indent=4))
