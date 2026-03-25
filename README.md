# BLT Preflight – RAG Demo

This repository contains two implementations demonstrating how security documentation can be queried interactively to provide contextual guidance for contributors.

The goal is to show how contributor tools like **Preflight** could provide contextual security guidance by retrieving relevant information from OWASP-style documentation.

---

## Implementations

###  — Embedding-Based Demo (`preflight_rag_demo.py`)
A second implementation using **sentence-transformers (all-MiniLM-L6-v2)** and **ChromaDB** for semantic vector retrieval. This reflects the actual architecture proposed for BLT-Preflight and demonstrates genuine RAG — embedding, vector storage, and similarity search.

---

## Project Structure

```
BLT-Preflight-Prototype/
│
├── preflight_rag_demo.py    # Embedding-based RAG demo (sentence-transformers + ChromaDB)
├── owasp_docs.txt           # Security knowledge base
└── README.md                # Project documentation
```

---

## Embedding-Based RAG Demo

### How it works

1. **Document Loading** — OWASP documentation chunks loaded from `owasp_docs.txt`
2. **Embedding** — Chunks embedded using `sentence-transformers (all-MiniLM-L6-v2)`
3. **Vector Storage** — Embeddings stored in ChromaDB (persisted to `.chromadb/` directory)
4. **Semantic Retrieval** — Query embedded and compared against stored chunks via cosine similarity
5. **Response** — Top matching chunks returned as contextual guidance

### Requirements

```
sentence-transformers
chromadb
```

Install with:

```bash
pip install sentence-transformers chromadb
```

### Running

```bash
python preflight_rag_demo.py
```

### Example

```
Query: I modified the login flow and changed session handling
  [OWASP A07] Identification and Authentication Failures: Confirmation of the user's identity...

Query: I added a new API endpoint without authentication checks
  [OWASP A01] Broken Access Control: Restrictions on what authenticated users are allowed to do...
```

---

## Example Questions to Try

- What is Broken Access Control?
- How can attackers access other users' data?
- What causes privilege escalation?
- How to prevent injection vulnerabilities?
- What are authentication failures?

---


## Purpose

This repository serves as a proof-of-concept for the **AI Assisted Contribution Guidance for BLT-Preflight** GSoC 2026 proposal. It demonstrates how security documentation can be queried interactively to help contributors understand vulnerabilities and best practices before submitting code.

The  implementation reflects the actual proposed architecture — sentence-transformers for embedding, ChromaDB for vector storage, and semantic similarity for retrieval.

---

## License

This project is provided for demonstration and educational purposes.
