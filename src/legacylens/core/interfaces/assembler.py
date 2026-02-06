"""Context assembler interface for building LLM context from results."""

from abc import ABC, abstractmethod
from typing import Any


class IContextAssembler(ABC):
    """Abstract assembler for building a single context string from search/rerank results."""

    @abstractmethod
    def assemble(self, results: list[dict[str, Any]], query: str) -> str:
        """Build a context string (e.g. with citations) from results for the LLM.

        Args:
            results: Reranked results (e.g. from IReranker.rerank).
            query: Original user query.

        Returns:
            Assembled context string (e.g. markdown with file/line references).
        """
        ...
