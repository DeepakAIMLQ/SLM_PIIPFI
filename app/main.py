#Fast API Call
#Created By: Deepak Singh 
#Created on: 04-Oct-2025
#Modified On: 07-Oct-2025
#Version: 1.0.0.0
#---------------------------------------------

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import shutil
import os
import json

from app.reader import read_file
from app.extractor import extract_entities
from app.synthetic import generate_synthetic_jsonl
from app.config import INPUT_DIR, OUTPUT_DIR
from app.chunking import chunk_text

app = FastAPI(title="Multi-domain PII/PHI/PFI Extractor")

# ---------------- Enable CORS ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://slmpiipfi-9gabdgkmvbujftgpiy4fpk.streamlit.app"],  # Allow all origins. Change to specific domains for production.
    allow_credentials=True,
    allow_methods=["*"],   # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],   # Allow all headers
)

# ---------------- API Endpoints ----------------
@app.post("/extract/")
async def extract(file: UploadFile = File(...)):
    file_path = os.path.join(INPUT_DIR, file.filename)
    Path(INPUT_DIR).mkdir(exist_ok=True)
    
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    
    text = read_file(file_path)
    res = extract_entities(text)
    res["file_name"] = file.filename
    
    out_file = os.path.join(OUTPUT_DIR, file.filename.replace(".", "_") + ".json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(res, f, indent=2, ensure_ascii=False)
    
    return {
        "message": "Extraction completed successfully",
        "output_file": out_file,
        "result": res
    }

@app.get("/generate_synthetic/")
def generate_synthetic(samples: int = 200):
    out_file = generate_synthetic_jsonl(samples)
    return {
        "message": "Synthetic JSONL created",
        "file": out_file
    }
