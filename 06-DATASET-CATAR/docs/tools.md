# 🧰 CATAR — Documentation des outils (tools/)  
*Version 1.0 — Référence interne*

Le dossier `tools/` contient les scripts utilitaires destinés aux développeurs, testeurs et intégrateurs du Subnet CATAR.  
Ces outils facilitent :

- le test manuel  
- la validation du dataset  
- la comparaison de modèles  
- l’inspection des réponses  
- la génération de rapports  

Ce document décrit chaque outil, son rôle, son fonctionnement et son usage.

---

# 1. Structure du dossier tools/

```
tools/
    test_interactif.py
    validate_dataset.py
    inspect_response.py
    compare_models.py
    export_csv.py
    utils.py
```

> Certains scripts peuvent ne pas encore exister dans ton dépôt :  
> **ce document définit la structure officielle**, que tu pourras compléter progressivement.

---

# 2. test_interactif.py  
### 🎮 Test manuel interactif

Script permettant de :

- choisir un invariant T‑XX  
- récupérer un prompt via l’API  
- saisir une réponse (humaine ou modèle)  
- obtenir un score CATAR en direct  
- afficher les marqueurs détectés  

### Usage

```bash
python tools/test_interactif.py
```

### Fonctionnalités

- sélection interactive  
- affichage du prompt  
- scoring en direct  
- JSON formaté  
- idéal pour les démonstrations et le debug

---

# 3. validate_dataset.py  
### ✔️ Validation structurelle du dataset

Ce script vérifie que :

- tous les fichiers JSON respectent `schema.json`  
- les champs obligatoires sont présents  
- les types sont corrects  
- les UUID sont valides  
- les dates sont au format ISO  
- aucune dérive n’est présente dans les curated  

### Usage

```bash
python tools/validate_dataset.py
```

### Sorties

- liste des erreurs  
- rapport de conformité  
- statut global (OK / FAIL)

---

# 4. inspect_response.py  
### 🔍 Inspection d’une réponse spécifique

Permet de charger une réponse (raw ou curated) et d’afficher :

- le prompt  
- la réponse  
- les marqueurs  
- le score  
- les métadonnées  

### Usage

```bash
python tools/inspect_response.py <uuid>
```

### Fonctionnalités

- inspection rapide  
- utile pour le debug  
- idéal pour analyser une dérive

---

# 5. compare_models.py  
### ⚖️ Comparaison de modèles IA

Permet de comparer :

- deux modèles  
- un modèle vs. benchmark global  
- plusieurs modèles en parallèle  

### Usage

```bash
python tools/compare_models.py --models gpt-4o-mini mistral-large deepseek-v3
```

### Sorties

- tableau comparatif  
- scores moyens  
- écarts‑types  
- marqueurs dominants  
- figures (si activé)

---

# 6. export_csv.py  
### 📤 Export du benchmark en CSV

Permet d’exporter :

- uuid  
- task_id  
- prompt  
- réponse  
- score  
- modèle  
- marqueurs  

### Usage

```bash
python tools/export_csv.py
```

### Sortie

```
benchmark/catar-benchmark.csv
```

---

# 7. utils.py  
### 🧱 Fonctions utilitaires internes

Contient :

- chargement JSON  
- validation UUID  
- normalisation des champs  
- fonctions de logging  
- wrappers API  

Ce fichier est utilisé par la majorité des scripts du dossier `tools/`.

---

# 8. Bonnes pratiques pour tools/

- chaque script doit être **documenté**  
- chaque script doit être **idempotent**  
- aucune dépendance externe non listée dans `requirements.txt`  
- sortie toujours **lisible** (JSON ou tableau)  
- pas de modification du dataset sans confirmation explicite  
- compatibilité avec `schema.json` obligatoire  

---

# 9. Roadmap tools/

- `generate_report.py` (rapport PDF/Markdown)  
- `detect_anomalies.py` (détection automatique de dérives)  
- `model_wrapper.py` (intégration multi‑modèles)  
- `stress_test.py` (tests massifs)  

---

Fin de `tools.md`.
