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
