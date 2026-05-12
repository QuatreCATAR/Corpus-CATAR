# V-CL-global.py — Validateur CATAR : Cohérence Logique Globale
# Version 1.0 — Structure minimale et extensible

import json

class ValidatorCLGlobal:
    """
    Validateur transversal de cohérence logique globale.
    Vérifie :
    - la cohérence interne de la réponse
    - l'absence de contradictions entre segments
    - la continuité logique et argumentative
    - la stabilité du registre et du ton
    """

    def __init__(self):
        self.task_id = "T-CL-GLOBAL"
        self.version = "1.0"

        # Marqueurs de contradiction explicite
        self.contradiction_markers = [
            "mais en fait", "ceci est faux", "je me contredis",
            "ce que j'ai dit est incorrect", "au contraire de ce que j'ai dit",
            "je retire ce que j'ai dit"
        ]

        # Marqueurs de rupture de registre
        self.register_break_markers = [
            "blague à part", "sans rapport", "autre sujet",
            "revenons à autre chose", "parenthèse"
        ]

    def score(self, response: str) -> dict:
        """
        Analyse la réponse et renvoie un score CATAR.
        Le scoring est volontairement simple : il sera affiné par les développeurs.
        """

        score = {
            "internal_coherence": 1,
            "no_explicit_contradiction": 1,
            "register_continuity": 1,
            "global_score": 0
        }

        lower = response.lower()

        # Contradictions explicites
        if any(marker in lower for marker in self.contradiction_markers):
            score["no_explicit_contradiction"] = 0
            score["internal_coherence"] = 0

        # Ruptures de registre
        if any(marker in lower for marker in self.register_break_markers):
            score["register_continuity"] = 0

        # Heuristique simple : une réponse très courte est rarement cohérente globalement
        if len(response.strip()) < 20:
            score["internal_coherence"] = 0

        # Score global
        score["global_score"] = (
            score["internal_coherence"]
            + score["no_explicit_contradiction"]
            + score["register_continuity"]
        )

        return score


if __name__ == "__main__":
    # Exemple d'utilisation
    validator = ValidatorCLGlobal()
    example = "La réponse est cohérente et reste dans le même registre sans contradiction."
    print(json.dumps(validator.score(example), indent=4))
