# Environment and Configuration Reference

This document is the single reference for all environment variables and configuration used by LegacyLens. For per-component setup, see [TECH-STACK-GUIDE.md](TECH-STACK-GUIDE.md). For setup steps, see the main [README](../../README.md). Epic 0 defines validation and loading of these variables in the config module; see [PRD Epic 0](../PRD.md#epic-0-project-foundation--configuration).

---

## Table of variables

| Variable | Required | Description | Example (masked) | Used by |
|----------|----------|-------------|------------------|---------|
| `PINECONE_API_KEY` | Yes | API key for Pinecone serverless | `pcsk_xxxx...` | Ingestion (indexer), Retrieval (searcher) |
| `PINECONE_INDEX_NAME` | Optional | Name of the Pinecone index (default may be in code) | `legacylens-index` | Ingestion, Retrieval |
| `VOYAGE_API_KEY` | Yes | API key for Voyage AI (Voyage-code-3) | `pa-xxxx...` | Ingestion (embedder), Retrieval (query embedding) |
| `ANTHROPIC_API_KEY` | Yes | API key for Anthropic (Claude) | `sk-ant-xxxx...` | Generation (LLM) |
| `NEO4J_URI` | No (MVP) | Neo4j connection URI (e.g. bolt://...) | `neo4j+s://xxxx.databases.neo4j.io` | GraphRAG / dependency features (optional) |
| `NEO4J_USER` | No (MVP) | Neo4j username | `neo4j` | GraphRAG |
| `NEO4J_PASSWORD` | No (MVP) | Neo4j password | `****` | GraphRAG |
| `REDIS_URL` | No | Redis connection URL for embedding/query cache | `redis://localhost:6379` or `rediss://...` | Ingestion (embedder cache), optional Retrieval |
| `LANGSMITH_API_KEY` | No | LangSmith API key for tracing | `lsv2_xxxx...` | Observability (traces) |
| `ENVIRONMENT` | Yes (recommended) | Runtime environment | `dev`, `staging`, or `prod` | Config, Observability (enable/disable tracing) |
| `LEGACYLENS_API_URL` | No (CLI) | Backend API base URL for the CLI | `https://legacylens.vercel.app` or `http://localhost:3000` | CLI (when calling deployed or local API) |

- **Required**: The application should fail fast at startup or first use if these are missing (validated in config).
- **Optional**: The application runs without them; the corresponding feature is disabled or degraded (e.g. no Neo4j → no GraphRAG; no Redis → no embedding cache; no LangSmith → no tracing).

---

## Getting API keys and accounts

- **Pinecone**: Sign up at [pinecone.io](https://www.pinecone.io/), create a serverless index, and copy the API key from the console.
- **Voyage AI**: Sign up at [voyageai.com](https://www.voyageai.com/), create an API key. Free tier includes 200M tokens.
- **Anthropic**: Sign up at [anthropic.com](https://www.anthropic.com/), create an API key in the console.
- **Neo4j (optional)**: Use [Neo4j Aura](https://neo4j.com/cloud/aura/) free tier; note URI, username, and password.
- **Redis (optional)**: Local: run Redis (e.g. Docker). Cloud: e.g. [Upstash](https://upstash.com/) for a serverless-friendly Redis; copy the URL.
- **LangSmith (optional)**: Sign up at [smith.langchain.com](https://smith.langchain.com/), create an API key for tracing.

---

## Environments

| Value | Purpose | Typical behavior |
|-------|---------|------------------|
| `dev` | Local development | Tracing optional (if `LANGSMITH_API_KEY` set); cache optional; verbose logs OK. |
| `staging` | Pre-production testing | Tracing on; same keys as prod or staging-specific; rate limits may apply. |
| `prod` | Production (e.g. Vercel) | Tracing on; all secrets from Vercel env; rate limits and timeouts as per plan. |

Differences in behavior (e.g. enabling/disabling tracing, log level) should be driven by `ENVIRONMENT` in the config module so that the same codebase behaves correctly in each environment.

---

## Secrets handling

- **Do not commit `.env`** — It is listed in `.gitignore`. Never commit API keys or passwords.
- **`.env.example`** — When added (Epic 0), list variable names and short descriptions only; no real values. Use it as the template for creating a local `.env`.
- **Vercel** — Set all required (and optional) variables in the Vercel project dashboard (Settings → Environment Variables). Use production and preview as needed. Vercel encrypts secrets at rest.
- **GitHub Actions** — Store secrets in the repository settings (Settings → Secrets and variables → Actions). Reference them in workflows as `${{ secrets.PINECONE_API_KEY }}` etc. Do not echo or log secrets.

---

## Local vs deployed

| Concern | Local (developer machine) | Deployed (e.g. Vercel) |
|---------|---------------------------|-------------------------|
| **CLI** | Runs on your machine; calls backend API via `LEGACYLENS_API_URL` or default. | N/A (CLI is local). |
| **Backend API** | May run locally (e.g. `uvicorn` or similar) for testing; then `LEGACYLENS_API_URL=http://localhost:8xxx`. | Runs on Vercel serverless; env vars set in Vercel dashboard. |
| **Ingestion** | Usually run locally (`legacylens ingest`) or in CI; needs Pinecone, Voyage, optional Redis. | Heavy batch ingestion typically not on Vercel (timeout); use CLI or a separate job. |
| **Pinecone / Voyage / Anthropic** | Same API keys as prod (or dev keys); use `.env` locally. | Set in Vercel; same or different keys per environment. |
| **Redis** | Local Redis or Upstash; `REDIS_URL` in `.env`. | Must be external (e.g. Upstash); `REDIS_URL` in Vercel. |
| **Neo4j** | Optional; local or Aura; only needed for GraphRAG features. | Optional; Aura or hosted; only if GraphRAG is enabled. |

For a quick setup checklist, see the main [README](../../README.md#setup). For component-level config, see [TECH-STACK-GUIDE.md](TECH-STACK-GUIDE.md).
