#Created by : Deepak Singh
#Created on: 5-10-2025
#Updted on: 9-10-2025
#Des: Updated to run on Docker both Frondend and Backend

# ---- Base Image ----
FROM python:3.11-slim

# ---- Environment Settings ----
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ---- Install Core Dependencies ----
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# ---- Set working dir ----
WORKDIR /app

# ---- Copy requirements early (for caching) ----
COPY requirements.txt .

# ---- Install Python dependencies ----
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir torch==2.1.0 --index-url https://download.pytorch.org/whl/cpu \
    && pip install --no-cache-dir -r requirements.txt

# ---- Copy code ----
COPY . .

# ---- Expose Ports ----
EXPOSE 8000

# ---- Start FastAPI ----
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
