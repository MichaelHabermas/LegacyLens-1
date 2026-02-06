# LegacyLens Design Document

**Document Version**: 1.0

**Author**: Michael (@habermoose)

**Date**: February 06, 2026

**Based On**: Pre-Search Report (INITIAL.md), Record Architecture Decisions (RECORD-ARCHITECTURE-DECISIONS.md), Identify Tradeoffs (IDENTIFY-TRADEOFFS.md), Tech Stack Options (TECH-STACK-OPTIONS.md), Pre-Search Checklist (PRE-SEARCH-CHECKLIST.md), and Project Specification (G4 Week 2 - LegacyLens.pdf).

## Introduction

LegacyLens is a Retrieval-Augmented Generation (RAG) system designed to make legacy enterprise codebases (e.g., COBOL or Fortran) queryable via natural language. It addresses the challenge of understanding large, undocumented codebases by providing accurate retrieval of code snippets, file/line references, and LLM-generated explanations. The system prioritizes simplicity, precision (>70% top-5), low latency (<3s), and cost efficiency (<$10 for dev), while scaling from MVP (basic pipeline in 24 hours) to production (100-100K users).

This design document locks in the chosen tech stack and methodologies from pre-research, emphasizing a modular architecture adhering to SOLID principles (Single Responsibility, Open-Closed, Liskov Substitution, Interface Segregation, Dependency Inversion). The design is broken down agilely into Epics and User Stories for iterative development. Key decisions incorporate 2026 trends like code-optimized embeddings, hybrid search, GraphRAG for dependencies, and agentic workflows.

**Target Codebase**: GnuCOBOL (open-source COBOL compiler) as the primary, with potential expansion to LAPACK (Fortran). This aligns with the project spec's requirements for ingesting at least one legacy codebase (>10K LOC across 50+ files).

**Overall Goals**:

- Achieve 100% codebase coverage with batch/incremental ingestion.
- Support features like dependency mapping, impact analysis, and code explanations.
- Handle failure modes gracefully (e.g., "I don't know" for no-results).
- Deploy publicly via Vercel, with a CLI query interface.

## Architecture Overview

The system follows a modular, layered architecture:

- **Ingestion Layer**: Parses, chunks, embeds, and stores code.
- **Retrieval Layer**: Handles query embedding, hybrid search, reranking, and context assembly.
- **Generation Layer**: Uses LLM for answer synthesis with citations.
- **Interface Layer**: CLI for natural language queries.
- **Observability & Caching Layer**: Monitoring and optimization.

This modular design ensures SOLID compliance:

- **Single Responsibility**: Each module handles one concern (e.g., chunking module only splits code).
- **Open-Closed**: Modules are extensible via interfaces (e.g., add new parsers without modifying core ingestion).
- **Liskov Substitution**: Subclasses (e.g., COBOL-specific chunker) can replace base classes without breaking behavior.
- **Interface Segregation**: Small, focused interfaces (e.g., IEmbedder for embedding logic).
- **Dependency Inversion**: High-level modules depend on abstractions (e.g., inject vector DB via interface).

Data Flow:

1. Codebase ingested → Chunked (syntax-aware) → Embedded → Stored in Pinecone with metadata.
2. Query → Embedded → Hybrid search → Reranked → Context assembled.
3. Context + Prompt → LLM → Response with citations.
4. Caching (Redis) for repeated embeddings/queries.

## Locked-In Tech Stack

Based on Stack 3 (Managed Cloud) from pre-research, selected for balancing MVP speed, precision, and scalability. All components support legacy code specifics (e.g., AST-based chunking for COBOL paragraphs).

