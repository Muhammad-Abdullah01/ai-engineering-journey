import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))

class QAError(Exception):
    pass

def answer_question(question :str , context_chunks: list[str]) -> str:
    """
    Generate an answer grounded in the retrieved document chunks.
    """

    context = "\n\n".join(context_chunks)

    prompt = (
        f"Answer the question using ONLY the context below. "
        f"If the answer isn't in the context, say you don't know.\n\n"
        f"Context:\n{context}\n\n"
        f"Question: {question}\n\n"
        f"Answer:"
    )
    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        raise QAError(f"Could not generate answer: {e}")
    