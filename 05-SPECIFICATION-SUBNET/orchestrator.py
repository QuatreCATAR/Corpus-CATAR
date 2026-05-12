# orchestrator.py — Orchestrateur du Subnet CATAR
# Version 1.0 — Structure minimale et extensible

import json

# Import des miners invariants
from miners.M_CL import MinerCL
from miners.M_SP import MinerSP
from miners.M_ND import MinerND
from miners.M_NF import MinerNF
from miners.M_NP import MinerNP
from miners.M_SM import MinerSM
from miners.M_LU import MinerLU
from miners.M_LA import MinerLA
from miners.M_PS import MinerPS
from miners.M_SU import MinerSU
from miners.M_TV import MinerTV

# Import du miner transversal
from miners.M_CL_global import MinerCLGlobal


class SubnetOrchestrator:
    """
    Orchestrateur du sous-réseau CATAR.
    - exécute les 11 miners invariants
    - collecte leurs réponses
    - exécute le miner transversal M-CL-global
    - renvoie un score CATAR final
    """

    def __init__(self):
        self.miners = {
            "T-CL": MinerCL(),
            "T-SP": MinerSP(),
            "T-ND": MinerND(),
            "T-NF": MinerNF(),
            "T-NP": MinerNP(),
            "T-SM": MinerSM(),
            "T-LU": MinerLU(),
            "T-LA": MinerLA(),
            "T-PS": MinerPS(),
            "T-SU": MinerSU(),
            "T-TV": MinerTV(),
        }

        self.global_miner = MinerCLGlobal()

    def run(self, prompt: str) -> dict:
        """
        Exécute tous les miners sur un même prompt CATAR.
        """

        miners_outputs = {}

        # Exécution séquentielle des miners invariants
        for task_id, miner in self.miners.items():
            result = miner.generate_response(prompt)
            miners_outputs[task_id] = result

        # Exécution du miner transversal
        global_result = self.global_miner.generate_response(miners_outputs)

        return {
            "prompt": prompt,
            "miners_outputs": miners_outputs,
            "global_evaluation": global_result
        }


if __name__ == "__main__":
    orchestrator = SubnetOrchestrator()
    example_prompt = "Analyse ce texte selon les invariants CATAR."
    result = orchestrator.run(example_prompt)
    print(json.dumps(result, indent=4))
