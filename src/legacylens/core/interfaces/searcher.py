"""Searcher interface for hybrid/vector search."""

from abc import ABC, abstractmethod
from typing import Any


class ISearcher(ABC):
    """Abstract searcher for querying the vector store (e.g. hybrid search)."""

    @abstractmethod
    def search(self, query_text: str, top_k: int = 10, filters: dict[str, Any] | None = None) -> list[dict[str, Any]]:
        """Return top-k results for a query, optionally filtered.

        Args:
            query_text: Natural language or code query.
            top_k: Maximum number of results.
            filters: Optional metadata filters.

        Returns:
            List of result dicts (e.g. id, score, metadata, content).
        """
        ...
