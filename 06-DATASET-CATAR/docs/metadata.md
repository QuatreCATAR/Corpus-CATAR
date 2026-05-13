# 🗂️ CATAR — Documentation du dossier metadata/  
*Version 1.0 — Référence interne*

Le dossier `metadata/` contient les fichiers de définition, de versionnement et de cohérence structurelle du dataset CATAR.  
Il constitue la **source de vérité** pour :

- la structure JSON du dataset  
- les versions du Subnet  
- les informations globales du corpus  
- les contraintes de validation  
- les dépendances internes  

Ce document décrit chaque fichier, son rôle et son usage.

---

# 1. Structure du dossier metadata/

```
metadata/
    schema.json
    dataset-info.json
    version-history.md
    invariants-index.json
```

> Certains fichiers peuvent ne pas encore exister dans ton dépôt :  
> **ce document définit la structure officielle**, que tu pourras compléter progressivement.

---

# 2. schema.json  
### 📐 Schéma JSON global du dataset

Ce fichier définit :

- les champs obligatoires  
- les types  
- les formats  
- les contraintes  
- les relations internes  

Il est utilisé par :

- `validate_dataset.py`  
- les tests unitaires  
- les scripts de génération  
- les outils d’analyse  

### Exemple (simplifié)

```json
{
  "response": { "type": "string" },
  "task_id": { "type": "string" },
  "uuid": { "type": "string", "format": "uuid" },
  "timestamp": { "type": "string", "format": "date-time" }
}
```

---

# 3. dataset-info.json  
### 🧬 Métadonnées globales du dataset

Ce fichier contient :

- le nom du dataset  
- la version  
- la date de génération  
- le nombre total d’entrées  
- les modèles inclus  
- les invariants couverts  
- les statistiques globales  

### Exemple

```json
{
  "dataset_name": "CATAR-DATASET",
  "version": "1.0",
  "generated_on": "2026-05-13",
  "total_entries": 1650,
  "models": ["gpt-4o-mini", "mistral-large"],
  "invariants": ["T-ND", "T-NF", "T-NP", "T-SM", "T-SU"]
}
```

---

# 4. version-history.md  
### 🕰️ Historique des versions du Subnet CATAR

Ce fichier documente :

- les changements majeurs  
- les corrections  
- les ajouts d’invariants  
- les modifications du scoring  
- les évolutions du benchmark  
- les mises à jour du schéma  

### Exemple

```
## v1.0 — 2026-05-13
- Première version stable du dataset
- Ajout des 11 invariants
- Ajout du benchmark v1
- Ajout du schéma JSON global
```

---

# 5. invariants-index.json  
### 🧩 Index global des invariants T‑XX

Ce fichier liste :

- les invariants disponibles  
- leurs niveaux  
- leurs variations  
- leurs chemins dans le dataset  

### Exemple

```json
{
  "T-ND": {
    "levels": 5,
    "variations": 3,
    "path": "prompts/T-ND/"
  }
}
```

---

# 6. Rôle du dossier metadata/

Le dossier `metadata/` garantit :

- la cohérence du dataset  
- la reproductibilité  
- la compatibilité ascendante  
- la validation automatique  
- la documentation interne  

Il est essentiel pour :

- les développeurs  
- les validateurs  
- les outils d’analyse  
- les scripts de génération  

---

# 7. Validation automatique

Pour vérifier la conformité du dataset :

```bash
python tools/validate_dataset.py
```

Ce script :

- charge `schema.json`  
- valide chaque fichier du dataset  
- signale les erreurs  
- empêche les incohérences  

---

# 8. Bonnes pratiques

- toujours mettre à jour `version-history.md`  
- ne jamais modifier `schema.json` sans justification  
- garder `dataset-info.json` synchronisé  
- documenter chaque changement structurel  
- versionner chaque évolution du Subnet  

---

Fin de `metadata.md`.
