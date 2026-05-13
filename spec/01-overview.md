# CATAR Subnet — Overview

## 1. Purpose of the Subnet
The CATAR subnet evaluates the **coherence**, **stability**, and **self-consistency** of AI-generated text using a universal framework based on:

- invariants T‑XX  
- validateurs T‑XX  
- marqueurs  
- pondérations  
- scoring  
- agrégation  

The subnet provides a **numerical score** and a **structured JSON analysis** for any text.

## 2. High-Level Architecture
The subnet follows a 5‑stage pipeline:

1. **Input**  
   A prompt or text is submitted to the subnet.

2. **Invariant Extraction**  
   The text is analyzed through the CATAR invariants (T‑01 to T‑14).

3. **Validation**  
   Each invariant is evaluated by a dedicated validator.

4. **Scoring**  
   The subnet aggregates all validator outputs into a global score.

5. **Output**  
   A JSON object containing:
   - invariant-level scores  
   - markers  
   - explanations  
   - global CATAR score  

## 3. Why CATAR on Bittensor?
CATAR provides:

- a **universal coherence metric**  
- a **safety layer** for AI systems  
- a **benchmarking tool** for large language models  
- a **shared standard** for evaluating reasoning quality  

The subnet allows miners to contribute high-quality validation and scoring, while validators ensure consistency and reliability.

## 4. Inputs and Outputs
### Input
- text (string)
- optional metadata (language, context, domain)

### Output
A structured JSON object containing:

- invariant-level evaluations  
- markers and explanations  
- normalized scores  
- global CATAR score  
- metadata  

## 5. Core Principles
- **Universality** : CATAR applies to any text, any domain.  
- **Neutrality** : no ideology, no bias, no cultural assumptions.  
- **Transparency** : every score is justified by markers.  
- **Stability** : same input → same score.  
- **Safety** : detects contradictions, hallucinations, incoherence.  

## 6. Components of the Subnet
- **Invariants T‑XX**  
- **Validators**  
- **Scoring Engine**  
- **Benchmark Memory**  
- **API Layer**  

## 7. Dependencies
The subnet relies on:

- the CATAR Corpus  
- the Code MINOU (stabilization protocol)  
- the Dataset CATAR (training + examples)  
- the UML documentation (architecture)  

## 8. Next Sections
The following files describe each component in detail:

- `02-invariants.md`  
- `03-validators.md`  
- `04-scoring.md`  
- `05-api.md`  
- `06-miner-behavior.md`  
- `07-validator-behavior.md`  
- `08-json-format.md`  
- `09-security.md`  
- `10-roadmap.md`
