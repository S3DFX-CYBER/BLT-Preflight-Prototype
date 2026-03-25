# rag.py — minimal REAL offline RAG demo for GSOC 2026

from sentence_transformers import SentenceTransformer
import chromadb

# Step 1: Load docs
with open("owasp_docs.txt", "r") as f:
    docs = [line.strip() for line in f if line.strip()]

# Step 2: Initialize embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Step 3: Initialize ChromaDB (in-memory for demo)
client = chromadb.Client()
collection = client.create_collection(name="owasp_docs")

# Step 4: Embed and store documents
embeddings = model.encode(docs).tolist()

collection.add(
    documents=docs,
    embeddings=embeddings,
    ids=[str(i) for i in range(len(docs))]
)

# Step 5: Retrieval function (semantic)
def retrieve(query, top_n=5):
    query_embedding = model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=top_n
    )

    return results["documents"][0]

# Step 6: Main loop
if __name__ == "__main__":
    query = input("Enter your security question: ")

    relevant_docs = retrieve(query)

    print("\nAnswer:\nBased on retrieved OWASP context:")
    for doc in relevant_docs:
        print(f" - {doc}")
