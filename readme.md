# PII/PHI/PFI Extraction POC

## Features
- Upload multiple files: PDF, DOCX, XLSX, CSV, TXT
- Detect PII (Names, Emails, Phones, SSNs), PHI (Medical Conditions), PFI (Credit Cards, Accounts, Amounts)
- Streamlit frontend + FastAPI backend
- Dockerized for deployment

## Run locally

```bash
# Install dependencies
pip install -r requirements.txt

# Start FastAPI + Streamlit via Docker
docker build -t pii-extractor .
docker run -p 8000:8000 -p 8501:8501 pii-extractor
