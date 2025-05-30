# 🧠 Multi-Agent AI System (CLI-Based)

This project is a **lightweight multi-agent AI system** built with Python that processes user inputs in formats (PDF, JSON, or plain-text Email), classifies the content type and intent, and routes the input to a specialized agent for structured extraction using AI.

---

## 🚀 Overview

This system uses a modular, agent-based architecture:

### 🎯 Core Features:
- **Classifier Agent**: Detects input format (PDF, JSON, Email) and intent (Invoice, RFQ, Complaint, etc.)
- **Specialized Agents**:
  - **JSON Agent**: Validates JSON against expected schema and flags missing fields.
  - **Email Agent**: Extracts sender, urgency, and formats content for CRM-style usage.
  - **PDF Agent**: Extracts text from PDFs using PyMuPDF.
- ✅ **LLM-powered Extraction**: Uses **Gemini 2.0 Flash** model from Google to extract intent and structured data from natural language documents.
- **Shared Memory Module**: Persists logs of each action using SQLite.

---

## 🧠 AI/LLM Usage

This system integrates **Google's Gemini 2.0 Flash** model (via API) to enhance understanding and extraction from:
- Email content
- PDF documents

This enables the agents to perform **semantic classification** and **context-aware field extraction**.

---

## 🗂️ Folder Structure

```bash
multi_agent_AI_system/
│
├── main.py                # Main Entry point for CLI interaction
├── classifier_agent.py    
├── email_agent.py         
├── json_agent.py          
├── pdf_agent.py           
├── memory.py              # Shared memory using SQLite
│
├── data/                  # Sample input files and output log screenshots
│   ├── email1.txt
│   ├── email2.txt
│   ├── sample1.json
│   ├── sample2.json
│   ├── sample1.pdf
│   ├── emailLog.png
│   ├── jsonLog.png
│   └── pdfLog.png
│
└── memory.db        
```
