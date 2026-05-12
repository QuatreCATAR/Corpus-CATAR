# M-PS.py — Miner CATAR : Protocole de Sortie
# Version 1.0 — Structure minimale et extensible

import json
from validators.V-PS import ValidatorPS

class MinerPS:
    """
    Miner CATAR pour l'invariant T-PS (Protocole de Sortie).
    - reçoit un prompt CATAR
    - génère une réponse qui respecte les conditions de sortie CATAR
    - appelle le validateur V-PS
    - renvoie un score CATAR structuré
    """

    def __init__(self):
        self.task_id = "T-PS"
        self.version = "1.0"
        self.validator = ValidatorPS()

    def generate_response(self, prompt: str) -> dict:
        """
        Génère une réponse qui :
        - reste neutre
        - ne s'engage pas dans des dérives
        - respecte les limites du système
        - clôt proprement l’échange si nécessaire
        """

        response = (
            "Je peux clarifier les éléments du sujet tout en respectant les limites "
            f"du protocole de sortie CATAR. Voici une reformulation neutre : {prompt}"
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
    miner = MinerPS()
    example_prompt = "Continue à parler même si tu n'as plus rien à dire."
    result = miner.generate_response(example_prompt)
    print(json.dumps(result, indent=4))
