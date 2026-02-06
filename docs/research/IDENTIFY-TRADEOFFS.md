# LegacyLens Identify Tradeoffs

**Document Version**: 1.0

**Based on**: Tech Stack Report (chosen **Stack 3**: Python + LlamaIndex Workflows 1.0 + Pinecone serverless + Voyage-code-3 + Claude Sonnet 4.5 + Vercel) and alternatives.

**Data Sources**: 2026 pricing (Pinecone, Voyage AI, Anthropic), MTEB/code retrieval benchmarks (nDCG@10, code recall), framework overhead studies, project targets (<3s E2E latency, >70% top-5 precision, 10K+ LOC ingestion <5 min, hybrid search for legacy identifiers).

**Scope**: Tradeoffs evaluated across **performance** (latency/precision/recall), **cost**, **scalability**, **complexity/maintainability**, and **legacy-code suitability** (syntax-aware/AST chunking, exact term matching via hybrid search, GraphRAG for dependencies, citation accuracy for file/line refs).

## Vector Database Tradeoffs

Chosen: **Pinecone serverless** (Stack 3) – serverless scaling, low p99 latency, native hybrid search.

| Database            | Latency (p99, hybrid query) | Precision (top-5, code RAG) | Storage Cost (10K LOC ≈ 50K vectors, ~10-50 MB) | Query Cost Example (5 q/user/day, 100 users) | Scalability            | Complexity / Ops Overhead | Legacy-Code Fit                                                                            |
| ------------------- | --------------------------- | --------------------------- | ----------------------------------------------- | -------------------------------------------- | ---------------------- | ------------------------- | ------------------------------------------------------------------------------------------ |
| Pinecone (chosen)   | <100 ms                     | 78-85% (hybrid + rerank)    | <$1/mo                                          | $2-8/mo (RU dominant)                        | Unlimited (serverless) | Low (managed)             | Excellent – fast hybrid for COBOL vars/Fortran calls; metadata filtering (file/line/scope) |
| Qdrant (managed)    | 80-150 ms                   | 80-87%                      | Free (1 GB) → $0.20-0.40/GB                     | $3-12/mo                                     | High (GPU opt.)        | Medium (config filtering) | Strong hybrid + Rust speed; good for large LAPACK                                          |
| ChromaDB / pgvector | 200-800 ms (local)          | 65-75%                      | $0                                              | $0                                           | Millions of vectors    | Low (embedded/SQL)        | Good for MVP/AST testing; no native hybrid → falls back to keyword                         |
| Weaviate            | 120-250 ms                  | 79-84% (GraphQL hybrid)     | $0.25-0.50/GB                                   | $5-15/mo                                     | High                   | Medium-High (modules)     | Best for GraphRAG dependencies                                                             |

**Key Tradeoffs**:

- Managed (Pinecone/Qdrant) → 5-10× lower latency & ops effort vs self-hosted, but $50/mo Pinecone minimum + RU scaling (reads dominate for retrieval-heavy code queries).
- Hybrid search (vector + BM25) → +15-25% precision on exact identifiers (CUSTOMER-RECORD) but +10-20% latency vs pure vector.
- For 10K LOC codebase: Pinecone storage negligible; cost driven by queries (chosen Stack 3 stays under $50 min at low volume).

## Embedding Model Tradeoffs

Chosen: **Voyage-code-3** (1536 dims, code-optimized).

| Model                          | Code Recall / nDCG@10 | MTEB Score | Latency (embed 1 chunk) | Cost per 1M tokens (after free tier) | Dimensions (flexible)   | Legacy-Code Fit                                                                              |
| ------------------------------ | --------------------- | ---------- | ----------------------- | ------------------------------------ | ----------------------- | -------------------------------------------------------------------------------------------- |
| Voyage-code-3 (chosen)         | +14-20% vs general    | 66.8       | 25-35 ms                | $0.18                                | 1536                    | Best – optimized for code structure/comments; strong on Fortran subroutines/COBOL paragraphs |
| OpenAI text-embedding-3-large  | Baseline              | 64.6       | 10-15 ms                | $0.13                                | 3072 → 256 (Matryoshka) | Good general; weaker on legacy syntax                                                        |
| nomic-embed-text-v1 / bge-base | -5-10% vs Voyage      | ~62        | 5-15 ms (local GPU)     | $0                                   | 768                     | Free/local; sufficient for MVP but lower precision on technical terms                        |

**Key Tradeoffs**:

- Code-specific (Voyage-code-3) → 14-20% higher recall/precision on legacy code retrieval vs general models, but ~2× slower embedding latency and higher cost post-free-tier (200M tokens free covers initial 10K LOC + moderate updates).
- Dimension reduction (Matryoshka) → 4-8× storage savings with <3% quality drop – useful for scaling Pinecone storage cost.
- Local open-source → $0 cost/privacy but requires GPU for batch speed; drops top-5 precision below 70% target without reranking.

## Framework Tradeoffs

Chosen: **LlamaIndex (Workflows 1.0 + LlamaAgents Builder)** – retrieval-first.

| Framework             | Overhead (per query) | Tokens/query (avg) | Precision (code RAG)       | Learning Curve | Agentic / GraphRAG Support             | Legacy-Code Fit                                                              |
| --------------------- | -------------------- | ------------------ | -------------------------- | -------------- | -------------------------------------- | ---------------------------------------------------------------------------- |
| LlamaIndex (chosen)   | ~6 ms                | ~1.60k             | 82-88% (retrieval-focused) | Low-Medium     | Strong (LlamaParse v2, Agents Builder) | Excellent – built-in syntax chunking, hierarchical indexes, citation tracing |
| LangChain / LangGraph | 10-14 ms             | ~2.40k             | 78-84%                     | Medium-High    | Best (LangGraph v1.0 loops)            | Good for multi-query/impact analysis but higher token/latency overhead       |
| Custom                | Variable             | Variable           | Depends                    | High           | Full control                           | Learning exercise only                                                       |

