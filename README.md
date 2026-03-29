# 🚗 Automotive GenAI Assistant

## 🧠 Overview

This project is a modular Automotive GenAI Assistant prototype designed for both knowledge-intensive and vehicle-related use cases.

It combines:

* Retrieval-Augmented Generation (RAG)
* Conversational Memory
* Agent-based Query Routing
* Tool Integration Simulation

👉 The system demonstrates how LLM-based assistants can be structured using a layered architecture for real-world automotive applications.

---

## 🚀 Key Features

* Modular RAG pipeline for domain-specific document retrieval
* Persistent FAISS vector store for efficient semantic search
* Multi-turn conversational memory for contextual interaction
* Agent-based routing between knowledge queries and system/tool queries
* Simulated tool layer for vehicle interaction
* Automotive-focused knowledge base (ADAS, AUTOSAR, OTA, diagnostics)

---

## 🏗️ System Architecture

```text
User Query
   ↓
Intent Routing
   ↓
 ┌──────────────────────┬─────────────────────┐
 │ Knowledge-based Query │ Vehicle/System Query │
 └──────────────────────┴─────────────────────┘
            ↓                         ↓
       RAG Pipeline               Tool Layer
            ↓                         ↓
   Context Retrieval          Structured Response
            ↓                         ↓
          LLM                  Final Answer
            ↓
      Final Answer
```

---

## 🧩 Architectural Design

The system follows a modular AI architecture with clear separation of concerns.

### 1. Data Layer (Vector Store)

A FAISS-based vector database stores embedded automotive domain knowledge.
Embeddings are generated once and reused across sessions.

### 2. Retrieval Layer

Performs semantic search to identify relevant context for user queries.

### 3. LLM Reasoning Layer

Generates grounded responses using retrieved context and conversation history.

### 4. Memory Layer

Maintains recent conversation history for multi-turn interaction.

### 5. Agent Layer (Query Routing)

Routes queries into:

* knowledge queries → RAG pipeline
* system queries → tool layer

### 6. Tool Layer (Execution)

Simulates vehicle-related APIs:

* vehicle speed
* fault codes
* ADAS status

---

### ⭐ Key Design Principle

The system separates:

* retrieval (data)
* reasoning (LLM)
* execution (tools)

This aligns with real-world enterprise AI system architecture.

---

## 💡 Example Use Cases

### Knowledge Query

User: What is AUTOSAR?
Assistant: AUTOSAR is a standardized automotive software architecture...

### Follow-up (Memory)

User: And what about Adaptive AUTOSAR?
Assistant: Adaptive AUTOSAR is designed for high-performance computing...

### Vehicle Interaction (Tool Calling)

User: What is the current vehicle speed?
Assistant: Current vehicle speed is 72 km/h

---

## 🛠️ Tech Stack

* Python
* OpenAI API (LLM + Embeddings)
* FAISS (Vector Database)
* LangChain (light usage / optional)
* PyPDF

---

## 📂 Project Structure

```text
AUTOMOTIVE-GENAI-PROJECTS/
├── app/
│   ├── agent.py
│   ├── llm.py
│   ├── memory.py
│   ├── prompts.py
│   ├── retriever.py
│   ├── tools.py
│   └── vector_store.py
├── data/
│   ├── raw_docs/
│   └── vector_store/   # generated locally
├── assets/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Set API key

```text
OPENAI_API_KEY=your_api_key
```

### 3. Run

```bash
python main.py
```

---

## 🔮 Future Extensions

* Replace rule-based routing with LLM-based intent classification
* Implement structured JSON tool calling
* Integrate real backend vehicle APIs
* Add safety guardrails and validation
* Deploy as cloud-based or edge AI service

---

## 🎯 Why This Project Matters

This project demonstrates how Generative AI can be applied in automotive systems beyond simple chat interfaces.

It reflects:

* system-level AI architecture thinking
* integration of AI with real-world domains
* separation of reasoning and execution
* extensibility toward enterprise AI systems

---

## 👤 Author

This project reflects a transition from automotive system architecture to AI system architecture, focusing on bridging:

* AI systems (LLM, RAG)
* Automotive systems (ECU, diagnostics, OTA)
* Human interaction (cockpit assistant)


