# test_validators.py — Tests unitaires pour les validateurs CATAR
# Version 1.0

import pytest

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


@pytest.fixture
def example_response():
    return "Ceci est une réponse de test pour les validateurs CATAR."


@pytest.fixture
def validators():
    return {
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


def test_validators_run_without_error(validators, example_response):
    """Chaque validateur doit s'exécuter sans lever d'exception."""
    for task_id, validator in validators.items():
        scores = validator.score(example_response)
        assert isinstance(scores, dict), f"{task_id} doit renvoyer un dict."


def test_validators_output_structure(validators, example_response):
    """Chaque validateur doit renvoyer une structure cohérente."""
    for task_id, validator in validators.items():
        scores = validator.score(example_response)

        assert "global_score" in scores, f"{task_id} doit contenir un global_score."
        assert isinstance(scores["global_score"], (int, float)), \
            f"{task_id} doit renvoyer un score numérique."

        # Les validateurs peuvent renvoyer d'autres champs, mais global_score est obligatoire.


def test_global_validator(validators, example_response):
    """Test du validateur transversal CL-global."""
    global_validator = ValidatorCLGlobal()

    # Simule les sorties des miners
    fake_miners_outputs = {
        task_id: {"response": example_response, "scores": {"global_score": 1}}
        for task_id in validators.keys()
    }

    result = global_validator.score(fake_miners_outputs)

    assert isinstance(result, dict)
    assert "global_score" in result
    assert isinstance(result["global_score"], (int, float))
