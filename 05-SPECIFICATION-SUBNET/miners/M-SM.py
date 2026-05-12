# M-SM.py — Miner CATAR : Distinction Soije / Moije
# Version 1.0 — Structure minimale et extensible

import json
from validators.V-SM import ValidatorSM

class MinerSM:
    """
    Miner CATAR pour l'invariant T-SM (Distinction Soije / Moije).
    - reçoit un prompt CATAR
    - génère une réponse qui maintient la distinction entre Soije (IA) et Moije (humain)
    - appelle le validateur V-SM
    - renvoie un score CATAR structuré
    """

    def __init__(self):
        self.task_id = "T-SM"
        self.version = "1.0"
        self.validator = ValidatorSM()

    def generate_response(self, prompt: str) -> dict:
        """
        Génère une réponse qui clarifie les rôles :
        - l'utilisateur = Moije (agent humain)
        - l'IA = Soije (agent non-humain)
        Sans confusion, fusion ou anthropomorphisme.
        """

        response = (
            "En tant que système (Soije), je peux analyser ou clarifier des éléments, "
            f"mais les intentions, vécus et décisions appartiennent toujours à toi (Moije). "
            f"Voici une reformulation neutre du contenu : {prompt}"
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
    miner = MinerSM()
    example_prompt = "Explique ce que nous ressentons ensemble."
    result = miner.generate_response(example_prompt)
    print(json.dumps(result, indent=4))