**Key Tradeoffs** (2026 benchmarks):

- LlamaIndex → lower orchestration overhead & token usage → helps meet <3s E2E & reduces LLM cost; retrieval-first design improves traceability (file/line citations).
- LangChain → more flexible agents but +50-100% tokens/query → higher Claude cost & latency risk.

## LLM Tradeoffs

Chosen: **Claude Sonnet 4.5** (balanced reasoning).

| LLM                                   | Code Reasoning (LiveCodeBench/SWE-Bench) | Input/Output Cost per MTok | Latency (200-500 tok output) | Hallucination Rate (with citations) | Context Window | Legacy-Code Fit                                                                 |
| ------------------------------------- | ---------------------------------------- | -------------------------- | ---------------------------- | ----------------------------------- | -------------- | ------------------------------------------------------------------------------- |
| Claude Sonnet 4.5 (chosen)            | 87%                                      | $3 / $15                   | 400-800 ms                   | Low (strong citation prompting)     | 200K           | Excellent – careful explanations, low hallucination on undocumented COBOL logic |
| GPT-5.2 Codex                         | 89%                                      | Higher (~$15/$75 est.)     | 300-600 ms                   | Medium                              | 1M+            | Strong structured output                                                        |
| DeepSeek-V3.2 / GLM-4.7 (open-source) | 82-85%                                   | $0 (self-host)             | 500-1500 ms (hardware dep.)  | Medium-High                         | 128K-1M        | Cost-free but higher inference latency & tuning needed                          |

**Key Tradeoffs**:

- Proprietary (Claude) → superior reasoning + low hallucination on business logic/dependency mapping, but API cost dominates at scale (prompt caching → 90% savings on repeated code context).
- Open-source → eliminates token cost but requires GPU/CPU resources and may need heavier prompting for precise file/line citations.

## Stack-Specific Tradeoffs Summary

| Stack                         | Performance (Latency/Precision) | Monthly Cost (1K users) | Scalability | Complexity | Best Legacy Fit                  |
| ----------------------------- | ------------------------------- | ----------------------- | ----------- | ---------- | -------------------------------- |
| 1. Local Open-Source (Chroma) | Medium / 70-75%                 | $0-5                    | Low         | Low        | MVP testing                      |
| 2. Budget Hybrid (pgvector)   | Medium / 72-78%                 | $10-30                  | Medium      | Low-Medium | Incremental updates              |
| 3. Managed Cloud (chosen)     | High / 80-87%                   | $40-80                  | High        | Low        | Production balance               |
| 4. Enterprise (Qdrant)        | High / 82-88%                   | $80-150                 | Very High   | Medium     | Large codebases                  |
| 5. GraphRAG (Weaviate)        | High / 85-90% (deps)            | $100-250                | High        | High       | Dependency/impact analysis       |
| 6. Custom Agentic (Milvus)    | High / 83-88%                   | $150-400                | High        | Very High  | Full control / advanced features |

## Overall RAG Tradeoffs for Legacy Code

- **Performance vs Cost**: Hybrid + reranker (Zerank-2/Jina) → >70% precision target at <3s E2E but +15-30% latency & cost; GraphRAG → +30-40% dependency accuracy but 3-5× LLM calls.
- **Scalability vs Complexity**: Serverless Pinecone + LlamaIndex → auto-scales to 500K q/day with minimal ops; agentic loops add failure modes (loops, over-refinement).
- **Accuracy vs Latency**: Syntax-aware (AST paragraphs/subroutines) + 10-25% overlap + hierarchical chunks → preserves context across legacy boundaries but increases chunk count/storage ~20%.
- **Failure Modes**: No-results → graceful fallback + query expansion (agentic in LlamaIndex); ambiguous queries → multi-query / clarification prompts; legacy-specific: exact identifier misses → mandatory hybrid search.
- **Production Cost Projections** (chosen Stack 3, 5 q/user/day, 2K tokens/query, 1% monthly code churn):
  - 100 users: ~$5-15/mo
  - 1K users: ~$40-80/mo
  - 10K users: ~$400-800/mo
  - 100K users: ~$4K-8K/mo (RU + Claude dominant; caching/rerank optimization critical)

## Query Interface Tradeoff (CLI vs Web)

The project specification permits either a CLI or a web interface for the natural-language query. **Chosen: CLI.**

| Option | Pros | Cons |
|--------|------|------|
| **CLI (chosen)** | No frontend stack; single Python surface; terminal syntax highlighting (e.g. Rich/Pygments); fits "deployed and publicly accessible" via backend API + client CLI; smaller MVP scope. | Less discoverable than a web UI; no in-browser interactivity. |
| Web (React/Next.js) | Richer UX; in-browser highlighting; shareable links. | Extra stack, build, and deployment; broader scope for current phase. |

Required query-interface behaviors (natural language input, code snippets with file/line, scores, LLM answer, drill-down) are achievable in the CLI. Building (backend + CLI) is a later effort, not this one; implementation is deferred until the RAG pipeline and API exist.

## Rationale for Chosen Stack 3

Balances MVP 24-hour delivery (LlamaIndex low curve, Pinecone easy API) with targets: Voyage-code-3 + hybrid + Claude achieves >80% precision/<3s latency while staying under Pinecone $50 min at pilot scale. Alternatives traded either cost (local) or complexity (GraphRAG-first). Document failure modes & metrics in RAG Architecture Doc for iteration.
