# Automotive In-Vehicle RAG Assistant

## 🚗 Project Overview

This project implements a vehicle-oriented Retrieval-Augmented Generation (RAG) assistant designed for in-vehicle AI use cases.

It simulates an intelligent cockpit assistant that can answer driver questions about:
- ADAS (Advanced Driver Assistance Systems)
- AUTOSAR software architecture
- OTA (Over-the-Air updates)
- Vehicle diagnostics
- Cockpit AI assistance

The system retrieves relevant domain knowledge from a local knowledge base and generates grounded responses using LLMs, reducing hallucination and improving reliability.

## 🎯 Key Features

- Document ingestion from automotive knowledge files
- Text chunking for retrieval optimization
- Semantic embedding using OpenAI
- Vector similarity search with FAISS
- Context-grounded answer generation using LLM
- Interactive CLI-based assistant simulation

## 🧠 System Architecture

User Query  
→ Vector Retrieval (FAISS)  
→ Context Assembly  
→ LLM (GPT)  
→ Final Answer

## 🛠️ Tech Stack

- Python
- LangChain
- OpenAI API
- FAISS
- python-dotenv

## 🚘 Automotive Context

Unlike generic RAG demos, this project focuses on automotive-specific domains such as ADAS, AUTOSAR, OTA, and diagnostics.

It reflects real-world in-vehicle AI assistant scenarios, where responses must be:
- Context-aware  
- Safety-conscious  
- Concise and non-distracting  

This makes the system closer to real production use cases in software-defined vehicles.


<img width="372" height="607" alt="image" src="https://github.com/user-attachments/assets/5967f01a-8f61-48da-8560-0af675e314ce" />


