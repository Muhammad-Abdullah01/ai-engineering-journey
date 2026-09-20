from loader import load_document, DocumentLoadError
from chunker import chunk_text
from vector_store import VectorStore, VectorStoreError
from qa import answer_question, QAError


def main():
    print("RAG Document Q&A Tool")
    print("=" * 40)

    file_path = input("Enter path to your document (.txt or .pdf): ").strip()

    try:
        print("Loading document...")
        text = load_document(file_path)

        print("Chunking document...")
        chunks = chunk_text(text)
        print(f"Created {len(chunks)} chunks.")

        print("Embedding and storing chunks (this may take a moment)...")
        store = VectorStore()
        store.add_chunks(chunks)
        print("Document ready. Ask your questions below.\n")

    except (DocumentLoadError, VectorStoreError) as e:
        print(f"Setup failed: {e}")
        return

    print("Type 'quit' to exit.\n")

    while True:
        question = input("Ask a question: ").strip()

        if question.lower() == "quit":
            print("Goodbye!")
            break

        try:
            relevant_chunks = store.search(question)
            answer = answer_question(question, relevant_chunks)
            print(f"\n💬 {answer}\n")
        except (VectorStoreError, QAError) as e:
            print(f"\n⚠️ Error: {e}\n")


if __name__ == "__main__":
    main()