# BLT Preflight – Offline RAG Demo

This repository contains a **minimal offline Retrieval-Augmented Generation (RAG) prototype** created to demonstrate how security documentation can be queried interactively.

The goal of this demo is to show how contributor tools like **Preflight** could provide contextual security guidance by retrieving relevant information from OWASP-style documentation.

This implementation is intentionally lightweight and runs **fully offline** using a simple keyword-based retrieval approach.

---

## Overview

The demo demonstrates the core RAG pipeline:

1. **Document Loading**
   - Security knowledge is stored in a text file (`docs.txt`).

2. **Retrieval**
   - When a user asks a question, the system searches the document for relevant lines using keyword matching.

3. **Response Generation**
   - The most relevant lines are returned as contextual answers.

This prototype focuses on demonstrating the **concept of document retrieval for security guidance**, rather than full AI-powered generation.

---

## Project Structure

preflight-offline-rag-demo/ │ ├── rag.py        # Main RAG demo script ├── docs.txt      # Security knowledge base └── README.md     # Project documentation

---

## Requirements

- Python 3.x  
- Works in:
  - Pydroid (Android)
  - Termux
  - Linux / macOS / Windows Python environments

No external libraries are required.

---

## Running the Demo

1. Clone the repository

```bash
git clone https://github.com/yourusername/preflight-offline-rag-demo.git
cd preflight-offline-rag-demo

2. Run the script



python rag.py

3. Enter a security question when prompted.



Example:

Enter your security question: What is Broken Access Control?

Example output:

Answer:
Based on the context:
 - Broken Access Control occurs when users can access resources they should not.
 - Violation of the principle of least privilege happens when users have more permissions than needed.


---

Example Questions to Try

What is Broken Access Control?

How can attackers access other users data?

What causes privilege escalation?

How to prevent access control failures?



---

Limitations

This demo intentionally uses simple keyword matching, so it has some limitations:

It does not understand natural language semantics.

Answers depend on keywords present in docs.txt.

It retrieves relevant lines rather than generating new explanations.


These limitations are acceptable for demonstrating the RAG concept in a minimal offline environment.


---

Future Improvements

Possible enhancements include:

Semantic search using embeddings

Vector databases for efficient retrieval

Integration with LLMs for answer generation

Larger curated OWASP security datasets

Integration with Preflight contributor tooling



---

Purpose

This repository serves as a proof-of-concept for using RAG to provide contextual security guidance within developer tooling like Preflight.

The demo illustrates how security documentation can be queried interactively to help developers understand vulnerabilities and best practices.


---

License

This project is provided for demonstration and educational purposes.

