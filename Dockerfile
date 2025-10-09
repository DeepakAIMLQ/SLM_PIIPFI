#Created by : Deepak Singh
#Created on: 5-10-2025
#Updted on: 9-10-2025
#Des: Updated to run on Docker both Frondend and Backend

FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependency files
COPY requirements.txt .

# Install dependencies efficiently
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy all app files
COPY . .

# Expose backend port
EXPOSE 8000

# Run both FastAPI and Streamlit if needed
CMD ["bash", "-c", "uvicorn backend.main:app --host 0.0.0.0 --port 8000 & streamlit run frontend/app.py --server.port 8501 --server.address 0.0.0.0"]
