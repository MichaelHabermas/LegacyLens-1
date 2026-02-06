"""Core abstract interfaces for ingestion, retrieval, and generation."""

from legacylens.core.interfaces.parser import IParser
from legacylens.core.interfaces.chunker import IChunker
from legacylens.core.interfaces.embedder import IEmbedder
from legacylens.core.interfaces.indexer import IIndexer
from legacylens.core.interfaces.searcher import ISearcher
from legacylens.core.interfaces.reranker import IReranker
from legacylens.core.interfaces.assembler import IContextAssembler
from legacylens.core.interfaces.llm_provider import ILLMProvider

__all__ = [
    "IParser",
    "IChunker",
    "IEmbedder",
    "IIndexer",
    "ISearcher",
    "IReranker",
    "IContextAssembler",
    "ILLMProvider",
]
