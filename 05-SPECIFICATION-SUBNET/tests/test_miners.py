# test_miners.py — Tests unitaires pour les miners CATAR
# Version 1.0

import pytest

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


@pytest.fixture
def example_prompt():
    return "Ceci est un prompt de test pour les miners CATAR."


@pytest.fixture
def miners():
    return {
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


def test_miners_run_without_error(miners, example_prompt):
    """Vérifie que chaque miner s'exécute sans lever d'exception."""
    for task_id, miner in miners.items():
        result = miner.generate_response(example_prompt)
        assert isinstance(result, dict), f"{task_id} doit renvoyer un dict."


def test_miners_output_structure(miners, example_prompt):
    """Vérifie que chaque miner renvoie les champs attendus."""
    for task_id, miner in miners.items():
        result = miner.generate_response(example_prompt)

        assert "task_id" in result
        assert "response" in result
        assert "scores" in result
        assert "global_score" in result

        assert isinstance(result["task_id"], str)
        assert isinstance(result["response"], str)
        assert isinstance(result["scores"], dict)
        assert isinstance(result["global_score"], (int, float))


def test_global_miner(miners, example_prompt):
    """Vérifie que le miner global fonctionne avec les sorties des miners."""
    global_miner = MinerCLGlobal()

    miners_outputs = {
        task_id: miner.generate_response(example_prompt)
        for task_id, miner in miners.items()
    }

    result = global_miner.generate_response(miners_outputs)

    assert "task_id" in result
    assert "response" in result
    assert "scores" in result
    assert "global_score" in result
    assert "inputs_analyzed" in result

    assert isinstance(result["inputs_analyzed"], list)
    assert len(result["inputs_analyzed"]) == len(miners)