| Component              | Chosen Technology                                                         | Rationale                                                                                                                     | Documentation Link                                                                                                                            |
| ---------------------- | ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **Language/Framework** | Python + LlamaIndex (Workflows 1.0 + LlamaAgents Builder + LlamaParse v2) | Retrieval-focused with low learning curve; supports syntax-aware chunking, agentic refinement, and integrations for GraphRAG. | [LlamaIndex Docs](https://docs.llamaindex.ai/)                                                                                                |
| **Vector Database**    | Pinecone Serverless (managed cloud, hybrid search)                        | Low-latency hybrid search (<100ms p99); free tier for MVP (up to 2GB); metadata filtering for file/line/scope.                | [Pinecone Docs](https://docs.pinecone.io/)                                                                                                    |
| **Embedding Model**    | Voyage-code-3 (API, 1536 dims)                                            | Code-optimized (14-20% better recall on code benchmarks); batch processing with 200M free tokens.                             | [Voyage AI Docs](https://docs.voyageai.com/)                                                                                                  |
| **LLM**                | Claude 4.5 Sonnet (API)                                                   | Strong code reasoning (87% on benchmarks); low hallucination; citation-focused prompting.                                     | [Anthropic Docs](https://docs.anthropic.com/)                                                                                                 |
| **Reranker**           | Zerank-2                                                                  | Precision boost via second-pass reranking; integrates with LlamaIndex.                                                        | [Hugging Face Zerank Model](https://huggingface.co/models?search=zerank) (assuming open-source variant; or custom integration per benchmarks) |
| **Graph Database**     | Neo4j (for GraphRAG dependencies)                                         | Enables dependency mapping (e.g., function calls); integrates with LlamaIndex for advanced features.                          | [Neo4j Docs](https://neo4j.com/docs/)                                                                                                         |
| **Caching**            | Redis                                                                     | Embedding/query caching via content hashes; reduces API calls.                                                                | [Redis Docs](https://redis.io/docs/)                                                                                                          |
| **Deployment**         | Vercel Serverless (free MVP tier)                                         | Quick deploy; auto-scaling; edge functions for low latency.                                                                   | [Vercel Docs](https://vercel.com/docs)                                                                                                        |
| **Query Interface**    | CLI (Python-based, using Rich/Pygments for syntax highlighting)           | Smaller MVP scope; supports natural language input, snippets, citations, and drill-down; backend API publicly accessible.     | [Rich Docs](https://rich.readthedocs.io/en/stable/) / [Pygments Docs](https://pygments.org/docs/)                                             |
| **Observability**      | Arize Phoenix / LangSmith                                                 | Traces for latency/precision; RAGAS metrics for evaluation.                                                                   | [Arize Phoenix Docs](https://docs.arize.com/phoenix/) / [LangSmith Docs](https://docs.smith.langchain.com/)                                   |
| **Evaluation**         | RAGAS / DeepEval                                                          | Measures precision, recall, faithfulness; synthetic datasets for testing.                                                     | [RAGAS Docs](https://docs.ragas.io/en/stable/) / [DeepEval Docs](https://docs.confident-ai.com/docs/)                                         |
| **CI/CD**              | GitHub Actions                                                            | Automated ingestion updates on code changes.                                                                                  | [GitHub Actions Docs](https://docs.github.com/en/actions)                                                                                     |

**Methodologies**:

- **Chunking**: Syntax-aware via AST (LlamaParse v2 for boundaries like COBOL paragraphs/Fortran subroutines) + hierarchical (file → section → function) with 10-25% overlap; fallback to semantic splitting.
- **Retrieval Pipeline**: Query parsing → Embedding → Hybrid search (top-k=20-50) → Zerank-2 rerank (top-5-10) → Context assembly + multi-query expansion (agentic).
- **Ingestion**: Batch for initial, incremental via GitHub Actions; <5 min for 10K LOC.
- **Cost Projections**: Dev: <$10 (free tiers); Production: $5-15/mo (100 users), scaling to $4K-8K/mo (100K users) assuming 5 queries/user/day, 2K tokens/query.
- **Failure Handling**: Graceful fallbacks (e.g., no-results prompt); query expansion for ambiguity; observability for debugging.

## Modular Design

The system is divided into independent modules, each following SOLID principles for maintainability and extensibility. Modules communicate via interfaces/abstract classes in Python (e.g., using ABC from abc module).

1. **Ingestion Module** (Single Responsibility: Handle code parsing and storage).
   - Interfaces: IParser (for language-specific AST), IChunker, IEmbedder, IIndexer.
   - Extensible: Add Fortran parser without changing core (Open-Closed).
   - Dependencies: Injected via constructor (Dependency Inversion).

2. **Retrieval Module** (Single Responsibility: Search and rerank).
   - Interfaces: ISearcher (hybrid search), IReranker.
   - Substitutable: Swap Pinecone for Qdrant via interface (Liskov).
   - Segregated: Separate interfaces for vector vs keyword search.

3. **Generation Module** (Single Responsibility: LLM prompting and response).
   - Interfaces: ILLMProvider.
   - Focused: Only handles synthesis; no retrieval logic.

4. **Interface Module** (Single Responsibility: User input/output).
   - CLI-specific; extensible to web if needed.

5. **Observability Module** (Single Responsibility: Logging/metrics).
   - Integrates across layers without tight coupling.

This modularity allows agile iteration: e.g., develop Ingestion first for MVP.

## Agile Breakdown

Development is structured agilely into Epics (high-level features) and User Stories (actionable items with acceptance criteria). This supports iterative sprints: MVP (24 hours: basic Epics), Early Submission (4 days: full features), Final (7 days: polish). User Stories are prioritized (P1: Must-Have for MVP; P2: Nice-to-Have).

### Epic 1: Codebase Ingestion

- **Description**: Ingest legacy code, chunk, embed, and store with metadata.
- **User Stories**:
  - As a developer, I want to ingest GnuCOBOL codebase files so that all code is indexed (P1). Acceptance: Batch process >10K LOC <5 min; 100% coverage.
  - As a developer, I want syntax-aware chunking for COBOL paragraphs so that logical units are preserved (P1). Acceptance: Use LlamaParse v2; hierarchical with 10-25% overlap.
  - As a developer, I want embeddings generated and cached so that re-ingestion is efficient (P1). Acceptance: Voyage-code-3 API; Redis hashing for skips.
  - As a developer, I want incremental updates triggered on code changes so that the index stays current (P2). Acceptance: GitHub Actions integration.

### Epic 2: Retrieval Pipeline

- **Description**: Embed queries, perform hybrid search, rerank, and assemble context.
- **User Stories**:
  - As a user, I want hybrid search for exact terms like "CUSTOMER-RECORD" so that results are precise (P1). Acceptance: Pinecone hybrid; top-k=20-50; >70% precision.
  - As a user, I want reranking of results so that top-5 are most relevant (P1). Acceptance: Zerank-2; <3s E2E latency.
  - As a user, I want metadata filtering (file/line/scope) in searches so that context is accurate (P1). Acceptance: Include in responses.
  - As a user, I want multi-query expansion for ambiguous queries so that results improve (P2). Acceptance: Agentic via LlamaAgents.

### Epic 3: Answer Generation

- **Description**: Synthesize responses with citations using LLM.
- **User Stories**:
  - As a user, I want LLM-generated explanations with file/line citations so that answers are traceable (P1). Acceptance: Claude 4.5 Sonnet; strict prompting.
  - As a user, I want graceful handling of no-results so that I get "I don't know" instead of hallucinations (P1). Acceptance: Faithfulness metrics >90%.
  - As a user, I want dependency mapping in responses so that I understand impacts (P2). Acceptance: GraphRAG via Neo4j.

### Epic 4: Query Interface

- **Description**: Provide CLI for natural language interaction.
- **User Stories**:
  - As a user, I want a CLI to input queries and view results so that I can interact easily (P1). Acceptance: Natural language; syntax-highlighted snippets via Rich/Pygments.
  - As a user, I want confidence scores and drill-down options so that I can refine queries (P1). Acceptance: Display in output.
  - As a user, I want the backend API publicly accessible so that it meets deployment requirements (P1). Acceptance: Vercel-hosted.

### Epic 5: Observability & Optimization

- **Description**: Monitor, evaluate, and optimize performance.
- **User Stories**:
  - As a developer, I want traces for latency/precision so that I can debug (P1). Acceptance: LangSmith/Phoenix integration.
  - As a developer, I want evaluation metrics so that I can measure success (P2). Acceptance: RAGAS on synthetic datasets.
  - As a developer, I want alerting for failures so that the system is reliable (P2). Acceptance: Thresholds for latency/errors.
