# rag.py — minimal offline RAG demo for GSoC 2026
# Step 1: load docs
with open("owasp_docs.txt", "r") as f:
    docs = [line.strip() for line in f if line.strip()]

# Step 2: Retrieval function
def retrieve(query, top_n=5):
    query_words = query.lower().split()
    scored = []

    for line in docs:
        line_lower = line.lower()
        score = sum(1 for word in query_words if word in line_lower)
        if score > 0:
            scored.append((score, line))

    scored.sort(reverse=True, key=lambda x: x[0])
    return [line for _, line in scored[:top_n]]

# Step 3: main loop
if __name__ == "__main__":
    query = input("Enter your security question: ")
    relevant_lines = retrieve(query)

    print("\nAnswer:\n Based on the context:")
    for line in relevant_lines:
        print(f" - {line}")
