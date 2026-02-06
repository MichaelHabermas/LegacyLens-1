# LegacyLens Record Architecture Decisions

**Document Version**: 1.0

**Based on**: Tech Stack Report (elaborated stacks), Identify Tradeoffs Report (pros/cons, benchmarks), Project Specification (G4 Week 2 - LegacyLens.pdf), Pre-Search Checklist (PRE-SEARCH-CHECKLIST.md with 2026 updates), and testing scenarios/performance targets.

**Scope**: This document records key architecture decisions for the LegacyLens RAG system, focusing on legacy codebases (e.g., COBOL/Fortran like GnuCOBOL or LAPACK). Decisions prioritize MVP delivery (24 hours: basic pipeline), early submission (4 days: full features), and final polish (7 days: deployment/documentation). Chosen elements balance speed, precision (>70% top-5), latency (<3s), cost (<$10 dev), and scalability (100-100K users).

**Overall Rationale**: Emphasize accurate retrieval over complexity, per project guidance ("simple RAG with accurate retrieval beats complex garbage"). Leverage 2026 trends: code-optimized embeddings, hybrid search, GraphRAG for dependencies, agentic workflows for refinement. All decisions support syntax-aware chunking (AST-based for paragraphs/subroutines), metadata (file/line/scope), and features (e.g., dependency mapping, impact analysis).

**Failure Modes Considered**: Addressed via graceful fallbacks (e.g., "I don't know" for no-results), query expansion for ambiguity, and observability (e.g., LangSmith traces).

**Next Steps**: Use this for RAG Architecture Doc submission (1-2 pages), interview prep (e.g., discuss tradeoffs), and iteration based on evaluation (RAGAS metrics, SWE-Bench for code).

## Chosen Overall Architecture: Stack 3 - Managed Cloud

**Design**: Python backend with LlamaIndex (Workflows 1.0 + LlamaAgents Builder for agentic refinement and LlamaParse v2 for syntax chunking). Vector DB: Pinecone serverless (managed cloud, hybrid search). Embeddings: Voyage-code-3 (API, 1536 dims). LLM: Claude 4.5 Sonnet (API). Deployment: Vercel serverless (free MVP tier). Additional: Zerank-2 reranker for precision, Neo4j integration for GraphRAG (dependencies), Redis for embedding caching.

**Rationale**: Balances MVP speed (low learning curve, managed ops) with production targets: <3s E2E latency via serverless, >80% precision on code recall (Voyage + hybrid), 100% coverage for 10K+ LOC ingestion (<5 min batch). Supports 4+ code features (e.g., dependency mapping via GraphRAG, impact analysis via agents). Cost-effective dev (<$10 using free tiers/200M Voyage tokens); scales to 100K users (~$4K-8K/mo assuming 5 queries/user/day, 2K tokens/query, 1% monthly churn). Aligns with Pre-Search Phase 1 (budget/time constraints) and Phase 2 (retrieval-focused). Tested against scenarios like "Explain CALCULATE-INTEREST" with correct file/line citations.

**Alternatives Considered**:

- Stack 1 (Local Open-Source: ChromaDB + nomic-embed + DeepSeek-V3.2): For $0 cost/privacy; rejected for scalability limits (no auto-scaling for bursts) and lower precision (65-75% without hybrid).
- Stack 4 (Enterprise Scale: Qdrant + LangChain + OpenAI embeddings + GPT-5.2): For GPU/large codebases; rejected for higher MVP complexity (LangChain overhead) and cost ($10-20 dev).
- Stack 5 (GraphRAG Enhanced: Weaviate + Qwen3 + Gemini): If dependencies primary; alternative for long-context but adds ops burden early.

  **Impact on Project**: Enables basic retrieval first (priority 7-10 in Build Strategy), then advanced features (11-14); meets AI Cost Analysis (dev spend breakdown, projections).

## Vector Database Decision

**Chosen**: Pinecone serverless (managed cloud, free tier up to 2GB).

**Rationale**: Selected for production scale (unlimited vectors, <100ms p99 latency) and easy setup (no ops overhead, fits 24-hour MVP). Native hybrid search (vector + BM25) essential for legacy code (exact terms like "CUSTOMER-RECORD" + semantic). Supports metadata filtering (file/path/line) and scaling characteristics (RU-based, auto-index optimization). Per tradeoffs, low complexity vs self-hosted; free tier covers 50K vectors (~10K LOC codebase). Aligns with Pre-Search Phase 2 (managed vs self-hosted, hybrid needed).

**Alternatives Considered**:

- Qdrant (managed/hybrid): For Rust speed/GPU; rejected for slight higher config complexity in MVP.
- pgvector/ChromaDB (self-hosted/embedded): For $0 cost/SQL familiarity; rejected for no native hybrid (drops precision 10-15%) and limited scale.
- Weaviate/Milvus: For GraphQL/GPU; overkill for initial, but viable add-on for GraphRAG.

  **Edge Cases**: Handles large queries via top-k=20-50 + rerank; failure mode: high RU on bursts mitigated by caching.

## Embedding Strategy Decision

**Chosen**: Voyage-code-3 (API, 1536 dims, code-optimized; batch processing with 10-25% overlap).

**Rationale**: Code-specific model outperforms generals by 14-20% on recall (MTEB/code benchmarks), ideal for legacy syntax (COBOL paragraphs, Fortran subroutines). 200M free tokens cover dev ingestion/updates; Matryoshka-like flexibility for dimension reduction if storage scales. Fits chunking (512-8192 tokens) and metadata preservation (scope chains). Per Phase 2, API-based for MVP speed; local fallback possible.

