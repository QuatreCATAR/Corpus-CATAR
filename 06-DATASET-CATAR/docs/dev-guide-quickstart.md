# 🚀 CATAR — Dev Guide Quickstart

Ce guide fournit une vue rapide et opérationnelle pour utiliser, tester et intégrer le Subnet CATAR.

---

## 1. Installer le Subnet CATAR
- Cloner le dépôt
- Installer Python 3.10+
- Installer les dépendances :
```bash
pip install -r requirements.txt
```

---

## 2. Structure essentielle
```
06-DATASET-CATAR/
    prompts/        → Prompts T‑XX
    responses/      → Réponses brutes + curated
    scores/         → Scores bruts + agrégés
    benchmark/      → Benchmark + figures
    api/            → API JSON + OpenAPI
    tools/          → Scripts utilitaires
    docs/           → Documentation
```

---

## 3. Générer une réponse CATAR
Utiliser l’API :

```bash
POST /catar/generate
```

Payload minimal :
```json
{
  "task_id": "T-ND",
  "prompt": "Analyse ce texte...",
  "model": "gpt-4o-mini"
}
```

---

## 4. Scorer une réponse
```bash
POST /catar/score
```

Payload :
```json
{
  "task_id": "T-ND",
  "response": "..."
}
```

---

## 5. Tester manuellement (script interactif)
```bash
python tools/test_interactif.py
```

Fonctionnalités :
- choix d’un invariant  
- récupération d’un prompt  
- saisie d’une réponse  
- scoring en direct  

---

## 6. Générer le dataset complet
```bash
python generate_dataset.py
```

---

## 7. Agréger les scores
```bash
python aggregate_scores.py
```

---

## 8. Construire le benchmark
```bash
python benchmark/build_benchmark.py
```

---

## 9. Visualiser les résultats
```bash
python benchmark/visualize_benchmark.py
```

---

## 10. Endpoints essentiels de l’API
- `/catar/generate`  
- `/catar/score`  
- `/catar/stats`  
- `/catar/prompt/{task}/{level}/{variation}`

---

**Quickstart terminé.**  
Pour les détails complets, voir `dev-guide.md`.
