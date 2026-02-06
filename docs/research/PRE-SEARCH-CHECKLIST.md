Questions:

3. Time to Ship
• MVP timeline?
• Which features are must-have vs nice-to-have?
• Framework learning curve acceptable?
4. Data Sensitivity
• Is the codebase open source or proprietary?
• Can you send code to external APIs?
• Data residency requirements?
5. Team & Skill Constraints
• Familiarity with vector databases?
• Experience with RAG frameworks (LangChain, LlamaIndex)?
• Comfort with the target legacy language?
Phase 2: Architecture Discovery
6. Vector Database Selection
• Managed vs self-hosted?
• Filtering and metadata requirements?
• Hybrid search (vector + keyword) needed?
• Scaling characteristics?
7. Embedding Strategy
• Code-specific vs general-purpose model?
• Dimension size tradeoffs?
• Local vs API-based embedding?
• Batch processing approach?
8. Chunking Approach
• Syntax-aware vs fixed-size?
• Optimal chunk size for your embedding model?
• Overlap strategy?
• Metadata to preserve?
9. Retrieval Pipeline
• Top-k value for similarity search?
• Re-ranking approach?
• Context window management?
• Multi-query or query expansion?
10. Answer Generation
• Which LLM for synthesis?
• Prompt template design?
• Citation/reference formatting?
• Streaming vs batch response?
11. Framework Selection
• LangChain vs LlamaIndex vs custom?
• Evaluation and observability needs?
• Integration requirements?
Phase 3: Post-Stack Refinement
12. Failure Mode Analysis
• What happens when retrieval finds nothing relevant?
• How to handle ambiguous queries?
• Rate limiting and error handling?
13. Evaluation Strategy
• How to measure retrieval precision?
• Ground truth dataset for testing?
• User feedback collection?
14. Performance Optimization
• Caching strategy for embeddings?
• Index optimization?
• Query preprocessing?
15. Observability
• Logging for debugging retrieval issues?
• Metrics to track (latency, precision, usage)?
• Alerting needs?
16. Deployment & DevOps
• CI/CD for index updates?
• Environment management?
• Secrets handling for API keys?


Answers:

Based on the research and requirements for the **LegacyLens** project, here is the completed Pre-Search Checklist to guide your RAG implementation for legacy codebases.

### Phase 1: Define Your Constraints

**1. Scale & Load Profile**

* **Target Codebase Size:** Minimum 10,000+ lines of code (LOC) across 50+ files to represent enterprise complexity `[1]`.
* **Query Volume:** Expected to scale from 500 queries/day (pilot) to 500,000 queries/day (enterprise) `[2, 3]`.
* **Ingestion:** Batch ingestion for initial setup, with incremental updates via automated pipelines to detect code changes and update the index without full rebuilds `[4, 5]`.
* **Latency:** End-to-end query latency must remain below 3 seconds to maintain developer productivity `[1]`.

**2. Budget & Cost Ceiling**

* **Vector Database Hosting:** Managed services like Pinecone start at ~$30–$70/mo for starter tiers, scaling to $500–$2,000/mo for 5M–10M vectors `[2]`.
* **Embedding API:** OpenAI `text-embedding-3-small` is highly cost-efficient at $0.02 per 1M tokens, while Voyage Code 2 (optimized for code) is $0.12 per 1M tokens `[6, 7]`.
* **LLM API:** GPT-4o costs ~$2.50 per 1M input tokens; Claude 3.5 Sonnet is ~$3.00 per 1M input tokens `[8, 9]`.
* **Trade-offs:** Trade money for time by using managed vector databases (Pinecone/Zilliz) to eliminate infrastructure overhead like monitoring and scaling `[10, 11]`.

**3. Time to Ship**

* **MVP Timeline:** 24 hours for a basic working RAG pipeline `[1]`.
* **Must-Haves:** Syntax-aware chunking, vector storage, semantic search, and basic answer generation with file/line citations `[1]`.
* **Nice-to-Haves:** Advanced features like dependency mapping, translation hints, and impact analysis `[1]`.

**4. Data Sensitivity**

* **Codebase Type:** The target projects (GnuCOBOL, LAPACK, etc.) are open source, allowing the use of external LLM/embedding APIs `[1]`.
* **Data Residency:** Proprietary enterprise logic in regulated sectors may require self-hosted, air-gapped models like DeepSeek Coder V2 to meet security requirements `[12, 13]`.

