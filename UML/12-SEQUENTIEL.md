 # 📘 UML — Sequential Diagram of the CATAR Pipeline (SEQUENTIEL)

**File:** `12-SEQUENTIEL.md`  
**Category:** UML — Sequential / Execution Flow  
**Version:** 1.0  
**Project:** Corpus‑CATAR  
**Author:** Quatre CATAR  

---

## 📝 Description / Description

**FR —**  
Ce diagramme représente le **flux séquentiel complet du pipeline CATAR**, en détaillant l’ordre exact des interactions entre les différents participants :  
- l’Utilisateur  
- le module « Prompts T‑XX »  
- le Modèle IA  
- les réponses brutes (RAW)  
- les réponses curated  
- les validateurs T‑XX  
- le module de scoring  
- les scores agrégés  
- le benchmark final  

Chaque étape du diagramme correspond à une action explicitement visible dans le fichier, par exemple :  
- *Sélection d’un invariant T‑XX*   
- *Envoi du prompt au modèle IA*   
- *Génération de la réponse brute*   
- *Nettoyage / stabilisation*   
- *Passage dans le validateur T‑XX*   
- *Détection des marqueurs + score brut*   
- *Agrégation statistique*   
- *Fusion finale dans le benchmark*   

Ce diagramme constitue la **représentation la plus précise de l’ordre d’exécution** du Subnet CATAR.

**EN —**  
This diagram represents the **full sequential flow of the CATAR pipeline**, detailing the exact order of interactions between the different participants:  
- the User  
- the “Prompts T‑XX” module  
- the AI Model  
- raw responses  
- curated responses  
- T‑XX validators  
- the scoring module  
- aggregated scores  
- the final benchmark  

Each step corresponds to an action explicitly visible in the file, such as:  
- *Selection of a T‑XX invariant*   
- *Sending the prompt to the AI model*   
- *Generation of the raw response*   
- *Cleaning / stabilization*   
- *Passing through the T‑XX validator*   
- *Marker detection + raw score*   
- *Statistical aggregation*   
- *Final fusion into the benchmark*   

This diagram provides the **most precise representation of the execution order** of the CATAR Subnet.

---

## 🧩 Diagramme / Diagram

*(The existing diagram begins here.)*


Participant Utilisateur
Participant "Prompts T‑XX"
Participant "Modèle IA"
Participant "Responses RAW"
Participant "Responses Curated"
Participant "Validateurs T‑XX"
Participant "Scoring"
Participant "Scores Agrégés"
Participant "Benchmark"

Utilisateur -> "Prompts T‑XX": 1. Sélection d’un invariant T‑XX
"Prompts T‑XX" -> Utilisateur: Prompt généré (niveau + variation)

Utilisateur -> "Modèle IA": 2. Envoi du prompt
"Modèle IA" -> "Responses RAW": 3. Génération de la réponse brute

"Responses RAW" -> "Responses Curated": 4. Nettoyage / stabilisation

"Responses Curated" -> "Validateurs T‑XX": 5. Passage dans le validateur
"Validateurs T‑XX" -> "Scoring": 6. Détection des marqueurs + score brut

"Scoring" -> "Scores Agrégés": 7. Agrégation statistique
"Scores Agrégés" -> "Benchmark": 8. Fusion finale (prompt + réponse + score)

"Benchmark" -> Utilisateur: 9. Résultats + visualisations
