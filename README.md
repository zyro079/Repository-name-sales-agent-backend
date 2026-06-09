# Sales Agent Backend

A FastAPI-based Sales Agent Backend with memory storage, product catalog search, REST APIs, SQLite database integration, and Railway cloud deployment.

## Features

* Product catalog search
* User conversation memory
* Chat API endpoint
* User history retrieval
* Memory clearing
* Health monitoring endpoint
* SQLite database storage
* Railway deployment
* Swagger API documentation

---

## Tech Stack

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Uvicorn
* Railway
* GitHub

---

## Installation

Clone the repository:

```bash
git clone https://github.com/zyro079/Repository-name-sales-agent-backend.git
cd Repository-name-sales-agent-backend
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

## Deployment

Railway URL:

https://repository-name-sales-agent-backend-production.up.railway.app

Swagger Documentation:

https://repository-name-sales-agent-backend-production.up.railway.app/docs

Health Endpoint:

https://repository-name-sales-agent-backend-production.up.railway.app/health

---

## API Endpoints

### Home

GET /

Response:

```json
{
  "message": "Sales Agent API Running"
}
```

### Health Check

GET /health

Response:

```json
{
  "status": "healthy"
}
```

### Catalog

GET /catalog

Returns available products from catalog.json.

### Chat

POST /chat/{user_id}

Request:

```json
{
  "message": "laptop"
}
```

Response:

```json
{
  "response": "I found 1 matching product(s).",
  "memory_count": 1,
  "catalog_results": [],
  "eval": {
    "groundedness": 0.9,
    "relevance": 0.9,
    "confidence": 0.9,
    "flagged": false
  }
}
```

### User History

GET /history/{user_id}

Returns saved conversation history.

### Clear Memory

DELETE /memory/{user_id}

Response:

```json
{
  "message": "Memory cleared for user_id"
}
```

---

## Project Structure

```text
sales-agent-backend/
│
├── main.py
├── database.py
├── models.py
├── memory.py
├── tools.py
├── catalog.json
├── requirements.txt
├── README.md
└── sales_agent.db
```

---

## Author

Siraj

GitHub:
https://github.com/zyro079
