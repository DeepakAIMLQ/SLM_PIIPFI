# ---- Base image ----
FROM python:3.11-slim

# ---- Set environment vars ----
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ---- Install system dependencies ----
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# ---- Create working directory ----
WORKDIR /app

# ---- Copy requirements first (better caching) ----
COPY requirements.txt .

# ---- Install Python dependencies ----
# Use PyTorch CPU wheels from official repo
RUN pip install --upgrade pip \
    && pip install --no-cache-dir torch==2.1.0 --index-url https://download.pytorch.org/whl/cpu \
    && pip install --no-cache-dir -r requirements.txt

# ---- Copy application code ----
COPY . .

# ---- Expose FastAPI port ----
EXPOSE 8000

# ---- Start the FastAPI app ----
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
