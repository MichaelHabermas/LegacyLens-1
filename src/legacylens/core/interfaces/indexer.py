"""Indexer interface for vector store operations."""

from abc import ABC, abstractmethod
from typing import Any


class IIndexer(ABC):
    """Abstract indexer for upserting and deleting vectors in a store (e.g. Pinecone)."""

    @abstractmethod
    def upsert(self, ids: list[str], vectors: list[list[float]], metadata: list[dict[str, Any]]) -> None:
        """Upsert vectors with metadata into the index.

        Args:
            ids: Unique identifiers for each vector.
            vectors: Embedding vectors.
            metadata: Metadata dict per vector (e.g. file_path, line_start, line_end).
        """
        ...

    @abstractmethod
    def delete(self, ids: list[str]) -> None:
        """Delete vectors by ID.

        Args:
            ids: Identifiers to delete.
        """
        ...
