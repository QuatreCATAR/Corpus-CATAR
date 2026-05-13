# CATAR Subnet — Scoring Engine

## 1. Purpose of the Scoring Engine
The scoring engine aggregates the outputs of all validators (T‑01 to T‑14) into a single, normalized CATAR score.

The score reflects:
- coherence,
- stability,
- neutrality,
- non‑hallucination,
- structural integrity.

It is deterministic and fully explainable.

---

## 2. Inputs to the Scoring Engine

The scoring engine receives a list of validator outputs:

```json
[
  {
    "invariant": "T-01",
    "score": 0.82,
    "markers_positive": [...],
    "markers_negative": [...],
    "explanation": "..."
  },
  {
    "invariant": "T-02",
    "score": 0.74,
    "markers_positive": [...],
    "markers_negative": [...],
    "explanation": "..."
  }
]
```

Each validator contributes:
- a local score,
- markers,
- explanations.

---

## 3. Weighting System

Each invariant T‑XX has a weight **wXX**.

Example (illustrative only):
- T‑01 (cohérence interne): w = 1.2  
- T‑10 (non‑hallucination): w = 1.5  
- T‑14 (stabilité Soije/Moije): w = 1.3  
- autres invariants: w = 1.0  

Weights ensure that critical invariants have stronger influence.

Weights are:
- fixed,
- transparent,
- documented,
- identical for all miners and validators.

---

## 4. Aggregation Formula

The global CATAR score is computed as:



\[
Score_{CATAR} = \frac{\sum_{i=1}^{14} (score_i \cdot w_i)}{\sum_{i=1}^{14} w_i}
\]



Where:
- \( score_i \) = local score of invariant T‑i  
- \( w_i \) = weight of invariant T‑i  

The result is normalized between **0** and **1**.

---

## 5. Marker-Based Adjustments

Markers influence the score through:
- bonuses (coherence, clarity, pertinence…)
- penalties (contradiction, hallucination, domination…)

Adjustments are:
- bounded,
- deterministic,
- documented.

No validator can arbitrarily inflate or deflate the score.

---

## 6. Output Format

The scoring engine returns:

```json
{
  "global_score": 0.81,
  "invariant_scores": {
    "T-01": 0.82,
    "T-02": 0.74,
    "T-03": 0.91,
    ...
  },
  "weights": {
    "T-01": 1.2,
    "T-02": 1.0,
    ...
  },
  "markers": {
    "positive": [...],
    "negative": [...]
  },
  "explanation": "The text is coherent, mostly factual, with minor structural issues."
}
```

---

## 7. Requirements for Scoring

The scoring engine must:
- be deterministic,
- be transparent,
- justify every score with markers,
- avoid hallucination,
- avoid over‑interpretation,
- follow the Code MINOU.

---

## 8. Interaction with Other Components

- Receives data from **validators**  
- Sends results to the **API**  
- Contributes to the **benchmark memory**  
- Ensures consistency across miners  

---

## 9. Next Sections

- `05-api.md`  
- `06-miner-behavior.md`  
- `07-validator-behavior.md`