**Alternatives Considered**:

- OpenAI text-embedding-3-large (3072 dims): Higher quality general but weaker on code (+ higher cost post-free).
- nomic-embed-text-v1/bge-base (local, 768 dims): $0/privacy; rejected for 5-10% lower precision on technical terms.
- Jina Embeddings v4: Multimodal alternative if comments heavy; similar but Voyage edges on code datasets.  
  **Edge Cases**: Batch skips via content-hash (Redis); failure: API downtime → local fallback plan.

## Chunking Approach Decision

**Chosen**: Syntax-aware via AST (LlamaParse v2 for boundaries: functions/paragraphs/subroutines) + hierarchical (file → section → function) with 10-25% overlap; fallback semantic splitting (LLM for unstructured).

**Rationale**: Legacy code demands natural boundaries to preserve logic (e.g., COBOL PARAGRAPH); AST > fixed-size for precision (+20-30% context retention). Hierarchical + overlap meets retrieval needs (top-k assembly with surrounding context). Per project, document approach; aligns with Pre-Search Phase 8 (optimal size for embeddings). Ingestion throughput: <5 min for 10K LOC.

**Alternatives Considered**:

- Fixed-size + overlap: Simple fallback; rejected as primary (loses logical units in legacy).
- Semantic (LLM-only): Accurate but slow/costly for batch; used as hybrid.

  **Edge Cases**: Overlap handles cross-boundary queries; failure: ambiguous boundaries → manual review in eval.

## Retrieval Pipeline Decision

**Chosen**: Query processing (parse NL, extract entities) → embedding (same model) → hybrid similarity search (top-k=20-50) → Zerank-2 rerank (top-5-10) → context assembly (with metadata) + multi-query expansion (agentic via LlamaAgents).

**Rationale**: Ensures >70% precision via multiphase (hybrid + rerank reduces noise); agentic expansion for ambiguous tests (e.g., "Show error handling patterns"). Context window management via focused prompting/citations. Per Phase 2/3, re-ranking mandatory; low latency (<3s E2E).

**Alternatives Considered**:

- No rerank: Faster but <70% precision.
- LangGraph loops: More agentic; rejected for added complexity in MVP.

  **Edge Cases**: No-relevant → fallback prompt; rate limiting via Vercel.

## Answer Generation Decision

**Chosen**: Claude 4.5 Sonnet with citation-focused prompts (strict file/line refs, streaming response).

**Rationale**: Strong code reasoning (87% benchmarks), low hallucination; fits synthesis (e.g., "Explain function in English"). Prompt templates enforce accuracy; streaming for UX. Per Phase 10, Claude over open-source for depth.

**Alternatives Considered**:

- GPT-5.2 Codex: Similar quality, higher cost.
- DeepSeek-V3.2: $0/self-hosted; rejected for inference latency.

  **Edge Cases**: Hallucination → faithfulness metrics in eval.

## Framework Decision

**Chosen**: LlamaIndex (retrieval/document-focused).

**Rationale**: Lower curve for indexing/chunking; integrations for eval/observability. Per tradeoffs, better token efficiency.

**Alternatives Considered**:

- LangChain: Agentic; higher overhead.
- Custom: Control; too time-intensive.

## LLM Decision

**Chosen**: Claude 4.5 Sonnet.  
**Rationale**: Balanced cost/quality for code; see tradeoffs.  
**Alternatives Considered**: Open-source for savings.

## Query Interface Decision

**Chosen**: CLI as the primary (and only, at this stage) query interface.

**Rationale**: The project specification allows "CLI or web" for the natural-language query interface. A CLI keeps the MVP scope smaller (no frontend framework or deployment), fits the existing Python/LlamaIndex backend, and still meets required behaviors: natural language input, display of code snippets with syntax highlighting (terminal via e.g. Rich/Pygments), file/line references, confidence scores, LLM-generated answer, and drill-down (e.g. via a `show` command or flag). The deployed backend (API) remains publicly accessible; the CLI is the client used to interact with it.

**Alternatives Considered**:

- Web (React/Next.js): Richer UX and in-browser syntax highlighting; rejected for current phase to reduce scope and avoid a separate frontend stack.
- Streamlit: Fast web UI from Python; rejected in favor of a dedicated CLI for consistency with the "CLI" choice and simpler deployment story.

**Impact**: No change to vector DB, embeddings, chunking, LLM, or deployment. Backend exposes a query API; CLI consumes it. Building (backend + CLI) is a later effort, not this one; implementation of the CLI is deferred until the RAG pipeline and API are in place.

## Deployment & Observability Decision

**Chosen**: Vercel serverless; Arize Phoenix/LangSmith for traces/metrics (latency, precision, usage). CI/CD via GitHub Actions for updates.  
**Rationale**: Free/quick deploy; secrets via env vars. Per Phase 3/16, auto-updates for code churn.  
**Alternatives Considered**: Railway/AWS: Similar; Vercel edges on edge functions.

## Performance Optimization & Evaluation Decision

**Chosen**: Caching (Redis hashes), index opt (metadata filtering), eval with RAGAS/DeepEval (precision/recall/faithfulness); ground truth from synthetic datasets.  
**Rationale**: Meets targets; user feedback loop. Per Phase 3.  
**Alternatives Considered**: SWE-Bench for code-specific.

## Cost Projections & Analysis

**Dev Spend**: <$10 (free tiers).  
**Projections**: As in tradeoffs (e.g., 100 users: $5-15/mo). Assumptions: 5 q/day, 2K tokens/q.  
**Rationale**: Tracks embedding/LLM/DB; trade money for time (managed services).
