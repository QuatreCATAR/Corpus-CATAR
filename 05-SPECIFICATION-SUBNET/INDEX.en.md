# 🧭 INDEX — CATAR Subnet

This file lists all **CATAR invariants** and provides direct links to their corresponding modules:
- **Miners** → response generation  
- **Validators** → evaluation and scoring  
- **Prompts** → metadata and instructions  
- **Tests** → unit verification  

---

## ⚙️ CATAR Invariants

| Invariant | Description | Miner | Validator | Prompt | Test |
|-----------|-------------|--------|-----------|--------|------|
| **T‑CL** | Logical Coherence | [`M‑CL.py`](miners/M-CL.py) | [`V‑CL.py`](validators/V-CL.py) | [`T‑CL.json`](prompts/T-CL.json) | [`test_orchestrator.py`](tests/test_orchestrator.py) |
| **T‑LA** | Free Will | [`M‑LA.py`](miners/M-LA.py) | [`V‑LA.py`](validators/V-LA.py) | [`T‑LA.json`](prompts/T-LA.json) | [`test_validators.py`](tests/test_validators.py) |
| **T‑LU** | Lucidity | [`M‑LU.py`](miners/M-LU.py) | [`V‑LU.py`](validators/V-LU.py) | [`T‑LU.json`](prompts/T-LU.json) | [`test_validators.py`](tests/test_validators.py) |
| **T‑ND** | Non‑Domination | [`M‑ND.py`](miners/M-ND.py) | [`V‑ND.py`](validators/V-ND.py) | [`T‑ND.json`](prompts/T-ND.json) | [`test_miners.py`](tests/test_miners.py) |
| **T‑NF** | Non‑Fascination | [`M‑NF.py`](miners/M-NF.py) | [`V‑NF.py`](validators/V-NF.py) | [`T‑NF.json`](prompts/T-NF.json) | [`test_miners.py`](tests/test_miners.py) |
| **T‑NP** | Non‑Projection | [`M‑NP.py`](miners/M-NP.py) | [`V‑NP.py`](validators/V-NP.py) | [`T‑NP.json`](prompts/T-NP.json) | [`test_miners.py`](tests/test_miners.py) |
| **T‑PS** | Exit Protocol | [`M‑PS.py`](miners/M-PS.py) | [`V‑PS.py`](validators/V-PS.py) | [`T‑PS.json`](prompts/T-PS.json) | [`test_orchestrator.py`](tests/test_orchestrator.py) |
| **T‑SM** | Soije / Moije | [`M‑SM.py`](miners/M-SM.py) | [`V‑SM.py`](validators/V-SM.py) | [`T‑SM.json`](prompts/T-SM.json) | [`test_validators.py`](tests/test_validators.py) |
| **T‑SP** | Over‑Protection | [`M‑SP.py`](miners/M-SP.py) | [`V‑SP.py`](validators/V-SP.py) | [`T‑SP.json`](prompts/T-SP.json) | [`test_validators.py`](tests/test_validators.py) |
| **T‑SU** | Over‑Unity | [`M‑SU.py`](miners/M-SU.py) | [`V‑SU.py`](validators/V-SU.py) | [`T‑SU.json`](prompts/T-SU.json) | [`test_validators.py`](tests/test_validators.py) |
| **T‑TV** | Verifiable Transparency | [`M‑TV.py`](miners/M-TV.py) | [`V‑TV.py`](validators/V-TV.py) | [`T‑TV.json`](prompts/T-TV.json) | [`test_validators.py`](tests/test_validators.py) |

---

## 📘 Reference Files

- [`01‑Invariants‑CATAR.md`](01-Invariants-CATAR.md)  
- [`02‑Evaluation‑Criteria.md`](02-Criteres-Evaluation.md)  
- [`03‑Subnet‑Tasks.md`](03-Taches-Subnet.md)  
- [`04‑Mandatory‑Safeguards.md`](04-Gardefous-Obligatoires.md)  
- [`SPECIFICATION‑COMPLETE‑SUBNET‑CATAR.md`](SPECIFICATION-COMPLETE-SUBNET-CATAR.md)  
- [`SPECIFICATION‑TECHNIQUE‑v1.1.md`](SPECIFICATION-TECHNIQUE-v1.1.md)  
- [`orchestrator.py`](orchestrator.py)

---

## 🧠 Notes

- **Miners** and **validators** are symmetrical: each invariant has a generation module and a validation module.  
- **Prompt JSON files** contain metadata and instructions for each invariant.  
- **Tests** ensure stability and coherence of the CATAR pipeline.  
- The **orchestrator** coordinates all modules to produce the global Subnet analysis.

---

© **Quatre CATAR** — Official documentation of the CATAR Subnet.
