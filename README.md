\# Sales Agent Backend



\## Overview



This project is a FastAPI-based AI Sales Agent backend that supports:



\* Product catalog lookup

\* User conversation memory

\* SQLite database storage

\* Tool calling

\* Conversation history retrieval



\## Features



\### Product Catalog



Reads products from `catalog.json` and searches plans and features.



\### Memory System



Stores user messages in SQLite and retrieves previous conversation history.



\### API Endpoints



\#### GET /



Returns API status.



\#### GET /health



Returns health status.



\#### GET /catalog



Returns available plans from the catalog.



\#### POST /chat/{user\_id}



Stores a user message, searches the catalog, and returns matching results.



\#### GET /chat/{user\_id}/history



Returns conversation history for a user.



\#### DELETE /chat/{user\_id}/memory



Clears conversation memory for a user.



\## Technologies



\* Python

\* FastAPI

\* SQLite

\* SQLAlchemy

\* Pydantic



\## Installation



```bash

pip install -r requirements.txt

```



\## Run



```bash

python -m uvicorn main:app --reload

```



\## Swagger Documentation



Open:



```text

http://127.0.0.1:8000/docs

```



