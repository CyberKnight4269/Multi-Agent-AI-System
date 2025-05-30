# 🧠 Multi-Agent AI System (CLI-Based)

This project is a **lightweight multi-agent AI system** built with Python that processes user inputs in various formats (PDF, JSON, or plain-text Email), classifies the content type and intent, and routes the input to a specialized agent for structured extraction.

---

## 🚀 Overview

This system uses a modular, agent-based architecture:

### 🎯 Core Features:
- **Classifier Agent**: Detects input format (PDF, JSON, Email) and intent (Invoice, RFQ, Complaint, etc.)
- **Specialized Agents**:
  - **JSON Agent**: Validates JSON against expected schema and flags missing fields.
  - **Email Agent**: Extracts sender, urgency, and formats content for CRM-style usage.
  - **PDF Agent**: Extracts text from PDFs using PyMuPDF library for python.
- **Shared Memory Module**: Persists logs of each action (source, intent, extracted values) using SQLite.

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
