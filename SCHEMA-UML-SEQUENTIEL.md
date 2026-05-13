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
