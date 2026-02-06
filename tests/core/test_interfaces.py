"""Tests that core interfaces are abstract and data models validate."""

import pytest
from pydantic import ValidationError

from legacylens.core.interfaces import (
    IParser,
    IChunker,
    IEmbedder,
    IIndexer,
    ISearcher,
    IReranker,
    IContextAssembler,
    ILLMProvider,
)
from legacylens.core.models import Chunk, Query, SearchResult


@pytest.mark.parametrize(
    "abstract_class",
    [
        IParser,
        IChunker,
        IEmbedder,
        IIndexer,
        ISearcher,
        IReranker,
        IContextAssembler,
        ILLMProvider,
    ],
)
def test_interface_is_abstract(abstract_class: type) -> None:
    """Each interface is abstract and cannot be instantiated directly."""
    with pytest.raises(TypeError):
        abstract_class()


def test_chunk_model_validates() -> None:
    """Chunk model accepts valid data."""
    c = Chunk(content="hello", metadata={"file_path": "x.cob"})
    assert c.content == "hello"
    assert c.metadata["file_path"] == "x.cob"
    assert c.embedding is None
    c2 = Chunk(content="world", embedding=[0.1, 0.2])
    assert c2.embedding == [0.1, 0.2]


def test_query_model_validates() -> None:
    """Query model accepts valid data and enforces top_k bounds."""
    q = Query(text="find main")
    assert q.text == "find main"
    assert q.top_k == 10
    q2 = Query(text="x", top_k=5, filters={"lang": "cobol"})
    assert q2.top_k == 5
    assert q2.filters == {"lang": "cobol"}
    with pytest.raises(ValidationError):
        Query(text="x", top_k=0)
    with pytest.raises(ValidationError):
        Query(text="x", top_k=101)


def test_search_result_model_validates() -> None:
    """SearchResult model accepts chunks, scores, and citations."""
    chunk = Chunk(content="code", metadata={})
    sr = SearchResult(chunks=[chunk], scores=[0.9], citations=["file.cob:10"])
    assert len(sr.chunks) == 1
    assert sr.chunks[0].content == "code"
    assert sr.scores == [0.9]
    assert sr.citations == ["file.cob:10"]
    sr_empty = SearchResult()
    assert sr_empty.chunks == []
    assert sr_empty.scores == []
    assert sr_empty.citations == []
