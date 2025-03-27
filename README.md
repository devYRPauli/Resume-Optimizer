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

1. Parse your resume text from PDF, DOCX, or TXT
2. Use a local LLM (Mistral via Ollama) to extract structured keywords
3. Extract keywords from the job description in the same way
4. Compare both keyword sets and calculate a match score
5. Display results by category, with download options

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
```

---

### 🧠 2. Install Ollama + Pull Mistral
Run the setup script:
```bash
bash ollama_model.sh
```
This will install Ollama and download the Mistral model locally.
(Make sure you allow permissions if prompted.)

---

### 🐍 3. Set Up Python Environment
Install required Python libraries:
```bash
pip install -r requirements.txt
```

---

### ▶️ 4. Run the App
Launch the app with:
```bash
streamlit run app.py
```
Then open your browser and go to:
```bash
http://localhost:8501
```

---

### 📂 Folder Structure
```bash
Resume-Optimizer/
├── app.py                # Main Streamlit app
├── ollama_model.sh       # Installs Ollama + pulls Mistral
├── requirements.txt      # Python dependencies
├── README.md             # You're reading it
└── .gitignore
```

---

### 📦 How to Share or Distribute
This project works 100% offline.   
To share it with others, just zip the folder and send it.   
Once unzipped, they simply run:
```bash
bash ollama_model.sh
pip install -r requirements.txt
streamlit run app.py
```

---

### 🧩 Powered By

- [Streamlit](https://streamlit.io/) – frontend
- [Ollama](https://ollama.com/) – local LLM runner
- [Mistral LLM](https://docs.mistral.ai/) – model used for keyword extraction
- [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) – PDF parser
- `bash python-docx ` – Word parser

---

### 💬 Contributing
Pull requests and feedback welcome!   
Feel free to fork the repo and submit suggestions to improve keyword scoring, UI, or logic.

---

### 📜 License
MIT License  
© 2025 [@devYRPauli](https://github.com/devYRPauli)

---
