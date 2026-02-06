"""Chunker interface for syntax-aware code chunking."""

from abc import ABC, abstractmethod
from typing import Any


class IChunker(ABC):
    """Abstract chunker for splitting parsed code into chunks with optional overlap."""

    @abstractmethod
    def chunk(self, parsed: Any) -> list[dict[str, Any]]:
        """Split parsed content into chunks (e.g. with paragraph/section boundaries and overlap).

        Args:
            parsed: Output from a parser (e.g. IParser.parse_file).

        Returns:
            List of chunk dicts (e.g. with 'content', 'metadata' keys) or Chunk-like objects.
        """
        ...
