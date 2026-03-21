# Automotive In-Vehicle RAG Assistant

This project implements a vehicle-oriented Retrieval-Augmented Generation (RAG) assistant for automotive knowledge using Python, LangChain, FAISS, and OpenAI.

It is designed as a prototype for in-vehicle AI use cases such as:
- ADAS feature explanation
- AUTOSAR architecture knowledge
- OTA update guidance
- Diagnostics-related Q&A
- Cockpit assistant support

## Features

- Local document ingestion from automotive knowledge files
- Text chunking for retrieval preparation
- Semantic embeddings using OpenAI
- Vector similarity search with FAISS
- Context-grounded answer generation with LLM
- Interactive command-line query flow

## Architecture

User Query → Retrieval → Context Assembly → LLM → Answer

## Tech Stack

- Python
- LangChain
- OpenAI API
- FAISS
- python-dotenv

## Project Structure

```text
data/docs/
  adas_notes.txt
  autosar_notes.txt
  ota_notes.txt
  diagnostics_notes.txt
  cockpit_assistant_notes.txt

src/
  load_docs.py
  split_docs.py
  embed_store.py
  rag_pipeline.py
