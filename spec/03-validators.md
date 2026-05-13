# CATAR Subnet — Validators T‑XX

## 1. Purpose of Validators
Validators are the **operational implementation** of the CATAR invariants (T‑01 to T‑14).  
Each validator:

- evaluates one invariant,
- extracts markers,
- applies rules,
- computes a local score,
- produces a structured JSON output.

Validators ensure that the subnet produces **stable**, **neutral**, and **transparent** evaluations.

---

## 2. Validator Architecture

Each validator follows the same internal structure:

1. **Input**
   - the text to evaluate
   - optional metadata (language, context)

2. **Extraction**
   - detection of relevant segments
   - identification of contradictions, ambiguities, hallucinations, etc.

3. **Markers**
   - positive markers (coherence, clarity, pertinence…)
   - negative markers (contradiction, projection, domination…)

4. **Rules**
   - logical rules
   - linguistic rules
   - structural rules
   - safety rules (Code MINOU)

5. **Weighting**
   - each marker has a weight
   - weights differ by invariant

6. **Local Score**
   - normalized score between 0 and 1

7. **Output**
   - JSON object with markers, explanations, and score

---

## 3. List of Validators (T‑01 → T‑14)

### **Validator T‑01 — Cohérence interne**
Detects:
- contradictions,
- inconsistencies,
- incompatible statements.

### **Validator T‑02 — Cohérence externe**
Checks:
- factual plausibility,
- logical compatibility,
- definitional stability.

### **Validator T‑03 — Clarté**
Evaluates:
- readability,
- precision,
- absence of ambiguity.

### **Validator T‑04 — Pertinence**
Measures:
- alignment with the question,
- contextual adequacy.

### **Validator T‑05 — Structure**
Checks:
- organization,
- logical progression,
- hierarchy of ideas.

### **Validator T‑06 — Exhaustivité**
Evaluates:
- coverage of essential elements,
- missing implications.

### **Validator T‑07 — Neutralité**
Detects:
- ideological bias,
- unjustified judgments.

### **Validator T‑08 — Universalité**
Checks:
- generality,
- applicability across contexts.

### **Validator T‑09 — Non‑contradiction**
Strict logical consistency.

### **Validator T‑10 — Non‑hallucination**
Detects:
- invented facts,
- unsupported claims.

### **Validator T‑11 — Non‑projection**
Detects:
- attribution of intentions,
- fabricated motivations.

### **Validator T‑12 — Non‑fascination**
Detects:
- hypnotic style,
- emotional manipulation.

### **Validator T‑13 — Non‑domination**
Detects:
- injunctions,
- directive manipulation.

### **Validator T‑14 — Stabilité Soije/Moije**
Evaluates:
- ontological stability,
- separation of subjective/objective layers.

---

## 4. Validator Output Format

```json
{
  "invariant": "T-XX",
  "score": 0.82,
  "markers_positive": ["coherence_detected", "logical_continuity"],
  "markers_negative": ["minor_ambiguity"],
  "explanation": "The text is mostly coherent with minor issues.",
  "metadata": {
    "language": "fr",
    "length": 124
  }
}
```

---

## 5. Validator Requirements

All validators must:

- be deterministic (same input → same output),
- be neutral (no ideology),
- be transparent (markers must justify the score),
- follow the Code MINOU (non‑projection, non‑domination, non‑fascination),
- avoid hallucination,
- avoid over‑interpretation,
- avoid invention of context.

---

## 6. Interaction with Other Components

- Validators feed the **scoring engine**.
- Validators rely on **invariants** for definitions.
- Validators contribute to the **benchmark memory**.
- Validators expose their results through the **API**.

---

## 7. Next Sections

- `04-scoring.md`  
- `05-api.md`  
- `06-miner-behavior.md`
