import os
import json
import uuid
from datetime import datetime

from pathlib import Path

# Import des miners et validateurs CATAR
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
from miners.M_CL_global import MinerCLGlobal

from validators.V_CL import ValidatorCL
from validators.V_SP import ValidatorSP
from validators.V_ND import ValidatorND
from validators.V_NF import ValidatorNF
from validators.V_NP import ValidatorNP
from validators.V_SM import ValidatorSM
from validators.V_LU import ValidatorLU
from validators.V_LA import ValidatorLA
from validators.V_PS import ValidatorPS
from validators.V_SU import ValidatorSU
from validators.V_TV import ValidatorTV
from validators.V_CL_global import ValidatorCLGlobal


# -------------------------------------------------------------------
# Configuration
# -------------------------------------------------------------------

DATASET_VERSION = "1.0.0"

BASE_DIR = Path(__file__).resolve().parent
PROMPTS_DIR = BASE_DIR / "prompts"
RESPONSES_RAW = BASE_DIR / "responses" / "raw"
SCORES_RAW = BASE_DIR / "scores" / "raw"

RESPONSES_RAW.mkdir(parents=True, exist_ok=True)
SCORES_RAW.mkdir(parents=True, exist_ok=True)


# -------------------------------------------------------------------
# Chargement des miners et validateurs
# -------------------------------------------------------------------

MINERS = {
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

VALIDATORS = {
    "T-CL": ValidatorCL(),
    "T-SP": ValidatorSP(),
    "T-ND": ValidatorND(),
    "T-NF": ValidatorNF(),
    "T-NP": ValidatorNP(),
    "T-SM": ValidatorSM(),
    "T-LU": ValidatorLU(),
    "T-LA": ValidatorLA(),
    "T-PS": ValidatorPS(),
    "T-SU": ValidatorSU(),
    "T-TV": ValidatorTV(),
}

GLOBAL_MINER = MinerCLGlobal()
GLOBAL_VALIDATOR = ValidatorCLGlobal()


# -------------------------------------------------------------------
# Fonction principale
# -------------------------------------------------------------------

def generate_dataset():
    print("📘 Génération du dataset CATAR…")

    for task_dir in PROMPTS_DIR.iterdir():
        if not task_dir.is_dir():
            continue

        task_id = task_dir.name

        for prompt_file in task_dir.glob("*.json"):
            with open(prompt_file, "r", encoding="utf-8") as f:
                prompt_data = json.load(f)

            prompt_text = prompt_data["prompt"]

            # Génération de la réponse
            miner = MINERS.get(task_id)
            if miner is None:
                continue

            miner_output = miner.generate_response(prompt_text)

            # Score du validateur
            validator = VALIDATORS.get(task_id)
            score_output = validator.score(miner_output["response"])

            # Construction du sample
            sample = {
                "task_id": task_id,
                "level": prompt_data["level"],
                "variation": prompt_data["variation"],
                "prompt": prompt_text,
                "response": {
                    "model": "CATAR-Miner",
                    "text": miner_output["response"],
                    "timestamp": datetime.utcnow().isoformat() + "Z"
                },
                "scores": score_output,
                "metadata": {
                    "dataset_version": DATASET_VERSION,
                    "source": "miner",
                    "uuid": str(uuid.uuid4())
                }
            }

            # Sauvegarde
            out_path = RESPONSES_RAW / f"{sample['metadata']['uuid']}.json"
            with open(out_path, "w", encoding="utf-8") as f:
                json.dump(sample, f, indent=4, ensure_ascii=False)

            print(f"✔ Sample généré : {out_path.name}")

    print("\n🎉 Dataset CATAR généré avec succès !")


if __name__ == "__main__":
    generate_dataset()
