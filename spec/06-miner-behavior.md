# CATAR Subnet — Miner Behavior

## 1. Purpose of Miners
Miners in the CATAR subnet are responsible for producing **high‑quality evaluations** of text using:

- the invariants T‑01 → T‑14,
- the validators,
- the scoring engine,
- the CATAR JSON format.

Miners must be **deterministic**, **neutral**, and **transparent**.

---

## 2. Responsibilities of Miners

### **2.1. Receive Input**
Miners receive:
- a text to evaluate,
- optional metadata (language, context).

### **2.2. Run All Validators**
Miners must execute **all 14 validators**:

- T‑01 Cohérence interne  
- T‑02 Cohérence externe  
- T‑03 Clarté  
- T‑04 Pertinence  
- T‑05 Structure  
- T‑06 Exhaustivité  
- T‑07 Neutralité  
- T‑08 Universalité  
- T‑09 Non‑contradiction  
- T‑10 Non‑hallucination  
- T‑11 Non‑projection  
- T‑12 Non‑fascination  
- T‑13 Non‑domination  
- T‑14 Stabilité Soije/Moije  

### **2.3. Produce Markers**
Each validator must output:
- positive markers,
- negative markers,
- explanations.

### **2.4. Compute Local Scores**
Each validator computes a normalized score (0 → 1).

### **2.5. Aggregate Scores**
Miners must apply the CATAR scoring engine to produce:
- invariant-level scores,
- global score,
- markers,
- explanations.

### **2.6. Return JSON Output**
Miners return a structured JSON object (see `08-json-format.md`).

---

## 3. Requirements for Miners

### **3.1. Determinism**
Same input → same output.  
No randomness allowed.

### **3.2. Neutrality**
Miners must:
- avoid ideological bias,
- avoid projection,
- avoid domination,
- avoid fascination.

### **3.3. Transparency**
Every score must be justified by markers.

### **3.4. Safety (Code MINOU)**
Miners must:
- avoid hallucination,
- avoid invention of context,
- avoid over‑interpretation,
- avoid hidden assumptions.

### **3.5. Performance**
Miners must respond within the time constraints of the Bittensor network.

---

## 4. Miner Output Example

```json
{
  "global_score": 0.81,
  "invariants": {
    "T-01": { "score": 0.82, "markers_positive": [...], "markers_negative": [...], "explanation": "..." },
    "T-02": { "score": 0.74, "markers_positive": [...], "markers_negative": [...], "explanation": "..." }
  },
  "markers": {
    "positive": ["coherence_detected", "clarity"],
    "negative": ["minor_inconsistency"]
  },
  "metadata": {
    "language": "fr",
    "length": 124
  }
}
```

---

## 5. Interaction with Other Components

- Miners use **validators** to compute invariant scores.  
- Miners use the **scoring engine** to compute the global score.  
- Miners send results to **validators (network role)** for verification.  
- Miners contribute to the **benchmark memory**.

---

## 6. Next Sections

- `07-validator-behavior.md`  
- `08-json-format.md`  
- `09-security.md`
