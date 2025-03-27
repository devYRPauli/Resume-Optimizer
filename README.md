
# Resume Match Analyzer 🧠📄

Upload your resume and compare it against any job description to see how well it matches. Powered by Mistral via Ollama — runs completely locally.

## 🚀 How to Run

1. Clone or download this repo
2. Run the setup script:
```bash
bash ollama_model.sh
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Launch the app:
```bash
streamlit run app.py
```

## 🧩 Features
- Upload PDF, DOCX, or TXT resumes
- Paste job descriptions
- Get categorized keyword comparison
- Match score + download missing keywords

All powered locally via [Ollama](https://ollama.com) and [Mistral](https://ollama.com/library/mistral).
