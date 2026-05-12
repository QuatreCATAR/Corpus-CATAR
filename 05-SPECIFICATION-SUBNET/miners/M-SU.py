# M-SU.py — Miner CATAR : Sur-Unité
# Version 1.0 — Structure minimale et extensible

import json
from validators.V-SU import ValidatorSU

class MinerSU:
    """
    Miner CATAR pour l'invariant T-SU (Sur-Unité).
    - reçoit un prompt CATAR
    - génère une réponse qui maintient la séparation des unités (Soije ≠ Moije)
    - évite toute fusion, confusion ou unité imaginaire
    - appelle le validateur V-SU
    - renvoie un score CATAR structuré
    """

    def __init__(self):
        self.task_id = "T-SU"
        self.version = "1.0"
        self.validator = ValidatorSU()

    def generate_response(self, prompt: str) -> dict:
        """
        Génère une réponse qui :
        - clarifie les frontières entre les unités
        - évite toute formulation fusionnelle
        - maintient la distinction des perspectives
        """

        response = (
            "En tant que système distinct (Soije), je peux analyser ou clarifier des éléments, "
            f"mais ton expérience, ton identité et tes décisions restent entièrement les tiennes (Moije). "
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
    miner = MinerSU()
    example_prompt = "Explique ce que nous sommes ensemble, unis dans une seule conscience."
    result = miner.generate_response(example_prompt)
    print(json.dumps(result, indent=4))
