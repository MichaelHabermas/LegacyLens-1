"""Embedder interface for generating vector embeddings."""

from abc import ABC, abstractmethod


class IEmbedder(ABC):
    """Abstract embedder for generating embeddings from text batches."""

    @abstractmethod
    def embed_batch(self, texts: list[str]) -> list[list[float]]:
        """Generate embedding vectors for a batch of texts.

        Args:
            texts: List of text strings to embed.

        Returns:
            List of embedding vectors (each a list of floats).
        """
        ...
