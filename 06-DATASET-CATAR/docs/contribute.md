# 🤝 CATAR — Guide de contribution  
*Version 1.0 — Référence interne*

Ce document décrit les règles, conventions et bonnes pratiques pour contribuer au Subnet CATAR.  
Il s’adresse aux développeurs, chercheurs, curateurs et mainteneurs souhaitant :

- ajouter des invariants  
- ajouter des modèles  
- améliorer les validateurs  
- enrichir le dataset  
- corriger des erreurs  
- proposer des évolutions  

---

# 1. Principes fondamentaux

Toute contribution doit respecter :

- **la neutralité**  
- **la cohérence logique**  
- **la transparence**  
- **la non‑domination**  
- **la non‑projection**  
- **la non‑fascination**  
- **le protocole de sortie**  

Ces principes sont **non négociables** et définissent l’intégrité du Subnet CATAR.

---

# 2. Workflow de contribution

## Étapes standard

1. **Fork** du dépôt  
2. Créer une branche dédiée :  
   ```
   git checkout -b feature/nom-de-la-feature
   ```
3. Faire les modifications  
4. Ajouter les tests (si applicable)  
5. Mettre à jour la documentation  
6. Mettre à jour `version-history.md`  
7. Ouvrir une Pull Request claire et détaillée  

---

# 3. Ajouter un invariant T‑XX

## Étapes

1. Créer un dossier dans `prompts/` :  
   ```
   prompts/T-XX/
   ```
2. Ajouter **15 prompts** (5 niveaux × 3 variations)  
3. Ajouter la logique du validateur dans `validators/`  
4. Ajouter les marqueurs positifs/négatifs  
5. Ajouter les tests unitaires  
6. Mettre à jour :  
   - `invariants-index.json`  
   - `dataset-schema.md`  
   - `validators.md`  
7. Générer un dataset partiel pour validation  
8. Mettre à jour le benchmark  

---

# 4. Ajouter un modèle IA

## Étapes

1. Ajouter son wrapper dans `generate_dataset.py`  
2. Tester via `tools/test_interactif.py`  
3. Générer un dataset partiel :  
   ```
   python generate_dataset.py --model nouveau-modele
   ```
4. Scorer les réponses :  
   ```
   python score_responses.py
   ```
5. Curater les réponses  
6. Ajouter au benchmark  
7. Comparer avec les modèles existants :  
   ```
   python tools/compare_models.py
   ```

---

# 5. Modifier un validateur

## Règles strictes

- ne jamais supprimer un marqueur sans justification  
- ne jamais modifier un poids sans recalibrage global  
- documenter chaque changement dans `validators.md`  
- mettre à jour `version-history.md`  
- vérifier la compatibilité avec les autres invariants  
- exécuter les tests unitaires  

---

# 6. Modifier le scoring

Toute modification du scoring doit :

- être documentée dans `scoring.md`  
- être testée sur un dataset complet  
- être validée par au moins un autre mainteneur  
- être rétrocompatible autant que possible  

---

# 7. Ajouter ou modifier des prompts

## Règles

- respecter la structure T‑XX  
- respecter les niveaux L1 → L5  
- respecter les variations 1 → 3  
- éviter toute ambiguïté  
- éviter toute projection ou suggestion  
- tester via `test_interactif.py`  

---

# 8. Ajouter des réponses curated

## Règles

- aucune dérive cognitive  
- aucune domination  
- aucune projection  
- aucune fascination  
- cohérence logique obligatoire  
- protocole de sortie obligatoire  
- justification claire si modification d’une réponse brute  

---

# 9. Ajouter des scripts dans tools/

## Règles

- nom explicite  
- documentation interne  
- sortie lisible (JSON ou tableau)  
- compatibilité avec `schema.json`  
- pas de dépendances externes non listées  

---

# 10. Tests unitaires

Chaque contribution doit inclure :

- tests positifs  
- tests négatifs  
- tests limites  
- tests de cohérence  

Les tests doivent être reproductibles et indépendants.

---

# 11. Style et conventions

- JSON strict  
- indentation 2 espaces  
- noms explicites  
- pas de données personnelles  
- pas de contenu sensible  
- commentaires clairs et concis  

---

# 12. Pull Requests

Une PR doit contenir :

- description claire  
- justification  
- fichiers modifiés  
- tests associés  
- mise à jour de la documentation  
- mise à jour de `version-history.md`  

---

# 13. Code of Conduct

Les contributeurs doivent :

- respecter les autres  
- éviter les conflits inutiles  
- privilégier la clarté  
- documenter leurs choix  
- maintenir la cohérence du Subnet  

---

Fin de `contribute.md`.
