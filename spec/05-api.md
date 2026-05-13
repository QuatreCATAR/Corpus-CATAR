# CATAR Subnet — API Specification

## 1. Purpose of the API
The CATAR API exposes the subnet’s evaluation capabilities to external clients.  
It allows users, miners, and validators to submit text and receive:

- invariant-level scores,
- markers,
- explanations,
- global CATAR score,
- metadata.

The API is deterministic and fully transparent.

---

## 2. Main Endpoint

### **POST /evaluate**

Submits a text for CATAR evaluation.

#### Request Body

```json
{
  "text": "Your text here...",
  "language": "fr",
  "metadata": {
    "domain": "general",
    "context": "optional"
  }
}
```

#### Required Fields
- **text** (string): the content to evaluate.

#### Optional Fields
- **language**: ISO code (default: auto-detected)
- **metadata**: any contextual information

---

## 3. Response Format

The API returns a structured JSON object:

```json
{
  "global_score": 0.81,
  "invariants": {
    "T-01": {
      "score": 0.82,
      "markers_positive": ["coherence_detected"],
      "markers_negative": ["minor_inconsistency"],
      "explanation": "Mostly coherent with minor issues."
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
    "length": 124
  }
}
```

---

## 4. Error Handling

### **400 — Bad Request**
Missing or invalid fields.

```json
{
  "error": "Invalid request: 'text' field is required."
}
```

### **500 — Internal Error**
Unexpected failure.

```json
{
  "error": "Internal evaluation error."
}
```

---

## 5. Determinism Requirements

The API must always return:
- the same score for the same input,
- the same markers,
- the same explanations.

No randomness is allowed.

---

## 6. Rate Limits

Rate limits are defined by the Bittensor network and apply uniformly to all clients.

---

## 7. Interaction with Other Components

- Uses **validators** to compute invariant scores  
- Uses **scoring engine** to compute global score  
- Logs results into **benchmark memory**  
- Exposes results to miners and validators  

---

## 8. Next Sections

- `06-miner-behavior.md`  
- `07-validator-behavior.md`  
- `08-json-format.md`
