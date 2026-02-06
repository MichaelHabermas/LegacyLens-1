"""SearchResult model for query responses."""

from pydantic import BaseModel, Field

from legacylens.core.models.chunk import Chunk


class SearchResult(BaseModel):
    """Result of a search: chunks, scores, and optional citations."""

    chunks: list[Chunk] = Field(default_factory=list, description="Retrieved chunks")
    scores: list[float] = Field(default_factory=list, description="Relevance scores per chunk")
    citations: list[str] = Field(default_factory=list, description="Citation strings (e.g. file:line)")
