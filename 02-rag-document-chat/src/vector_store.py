import chromadb
from embedder import embed_text, EmbeddingError


class VectorStoreError(Exception):
    pass


class VectorStore:
    def __init__(self, collection_name: str = "documents"):
        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection(name=collection_name)

    def add_chunks(self, chunks: list[str]) -> None:
        """
        Embed each chunk and store it in the vector database.
        """
        for i, chunk in enumerate(chunks):
            try:
                embedding = embed_text(chunk)
            except EmbeddingError as e:
                raise VectorStoreError(f"Failed to embed chunk {i}: {e}")

            self.collection.add(
                ids=[f"chunk_{i}"],
                embeddings=[embedding],
                documents=[chunk]
            )

    def search(self, query: str, top_k: int = 3) -> list[str]:
        """
        Find the most relevant chunks for a given query.
        """
        try:
            query_embedding = embed_text(query)
        except EmbeddingError as e:
            raise VectorStoreError(f"Failed to embed query: {e}")

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        return results["documents"][0] if results["documents"] else []