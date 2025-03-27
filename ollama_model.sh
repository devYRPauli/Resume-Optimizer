
#!/bin/bash
echo "Installing Ollama and pulling Mistral..."
curl -fsSL https://ollama.com/install.sh | sh
ollama pull mistral
echo "✅ Done. You can now run: streamlit run app.py"
