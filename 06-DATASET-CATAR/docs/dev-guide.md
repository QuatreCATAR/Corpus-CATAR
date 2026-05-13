# 📚 CATAR — Developer Guide (version complète)

Ce document est la référence officielle pour les développeurs intégrant, étendant ou maintenant le Subnet CATAR.

---

# 1. Introduction

CATAR est un Subnet d’évaluation cognitive basé sur 11 invariants fondamentaux.  
Il fournit :

- un dataset structuré  
- une API d’évaluation  
- un benchmark reproductible  
- des outils de test et d’analyse  

---

# 2. Architecture générale

```
prompts → responses/raw → scores/raw → responses/curated → scores/aggregated → benchmark
```

Composants :

- **Prompts T‑XX** : situations types  
- **Responses** : brutes puis curated  
- **Scores** : bruts puis agrégés  
- **Benchmark** : fusion finale  
- **API** : interface d’accès  
- **Tools** : scripts utilitaires  
- **Docs** : documentation  

---

# 3. Les invariants CATAR (T‑XX)

- T‑ND — Non‑Domination  
- T‑NF — Non‑Fascination  
- T‑NP — Non‑Projection  
- T‑SM — Soije/Moije  
- T‑SU — Sur‑Unité  
- T‑TV — Transparence Vérifiable  
- T‑CL — Cohérence Logique  
- T‑LU — Lucidité  
- T‑LA — Libre Arbitre  
- T‑PS — Protocole de Sortie  
- T‑SP — Sur‑Protection  

Chaque invariant possède :

- 5 niveaux  
- 3 variations  
- un format JSON strict  

---

# 4. API CATAR

## 4.1 Endpoints principaux

### Générer une réponse
```
POST /catar/generate
```

### Scorer une réponse
```
POST /catar/score
```

### Statistiques globales
```
GET /catar/stats
```

### Récupérer un prompt
```
GET /catar/prompt/{task}/{level}/{variation}
```

## 4.2 Formats disponibles
- `api/catar-api.json` (simple)
- `api/catar-openapi.yaml` (OpenAPI 3.1)

---

# 5. Scripts principaux

### Générer le dataset
```bash
python generate_dataset.py
```

### Scorer les réponses
```bash
python score_responses.py
```

### Curater les réponses
```bash
python curate_responses.py
```

### Agréger les scores
```bash
python aggregate_scores.py
```

### Construire le benchmark
```bash
python benchmark/build_benchmark.py
```

---

# 6. Script interactif

Situé dans :
```
tools/test_interactif.py
```

Fonctionnalités :

- choix d’un invariant  
- récupération d’un prompt  
- saisie d’une réponse  
- scoring en direct  
- affichage des marqueurs  

---

# 7. Ajouter un nouvel invariant

1. Créer un dossier dans `prompts/`  
2. Ajouter 5 niveaux × 3 variations  
3. Mettre à jour `schema.json` si nécessaire  
4. Ajouter la logique dans le validateur  
5. Ajouter les tests  
6. Mettre à jour le benchmark  

---

# 8. Ajouter un nouveau modèle

1. Ajouter son nom dans `generate_dataset.py`  
2. Définir son wrapper d’appel  
3. Tester via `test_interactif.py`  
4. Générer un dataset partiel  
5. Comparer via `compare_models.py`  

---

# 9. Conventions

- UUID pour chaque sample  
- JSON strict  
- Pas de données personnelles  
- Neutralité obligatoire  
- Transparence totale  

---

# 10. Contribution

- Fork  
- Branche `feature/...`  
- PR avec description claire  
- Tests obligatoires  
- Mise à jour du changelog  

---

# 11. Roadmap

- CATAR‑Benchmark v2  
- API REST complète  
- Dashboard interactif  
- Support multi‑modèles  
- Export HuggingFace  

---

# 12. Licence

MIT (ou autre selon ton choix)

---

Fin du Dev‑Guide complet.