**5. Team & Skill Constraints**

* **Frameworks:** LangChain or LlamaIndex are recommended to accelerate development, though LlamaIndex is noted for a lower learning curve in retrieval-heavy tasks `[14, 15]`.
* **Legacy Languages:** Lack of deep COBOL/Fortran expertise requires a reliance on deterministic code structures via Abstract Syntax Trees (AST) rather than purely probabilistic LLM reasoning `[16, 17]`.

---

### Phase 2: Architecture Discovery

**6. Vector Database Selection**

* **Managed vs. Self-Hosted:** Pinecone (Managed) is ideal for MVP speed; Qdrant (Self-hosted) offers high Rust-based performance and efficient memory mapping `[11]`.
* **Hybrid Search:** Essential for code; combining vector similarity with keyword search (BM25) is necessary to catch exact variable identifiers or technical terms `[10, 18]`.

**7. Embedding Strategy**

* **Model:** Use code-specific models like `voyage-code-2`, which shows a 14.52% improvement in recall on code datasets compared to general-purpose models `[19, 20]`.
* **Dimension Trade-offs:** Matryoshka learning in models like `text-embedding-3-large` allows shortening vectors (e.g., from 3072 to 256) to reduce storage costs with minimal quality loss `[21, 22]`.

**8. Chunking Approach**

* **Strategy:** Syntax-aware chunking via cAST (Abstract Syntax Trees) is superior to fixed-size splitting for code, using COBOL paragraphs or Fortran subroutines as natural boundaries `[23, 17]`.
* **Chunk Size/Overlap:** Optimal size is 400–1,000 tokens with 10–25% overlap to preserve context across logical units `[24, 25]`.
* **Metadata:** Preserve file path, line numbers, entity signatures, and scope chains (e.g., parent function name) `[26, 27]`.

**9. Retrieval Pipeline**

* **Re-ranking:** A mandatory second-pass re-ranker (e.g., Cohere Rerank) assesses top candidates to ensure technical relevance before synthesis `[2, 28]`.
* **Query Expansion:** Use LLMs to simplify complex queries or generate sub-queries to resolve long-range dependencies across multiple files `[29, 30]`.

**10. Answer Generation**

* **Synthesis LLM:** Claude 3.5 Sonnet is the current gold standard for project-level architectural reasoning and complex debugging `[12, 31]`.
* **Prompting:** Strict citation formatting is required to ensure the LLM quotes source code with precise file/line references `[32, 7]`.

**11. Framework Selection**

* **Choice:** LlamaIndex for retrieval-heavy indexing; LangChain (with LangGraph) if building complex agentic loops for code modernization `[14, 32]`.

---

### Phase 3: Post-Stack Refinement

**12. Failure Mode Analysis**

* **Missing Content:** If no relevant code is found, the system must return a graceful "I don't know" fallback rather than hallucinating `[33, 34]`.
* **Ambiguity:** Handle vague queries by backend query rewriting or presenting example inputs to the user `[33, 30]`.

**13. Evaluation Strategy**

* **Metrics:** Measure Context Precision, Context Recall, and Faithfulness (hallucination rate) using frameworks like RAGAS or DeepEval `[35, 36, 37]`.
* **Ground Truth:** Use synthetic dataset generation (LLM-as-a-Judge) from indexed code chunks to create baseline test cases `[38, 39]`.

**14. Performance Optimization**

* **Caching:** Store computed embeddings in Redis using content hashes as keys to skip reprocessing unchanged files `[40]`.
* **Token Efficiency:** Context-aware chunking and query simplification can reduce token usage by up to 80% per query `[41, 29]`.

**15. Observability**

* **Tools:** Arize Phoenix or LangSmith for trace-level visibility into query execution paths and latency bottlenecks `[42, 43]`.

**16. Deployment & DevOps**

* **CI/CD:** Use GitHub Actions to trigger automated data pipelines (parsing and upserting) whenever code is committed to specific subdirectories `[5, 44]`.
* **Hosting:** Deploy backend services on unified platforms like Railway or Render to avoid serverless timeouts (Vercel's default 60s limit) during complex RAG operations `[45, 46, 47]`.
