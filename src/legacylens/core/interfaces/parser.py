"""Parser interface for language-specific AST parsing."""

from abc import ABC, abstractmethod
from typing import Any


class IParser(ABC):
    """Abstract parser for extracting logical boundaries (e.g. paragraphs, sections) from source files."""

    @abstractmethod
    def parse_file(self, file_path: str, content: str) -> Any:
        """Parse a source file and return a structured representation (e.g. AST or list of blocks).

        Args:
            file_path: Path to the file (for metadata).
            content: Raw file content.

        Returns:
            Parser-specific structure (e.g. list of code blocks with boundaries).
        """
        ...
