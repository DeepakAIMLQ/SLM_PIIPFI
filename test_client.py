import streamlit as st
import requests
import os

FASTAPI_URL = "http://127.0.0.1:8000/extract"  # Update if your endpoint is different

st.set_page_config(page_title="📤 PII Extractor POC", layout="centered")

st.title("🔎 PII/PHI Extraction – FastAPI POC")
st.write("Upload one or more files and test the FastAPI backend pipeline.")

# ✅ Multi-file uploader – supports PDF, DOCX, XLSX, CSV, TXT
uploaded_files = st.file_uploader(
    "Upload one or more files",
    type=["pdf", "docx", "xlsx", "csv", "txt"],
    accept_multiple_files=True
)

if uploaded_files:
    if st.button("🚀 Send to FastAPI"):
        results = []

        for file in uploaded_files:
            # Save to temp location
            temp_path = os.path.join("temp", file.name)
            os.makedirs("temp", exist_ok=True)
            with open(temp_path, "wb") as f:
                f.write(file.getbuffer())

            # Prepare multipart form data
            files = {"file": (file.name, open(temp_path, "rb"), file.type)}

            try:
                response = requests.post(FASTAPI_URL, files=files)
                if response.status_code == 200:
                    results.append({
                        "filename": file.name,
                        "result": response.json()
                    })
                else:
                    results.append({
                        "filename": file.name,
                        "error": f"❌ Failed ({response.status_code}): {response.text}"
                    })
            except Exception as e:
                results.append({
                    "filename": file.name,
                    "error": f"⚠️ Connection error: {e}"
                })

        # 📊 Show results
        st.subheader("📦 Extraction Results")
        for r in results:
            st.markdown(f"### 📁 {r['filename']}")
            if "result" in r:
                st.json(r["result"])
            else:
                st.error(r["error"])
