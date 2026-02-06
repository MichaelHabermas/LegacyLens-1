# Pre-Search Checklist

Based on the research and requirements for the **LegacyLens** project, here is the completed Pre-Search Checklist to guide your RAG implementation for legacy codebases. This version incorporates 2026 updates, including current pricing, newer models (e.g., Voyage-code-3, Jina Embeddings v4), enhanced low-cost options (e.g., pgvector, open-source embeddings), and emerging trends like graph-RAG for dependency mapping and agentic workflows for code modernization.

## Phase 1: Define Your Constraints

### 1. Scale & Load Profile

- **Target codebase size?**  
  Minimum 10,000+ lines of code (LOC) across 50+ files to represent enterprise complexity.
- **Query volume and scaling expectations?**  
  Expected to scale from 500 queries/day (pilot) to 500,000 queries/day (enterprise), with support for bursts via serverless options like Pinecone or Turbopuffer.
- **Ingestion strategy (batch vs incremental)?**  
  Batch ingestion for initial setup, with incremental updates via automated pipelines (e.g., GitHub Actions) to detect code changes and update the index without full rebuilds; integrate graph-RAG for real-time dependency updates.
- **Latency requirements?**  
  End-to-end query latency must remain below 3 seconds to maintain developer productivity; achievable with low-latency embeddings like Jina Embeddings v4 and rerankers like Zerank-2.

### 2. Budget & Cost Ceiling

- **Vector database hosting budget?**  
  Free/low-cost starters: Pinecone free up to 2GB, Qdrant free 1GB forever cluster, Zilliz free 5GB; scale to $50-200/mo for 5M-10M vectors with managed services like Pinecone Standard ($50 min, $0.33/GB/mo) or Qdrant Hybrid (custom).
- **Embedding and LLM API cost expectations?**  
  Embeddings: Voyage-code-3 at $0.18 per 1M tokens (200M free); open-source alternatives like nomic-embed-text-v1 or Jina Embeddings v4 (free local). LLM: Claude 3.5 Sonnet ~$3 per 1M input tokens; open-source like DeepSeek-V3.2 or GLM-4.7 (free self-hosted).
- **Trade-offs (managed vs self-hosted)?**  
  Trade money for time by using managed vector databases (Pinecone/Qdrant) to eliminate infrastructure overhead; for low-cost, self-host pgvector (free in Postgres) or Chroma (embedded, free) to avoid usage fees.

### 3. Time to Ship

- **MVP timeline?**  
  24 hours for a basic working RAG pipeline.
- **Which features are must-have vs nice-to-have?**  
  Must-haves: syntax-aware chunking, vector storage, semantic search, and basic answer generation with file/line citations. Nice-to-haves: graph-RAG for dependency mapping, agentic loops for code modernization, translation hints, and impact analysis.
- **Framework learning curve acceptable?**  
  LlamaIndex (with 2026 Workflows 1.0 and LlamaAgents Builder) or LangChain (with LangGraph v1.0) are recommended; LlamaIndex has a lower learning curve for retrieval-heavy tasks, now with enhanced n8n integrations.

### 4. Data Sensitivity

- **Is the codebase open source or proprietary?**  
  The target projects (GnuCOBOL, LAPACK, etc.) are open source.
- **Can you send code to external APIs?**  
  Yes for these open-source targets; external LLM/embedding APIs are acceptable.
- **Data residency requirements?**  
  Proprietary enterprise logic in regulated sectors may require self-hosted, air-gapped models (e.g., DeepSeek-V3.2 or GLM-4.7) to meet security requirements; use Qdrant Private Cloud or Zilliz BYOC for isolated deployments.

### 5. Team & Skill Constraints

- **Familiarity with vector databases?**  
  LlamaIndex or LangChain can accelerate development and abstract much of the vector DB complexity; start with Chroma/pgvector for easy local prototyping.
- **Experience with RAG frameworks (LangChain, LlamaIndex)?**  
  Both are recommended; LlamaIndex (with 2026 updates like LlamaParse v2) is noted for a lower learning curve in retrieval-heavy tasks, while LangChain/LangGraph v1.0 excels in agentic loops.
