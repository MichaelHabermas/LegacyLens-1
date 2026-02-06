"""Tests for config module (Settings and get_settings)."""

import os

import pytest
from pydantic import ValidationError

from legacylens.core.config.settings import Settings, get_settings


def test_config_loads_from_env(monkeypatch: pytest.MonkeyPatch) -> None:
    """Settings loads from environment when required vars are set."""
    monkeypatch.setenv("PINECONE_API_KEY", "pcsk_test")
    monkeypatch.setenv("VOYAGE_API_KEY", "pa_test")
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant_test")
    get_settings.cache_clear()
    try:
        settings = get_settings()
        assert settings.PINECONE_API_KEY == "pcsk_test"
        assert settings.VOYAGE_API_KEY == "pa_test"
        assert settings.ANTHROPIC_API_KEY == "sk-ant_test"
        assert settings.ENVIRONMENT == "dev"
    finally:
        get_settings.cache_clear()


def test_config_validates_required_keys(monkeypatch: pytest.MonkeyPatch) -> None:
    """Missing required environment variables raise ValidationError."""
    for key in ("PINECONE_API_KEY", "VOYAGE_API_KEY", "ANTHROPIC_API_KEY"):
        monkeypatch.delenv(key, raising=False)
    get_settings.cache_clear()
    try:
        with pytest.raises(ValidationError):
            get_settings()
    finally:
        get_settings.cache_clear()


def test_config_singleton_pattern(monkeypatch: pytest.MonkeyPatch) -> None:
    """get_settings returns the same instance on repeated calls."""
    monkeypatch.setenv("PINECONE_API_KEY", "pcsk_singleton")
    monkeypatch.setenv("VOYAGE_API_KEY", "pa_singleton")
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant_singleton")
    get_settings.cache_clear()
    try:
        a = get_settings()
        b = get_settings()
        assert a is b
    finally:
        get_settings.cache_clear()


def test_config_default_values(monkeypatch: pytest.MonkeyPatch) -> None:
    """Default values are applied for optional and recommended fields."""
    monkeypatch.setenv("PINECONE_API_KEY", "pcsk_def")
    monkeypatch.setenv("VOYAGE_API_KEY", "pa_def")
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant_def")
    get_settings.cache_clear()
    try:
        settings = get_settings()
        assert settings.ENVIRONMENT == "dev"
        assert settings.PINECONE_INDEX_NAME == "legacylens-index"
        assert settings.NEO4J_USER == "neo4j"
        assert settings.NEO4J_URI == ""
        assert settings.REDIS_URL == ""
    finally:
        get_settings.cache_clear()


def test_config_environment_override(monkeypatch: pytest.MonkeyPatch) -> None:
    """ENVIRONMENT can be overridden via env."""
    monkeypatch.setenv("PINECONE_API_KEY", "pcsk_env")
    monkeypatch.setenv("VOYAGE_API_KEY", "pa_env")
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant_env")
    monkeypatch.setenv("ENVIRONMENT", "staging")
    get_settings.cache_clear()
    try:
        settings = get_settings()
        assert settings.ENVIRONMENT == "staging"
    finally:
        get_settings.cache_clear()
