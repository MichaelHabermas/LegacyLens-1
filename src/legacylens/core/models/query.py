"""Query model for search requests."""

from typing import Any

from pydantic import BaseModel, Field


class Query(BaseModel):
    """A user or system query with optional filters and top_k."""

    text: str = Field(..., description="Query text (natural language or code)")
    filters: dict[str, Any] = Field(default_factory=dict, description="Optional metadata filters")
    top_k: int = Field(default=10, ge=1, le=100, description="Maximum number of results to return")
