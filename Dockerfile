# Base image
FROM python:3.11-slim

# Set workdir
WORKDIR /app

# Copy project
COPY . /app

# Upgrade pip
RUN pip install --upgrade pip

# Install dependencies
RUN pip install -r requirements.txt

# Create temp folder
RUN mkdir -p temp

# Expose ports
EXPOSE 8000 8501

# Start both FastAPI and Streamlit
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port 8000 & streamlit run test_client.py --server.port 8501 --server.address 0.0.0.0"]
