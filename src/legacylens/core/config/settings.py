"""Settings loaded from environment with validation (pydantic-settings)."""

from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


EnvironmentKind = Literal["dev", "staging", "prod"]


class Settings(BaseSettings):
    """Application settings from environment variables. Required keys fail fast if missing."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Required
    PINECONE_API_KEY: str = Field(..., min_length=1, description="Pinecone serverless API key")
    VOYAGE_API_KEY: str = Field(..., min_length=1, description="Voyage AI API key (Voyage-code-3)")
    ANTHROPIC_API_KEY: str = Field(..., min_length=1, description="Anthropic (Claude) API key")

    # Recommended
    ENVIRONMENT: EnvironmentKind = Field(
        default="dev",
        description="Runtime environment: dev, staging, or prod",
    )

    # Optional
    PINECONE_INDEX_NAME: str = Field(default="legacylens-index", description="Pinecone index name")
    NEO4J_URI: str = Field(default="", description="Neo4j connection URI (optional)")
    NEO4J_USER: str = Field(default="neo4j", description="Neo4j username")
    NEO4J_PASSWORD: str = Field(default="", description="Neo4j password")
    REDIS_URL: str = Field(default="", description="Redis URL for cache (optional)")
    LANGSMITH_API_KEY: str = Field(default="", description="LangSmith API key for tracing (optional)")
    LEGACYLENS_API_URL: str = Field(
        default="",
        description="Backend API base URL for CLI (optional)",
    )


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return the singleton Settings instance. Loads from env on first call."""
    return Settings()
