# 📘 UML — CATAR Metamodel (METAMODELE)

**File:** `01-METAMODELE.md`  
**Category:** UML — Conceptual / Structural  
**Version:** 1.0  
**Project:** Corpus‑CATAR  
**Author:** Quatre CATAR  

---

## 📝 Description / Description

**FR —**  
Ce diagramme présente le **métamodèle CATAR**, c’est‑à‑dire la structure conceptuelle fondamentale qui organise l’ensemble du corpus.  
Il définit les entités centrales (Soije, Moije, Invariants T‑XX, Actes de Langage, Processus de Validation, Structures Cognitives) et leurs relations.  
Le métamodèle sert de squelette conceptuel reliant les couches cosmologiques, épistémiques et opérationnelles du système CATAR.

**EN —**  
This diagram presents the **CATAR metamodel**, the fundamental conceptual structure that organizes the entire corpus.  
It defines the core entities (Soije, Moije, T‑XX Invariants, Speech Acts, Validation Processes, Cognitive Structures) and their relationships.  
The metamodel acts as the conceptual backbone linking the cosmological, epistemic, and operational layers of the CATAR system.

---

## 🧩 Diagramme / Diagram

*(Le diagramme existant commence ici.)*

                          
                          +--------------------------------+
                          |        Métamodèle CATAR        |
                          +----------------+---------------+
                                           |
                                           |
                     ------------------------------------------------
                     |                                              |
             +------------------+                         +------------------+
             |   Entité : JEu   |                         | Entité : Monde   |
             | (Sujet cognitif) |                         | (Contexte)       |
             +--------+---------+                         +--------+---------+
                      |                                               |
                      | relation : "agit dans"                        |
                      v                                               v
             +------------------+                         +------------------+
             |  Processus       |                         |  Champs          |
             |  Cognitifs       |                         |  d’Influence     |
             +--------+---------+                         +--------+---------+
                      |                                               |
                      | relation : "génère"                           |
                      v                                               |
             +------------------+                                     |
             |  Actes de        |                                     |
             |  Langage         |                                     |
             +--------+---------+                                     |
                      |                                               |
                      | relation : "évalués par"                      |
                      v                                               |
             +------------------+                                     |
             |  Invariants      |<------------------------------------+
             |  T‑XX            |
             +--------+---------+
                      |
                      | relation : "définissent"
                      v
             +------------------+
             |  Critères        |
             |  Logiques        |
             +--------+---------+
                      |
                      | relation : "implémentés par"
                      v
             +------------------+
             |  Validateurs     |
             |  T‑XX            |
             +--------+---------+
                      |
                      | relation : "produisent"
                      v
             +------------------+
             |  Marqueurs       |
             | (P+, P−, D, C)   |
             +--------+---------+
                      |
                      | relation : "pondérés par"
                      v
             +------------------+
             |  Pondérations    |
             |  (w+, w−, wD, wC)|
             +--------+---------+
                      |
                      | relation : "calculent"
                      v
             +------------------+
             |  Score Brut      |
             +--------+---------+
                      |
                      | relation : "normalisé en"
                      v
             +------------------+
             | Score Normalisé  |
             +--------+---------+
                      |
                      | relation : "agrégé en"
                      v
             +------------------+
             | Benchmark Global |
             +------------------+