- **Comfort with the target legacy language?**  
  Lack of deep COBOL/Fortran expertise is addressed by relying on deterministic code structures via Abstract Syntax Trees (AST) rather than purely probabilistic LLM reasoning; enhance with code-specific models like Voyage-code-3.

---

## Phase 2: Architecture Discovery

### 6. Vector Database Selection

- **Managed vs self-hosted?**  
  Pinecone (managed, serverless) or Qdrant (managed/hybrid) for MVP speed; pgvector (self-hosted in Postgres) or Chroma (embedded) for low-cost, high-performance options.
- **Filtering and metadata requirements?**  
  Hybrid search (vector + keyword) supports filtering; metadata is used for file path, line numbers, and scope (see Chunking); add graph support (e.g., Neo4j integration) for dependency queries.
- **Hybrid search (vector + keyword) needed?**  
  Yes. Essential for code; combining vector similarity with keyword search (BM25) is necessary to catch exact variable identifiers or technical terms; Turbopuffer or Weaviate excel here.
- **Scaling characteristics?**  
  Free starters scale to production: Pinecone to unlimited vectors (~$50-200/mo for 5-10M); self-hosted like Qdrant/pgvector scale with your infrastructure (e.g., VPS at ~$5-50/mo).

### 7. Embedding Strategy

- **Code-specific vs general-purpose model?**  
  Use code-specific models like Voyage-code-3, which shows 14-20% improvement in recall on code datasets compared to general-purpose; open-source alternatives like Jina Embeddings v4 (multimodal for code + comments).
- **Dimension size tradeoffs?**  
  Matryoshka learning in models like OpenAI text-embedding-3-large allows shortening vectors (e.g., from 3072 to 256) to reduce storage costs with minimal quality loss; nomic-embed-text-v1 (768 dims) balances well.
- **Local vs API-based embedding?**  
  API-based (e.g., Voyage, OpenAI) for MVP; switch to local open-source (e.g., bge-base-en-v1.5, e5-base-v2) for cost savings and privacy; batch processing reduces API calls.
- **Batch processing approach?**  
  Batch ingestion for initial setup; use content-hash caching (e.g., Redis) to skip reprocessing unchanged files on updates; free 200M tokens with Voyage-code-3.

### 8. Chunking Approach

- **Syntax-aware vs fixed-size?**  
  Syntax-aware chunking via AST is superior to fixed-size splitting for code, using COBOL paragraphs or Fortran subroutines as natural boundaries; integrate graph-RAG for hierarchical chunks (file > function > dependency).
- **Optimal chunk size for your embedding model?**  
  512-8192 tokens with 10-25% overlap to preserve context across logical units, tested with longer-context models like Jina v4 (up to 8,192 tokens).
- **Overlap strategy?**  
  10-25% overlap to preserve context across logical units.
- **Metadata to preserve?**  
  File path, line numbers, entity signatures, and scope chains (e.g., parent function name); add graph metadata for dependencies.

### 9. Retrieval Pipeline

- **Top-k value for similarity search?**  
  Use an initial top-k retrieval (tune per index size, e.g., 20-50); a second-pass re-ranker narrows to the most relevant candidates (top-5-10).
- **Re-ranking approach?**  
  A mandatory second-pass re-ranker (e.g., Zerank-2 or Jina Reranker v2, open-source) assesses top candidates to ensure technical relevance before synthesis; outperforms Cohere v4 in some benchmarks.
- **Context window management?**  
  Re-ranker and citation-focused prompting keep context focused; query simplification can reduce token usage significantly; use agentic query expansion with LangGraph.
- **Multi-query or query expansion?**  
  Use LLMs to simplify complex queries or generate sub-queries to resolve long-range dependencies across multiple files; integrate agentic loops for iterative refinement.

### 10. Answer Generation

- **Which LLM for synthesis?**  
  GLM-4.7 or DeepSeek-V3.2 (open-source) for code reasoning and synthesis; Claude 3.5 Sonnet remains strong for architectural reasoning but consider self-hosted for cost.
