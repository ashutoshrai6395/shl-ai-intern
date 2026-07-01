# SHL AI Intern Assessment Recommender

## Overview
This project is a FastAPI-based REST API that recommends SHL assessments based on user job requirements. It supports conversational recommendations and follow-up questions for incomplete queries.

## Features
- Recommend SHL assessments based on job descriptions
- Conversational chat endpoint
- Health check endpoint
- FastAPI Swagger documentation
- Deployed on Render

## Tech Stack
- Python
- FastAPI
- Uvicorn
- Requests
- BeautifulSoup4

## API Endpoints

### Health Check
GET /health

Response:
```json
{
  "status": "ok"
}
```

### Chat
POST /chat

Example Request:
```json
{
  "messages": [
    {
      "role": "user",
      "content": "Looking for a Java developer"
    }
  ]
}
```

## Deployment

Live API:
https://shl-ai-intern-7fsd.onrender.com

Swagger Documentation:
https://shl-ai-intern-7fsd.onrender.com/docs