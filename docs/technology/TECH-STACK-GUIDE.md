# LegacyLens Tech Stack In-Depth Guide

This guide explains how to set up and use each technology in the LegacyLens RAG system. For rationale and alternatives, see [DESIGN-DOCUMENT.md](../research/DESIGN-DOCUMENT.md) and [RECORD-ARCHITECTURE-DECISIONS.md](../research/RECORD-ARCHITECTURE-DECISIONS.md). For tradeoff details, see [IDENTIFY-TRADEOFFS.md](../research/IDENTIFY-TRADEOFFS.md).

---

## Python and LlamaIndex

### What it is

- **Python**: 3.11+ is required for type hints, pattern matching, and modern async support used by LlamaIndex and API clients.
- **LlamaIndex**: A retrieval-focused framework providing document indexing, chunking, embedding integration, vector stores, and query pipelines. LegacyLens uses Workflows 1.0, LlamaAgents Builder, and LlamaParse v2.

### Why it was chosen

LlamaIndex offers a lower learning curve for retrieval-heavy tasks, built-in syntax-aware chunking (LlamaParse v2), agentic refinement (LlamaAgents Builder), and integrations for Pinecone, Voyage, Anthropic, and evaluation tools. See [RECORD-ARCHITECTURE-DECISIONS.md](../research/RECORD-ARCHITECTURE-DECISIONS.md#framework-decision).

### Setup

- Install Python 3.11+ and create a virtual environment. Dependencies are declared in `pyproject.toml` (e.g. `llama-index>=0.10.0`, `llama-index-llms-anthropic`, `llama-index-embeddings-voyageai`, etc.).
- Run `pip install -e .` from the repo root after Epic 0 is complete.

### How the project uses it

- **Ingestion**: LlamaParse v2 (or custom parsers) define boundaries for COBOL paragraphs/Fortran subroutines; hierarchical chunking (file → section → function) with 10–25% overlap is applied; LlamaIndex document/node abstractions feed into embedders and indexers.
- **Retrieval**: Query embedding, hybrid search (via Pinecone integration), and reranking are orchestrated through LlamaIndex components or custom modules that implement the project’s interfaces (`ISearcher`, `IReranker`).
- **Generation**: LlamaIndex LLM integrations (Anthropic/Claude) are used for answer synthesis with citation-focused prompts.
- **Code location**: Core interfaces live in `src/core/interfaces/`; ingestion in `src/ingestion/` (parsers, chunkers, embedders, indexers); retrieval in `src/retrieval/` (searchers, rerankers, assemblers); generation in `src/generation/` (llm_providers, prompt_templates). See [PRD.md](../PRD.md) module structure.

### Configuration and limits

- No framework-specific env vars; API keys are for Pinecone, Voyage, Anthropic (see [ENVIRONMENT-AND-CONFIG.md](ENVIRONMENT-AND-CONFIG.md)).
- LlamaIndex version: 0.10+ per PRD Appendix D.

### Troubleshooting

- Import errors: ensure the virtual environment is activated and `pip install -e .` has been run.
- Version conflicts: pin versions in `pyproject.toml` and reinstall.

---

## Pinecone Serverless

### What it is

Pinecone is a managed [vector database](../GLOSSARY.md) offering serverless indexes with native hybrid search (vector + keyword/BM25), metadata filtering, and auto-scaling. LegacyLens uses the serverless tier.

### Why it was chosen

Low p99 latency (<100 ms), native hybrid search for exact code identifiers (e.g. `CUSTOMER-RECORD`), free tier up to 2GB (covers ~50K vectors for ~10K LOC), and minimal ops. See [RECORD-ARCHITECTURE-DECISIONS.md](../research/RECORD-ARCHITECTURE-DECISIONS.md#vector-database-decision).

### Setup

1. Create an account at [Pinecone](https://www.pinecone.io/).
2. Create a serverless index with dimensions matching the embedding model (1536 for Voyage-code-3). Enable hybrid search if available for your plan.
3. Copy the API key and (if used) environment/host from the console. Set `PINECONE_API_KEY` and any index-specific env vars (e.g. `PINECONE_INDEX_NAME`) in `.env`.

### How the project uses it

- **Ingestion**: Embeddings and metadata (file path, line numbers, scope) are upserted via the indexer module (`IIndexer` implementation using Pinecone client).
- **Retrieval**: Hybrid search returns top-k (20–50) candidates; metadata is used for filtering and for inclusion in responses (file/line citations).
- **Metadata schema**: Store at least `file_path`, `line_start`, `line_end`, `scope` (e.g. paragraph or function name) so the CLI and LLM can cite accurately.

### Configuration and limits

- **Free tier**: Up to 2GB; sufficient for MVP and small codebases.
- **Cost**: At scale, usage is RU-based (read units); high query volume increases cost. Caching (Redis) reduces repeated reads. See [IDENTIFY-TRADEOFFS.md](../research/IDENTIFY-TRADEOFFS.md) for projections.
- **Timeouts**: Serverless indexes have request limits; batch upserts should respect rate limits.

### Troubleshooting

- Index not found: verify index name and region in env; ensure the index exists in the same environment as the API key.
- High latency: check region proximity to your deployment (e.g. Vercel); consider caching for repeated queries.

---

## Voyage-code-3

### What it is

Voyage-code-3 is a code-optimized embedding model (1536 dimensions) offered via the Voyage AI API. It is tuned for code structure, identifiers, and comments.

### Why it was chosen

Code-specific models show ~14–20% better recall on code benchmarks than general-purpose models; 200M free tokens cover dev and initial ingestion. See [RECORD-ARCHITECTURE-DECISIONS.md](../research/RECORD-ARCHITECTURE-DECISIONS.md#embedding-strategy-decision).

### Setup

1. Sign up at [Voyage AI](https://www.voyageai.com/).
2. Obtain an API key and set `VOYAGE_API_KEY` in `.env`.
3. Model name: use the exact identifier for Voyage-code-3 (e.g. `voyage-code-3` or as per current [Voyage AI docs](https://docs.voyageai.com/)).

### How the project uses it

- **Ingestion**: Code chunks are embedded in batch; the same model is used for consistency. Content-hash caching (Redis) skips re-embedding unchanged chunks.
- **Retrieval**: The user query is embedded with the same model before hybrid search.
- **Dimensions**: 1536; must match the Pinecone index dimension.

### Configuration and limits

- **Free tier**: 200M tokens; sufficient for 10K+ LOC and moderate re-ingestion.
- **Paid**: ~$0.18 per 1M tokens after free tier (see [IDENTIFY-TRADEOFFS.md](../research/IDENTIFY-TRADEOFFS.md)).
- **Token limits**: Respect max input length per Voyage docs; chunk sizes (512–8192 tokens) should stay within limit.

### Troubleshooting

- Auth errors: verify `VOYAGE_API_KEY` is set and valid.
- Rate limits: use batching and backoff; cache embeddings in Redis to reduce API calls.

---

## Claude 4.5 Sonnet

### What it is

Claude 4.5 Sonnet is an Anthropic LLM API model used for answer synthesis with strong code reasoning and low hallucination when given citation-focused prompts.

### Why it was chosen

Strong performance on code benchmarks (~87%), good at structured explanations and file/line citations, and lower hallucination risk with strict prompting. See [RECORD-ARCHITECTURE-DECISIONS.md](../research/RECORD-ARCHITECTURE-DECISIONS.md#answer-generation-decision).

### Setup

1. Create an account at [Anthropic](https://www.anthropic.com/).
2. Obtain an API key and set `ANTHROPIC_API_KEY` in `.env`.
3. Use the correct model ID (e.g. `claude-sonnet-4-20250514` or as per [Anthropic docs](https://docs.anthropic.com/)).

### How the project uses it

- **Generation**: Retrieved context (reranked chunks with metadata) is passed to Claude with a prompt that requires file/line citations and forbids inventing code. Streaming is used for better perceived latency.
- **No-results**: When retrieval finds nothing relevant, the system should respond with a graceful “I don’t know” (or similar) instead of letting the LLM hallucinate.
- **Prompt templates**: Stored in `src/generation/prompt_templates/`; enforce citation format and context window usage.

### Configuration and limits

- **Context window**: 200K tokens; keep assembled context within budget so the model can attend to all retrieved chunks.
- **Cost**: Input/output pricing per Anthropic; prompt caching can reduce cost for repeated context. See [IDENTIFY-TRADEOFFS.md](../research/IDENTIFY-TRADEOFFS.md) for cost projections.
- **Streaming**: Prefer streaming for CLI UX; batch only if needed for evaluation.

### Troubleshooting

- Rate limits: implement backoff; consider prompt caching for repeated code context.
- Hallucinations: tighten prompt (strict citation format, “only use provided context”); monitor with RAGAS faithfulness metrics.

---

## Zerank-2

### What it is

Zerank-2 is a reranker model used as a second-pass ranker: it takes the top-k results from hybrid search and returns the top-5–10 most relevant for context assembly.

### Why it was chosen

Second-pass reranking improves precision (meets >70% top-5 target) and integrates with LlamaIndex. See [DESIGN-DOCUMENT.md](../research/DESIGN-DOCUMENT.md) and [RECORD-ARCHITECTURE-DECISIONS.md](../research/RECORD-ARCHITECTURE-DECISIONS.md#retrieval-pipeline-decision).

### Setup

- Zerank-2 may be used via Hugging Face (local or API) or a LlamaIndex integration. Install the appropriate package (e.g. `llama-index-postprocessor` or Hugging Face `transformers`) and configure model name/path in code or config.
- No dedicated env var in the base setup; add one (e.g. `ZERANK_MODEL`) if you need to switch models or use a hosted endpoint.

### How the project uses it

- **Retrieval pipeline**: After hybrid search returns top-k=20–50, the reranker (implementing `IReranker`) scores and trims to top-5–10. These are passed to context assembly and then to the LLM.
- **Location**: `src/retrieval/rerankers/`.

### Configuration and limits

- **Latency**: Reranking adds time; keep total E2E under 3s (target). If running locally, GPU can reduce latency.
- **Model size**: If self-hosted, ensure enough memory/GPU for the model.

### Troubleshooting

- Model load errors: check Hugging Face model ID or API endpoint and credentials.
- Slow rerank: reduce top-k input or use a smaller/faster reranker variant if precision allows.

---

## Neo4j

### What it is

Neo4j is a graph database used for dependency mapping (e.g. which functions call which, call graphs). LegacyLens uses it for GraphRAG and advanced features like impact analysis.

### Why it was chosen

Enables dependency and call-graph queries (e.g. “What calls CUSTOMER-RECORD?”) and integrates with LlamaIndex for GraphRAG. See [DESIGN-DOCUMENT.md](../research/DESIGN-DOCUMENT.md) and [RECORD-ARCHITECTURE-DECISIONS.md](../research/RECORD-ARCHITECTURE-DECISIONS.md).

### Setup

- **Optional for MVP.** If used: sign up for [Neo4j Aura](https://neo4j.com/cloud/aura/) (free tier) or run Neo4j locally.
- Set `NEO4J_URI`, `NEO4J_USER`, and `NEO4J_PASSWORD` in `.env`. Config module should treat these as optional so the app runs without Neo4j.

### How the project uses it

- **When**: Post-MVP or when dependency/GraphRAG features are enabled. Ingestion may write call-graph or symbol relationships; retrieval may augment context with graph results.
- **Location**: Integration in ingestion (e.g. dependency extraction) and retrieval (graph-backed context) as needed; keep behind interfaces so the system works without Neo4j.

### Configuration and limits

- Free tier has limits on nodes/relationships and concurrent connections; production may require a paid plan.
- If env vars are missing, disable GraphRAG and dependency features gracefully.

### Troubleshooting

- Connection refused: check URI, firewall, and credentials.
- Timeouts: increase timeout in the Neo4j driver or reduce query complexity.

---

## Redis

### What it is

Redis is an in-memory store used for embedding and query caching. LegacyLens uses content hashes as keys to skip re-embedding unchanged chunks and to cache query results when appropriate.

### Why it was chosen

Reduces Voyage (and optionally LLM) API calls and speeds up re-ingestion and repeated queries. See [RECORD-ARCHITECTURE-DECISIONS.md](../research/RECORD-ARCHITECTURE-DECISIONS.md) and [DESIGN-DOCUMENT.md](../research/DESIGN-DOCUMENT.md).

### Setup

- **Local**: Run Redis locally (Docker or install) and set `REDIS_URL` (e.g. `redis://localhost:6379`).
- **Cloud**: Use a managed Redis (e.g. Upstash for serverless-friendly usage) and set `REDIS_URL` in `.env` and in Vercel env vars for the backend.
- If `REDIS_URL` is unset, the app should degrade gracefully (no cache; all embeddings and queries hit APIs).

### How the project uses it

- **Embedding cache**: Before calling Voyage for a chunk, compute a content hash; if the hash exists in Redis, reuse the stored embedding and skip the API call.
- **Query cache**: Optionally cache full query results keyed by query hash to avoid duplicate retrieval + generation for identical questions.
- **Location**: Used inside embedder and optionally in retrieval/generation; keep behind an abstraction so caching can be disabled or swapped.

### Configuration and limits

- **Local vs deployed**: Local dev can use a local Redis; Vercel serverless needs an external Redis (e.g. Upstash) since there is no local persistence.
- **Memory**: Size cache appropriately; TTL can be set to avoid unbounded growth.

### Troubleshooting

- Connection errors: verify `REDIS_URL` and that the Redis instance is reachable from the runtime (network/firewall).
- Missing cache: ensure content hashes are deterministic and keys are consistent across runs.

---

## Vercel Serverless

### What it is

Vercel hosts the LegacyLens backend as serverless functions (e.g. query API). It provides auto-scaling, edge options, and a simple deploy flow.

### Why it was chosen

Quick deploy, free tier for MVP, and backend API can be made publicly accessible for the CLI. See [RECORD-ARCHITECTURE-DECISIONS.md](../research/RECORD-ARCHITECTURE-DECISIONS.md#deployment--observability-decision).

### Setup

1. Connect the repo to Vercel and configure the project (e.g. Python runtime, build command, output directory for serverless functions).
2. Add all required env vars in the Vercel dashboard (Pinecone, Voyage, Anthropic, optional Neo4j, Redis, LangSmith, `ENVIRONMENT`).
3. Deploy; the query endpoint (e.g. `/api/query`) is then used by the CLI.

### How the project uses it

- **Backend API**: Exposes at least a query endpoint that accepts a natural-language question and returns the answer plus citations. The CLI calls this endpoint.
- **Ingestion**: May run locally or via a separate job; heavy batch ingestion is often better as a background job or CLI-only to avoid timeouts.

### Configuration and limits

- **Timeout**: Vercel serverless has a max execution time (e.g. 60s on free tier). Keep query latency under 3s so timeouts are unlikely; for long-running ingestion, use CLI or async jobs.
- **Env vars**: All secrets must be set in Vercel; do not commit `.env` to the repo.
- **Cold starts**: First request after idle may be slower; consider keep-warm or accept for MVP.

### Troubleshooting

- Timeouts: optimize retrieval and LLM calls; consider streaming to start the response earlier.
- Missing env: double-check variable names and that they are set for the correct environment (production/preview) in Vercel.

---

## CLI (Rich and Pygments)

### What it is

The query interface is a Python CLI built with Typer (or similar). Rich is used for formatted terminal output; Pygments for syntax highlighting of code snippets.

### Why it was chosen

CLI keeps MVP scope smaller than a web UI while still supporting natural language input, snippets with file/line, confidence scores, and drill-down (e.g. `show` command). See [RECORD-ARCHITECTURE-DECISIONS.md](../research/RECORD-ARCHITECTURE-DECISIONS.md#query-interface-decision).

### Setup

- Typer, Rich, and Pygments are listed in `pyproject.toml`. After `pip install -e .`, the `legacylens` entry point is available (once implemented in Epic 4).
- Configure the backend URL (e.g. env `LEGACYLENS_API_URL`) so the CLI points to the Vercel-deployed API or local server.

### How the project uses it

- **Commands**: `legacylens ingest <path>`, `legacylens query "<question>"`, `legacylens show <file_path> <line_number>`, `legacylens status`. See [README.md](../../README.md) and [PRD.md](../PRD.md) Epic 4.
- **Output**: Query results show the LLM answer, code snippets with file/line, and optionally confidence scores; use Rich for layout and Pygments for code blocks (e.g. COBOL lexer).
- **Location**: `src/interface/cli/`.

### Configuration and limits

- No strict limits; ensure long answers and many snippets don’t overwhelm the terminal (pagination or truncation if needed).

### Troubleshooting

- Entry point not found: run `pip install -e .` and ensure the script is in `PATH` or invoke as `python -m legacylens`.
- Backend unreachable: check `LEGACYLENS_API_URL` and network; for local dev, ensure the backend server is running.

---

## Observability (Arize Phoenix and LangSmith)

### What it is

- **LangSmith**: Tracing and monitoring for LLM and RAG pipelines (latency, token usage, traces).
- **Arize Phoenix**: Open-source observability for ML pipelines; can be used for retrieval and latency analysis.

### Why it was chosen

Traces and metrics support debugging latency and precision and align with evaluation (RAGAS). See [DESIGN-DOCUMENT.md](../research/DESIGN-DOCUMENT.md) and [RECORD-ARCHITECTURE-DECISIONS.md](../research/RECORD-ARCHITECTURE-DECISIONS.md#deployment--observability-decision).

### Setup

- **LangSmith**: Sign up at [LangSmith](https://smith.langchain.com/), get an API key, set `LANGSMITH_API_KEY` in `.env`. Optional for dev; enable in staging/prod.
- **Phoenix**: Optional; run locally or deploy and point the app to the Phoenix server if integrated.
- Set `ENVIRONMENT=dev|staging|prod` so tracing can be enabled per environment.

### How the project uses it

- **Traces**: Instrument query path (embedding → search → rerank → LLM) so each step is visible (latency, inputs/outputs).
- **Metrics**: Track latency (p50, p99), retrieval precision (e.g. via RAGAS), and token usage for cost and performance tuning.
- **Location**: `src/observability/`; instrumentation in retrieval and generation layers.

### Configuration and limits

- When `LANGSMITH_API_KEY` is unset, tracing is skipped so local dev works without an account.
- Sampling can be used in production to limit volume and cost.

### Troubleshooting

- No traces: confirm API key and that the SDK is initialized (e.g. LlamaIndex/LangChain callback or custom tracer).
- High overhead: reduce trace payload size or use sampling.

---

## Evaluation (RAGAS and DeepEval)

### What it is

- **RAGAS**: Metrics for RAG quality (context precision, context recall, faithfulness).
- **DeepEval**: Alternative evaluation framework for RAG and LLM outputs.

### Why it was chosen

To measure precision, recall, and faithfulness against targets (>70% top-5, >90% faithfulness) and to iterate on chunking and prompts. See [DESIGN-DOCUMENT.md](../research/DESIGN-DOCUMENT.md) and [PRE-SEARCH-CHECKLIST.md](../research/PRE-SEARCH-CHECKLIST.md).

### Setup

- Add RAGAS and/or DeepEval to `pyproject.toml` (dev or optional dependency). Run evaluation in CI or manually against a synthetic dataset or golden set.
- Ground truth: build synthetic question-answer pairs from indexed chunks (e.g. “What does paragraph X do?” with expected file/line).

### How the project uses it

- **When**: After retrieval and generation are stable; run on a fixed dataset to detect regressions. Can be part of Epic 5 or 6 and Post-MVP.
- **Metrics**: Context precision/recall (retrieval), faithfulness (no hallucination), and optionally answer relevance. Document targets in the PRD and track in dashboards or CI.
- **Location**: `tests/` or a dedicated `eval/` script; not required at runtime for the main app.

### Configuration and limits

- Evaluation can be slow and token-heavy if it calls the LLM; use a small representative dataset and cache where possible.

### Troubleshooting

- Metric definitions: see RAGAS/DeepEval docs for exact formulas and how to supply references and answers.
- Flaky scores: use a fixed seed and consistent dataset; run multiple times and average if needed.

---

## CI/CD (GitHub Actions)

### What it is

GitHub Actions runs workflows for tests, linting, and optionally ingestion triggers when code changes (e.g. on push to a branch that contains the target codebase).

### Why it was chosen

Automated ingestion updates keep the index current when the legacy codebase changes; CI ensures quality before merge. See [DESIGN-DOCUMENT.md](../research/DESIGN-DOCUMENT.md) and [RECORD-ARCHITECTURE-DECISIONS.md](../research/RECORD-ARCHITECTURE-DECISIONS.md#deployment--observability-decision).

### Setup

- Workflows live in `.github/workflows/`. Add a workflow that runs on push (or schedule) for the repo or a subpath containing the ingested codebase.
- Store secrets (Pinecone, Voyage, Anthropic, Redis, etc.) in GitHub Actions secrets and pass them as env vars to the job. Do not log secrets.
- Ingestion job: clone or use the repo content, run `legacylens ingest` (or equivalent script), and update the Pinecone index. May require a deploy key or token if the codebase is private.

### How the project uses it

- **Tests**: Run pytest (and lint) on every PR/push to `development` or `main`.
- **Ingestion**: Optional workflow that triggers on changes to the legacy code path; runs ingestion and upserts to Pinecone. Consider rate limits and job duration (e.g. 10K LOC <5 min).

### Configuration and limits

- GitHub Actions has concurrent and minute limits per plan; long-running ingestion may need a self-hosted runner or external job queue for large codebases.
- Secrets: use least-privilege keys and rotate periodically.

### Troubleshooting

- Job fails with “missing env”: add the secret in repo settings and reference it in the workflow.
- Ingestion timeout: split into smaller batches or run ingestion outside Actions (e.g. scheduled job elsewhere).

---

## Quick reference

| Component        | Technology              | Key env / config              | Docs link |
| ---------------- | ----------------------- | ----------------------------- | --------- |
| Language         | Python 3.11+            | -                             | [python.org](https://docs.python.org/3/) |
| Framework        | LlamaIndex 0.10+        | -                             | [docs.llamaindex.ai](https://docs.llamaindex.ai/) |
| Vector DB        | Pinecone Serverless     | `PINECONE_API_KEY`            | [docs.pinecone.io](https://docs.pinecone.io/) |
| Embeddings       | Voyage-code-3           | `VOYAGE_API_KEY`              | [docs.voyageai.com](https://docs.voyageai.com/) |
| LLM              | Claude 4.5 Sonnet        | `ANTHROPIC_API_KEY`           | [docs.anthropic.com](https://docs.anthropic.com/) |
| Reranker         | Zerank-2                | Optional model/env            | [huggingface.co](https://huggingface.co/) |
| Graph DB         | Neo4j                   | `NEO4J_URI`, `USER`, `PASSWORD` | [neo4j.com/docs](https://neo4j.com/docs/) |
| Cache            | Redis                   | `REDIS_URL`                   | [redis.io/docs](https://redis.io/docs/) |
| Deployment       | Vercel                  | All API keys in dashboard     | [vercel.com/docs](https://vercel.com/docs) |
| CLI              | Typer, Rich, Pygments   | `LEGACYLENS_API_URL` (optional) | [typer.tiangolo.com](https://typer.tiangolo.com/), [Rich](https://rich.readthedocs.io/), [Pygments](https://pygments.org/) |
| Observability    | LangSmith / Phoenix     | `LANGSMITH_API_KEY`           | [smith.langchain.com](https://docs.smith.langchain.com/), [Arize Phoenix](https://docs.arize.com/phoenix/) |
| Evaluation       | RAGAS / DeepEval        | -                             | [ragas.io](https://docs.ragas.io/), [confident-ai.com](https://docs.confident-ai.com/) |
| CI/CD            | GitHub Actions          | GitHub secrets                | [GitHub Actions](https://docs.github.com/en/actions) |

For a concise table and version pins, see [PRD Appendix D](../PRD.md#appendix-d-tech-stack-quick-reference). For env details, see [ENVIRONMENT-AND-CONFIG.md](ENVIRONMENT-AND-CONFIG.md).
