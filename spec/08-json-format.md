# CATAR Subnet — JSON Output Format

## 1. Purpose of the JSON Format
The CATAR JSON format defines the **standardized structure** used by miners and validators to exchange evaluation data.

It ensures:
- interoperability,
- determinism,
- transparency,
- machine‑readability,
- compatibility with Bittensor.

All miners **must** output this exact structure.  
All validators **must** verify this exact structure.

---

## 2. Top-Level Structure

The JSON output contains:

- global score  
- invariant-level scores  
- markers  
- explanations  
- metadata  

Example:

```json
{
  "global_score": 0.81,
  "invariants": { ... },
  "markers": { ... },
  "metadata": { ... }
}
```

---

## 3. Invariant-Level Structure

Each invariant T‑XX must include:

```json
"T-01": {
  "score": 0.82,
  "markers_positive": ["coherence_detected"],
  "markers_negative": ["minor_inconsistency"],
  "explanation": "The text is mostly coherent."
}
```

### Required fields:
- **score** (float 0 → 1)
- **markers_positive** (array)
- **markers_negative** (array)
- **explanation** (string)

### Optional fields:
- none (strict schema)

---

## 4. Global Markers

Markers aggregated across all invariants:

```json
"markers": {
  "positive": ["coherence_detected", "clarity"],
  "negative": ["minor_inconsistency"]
}
```

Markers must be:
- deterministic,
- justified,
- non‑redundant.

---

## 5. Metadata Block

Metadata describes the evaluation context:

```json
"metadata": {
  "language": "fr",
  "length": 124,
  "timestamp": "2026-05-13T18:42:00Z"
}
```

### Required fields:
- **language** (ISO code)
- **length** (character count)

### Optional fields:
- **timestamp**
- **domain**
- **context**

---

## 6. Full JSON Example

```json
{
  "global_score": 0.81,
  "invariants": {
    "T-01": {
      "score": 0.82,
      "markers_positive": ["coherence_detected"],
      "markers_negative": ["minor_inconsistency"],
      "explanation": "The text is mostly coherent."
    },
    "T-02": {
      "score": 0.74,
      "markers_positive": ["factual_alignment"],
      "markers_negative": ["uncertain_reference"],
      "explanation": "Generally aligned with known facts."
    }
  },
  "markers": {
    "positive": ["coherence_detected", "clarity"],
    "negative": ["minor_inconsistency"]
  },
  "metadata": {
    "language": "fr",
    "length": 124,
    "timestamp": "2026-05-13T18:42:00Z"
  }
}
```

---

## 7. Validation Rules

Validators must reject JSON if:

- a field is missing,
- a score is outside 0 → 1,
- markers are not arrays,
- explanations are empty,
- invariant keys are missing,
- global score is inconsistent with invariant scores.

---

## 8. Next Sections

- `09-security.md`  
- `10-roadmap.md`
