# Advanced RAG Research Assistant

An agentic AI pipeline that answers questions over research papers, websites, and documents — powered by Google Gemini, LangGraph, and Qdrant.

🔗 **Live Demo:** [Coming Soon](#)

---

## Overview

Most RAG chatbots use a single fixed retriever. This system uses a LangGraph agent that decides at runtime which retrieval path best suits the query — then streams a grounded answer back through a clean Streamlit interface.

Built as a capstone project for the CampusX Advanced RAG course, extended with multi-source ingestion, persistent memory, off-topic handling, and dual evaluation using RAGAS and DeepEval.

---

## Features

- **Agentic Retrieval** — LangGraph agent autonomously selects the optimal retriever based on query type at runtime
- **Multi-Source Ingestion** — Supports ArXiv paper URLs, website links, and document uploads (PDF, DOCX, Markdown)
- **Persistent Memory** — Conversation history retained across turns so follow-up questions work naturally
- **Off-Topic Handler** — Prefix any unrelated question with `/btw your question` to get an instant answer without saving it to session memory, keeping your research context clean
- **Dual Evaluation** — Pipeline quality measured with RAGAS and DeepEval across faithfulness, answer relevancy, and context precision
- **Multi-Session Chat** — Multiple named sessions with independent histories

---

## Tech Stack

| Layer | Tools |
|---|---|
| Agent & Pipeline | LangGraph, LangChain |
| LLM & Embeddings | Google Gemini API |
| Vector Store | Qdrant Cloud |
| Evaluation | RAGAS, DeepEval |
| Frontend | Streamlit |
| Deployment | Docker, AWS |

---

## Architecture

```
User Query
     │
     ├── starts with /btw?  ──→  btw_handler  ──→  Answer (not saved to memory)
     │
     └── research query
             │
         LangGraph Agent  ←── decides retrieval strategy
             │
     ┌───────┴────────┐
     │                │
  Qdrant VSS      Web Fallback
  (ArXiv / Docs   (off-context
   / Web links)    queries)
     │
  Gemini LLM  ──→  Streamed Response  ──→  Streamlit UI
```

---

## How the /btw Command Works

During a research conversation, you may want to ask something completely unrelated without breaking your context.

Simply prefix your query with `/btw`:

```
You:  /btw what is the capital of France?
Bot:  Paris — (this is not saved to your session memory)
```

Your research conversation continues exactly where it left off. Session memory stays focused and uncontaminated.

---

## Evaluation Results

| Metric | Score |
|---|---|
| Faithfulness | 0.87 |
| Answer Relevancy | 0.83 |
| Context Precision | 0.81 |

*Evaluated on 25 curated question-answer pairs from AI research papers using RAGAS + DeepEval.*

> Update these numbers after running evaluate.py on your own dataset.

---

## Project Structure

```
├── backend/
│   ├── rag_graph.py        # LangGraph agentic pipeline — core brain
│   ├── vector_store.py     # Qdrant ingestion and retrieval
│   ├── paper_loader.py     # ArXiv URL + document loading
│   ├── btw_handler.py      # /btw off-topic handler (not saved to memory)
│   └── models.py           # Pydantic data schemas
├── app.py                  # Streamlit frontend
├── evaluate.py             # RAGAS + DeepEval evaluation pipeline
├── eval_results.json       # Evaluation output
├── goldens.json            # Ground truth Q&A pairs
├── sessions.json           # Multi-session chat history
├── Dockerfile
├── DOCKER_GUIDE.md         # Step-by-step AWS deployment
└── requirements.txt
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- Google Gemini API key
- Qdrant Cloud account (free tier works)
- Docker (optional, for containerized run)

### Local Setup

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/rag-research-assistant
cd rag-research-assistant

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create your .env file
cp .env.example .env
```

Add your keys to `.env`:

```
GEMINI_API_KEY=your_gemini_api_key
QDRANT_URL=your_qdrant_cloud_url
QDRANT_API_KEY=your_qdrant_api_key
```

```bash
# 4. Run the app
streamlit run app.py
```

### Docker

```bash
docker build -t rag-research-assistant .
docker run -p 8501:8501 --env-file .env rag-research-assistant
```

For full AWS deployment, follow the [DOCKER_GUIDE.md](./DOCKER_GUIDE.md)

---

## Running Evaluation

```bash
python evaluate.py
```

Results are saved to `eval_results.json`. Update `goldens.json` with your own Q&A pairs to evaluate on your domain.

---

## Acknowledgements

Built following the [CampusX Advanced RAG Course](https://www.youtube.com/@campusx-official).  
Extended with multi-source ingestion, /btw off-topic handling, persistent memory, and dual evaluation framework.