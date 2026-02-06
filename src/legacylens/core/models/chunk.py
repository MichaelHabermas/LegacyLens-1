"""Chunk model for indexed code segments."""

from typing import Any

from pydantic import BaseModel, Field


class Chunk(BaseModel):
    """A code or text chunk with content, metadata, and optional embedding."""

    content: str = Field(..., description="Text content of the chunk")
    metadata: dict[str, Any] = Field(default_factory=dict, description="Metadata (e.g. file_path, line_start, line_end)")
    embedding: list[float] | None = Field(default=None, description="Optional embedding vector")
