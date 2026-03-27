# 🚗 Automotive In-Vehicle RAG Assistant

## 🧠 Overview

This project implements an **in-vehicle AI assistant prototype** designed for automotive use cases.

It combines:
- Retrieval-Augmented Generation (RAG)
- Tool Calling (vehicle interaction)
- Conversational Memory

The system simulates an intelligent cockpit assistant capable of answering driver queries related to:
- ADAS (Advanced Driver Assistance Systems)
- AUTOSAR architecture
- OTA (Over-the-Air updates)
- Vehicle diagnostics
- Real-time vehicle information (speed, faults, etc.)

---

## ⚙️ Key Features

### 1. RAG (Retrieval-Augmented Generation)
- Uses **FAISS vector database**
- Supports **multi-source documents (TXT + PDF)**
- Reduces hallucination through grounded responses

### 2. Tool Calling (Vehicle Interaction)
- Simulated vehicle APIs:
  - Vehicle speed
  - OTA status
  - Diagnostic Trouble Codes (DTC)
- Dynamic routing between knowledge and real-time data

### 3. Conversational Memory
- Maintains short-term chat history
- Enables multi-turn interaction
- Supports follow-up questions (e.g., *"What about Adaptive AUTOSAR?"*)

### 4. Persistent Vector Storage
- FAISS index is stored locally
- Avoids repeated embedding computation
- Improves startup performance and efficiency

---

## 🏗️ System Architecture
# 🚗 Automotive In-Vehicle RAG Assistant

## 🧠 Overview

This project implements an **in-vehicle AI assistant prototype** designed for automotive use cases.

It combines:
- Retrieval-Augmented Generation (RAG)
- Tool Calling (vehicle interaction)
- Conversational Memory

The system simulates an intelligent cockpit assistant capable of answering driver queries related to:
- ADAS (Advanced Driver Assistance Systems)
- AUTOSAR architecture
- OTA (Over-the-Air updates)
- Vehicle diagnostics
- Real-time vehicle information (speed, faults, etc.)

---

## ⚙️ Key Features

### 1. RAG (Retrieval-Augmented Generation)
- Uses **FAISS vector database**
- Supports **multi-source documents (TXT + PDF)**
- Reduces hallucination through grounded responses

### 2. Tool Calling (Vehicle Interaction)
- Simulated vehicle APIs:
  - Vehicle speed
  - OTA status
  - Diagnostic Trouble Codes (DTC)
- Dynamic routing between knowledge and real-time data

### 3. Conversational Memory
- Maintains short-term chat history
- Enables multi-turn interaction
- Supports follow-up questions (e.g., *"What about Adaptive AUTOSAR?"*)

### 4. Persistent Vector Storage
- FAISS index is stored locally
- Avoids repeated embedding computation
- Improves startup performance and efficiency

---

## 🏗️ System Architecture
Driver / Passenger
↓
Voice / UI Input
↓
ASR Layer
↓
Query Orchestrator
(Intent + Routing)
↙ ↘
RAG Pipeline Tool Calling Layer
(Knowledge) (Vehicle Functions)
↓ ↓
Vector DB Service Layer
(FAISS) (Vehicle APIs)
↓ ↓
LLM Runtime Vehicle Signals
↘ ↓
Response Generation
↓
HMI / Voice Output

---

## 🧩 Architecture Explanation

The system separates **knowledge-based reasoning** and **real-time vehicle interaction**:

- **RAG Path**
  - Handles static knowledge (e.g., AUTOSAR, ADAS, OTA)
  - Uses FAISS for semantic retrieval

- **Tool Path**
  - Handles dynamic vehicle data (e.g., speed, DTC, OTA status)
  - Simulates vehicle-side APIs

- **Orchestration Layer**
  - Determines whether to use RAG or Tool
  - Maintains conversation context (memory)

- **LLM Runtime**
  - Performs reasoning and response generation
  - Does NOT directly control vehicle functions

- **Service Layer**
  - Acts as a safety boundary
  - Translates AI outputs into structured vehicle interactions

---

## 🚀 Example Use Cases

### Knowledge Query
User: What is AUTOSAR?
Assistant: AUTOSAR is a standardized automotive software architecture...
### Follow-up (Memory)
User: And what about Adaptive AUTOSAR?
Assistant: Adaptive AUTOSAR is designed for high-performance computing...
### Vehicle Interaction (Tool Calling)
User: What is the current vehicle speed?
Assistant: The current vehicle speed is 87 km/h.

---

## 🛠️ Tech Stack

- Python
- LangChain
- OpenAI API (LLM + Embeddings)
- FAISS (Vector Database)
- PyPDF (PDF parsing)

---

## 📂 Project Structure

src/
├── rag_pipeline.py # Main assistant logic
├── embed_store.py # FAISS build/load (persistent storage)
├── load_docs.py # Load TXT/PDF documents
├── split_docs.py # Text chunking
├── vehicle_tools.py # Simulated vehicle APIs

data/docs/
├── adas_notes.txt
├── autosar_notes.txt
├── ota_notes.txt
├── diagnostics_notes.txt
├── cockpit_assistant_notes.txt
├── ota_manual.pdf

---

## 🧠 Design Principles

- Separation of concerns (RAG vs Tool vs LLM)
- Safety-aware architecture (LLM does not control ECU)
- Context-aware interaction (memory-enabled)
- Efficiency optimization (persistent vector store)

---

## 🎯 Future Improvements

- Integration with real vehicle middleware (AUTOSAR Adaptive)
- Deployment on edge devices (in-vehicle compute)
- Latency optimization for real-time interaction
- Voice interface integration (ASR + TTS)
- Cloud-based model update via OTA

---

## 💡 Author Notes

This project is designed as a **prototype for in-vehicle AI architecture**, focusing on bridging:

- AI systems (LLM, RAG)
- Automotive systems (ECU, diagnostics, OTA)
- Human interaction (cockpit assistant)

It reflects how generative AI can be integrated into future intelligent vehicles.






