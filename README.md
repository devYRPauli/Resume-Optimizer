# 📄 Resume Match Analyzer

A smart, privacy-first tool to analyze how well your resume aligns with a job description.  
Runs entirely **offline** using [Ollama](https://ollama.com) + [Mistral LLM](https://ollama.com/library/mistral) — no API keys or internet required!

---

## 🚀 Features

✅ Upload your resume in **PDF, DOCX, or TXT**  
✅ Paste any job description  
✅ Extract short, relevant **keywords grouped by category**:
- Technical Skills
- Tools & Technologies
- Certifications
- Responsibilities
- Soft Skills

✅ Receive:
- ✅ Matched Keywords
- ❌ Missing Keywords
- 📊 Match Score (based on overlap)
- 📥 Downloadable list of missing keywords

---

## 🧠 How It Works

1. Parse your resume text from PDF/DOCX/TXT
2. Use a local LLM (Mistral via Ollama) to extract structured keywords
3. Extract similar keywords from the job description
4. Compare both sets and calculate a match score
5. Display results, category-wise, with download option

---

## 💻 Local Installation & Usage

### ⚙️ Prerequisites

- Python 3.8+
- Linux/macOS or Windows (via WSL)
- [Ollama](https://ollama.com) installed
- ~4GB space to pull the Mistral model

---

### 🔧 1. Clone This Repository

```bash
git clone https://github.com/devYRPauli/Resume-Optimizer.git
cd Resume-Optimizer
