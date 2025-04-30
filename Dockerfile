FROM python:3.11-slim

# 1.  System deps
RUN apt-get update && apt-get install -y gcc curl && rm -rf /var/lib/apt/lists/*

# 2.  Poetry or pip
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 3.  Project code
COPY app/ ./app
COPY metadata/ ./metadata
COPY scripts/ ./scripts

# 4.  FastAPI + Uvicorn
ENV PYTHONUNBUFFERED=1
CMD ["uvicorn", "app.main:create_app", "--host=0.0.0.0", "--port=8080", "--factory"]
