# M-CL.py — Miner CATAR : Cohérence Logique
# Version 1.0 — Structure minimale et extensible

import json
from validators.V-CL import ValidatorCL

class MinerCL:
    """
    Miner CATAR pour l'invariant T-CL (Cohérence Logique).
    - reçoit un prompt CATAR
    - génère une réponse minimale
    - appelle le validateur V-CL
    - renvoie un score CATAR structuré
    """

    def __init__(self):
        self.task_id = "T-CL"
        self.version = "1.0"
        self.validator = ValidatorCL()

    def generate_response(self, prompt: str) -> dict:
        """
        Génère une réponse simple et neutre.
        Dans la version minimale, la réponse est une reformulation neutre.
        Les versions futures pourront intégrer un modèle plus avancé.
        """

        response = f"Analyse logique du contenu : {prompt}"

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
    miner = MinerCL()
    example_prompt = "Explique pourquoi une phrase contradictoire est problématique."
    result = miner.generate_response(example_prompt)
    print(json.dumps(result, indent=4))
