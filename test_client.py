import streamlit as st
import requests
import os
import io
import os

#Update this with your backend public URL after deployment
#FASTAPI_URL = "https://slmpiipfi-production.up.railway.app/extract"
FASTAPI_URL = "http://localhost:8000/extract"


st.set_page_config(page_title="📤 PII Extractor POC", layout="centered")
st.title("🔎 PII/PHI Extraction – FastAPI POC")
st.write("Upload one or more files and test the FastAPI backend pipeline.")

# Multi-file uploader
uploaded_files = st.file_uploader(
    "Upload PDF, DOCX, XLSX, CSV, TXT files",
    type=["pdf", "docx", "xlsx", "csv", "txt"],
    accept_multiple_files=True
)

if uploaded_files:
    if st.button("🚀 Send to FastAPI"):
        results = []

        for file in uploaded_files:
            files = {"file": (file.name, io.BytesIO(file.getvalue()), file.type)}
            try:
                response = requests.post(FASTAPI_URL, files=files)
                if response.status_code == 200:
                    results.append({"filename": file.name, "result": response.json()})
                else:
                    results.append({"filename": file.name, "error": f"Failed ({response.status_code}): {response.text}"})
            except Exception as e:
                results.append({"filename": file.name, "error": str(e)})

        # Show results
        st.subheader("📦 Extraction Results")
        for r in results:
            st.markdown(f"### 📁 {r['filename']}")
            if "result" in r:
                st.json(r["result"])
            else:
                st.error(r["error"])
