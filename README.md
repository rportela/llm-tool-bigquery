# llm-tool-bigquery

A secure REST API connecting OpenAI's function calling capabilities to BigQuery, enabling AI agents to directly query your data warehouse while maintaining access controls.

## Architecture

```
┌─────────┐      ┌───────────┐      ┌────────────┐      ┌────────────┐
│         │      │           │      │            │      │            │
│ FastAPI │─────▶│  BigQuery │◀────▶│ OpenAI    │◀────▶│  MCP       │
│ Server  │      │ Database  │      │ Tool      │      │  Client    │
│         │      │           │      │            │      │            │
└─────────┘      └───────────┘      └────────────┘      └────────────┘
```

## Clone repository

git clone https://github.com/rportela/llm-tool-bigquery.git
cd bq-openai-tool-api

# Install dependencies

pip install -r requirements.txt

# Set environment variables

export GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/credentials.json
export OPENAI_API_KEY=your_openai_api_key
export DATASETS_ALLOWLIST=dataset1,dataset2

# Run server

uvicorn app.main:app --reload
Environment Variables
Variable Description Required

## API Endpoints

GET /health
Health check endpoint to verify service status.

Example Response:

## Build Docker image

docker build -t bq-openai-tool-api .

## Run container

docker run -p 8000:8000 \
 -e GOOGLE_APPLICATION_CREDENTIALS=/app/credentials.json \
 -e OPENAI_API_KEY=your_openai_api_key \
 -e DATASETS_ALLOWLIST=dataset1,dataset2 \
 -v /path/to/your/credentials.json:/app/credentials.json \
 bq-openai-tool-api
