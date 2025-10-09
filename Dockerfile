#Created by : Deepak Singh
#Created on: 5-10-2025
#Updted on: 9-10-2025
#Des: Updated to run on Docker both Frondend and Backend

FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8501

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl \
    && pip install --upgrade pip \
    && pip install torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 --index-url https://download.pytorch.org/whl/cpu \
    && pip install -r requirements.txt \
    && rm -rf /var/lib/apt/lists/*

# Copy source
COPY . .

# Expose Streamlit’s public port
EXPOSE 8501

# Start both FastAPI and Streamlit
CMD ["bash", "start.sh"]
