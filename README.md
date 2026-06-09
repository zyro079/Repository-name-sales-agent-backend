# Sales Agent Backend

A FastAPI-based Sales Agent Backend that demonstrates persistent memory, tool usage, self-evaluation, and cloud deployment.

## Live Demo

**Railway URL**

https://repository-name-sales-agent-backend-production.up.railway.app

**Swagger Documentation**

https://repository-name-sales-agent-backend-production.up.railway.app/docs

**Health Endpoint**

https://repository-name-sales-agent-backend-production.up.railway.app/health

---

# Project Overview

This project implements a conversational Sales Assistant Agent for a SaaS company.

The agent:

* Searches a product catalog using tools
* Stores user conversations in persistent memory
* Retrieves user history across sessions
* Returns structured evaluation scores with every response
* Exposes REST APIs for frontend integration
* Is deployed publicly on Railway

---

# Architecture

```text
Client
  |
  v
POST /chat/{user_id}
  |
  v
FastAPI Route
  |
  v
Chat Service
  |
  +------------------------+
  |                        |
  v                        v
search_catalog()     get_user_memory()
  |                        |
  +-----------+------------+
              |
              v
      Generate Response
              |
              v
      Evaluation Layer
              |
              v
         JSON Response
```

---

# Product Catalog

```json
{
  "plans": [
    {
      "name": "Starter",
      "price": "$49/mo",
      "features": [
        "5 users",
        "API access",
        "email support"
      ]
    },
    {
      "name": "Growth",
      "price": "$199/mo",
      "features": [
        "25 users",
        "webhooks",
        "priority support"
      ]
    },
    {
      "name": "Enterprise",
      "price": "$499/mo",
      "features": [
        "unlimited users",
        "SSO",
        "audit logs",
        "SLA"
      ]
    }
  ]
}
```

---

# Features

* Persistent conversation memory
* Product catalog search
* Tool-based retrieval
* Self-evaluation scoring
* Conversation history endpoint
* Memory deletion endpoint
* Railway deployment
* Swagger API documentation

---

# Tech Stack

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Uvicorn
* GitHub
* Railway

---

# Installation

Clone the repository:

```bash
git clone https://github.com/zyro079/Repository-name-sales-agent-backend.git
cd Repository-name-sales-agent-backend
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run locally:

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## GET /

Returns API status.

Response:

```json
{
  "message": "Sales Agent API Running"
}
```

---

## GET /health

Response:

```json
{
  "status": "healthy"
}
```

---

## GET /catalog

Returns the SaaS pricing catalog.

---

## POST /chat/{user_id}

Request:

```json
{
  "message": "Tell me about Enterprise pricing"
}
```

Response:

```json
{
  "response": "I found 1 matching product(s).",
  "memory_count": 1,
  "catalog_results": [],
  "eval": {
    "groundedness": 0.90,
    "relevance": 0.90,
    "confidence": 0.90,
    "flagged": false
  },
  "tools_called": [
    "search_catalog",
    "get_user_memory"
  ]
}
```

---

## GET /history/{user_id}

Returns stored conversation history.

---

## DELETE /memory/{user_id}

Deletes all stored memory for a user.

---

# Memory Design

The application stores user conversations in SQLite using SQLAlchemy.

Each message is saved with:

* user_id
* role
* message

Memory retrieval occurs through the get_user_memory() tool.

This allows the same user_id to maintain context across multiple API calls and sessions.

### Why SQLite?

SQLite was selected because:

* Easy deployment
* Persistent storage
* No external infrastructure required

### Production Upgrade Path

For production scale, SQLite would be replaced with PostgreSQL while keeping the memory abstraction unchanged.

---

# Tool Design

The agent uses real callable tools:

### search_catalog(query)

Searches the SaaS pricing catalog.

### get_user_memory(user_id)

Retrieves stored conversation history from the database.

These tools reduce hallucination risk by grounding responses in stored data.

---

# Evaluation Design

Every response includes:

```json
{
  "groundedness": 0.90,
  "relevance": 0.90,
  "confidence": 0.90,
  "flagged": false
}
```

Current implementation uses deterministic backend-generated scores.

### Limitations

* No independent evaluation model
* No semantic quality validation
* No hallucination detection

### Future Improvements

* LLM-based self-evaluation
* Retrieval groundedness checks
* Human escalation workflows

---

# Cross-Session Memory Demonstration

### Call 1

```bash
curl -X POST "https://repository-name-sales-agent-backend-production.up.railway.app/chat/john" \
-H "Content-Type: application/json" \
-d "{\"message\":\"Tell me about Enterprise pricing\"}"
```

### Call 2

```bash
curl -X POST "https://repository-name-sales-agent-backend-production.up.railway.app/chat/john" \
-H "Content-Type: application/json" \
-d "{\"message\":\"Does that include SSO?\"}"
```

### Verify Memory

```bash
curl "https://repository-name-sales-agent-backend-production.up.railway.app/history/john"
```

The history endpoint demonstrates that memory persists across separate API requests.

---

# Project Structure

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

# Design Tradeoffs

### Why Tool-Based Retrieval?

Tool-based retrieval ensures responses are grounded in actual catalog data and stored memory.

### Why Not an LLM?

The project focuses on backend architecture, persistence, tool usage, and deployment rather than model performance.

### What Would Change At Scale?

* PostgreSQL
* Vector memory
* LLM-based evaluation
* Human review queues
* Advanced retrieval systems

---

# Author

Siraj

GitHub:
https://github.com/zyro079
