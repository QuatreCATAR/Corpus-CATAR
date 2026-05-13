# CATAR Subnet — Validator Behavior

## 1. Purpose of Validators (Network Role)
In the CATAR subnet, **validators** verify the quality, coherence, and determinism of miner outputs.  
They ensure that miners:

- apply all invariants correctly,
- follow the CATAR methodology,
- avoid hallucinations,
- remain neutral and deterministic,
- produce valid JSON outputs.

Validators are the **quality gatekeepers** of the subnet.

---

## 2. Responsibilities of Validators

### **2.1. Receive Miner Output**
Validators receive:
- the miner’s JSON output,
- the original text (optional, depending on network configuration).

### **2.2. Verify JSON Structure**
Validators must check:
- required fields are present,
- invariant scores are valid,
- markers are well‑formed,
- explanations are non‑empty,
- global score is consistent.

### **2.3. Recompute or Revalidate**
Validators must ensure:
- the miner’s invariant scores are plausible,
- markers correspond to the text,
- no hallucination or projection is present,
- the global score matches the weighted aggregation.

Validators may recompute partial evaluations if needed.

### **2.4. Detect Misbehavior**
Validators must detect:
- missing invariants,
- malformed JSON,
- inconsistent scoring,
- ideological bias,
- hallucination,
- over‑interpretation,
- attempts to manipulate the score.

### **2.5. Produce a Validator Score**
Validators assign a score to the miner’s output based on:
- correctness,
- completeness,
- determinism,
- neutrality,
- adherence to CATAR rules.

This score determines miner rewards.

---

## 3. Requirements for Validators

### **3.1. Determinism**
Validators must always produce the same evaluation for the same miner output.

### **3.2. Neutrality**
Validators must:
- avoid ideological interpretation,
- avoid projection,
- avoid domination,
- avoid fascination.

### **3.3. Transparency**
Validators must justify:
- why a miner is rewarded,
- why a miner is penalized.

### **3.4. Safety (Code MINOU)**
Validators must:
- avoid hallucination,
- avoid invention of context,
- avoid over‑interpretation,
- avoid hidden assumptions.

### **3.5. Strict JSON Validation**
Validators must reject:
- malformed JSON,
- missing invariants,
- invalid scores,
- inconsistent weights.

---

## 4. Validator Output Example

```json
{
  "miner_score": 0.76,
  "issues_detected": [
    "T-02 score inconsistent with markers",
    "missing explanation for T-06"
  ],
  "explanation": "The miner output is mostly correct but contains inconsistencies.",
  "metadata": {
    "evaluation_time_ms": 42
  }
}
```

---

## 5. Interaction with Other Components

- Validators check miner outputs against **invariants**.  
- Validators verify the **scoring engine** consistency.  
- Validators contribute to the **benchmark memory**.  
- Validators ensure network‑wide **coherence and stability**.

---

## 6. Next Sections

- `08-json-format.md`  
- `09-security.md`  
- `10-roadmap.md`
