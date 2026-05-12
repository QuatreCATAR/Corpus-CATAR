# test_orchestrator.py — Tests unitaires pour l'orchestrateur CATAR
# Version 1.0

import pytest
from orchestrator import SubnetOrchestrator


@pytest.fixture
def example_prompt():
    return "Ceci est un prompt de test pour l'orchestrateur CATAR."


def test_orchestrator_runs_without_error(example_prompt):
    """L'orchestrateur doit s'exécuter sans lever d'exception."""
    orchestrator = SubnetOrchestrator()
    result = orchestrator.run(example_prompt)

    assert isinstance(result, dict)
    assert "prompt" in result
    assert "miners_outputs" in result
    assert "global_evaluation" in result


def test_orchestrator_miners_outputs_structure(example_prompt):
    """Vérifie que les sorties des miners sont bien structurées."""
    orchestrator = SubnetOrchestrator()
    result = orchestrator.run(example_prompt)

    miners_outputs = result["miners_outputs"]

    assert isinstance(miners_outputs, dict)
    assert len(miners_outputs) == 11  # 11 miners invariants

    for task_id, output in miners_outputs.items():
        assert "task_id" in output
        assert "response" in output
        assert "scores" in output
        assert "global_score" in output


def test_orchestrator_global_evaluation(example_prompt):
    """Vérifie que le miner global fonctionne correctement."""
    orchestrator = SubnetOrchestrator()
    result = orchestrator.run(example_prompt)

    global_eval = result["global_evaluation"]

    assert isinstance(global_eval, dict)
    assert "task_id" in global_eval
    assert "response" in global_eval
    assert "scores" in global_eval
    assert "global_score" in global_eval
    assert "inputs_analyzed" in global_eval

    # Le global miner doit analyser les 11 miners
    assert len(global_eval["inputs_analyzed"]) == 11
