# 📄 ClarityDocs AI

> Translate complex legal contracts, medical reports, and official jargon into plain English instantly. Built for the Nebius x NVIDIA AI Hackathon.

## 💡 The Problem
Every day, people struggle to understand dense official documents—such as rental leases, terms of service, medical lab results, and insurance policies. Misinterpreting these documents leads to hidden fees, missed deadlines, and legal liabilities.

## 🚀 The Solution
**ClarityDocs AI** is an intelligent document-simplification assistant that parses raw text or multi-page PDFs and breaks them down using NVIDIA's advanced models. It delivers a structured, easy-to-read breakdown containing:
1. **Plain English Summary**: Core meaning in 2–3 sentences.
2. **Red Flags & Hidden Traps**: Non-standard clauses, penalties, or unusual liabilities.
3. **Action Items & Checklist**: Chronological steps and deadlines the user needs to follow.

## 🛠️ Tech Stack & Architecture
* **Frontend:** Streamlit (Python web UI with file upload and memory PDF parsing via `pypdf`)
* **Backend API:** OpenAI Python SDK targeting NVIDIA Build serverless endpoints (`https://integrate.api.nvidia.com/v1`)
* **Core Model:** `nvidia/nemotron-3.5-lightning-30b-a3b` (optimized for speed and structured markdown output)

## ⚙️ Local Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/YourUsername/claritydocs-ai.git](https://github.com/YourUsername/claritydocs-ai.git)
   cd claritydocs-ai

## 🧪 Sample Documents for Testing
You can download and test sample inputs located in the `/test_samples` folder:
- `raw_text_test_sample.txt` (Plain text input)
- `sample-terms-of-service-template.pdf` (Sample PDF contract)
