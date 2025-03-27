# 📄 Resume Match Analyzer

A smart Streamlit-based tool that analyzes how well your resume aligns with a job description — all powered **locally** by [Ollama](https://ollama.com) and the open-source [Mistral LLM](https://ollama.com/library/mistral). No internet-based LLMs or API keys required.

---

## 🚀 Features

✅ Upload your resume in **PDF, DOCX, or TXT**  
✅ Paste any job description  
✅ Extract keywords from both, **grouped by category**:
- Technical Skills  
- Tools & Technologies  
- Certifications  
- Responsibilities  
- Soft Skills  

✅ Get:
- ✅ Matched Keywords
- ❌ Missing Keywords
- 📊 Match Score (in %)
- 📥 Option to **download missing keywords**

---

## 🧠 Powered By

- [Streamlit](https://streamlit.io/) – frontend UI  
- [Ollama](https://ollama.com) – local LLM backend  
- [Mistral](https://ollama.com/library/mistral) – open-source language model  
- [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) – PDF parsing  
- `python-docx` – DOCX parsing  

---

## 🛠 Installation

> ⚠️ This app runs entirely **offline** using Ollama. Make sure your system supports it (macOS, Linux, or Windows with WSL).

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer
