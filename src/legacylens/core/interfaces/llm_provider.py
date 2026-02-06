"""LLM provider interface for answer generation."""

from abc import ABC, abstractmethod


class ILLMProvider(ABC):
    """Abstract LLM provider (e.g. Claude via Anthropic)."""

    @abstractmethod
    def generate(self, prompt: str, context: str, query: str) -> str:
        """Generate an answer given a prompt template, context, and query.

        Args:
            prompt: Prompt template or system message.
            context: Assembled context (e.g. from IContextAssembler.assemble).
            query: User query.

        Returns:
            Generated answer string (e.g. with citations).
        """
        ...
