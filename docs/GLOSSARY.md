# LegacyLens Glossary

Short definitions of terms used across the PRD, design doc, tradeoffs, and tech stack documentation. Use this when you need a shared meaning for a term.

---

## A–C

**AST (Abstract Syntax Tree)**  
A tree representation of source code structure (e.g. paragraphs, subroutines, blocks). Used for [syntax-aware chunking](#syntax-aware-chunking) so chunks follow logical boundaries instead of arbitrary character counts.

**BM25**  
A keyword-based ranking function often used for sparse search. In LegacyLens, combined with vector search in [hybrid search](#hybrid-search) to match exact identifiers (e.g. variable names) in code.

**Chunk**  
A segment of code (or text) that is embedded and stored as a single unit in the vector database. In LegacyLens, chunks are produced by syntax-aware chunking and carry metadata (file path, line numbers, scope).

**Chunking**  
The process of splitting a codebase into [chunks](#chunk). **Fixed-size chunking** uses character or token limits and may split logical units. **Syntax-aware chunking** uses language boundaries (e.g. COBOL paragraphs, Fortran subroutines). **Hierarchical chunking** organizes units at multiple levels (e.g. file → section → function).

**Citation**  
A reference to the source of an answer, typically a file path and line number(s). LegacyLens prompts the LLM to cite only retrieved context so answers are traceable and hallucinations are reduced.

**Context assembly**  
Building the string (and structure) passed to the LLM from the reranked chunks and their metadata, within the model’s context window.

---

## E–G

**Embedding**  
A dense vector representation of text or code produced by an embedding model. Similar content has similar vectors; similarity search over embeddings finds semantically related chunks.

**E2E latency (End-to-end latency)**  
Total time from the user issuing a query to receiving the final answer. LegacyLens targets <3s E2E.

**Faithfulness**  
In RAG evaluation (e.g. RAGAS), the extent to which the generated answer is supported by the retrieved context (no unsupported claims or “hallucinations”). LegacyLens targets high faithfulness (e.g. >90%).

**GraphRAG**  
An approach that augments RAG with a graph (e.g. Neo4j) of entities and relationships (e.g. call graphs, dependencies). Used in LegacyLens for dependency mapping and impact analysis (post-MVP).

---

## H–L

**Hybrid search**  
Search that combines vector similarity (dense retrieval) with keyword/sparse search (e.g. BM25). In LegacyLens, Pinecone hybrid search is used so both semantic similarity and exact identifiers (e.g. `CUSTOMER-RECORD`) are captured.

**LlamaIndex**  
A retrieval-focused framework for building RAG pipelines (indexing, chunking, embedding, vector stores, query flows). LegacyLens uses LlamaIndex with Workflows 1.0, LlamaAgents Builder, and LlamaParse v2.

**LlamaParse**  
A LlamaIndex component (v2 in LegacyLens) used for parsing documents and code with structure-aware boundaries (e.g. for syntax-aware chunking).

**Logical unit**  
A coherent piece of code defined by the language (e.g. a COBOL paragraph, a Fortran subroutine). Chunking aims to keep logical units intact when possible.

---

## P–R

**Precision**  
In retrieval: the fraction of retrieved items that are relevant (e.g. top-5 precision = how many of the top 5 results are correct). LegacyLens targets >70% top-5 precision. In RAGAS, “context precision” measures how much of the retrieved context is relevant to the question.

**Recall**  
In retrieval: the fraction of relevant items that are retrieved. In RAGAS, “context recall” measures how much of the ground-truth context was retrieved.

**RAG (Retrieval-Augmented Generation)**  
A pattern where relevant information is retrieved from a store, added to the LLM’s context, and the model generates an answer grounded in that context. LegacyLens is a RAG system for legacy codebases.

**Reranker**  
A second-pass model that scores the top-k results from initial search and selects the best few (e.g. top-5–10) for context assembly. LegacyLens uses Zerank-2 to improve precision.

**RU (Request Units)**  
Pinecone’s unit of consumption for serverless indexes (reads/writes). Cost scales with RU usage; caching reduces read RUs.

**Scope chain**  
Metadata that describes the lexical scope of a chunk (e.g. parent function or paragraph name). Stored with the chunk and used for filtering or display.

---

## S–Z

**Serverless**  
A model where the provider runs and scales infrastructure automatically (e.g. Pinecone serverless, Vercel functions). No explicit server management.

**Syntax-aware chunking**  
Chunking that respects language structure (e.g. [AST](#ast)-based boundaries like COBOL paragraphs or Fortran subroutines) so chunks are logical units rather than arbitrary slices.

**Top-k**  
The number of results returned from the first-stage search (e.g. 20–50) before [reranking](#reranker) trims to a smaller set (e.g. top-5–10) for context assembly.

**Vector database**  
A store that holds [embeddings](#embedding) (vectors) and supports similarity search (and often metadata filtering). LegacyLens uses Pinecone as the vector database.
