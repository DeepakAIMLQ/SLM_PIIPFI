# 🔐 PII / PHI / PFI Extraction & Synthetic Data Generator

A production-ready **FastAPI** application for extracting **PII (Personally Identifiable Information)**, **PHI (Protected Health Information)**, and **PFI (Protected Financial Information)** from uploaded documents, and for generating synthetic datasets for model training and testing.

---

## 🚀 Features

✅ Extract **PII / PHI / PFI** entities from text or file uploads  
✅ Generate **synthetic datasets** for AI/ML training  
✅ RESTful **FastAPI** endpoints  
✅ Interactive API docs via **Swagger UI**  
✅ Ready for **Docker** or **Cloud Deployment**  

---

## 🧱 Project Structure

```
project-root/
│
├── app/
│   ├── main.py                # FastAPI entry point
│   ├── routers/
│   │   ├── extract.py         # PII/PHI/PFI extraction logic
│   │   └── synthetic.py       # Synthetic data generation logic
│   ├── models/                # Data models / schemas
│   ├── utils/                 # Helper functions, preprocessing
│   └── __init__.py
│
├── requirements.txt           # Python dependencies
├── README.md                  # Documentation
└── .gitignore
```

---

## ⚙️ Setup Instructions

### 🧩 Step 1: Clone the Repository

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

### 🧩 Step 2: Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate        # On Linux/Mac
venv\Scripts\activate         # On Windows
```

### 🧩 Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Run the FastAPI Application

### 🧠 Step 4: Start the Server

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

After running this, the app will be available at:

👉 **http://localhost:8000**  
👉 **Swagger Docs:** [http://localhost:8000/docs](http://localhost:8000/docs)  
👉 **ReDoc UI:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🔍 API Endpoints

### 1️⃣ **Extract PII / PHI / PFI Entities**

**Endpoint:**  
```http
POST /extract/
```

**Description:**  
Upload a text file or document to extract sensitive entities like names, emails, medical conditions, and financial IDs.

**Request Example (via cURL):**
```bash
curl -X POST "http://localhost:8000/extract/"      -F "file=@sample.txt"
```

**Response Example:**
```json
{
  "PII": ["John Doe", "john.doe@email.com"],
  "PHI": ["Diabetes"],
  "PFI": ["Credit Card: 4532 7712 3456 7890"]
}
```

---

### 2️⃣ **Generate Synthetic Dataset**

**Endpoint:**  
```http
GET /generate_synthetic/?samples=200
```

**Description:**  
Generates synthetic data for testing or model fine-tuning.

**Request Example:**
```bash
curl "http://localhost:8000/generate_synthetic/?samples=200"
```

**Response Example:**
```json
{
  "status": "success",
  "samples_generated": 200,
  "file": "synthetic_dataset.json"
}
```

---

## 🧪 API Summary

| Step | Endpoint / Command | Description |
|------|--------------------|-------------|
| 1 | `pip install -r requirements.txt` | Install dependencies |
| 2 | `uvicorn app.main:app --reload --host 0.0.0.0 --port 8000` | Start the FastAPI server |
| 3 | `POST /extract/` | Upload file → Extracts PII/PHI/PFI JSON |
| 4 | `GET /generate_synthetic/?samples=200` | Generate synthetic dataset |

---

## 🧰 Tech Stack

| Component | Technology |
|------------|-------------|
| Backend Framework | **FastAPI** |
| Server | **Uvicorn** |
| Language | **Python 3.9+** |
| Data Handling | **Pandas, NumPy** |
| NLP / AI | **Hugging Face Transformers (optional)** |
| Documentation | **Swagger / ReDoc** |

---

## 🧑‍💻 Local Testing

Once the app is running, open:

- Swagger UI → [http://localhost:8000/docs](http://localhost:8000/docs)  
- ReDoc → [http://localhost:8000/redoc](http://localhost:8000/redoc)

You can test both `/extract/` and `/generate_synthetic/` endpoints directly in the browser.

---

## 🧩 Example Use Cases

- 🔍 **Information extraction** from unstructured text  
- 🧠 **Anonymization / redaction** pipelines for enterprises  
- 🧬 **Synthetic data creation** for LLM fine-tuning  
- 🧾 **Privacy-compliant dataset generation** for AI/ML research  

---

## 🤝 Contributing

Contributions are welcome!  
If you’d like to improve or extend the project, please:

1. Fork the repository  
2. Create a new branch (`feature/my-new-feature`)  
3. Commit your changes  
4. Submit a pull request 🚀  

---

## 📜 License

This project is licensed under the **MIT License**.  
Feel free to use and modify it for personal or commercial projects.

---

## 🌟 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/)
- [Hugging Face Transformers](https://huggingface.co/)
- [Uvicorn](https://www.uvicorn.org/)

---

> 💡 **Tip:**  
> For deploying on cloud (AWS / Azure / GCP), use `Dockerfile` + `uvicorn` with Gunicorn worker for production.

----------------

>> uvicorn app.main:app --reload

>> streamlit run test_client.py