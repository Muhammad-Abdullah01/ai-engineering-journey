import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(apikey = os.getenv("GEMINI_API_KEY"))

class EmbeddingError(Exception):
    pass

def embed_text(text : str) -> list[float]:
  
    # Convert text into a numerical embedding vector using Gemini.
    try:
        result = client.models.embed_content(
            model="text-embedding-004",
            contents=text
        )
        return result.embeddings[0].values
    except Exception as e:
        raise EmbeddingError(f"Could not generate embedding: {e}")
    

