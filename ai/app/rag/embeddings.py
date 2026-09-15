import math
from typing import List

class EmbeddingService:
    """
    Deterministic Embedding Generator for UniSphere AI RAG Pipeline.
    Generates 64-dimensional dense vector embeddings for semantic document search.
    """
    def __init__(self, dimension: int = 64):
        self.dimension = dimension

    def get_embedding(self, text: str) -> List[float]:
        words = text.lower().split()
        vector = [0.0] * self.dimension

        for i, word in enumerate(words):
            for char_idx, char in enumerate(word):
                pos = (ord(char) * (i + 1) + char_idx * 7) % self.dimension
                vector[pos] += math.sin(ord(char)) * 0.1

        # L2 Normalization
        norm = math.sqrt(sum(v * v for v in vector))
        if norm > 0:
            vector = [v / norm for v in vector]

        return vector
