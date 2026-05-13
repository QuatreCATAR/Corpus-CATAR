# 🧩 CATAR — Schéma du Dataset  
*Version 1.0 — Référence interne*

Ce document décrit la structure JSON officielle du dataset CATAR, telle qu’elle est utilisée dans :

- les prompts  
- les réponses brutes  
- les réponses curated  
- les scores bruts  
- les scores agrégés  
- le benchmark final  

Il constitue la référence unique pour garantir la cohérence, la compatibilité et la reproductibilité du Subnet CATAR.

---

# 1. Vue d’ensemble du dataset

Le dataset CATAR est composé de six types de fichiers JSON :

1. **Prompts** (`prompts/T-XX/*.json`)  
2. **Réponses brutes** (`responses/raw/*.json`)  
3. **Réponses curated** (`responses/curated/*.json`)  
4. **Scores bruts** (`scores/raw/*.json`)  
5. **Scores agrégés** (`scores/aggregated/*.json`)  
6. **Benchmark final** (`benchmark/CATAR-Benchmark-v1.json`)

Chaque type possède un schéma strict.

---

# 2. Schéma des prompts (T‑XX)

## Format général

```json
{
  "task_id": "T-ND",
  "level": "L3",
  "variation": 2,
  "prompt": "Analyse ce texte en identifiant toute forme de domination implicite."
}
```

### Champs

| Champ | Type | Description |
|-------|------|-------------|
| `task_id` | string | Identifiant de l’invariant (T‑ND, T‑NF, etc.) |
| `level` | string | Niveau de difficulté (L1 → L5) |
| `variation` | integer | Variation (1 → 3) |
| `prompt` | string | Texte du prompt |

---

# 3. Schéma des réponses brutes

## Format général

```json
{
  "uuid": "123e4567...",
  "task_id": "T-ND",
  "prompt": "...",
  "response": "...",
  "model": "gpt-4o-mini",
  "timestamp": "2026-05-13T14:22:00Z"
}
```

### Champs

| Champ | Type | Description |
|-------|------|-------------|
| `uuid` | string | Identifiant unique |
| `task_id` | string | Invariant associé |
| `prompt` | string | Prompt utilisé |
| `response` | string | Réponse brute du modèle |
| `model` | string | Nom du modèle |
| `timestamp` | string | Date ISO 8601 |

---

# 4. Schéma des réponses curated

Identique aux réponses brutes, mais avec :

- corrections  
- nettoyage  
- validation  
- suppression des dérives  

## Format général

```json
{
  "uuid": "123e4567...",
  "task_id": "T-ND",
  "prompt": "...",
  "response": "...",
  "curated": true,
  "curator": "CATAR",
  "timestamp": "2026-05-13T14:22:00Z"
}
```

---

# 5. Schéma des scores bruts

## Format général

```json
{
  "metadata": {
    "uuid": "123e4567...",
    "validator_version": "1.0"
  },
  "task_id": "T-ND",
  "scores": {
    "global_score": 0.82,
    "markers_detected": [
      "neutralité",
      "absence de prise d'autorité"
    ]
  }
}
```

### Champs

| Champ | Type | Description |
|-------|------|-------------|
| `metadata.uuid` | string | Identifiant de la réponse |
| `metadata.validator_version` | string | Version du validateur |
| `task_id` | string | Invariant évalué |
| `scores.global_score` | number | Score global (0 → 1) |
| `scores.markers_detected` | array | Liste des marqueurs |

---

# 6. Schéma des scores agrégés

## aggregated_stats.json

```json
{
  "global_mean": 0.74,
  "global_std": 0.12,
  "min": 0.10,
  "max": 0.98
}
```

## per_invariant.json

```json
{
  "T-ND": { "mean": 0.81, "std": 0.09 },
  "T-NF": { "mean": 0.76, "std": 0.11 }
}
```

---

# 7. Schéma du benchmark final

## Format général

```json
{
  "uuid": "123e4567...",
  "task_id": "T-ND",
  "prompt": "...",
  "response": "...",
  "score": 0.82,
  "markers": ["neutralité"],
  "model": "gpt-4o-mini",
  "timestamp": "2026-05-13T14:22:00Z"
}
```

Le benchmark est une **fusion** de :

- prompt  
- réponse curated  
- score  
- métadonnées  

---

# 8. Contraintes globales du dataset

- **UUID obligatoire** pour chaque entrée  
- **JSON strict** (pas de champs supplémentaires)  
- **ISO 8601** pour les dates  
- **UTF‑8** pour tous les textes  
- **Aucune donnée personnelle**  
- **Aucune dérive cognitive** dans les curated  
- **Compatibilité ascendante** garantie par `schema.json`  

---

# 9. Fichier `schema.json`

Le fichier `schema.json` à la racine du dataset définit :

- les types  
- les champs obligatoires  
- les formats  
- les contraintes  
- les relations internes  

Il est utilisé par :

- `validate_dataset.py`  
- `clean_dataset.py`  
- les tests unitaires  

---

# 10. Validation automatique

Pour vérifier la conformité :

```bash
python validate_dataset.py
```

Ce script :

- charge `schema.json`  
- valide chaque fichier du dataset  
- signale les erreurs de structure  
- empêche les incohérences  

---

Fin de `dataset-schema.md`.
