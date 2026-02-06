# LegacyLens

RAG-powered system to query legacy enterprise codebases (e.g. COBOL, Fortran) in natural language.

## Overview

LegacyLens ingests legacy code, indexes it with syntax-aware chunking and embeddings, and answers questions via a CLI with file/line citations. It targets codebases like GnuCOBOL (10K+ LOC) and uses Python, LlamaIndex, Pinecone, Voyage-code-3 embeddings, and Claude for generation.

## Prerequisites

- **Python** 3.11+
- **API keys / accounts**: Pinecone, Voyage AI, Anthropic (Claude). Optional: Neo4j, Redis, LangSmith.

## Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/MichaelHabermas/LegacyLens-1.git
   cd LegacyLens-1
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install the project**
   When the project is scaffolded (Epic 0), install in editable mode:

   ```bash
   pip install -e .
   ```

   Until then, install steps will be added here as dependencies are defined.

4. **Environment variables**
   Copy `.env.example` to `.env` and set the required variables. When `.env.example` is added (Epic 0), use it as the template. Required variables:
   - `PINECONE_API_KEY` — Pinecone serverless vector DB
   - `VOYAGE_API_KEY` — Voyage-code-3 embeddings
   - `ANTHROPIC_API_KEY` — Claude LLM
   - `NEO4J_URI`, `NEO4J_USER`, `NEO4J_PASSWORD` — Neo4j (for dependency graph; optional for MVP)
   - `REDIS_URL` — Redis (embedding/query cache)
   - `LANGSMITH_API_KEY` — (optional) LangSmith tracing
   - `ENVIRONMENT` — `dev`, `staging`, or `prod`

   Do not commit `.env`; it is listed in `.gitignore`.

## Getting started

1. **Configure environment** — Ensure `.env` is set up (see Setup).
2. **Ingest a codebase** — Index a legacy codebase (e.g. a GnuCOBOL checkout):

   ```bash
   legacylens ingest /path/to/codebase
   ```

3. **Ask a question** — Run a natural-language query:

   ```bash
   legacylens query "Where is the main entry point?"
   ```

   More examples:

   ```bash
   legacylens query "What functions modify CUSTOMER-RECORD?"
   legacylens query "Explain CALCULATE-INTEREST paragraph"
   ```

## Usage

| Command                                     | Description                                                                  |
| ------------------------------------------- | ---------------------------------------------------------------------------- |
| `legacylens ingest <path>`                  | Index a codebase (scan, parse, chunk, embed, store in Pinecone).             |
| `legacylens query "<question>"`             | Ask a natural-language question; returns an answer with file/line citations. |
| `legacylens show <file_path> <line_number>` | Show context around a given line (±50 lines).                                |
| `legacylens status`                         | Show config and index status.                                                |

### Example queries

- "Where is the main entry point?"
- "What functions modify CUSTOMER-RECORD?"
- "Explain CALCULATE-INTEREST paragraph"
- "Find all file I/O operations"
- "What are dependencies of MODULE-X?"
- "Show error handling patterns"

## Documentation

- [Documentation index](docs/README.md) — Map of all docs: onboarding, implementation, decisions, and quick reference.
- [Product requirements and roadmap](docs/PRD.md) — Epics, architecture, and implementation details.
- [Tech stack in-depth guide](docs/technology/TECH-STACK-GUIDE.md) — How to set up and use each technology (Pinecone, Voyage, Claude, Redis, Vercel, CLI, etc.).
- [RAG and legacy code primer](docs/technology/RAG-AND-LEGACY-PRIMER.md) — Concepts: RAG, legacy code, and why this stack.
- [Environment and configuration](docs/technology/ENVIRONMENT-AND-CONFIG.md) — Environment variables, required vs optional, and where to get API keys.
- [Glossary](docs/GLOSSARY.md) — Definitions of terms used across the docs.
- [PRD V1 (research)](docs/research/PRD-V1.md) — Original epic and user-story breakdown.

## License

See [LICENSE](LICENSE).
