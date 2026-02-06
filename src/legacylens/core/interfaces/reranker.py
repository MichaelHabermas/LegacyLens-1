"""Reranker interface for second-pass ranking."""

from abc import ABC, abstractmethod
from typing import Any


class IReranker(ABC):
    """Abstract reranker for refining search results (e.g. Zerank-2)."""

    @abstractmethod
    def rerank(self, query: str, results: list[dict[str, Any]], top_k: int = 5) -> list[dict[str, Any]]:
        """Rerank results by relevance to the query.

        Args:
            query: Original query text.
            results: Initial search results (e.g. from ISearcher.search).
            top_k: Number of results to return after reranking.

        Returns:
            Reranked list of result dicts.
        """
        ...
