# NEW import
from google import genai
from google.genai import types

# NEW setup
client = genai.Client(api_key="your_api_key")

# NEW embeddings
def generate_embeddings(text):
    response = client.models.embed_content(
        model="models/text-embedding-004",   # embedding-001 is also deprecated
        contents=text
    )
    return response.embeddings[0].values

# NEW text generation
def generate_text(prompt):
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )
    return response.text
