
import streamlit as st
import fitz
import docx
import os
import re
import ollama
from collections import defaultdict

def extract_text_from_resume(uploaded_file):
    try:
        ext = os.path.splitext(uploaded_file.name)[1].lower()
        if ext == '.pdf':
            return extract_text_from_pdf(uploaded_file)
        elif ext == '.docx':
            return extract_text_from_docx(uploaded_file)
        elif ext == '.txt':
            return uploaded_file.read().decode("utf-8")
        else:
            st.error("Unsupported file type.")
            return ""
    except Exception as e:
        st.error(f"Error reading resume: {e}")
        return ""

def extract_text_from_pdf(file):
    try:
        doc = fitz.open(stream=file.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        st.error(f"PDF error: {e}")
        return ""

def extract_text_from_docx(file):
    try:
        doc = docx.Document(file)
        return "\n".join([p.text for p in doc.paragraphs if p.text.strip() != ""])
    except Exception as e:
        st.error(f"DOCX error: {e}")
        return ""

def extract_keywords_by_category(text, label="job description"):
    if not text.strip():
        return defaultdict(list)

    prompt = f"""
Given the following {label}, extract relevant keywords and key phrases (1–3 words maximum) that represent core skills, tools, technologies, responsibilities, and qualifications.

✅ Group the keywords under the following categories:
- Technical Skills
- Tools/Technologies
- Certifications
- Responsibilities
- Soft Skills (only if explicitly mentioned)

❌ Do NOT include general job responsibilities or generic terms.

Return only the keywords grouped under these category headers, each on a new line as bullet points.

Text:
{text}
"""
    try:
        response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}])
        raw_output = response['message']['content']
    except Exception as e:
        st.error(f"Model error: {e}")
        return defaultdict(list)

    categories = defaultdict(list)
    current_category = None

    for line in raw_output.splitlines():
        line = line.strip()
        if not line:
            continue
        if any(cat.lower() in line.lower() for cat in ["technical", "tool", "certification", "responsibilities", "soft"]):
            current_category = line.split(":")[0].strip().lower()
        elif line.startswith(("-", "•", "*")) and current_category:
            keyword = line.lstrip("-•* ").strip().lower()
            if keyword:
                categories[current_category].append(keyword)

    return categories

def flatten_keywords(categorized_dict):
    all_keywords = []
    for kw_list in categorized_dict.values():
        all_keywords.extend(kw_list)
    return list(set(kw.strip().lower() for kw in all_keywords))

def compare_keywords(resume_keywords, jd_keywords):
    resume_set = set([kw.strip().lower() for kw in resume_keywords])
    jd_set = set([kw.strip().lower() for kw in jd_keywords])
    matched = sorted(list(resume_set & jd_set))
    missing = sorted(list(jd_set - resume_set))
    score = int((len(matched) / len(jd_set)) * 100) if jd_set else 0
    return matched, missing, score

st.set_page_config(page_title="Resume Match Analyzer", layout="centered")
st.title("📄 Resume Match Analyzer")
st.markdown("Upload your resume and paste a job description to see how well your resume aligns.")

resume_file = st.file_uploader("📄 Upload your resume (PDF, DOCX, or TXT)", type=["pdf", "docx", "txt"])
job_description = st.text_area("💼 Paste the job description here")

if resume_file and job_description.strip():
    resume_text = extract_text_from_resume(resume_file)
    if not resume_text.strip():
        st.error("Could not extract any text.")
    else:
        st.subheader("📄 Extracted Resume Text")
        st.text_area("Review the resume text below:", value=resume_text, height=300)

        if st.button("🔍 Analyze Resume"):
            with st.spinner("Analyzing..."):
                resume_kw = extract_keywords_by_category(resume_text, "resume")
                jd_kw = extract_keywords_by_category(job_description, "job description")
                resume_flat = flatten_keywords(resume_kw)
                jd_flat = flatten_keywords(jd_kw)

                if not jd_flat or not resume_flat:
                    st.error("Keyword extraction failed.")
                else:
                    matched, missing, score = compare_keywords(resume_flat, jd_flat)

                    st.success("✅ Analysis Complete!")
                    st.subheader("📊 Match Score")
                    st.markdown(f"**{score}%** of job keywords found in resume.")
                    
                    st.subheader("💼 JD Keywords")
                    for cat, kws in jd_kw.items():
                        with st.expander(cat.title()):
                            st.write(", ".join(kws))

                    st.subheader("🧠 Resume Keywords")
                    for cat, kws in resume_kw.items():
                        with st.expander(cat.title()):
                            st.write(", ".join(kws))

                    st.subheader("✅ Matched Keywords")
                    st.write(", ".join(matched) if matched else "None")

                    st.subheader("❌ Missing Keywords")
                    st.write(", ".join(missing) if missing else "None")

                    if missing:
                        st.download_button("⬇️ Download Missing Keywords", data="\n".join(missing),
                                           file_name="missing_keywords.txt", mime="text/plain")
else:
    st.info("Please upload your resume and paste the job description.")
