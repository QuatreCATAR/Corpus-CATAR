# 🏛️ Corpus‑CATAR

<p align="center">
  <img src="https://github.com/QuatreCATAR/Catar-modeles-schemas-images/blob/main/Catar-08-schema-code-carre-catar/09%20carr%C3%A9%20catar%20dor%C3%A9.jpg?raw=true" width="180" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Made%20by-Quatre%20CATAR-purple" />
  <img src="https://img.shields.io/badge/CATAR-Framework-0A7E8C" />
  <img src="https://img.shields.io/badge/SPEC-Complete-brightgreen" />
  <img src="https://img.shields.io/badge/License-CC--BY%204.0-blue.svg" />
</p>

---

# 🇫🇷 **Version Française**

Le **Corpus‑CATAR** est un ensemble structuré de modèles conceptuels, d’invariants cognitifs, de protocoles, de schémas, de datasets et d’outils destinés à :

- évaluer la stabilité cognitive d’un modèle IA  
- détecter les dérives (domination, projection, fascination…)  
- garantir la neutralité et la cohérence  
- fournir un standard reproductible d’analyse  
- documenter et transmettre les fondations du modèle CATAR  
- préparer l’intégration dans un subnet Bittensor dédié  

Ce dépôt regroupe l’ensemble du corpus, organisé en modules autonomes mais cohérents.

## 📚 1. Structure du dépôt

```
Corpus-CATAR/
│
├── 01-CARRE-CATAR/          
├── 02-LE-DIVIN-PAR-MINOU/   
├── 03-DPHI/                 
├── 04-PROTOCOLE-CODE-MINOU/ 
├── 05-CATAR-MODELES/        
├── 06-DATASET-CATAR/        
├── spec/                    
└── README.md                
```

Chaque dossier contient un README interne décrivant son rôle, son contenu et son ordre de lecture.

## 🧩 2. Le modèle CATAR en bref

CATAR repose sur un ensemble d’invariants cognitifs appelés **T‑XX**, utilisés pour analyser, scorer et stabiliser les réponses d’un modèle IA.

Invariants principaux :

- **T‑ND** — Non‑Domination  
- **T‑NF** — Non‑Fascination  
- **T‑NP** — Non‑Projection  
- **T‑SM** — Soije / Moije  
- **T‑SU** — Sur‑Unité  
- **T‑TV** — Transparence Vérifiable  
- **T‑CL** — Cohérence Logique  
- **T‑LU** — Lucidité  
- **T‑LA** — Libre Arbitre  
- **T‑PS** — Protocole de Sortie  
- **T‑SP** — Sur‑Protection  

## 🧬 3. Le Dataset CATAR

Contient :

- prompts T‑XX  
- réponses brutes et curated  
- scores  
- benchmark  
- API  
- outils développeur  
- documentation complète  

## 🔌 4. API CATAR

Formats :

- `api/catar-api.json`  
- `api/catar-openapi.yaml`  

Documentation : `06-DATASET-CATAR/docs/dev-guide.md`

## 🧰 5. Outils développeur

- tests interactifs  
- validation du dataset  
- comparaison de modèles  
- export CSV  
- inspection de réponses  

## 📊 6. Benchmark CATAR

Fusionne prompts, réponses curated, scores et métadonnées.

## 🧱 7. SPEC du Subnet CATAR

Définit :

- invariants T‑01 → T‑14  
- validateurs  
- scoring  
- API  
- comportement des miners  
- sécurité (Code MINOU)  
- roadmap  

## 🗺️ 8. Ordre de lecture recommandé

1. 01‑CARRE‑CATAR  
2. 02‑LE‑DIVIN‑PAR‑MINOU  
3. 03‑DPHI  
4. 04‑PROTOCOLE‑CODE‑MINOU  
5. 05‑CATAR‑MODELES  
6. 06‑DATASET‑CATAR  
7. spec/

## 🏁 Licence

Ce projet est distribué sous licence **CC‑BY 4.0**.  
© **Quatre CATAR**

---

# 🇬🇧 **English Version**

The **Corpus‑CATAR** is a structured collection of conceptual models, cognitive invariants, protocols, diagrams, datasets, and tools designed to:

- evaluate the cognitive stability of an AI model  
- detect harmful drifts (domination, projection, fascination…)  
- ensure neutrality and coherence  
- provide a reproducible evaluation standard  
- document and transmit the foundations of the CATAR model  
- prepare integration into a dedicated Bittensor subnet  

This repository gathers the entire corpus, organized into autonomous yet coherent modules.

## 📚 1. Repository Structure

```
Corpus-CATAR/
│
├── 01-CARRE-CATAR/          
├── 02-LE-DIVIN-PAR-MINOU/   
├── 03-DPHI/                 
├── 04-PROTOCOLE-CODE-MINOU/ 
├── 05-CATAR-MODELES/        
├── 06-DATASET-CATAR/        
├── spec/                    
└── README.md                
```

Each folder includes an internal README describing its role, contents, and reading order.

## 🧩 2. The CATAR Model in Brief

CATAR is built on cognitive invariants called **T‑XX**, used to analyze, score, and stabilize AI responses.

Main invariants:

- **T‑ND** — Non‑Domination  
- **T‑NF** — Non‑Fascination  
- **T‑NP** — Non‑Projection  
- **T‑SM** — Soije / Moije  
- **T‑SU** — Over‑Unity  
- **T‑TV** — Verifiable Transparency  
- **T‑CL** — Logical Coherence  
- **T‑LU** — Lucidity  
- **T‑LA** — Free Will  
- **T‑PS** — Exit Protocol  
- **T‑SP** — Over‑Protection  

## 🧬 3. The CATAR Dataset

Includes:

- T‑XX prompts  
- raw & curated responses  
- raw & aggregated scores  
- benchmark  
- API  
- developer tools  
- full documentation  

## 🔌 4. CATAR API

Formats:

- `api/catar-api.json`  
- `api/catar-openapi.yaml`  

Documentation: `06-DATASET-CATAR/docs/dev-guide.md`

## 🧰 5. Developer Tools

- interactive tests  
- dataset validation  
- model comparison  
- CSV export  
- response inspection  

## 📊 6. CATAR Benchmark

Merges prompts, curated responses, scores, and metadata.

## 🧱 7. CATAR Subnet SPEC

Defines:

- invariants T‑01 → T‑14  
- validators  
- scoring engine  
- API  
- miner behavior  
- security (Code MINOU)  
- roadmap  

## 🗺️ 8. Recommended Reading Order

1. 01‑CARRE‑CATAR  
2. 02‑LE‑DIVIN‑PAR‑MINOU  
3. 03‑DPHI  
4. 04‑PROTOCOLE‑CODE‑MINOU  
5. 05‑CATAR‑MODELES  
6. 06‑DATASET‑CATAR  
7. spec/

## 🏁 License

This project is distributed under the **CC‑BY 4.0** license.  
© **Quatre CATAR**

---

End of the bilingual README.