- **Prompt template design?**  
  Design prompts for strict citation formatting so the LLM quotes source code with precise file/line references; include agentic instructions for modernization hints.
- **Citation/reference formatting?**  
  Strict citation formatting is required—ensure the LLM quotes source code with precise file/line references.
- **Streaming vs batch response?**  
  Choose per product needs; streaming improves perceived latency for long answers; batch for offline analysis.

### 11. Framework Selection

- **LangChain vs LlamaIndex vs custom?**  
  LlamaIndex (with 2026 LlamaAgents Builder and LlamaParse v2) for retrieval-heavy indexing; LangChain (with LangGraph v1.0) if building complex agentic loops for code modernization.
- **Evaluation and observability needs?**  
  Use frameworks like RAGAS or DeepEval for metrics; Arize Phoenix or LangSmith for trace-level visibility (see Observability); LangGraph v1.0 adds built-in agent monitoring.
- **Integration requirements?**  
  Both integrate with common vector DBs and LLM APIs; choose based on retrieval vs agentic emphasis; n8n updates in LlamaIndex enhance workflow integrations.

---

## Phase 3: Post-Stack Refinement

### 12. Failure Mode Analysis

- **What happens when retrieval finds nothing relevant?**  
  The system must return a graceful "I don't know" fallback rather than hallucinating; use agentic rerouting to refine queries.
- **How to handle ambiguous queries?**  
  Handle vague queries by backend query rewriting or presenting example inputs to the user; integrate multi-query expansion.
- **Rate limiting and error handling?**  
  Define in ops runbook; use observability (Phoenix/LangSmith) to detect failures and latency spikes; agentic error recovery in LangGraph.

### 13. Evaluation Strategy

- **How to measure retrieval precision?**  
  Measure Context Precision, Context Recall, and Faithfulness (hallucination rate) using frameworks like RAGAS or DeepEval; include agentic benchmarks like SWE-Bench.
- **Ground truth dataset for testing?**  
  Use synthetic dataset generation (LLM-as-a-Judge) from indexed code chunks to create baseline test cases; add LegalBench-RAG style for code.
- **User feedback collection?**  
  Combine with faithfulness and recall metrics; user feedback can refine prompts and retrieval params.

### 14. Performance Optimization

- **Caching strategy for embeddings?**  
  Store computed embeddings in Redis using content hashes as keys to skip reprocessing unchanged files; local disk for open-source setups.
- **Index optimization?**  
  Syntax-aware chunking and metadata design (file path, line numbers, scope) support efficient filtering and retrieval; add graph indexes for dependencies.
- **Query preprocessing?**  
  Context-aware chunking and query simplification can reduce token usage by up to 80% per query; agentic preprocessing in LlamaIndex Workflows.

### 15. Observability

- **Logging for debugging retrieval issues?**  
  Use Arize Phoenix or LangSmith (updated v0.13 self-hosted) for trace-level visibility into query execution paths and latency bottlenecks.
- **Metrics to track (latency, precision, usage)?**  
  Track latency, retrieval precision/recall, and token usage; RAGAS/DeepEval for precision and faithfulness; include agent success rates.
- **Alerting needs?**  
  Define thresholds (e.g., latency, error rate) and wire to your ops stack; Phoenix/LangSmith support inspection and debugging.

### 16. Deployment & DevOps

- **CI/CD for index updates?**  
  Use GitHub Actions to trigger automated data pipelines (parsing and upserting) whenever code is committed to specific subdirectories; integrate with LlamaIndex SDKs.
- **Environment management?**  
  Deploy backend services on unified platforms (e.g., Railway, Render ~$5-20/mo); avoid serverless timeouts (e.g., Vercel's 60s limit) for complex RAG; use Qdrant Hybrid for edge.
- **Secrets handling for API keys?**  
  Use the platform’s secret management (e.g., GitHub Actions secrets, Railway/Render env vars); never commit keys; air-gapped for sensitive setups.
