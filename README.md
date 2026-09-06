# RAG Pipeline — FAISS

A Retrieval-Augmented Generation pipeline that ingests a small Markdown knowledge base, indexes it with FAISS, and answers user questions using a local LLM (Ollama), grounded strictly in retrieved context with source citations.

## Usage

### chat
```bash
python main.py chat
```
Ask questions, get cited answers grounded in retrieved context.

### eval
```bash
python main.py eval
```
Checks if the correct source doc is retrieved for known questions.

### eval-refusal
```bash
python main.py eval-refusal
```
Checks if the model says "I don't know" on out-of-KB questions instead of hallucinating.

## Stack

- Embeddings: sentence-transformers (all-MiniLM-L6-v2)
- Vector index: FAISS
- LLM: Ollama (llama3.2)
- Chunking: SpaCy sentence-aware splitting

## Files

- `ingest.py` — reads and parses the KB
- `chunking.py` — splits docs into chunks
- `index.py` — embeds chunks, builds FAISS index
- `main.py` — chat + eval entry point
- `eval_set.py` — evaluation questions
