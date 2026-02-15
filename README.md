# 🚀 Python Background Job Microservice (FastAPI + Redis + RQ)

A lightweight, production‑style microservice that processes background jobs using **FastAPI**, **Redis**, and **RQ**.  
This project demonstrates real‑world DevOps skills, including:

- API design  
- Background job queues  
- Worker processes  
- Multi‑terminal architecture  
- Linux + AWS EC2 deployment  
- Clean documentation and reproducible workflows  

This is the kind of system used in real companies for email sending, report generation, data processing, and asynchronous workflows.

---

# 🧱 Architecture Overview

This microservice follows a clean, decoupled architecture:

```
┌──────────────────────────┐        ┌──────────────────────────┐
│        FastAPI API       │        │        RQ Worker         │
│  - /enqueue              │        │  - Listens to Redis      │
│  - /status/{job_id}      │ <----> │  - Executes jobs         │
│  - /result/{job_id}      │        │  - Returns results       │
└─────────────┬────────────┘        └─────────────┬────────────┘
              │                                     │
              │                                     │
              ▼                                     ▼
        ┌──────────────────────────────────────────────────┐
        │                     Redis Queue                   │
        │  - Stores jobs                                    │
        │  - Tracks job state                               │
        │  - Holds results (TTL: 500 seconds)               │
        └──────────────────────────────────────────────────┘
```


This architecture mirrors real production systems used in modern microservices.

---

# ✨ Features

- Submit background jobs via REST API  
- Track job status (queued, started, finished, failed)  
- Retrieve job results  
- Redis‑backed queue  
- RQ worker process  
- FastAPI Swagger UI  
- Multi‑terminal workflow (API, worker, free terminal)  
- AWS EC2 deployment  

---

# 🛠 Tech Stack

| Component | Technology |
|----------|------------|
| API | FastAPI + Uvicorn |
| Queue | Redis |
| Worker | RQ (Redis Queue) |
| Language | Python 3 |
| Hosting | AWS EC2 (Amazon Linux) |
| OS | Linux |
| Tools | nano, systemctl, pip, venv |

---

# 📦 Installation & Setup

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd python-microservice
```
### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn redis rq
```

### 4. Start Redis (if running locally)

```bash
redis-server
```

5. Start the API (Terminal 1)
uvicorn main:app --host 0.0.0.0 --port 8000
6. Start the worker (Terminal 2)
python worker.py
7. Use Terminal 3 for testing and editing
# 📡 API Endpoints

## **POST /enqueue**

Submit a background job.

**Request:**
```json
{"name": "Franklin"}
```

**Response:**
```json
{"job_id": "<uuid>"}
```

![Screenshot #4](https://raw.githubusercontent.com/Franklindot04/python-background-job-microservice/main/Screenshot%204-%202026-02-15%20at%2010.39.51.png)
*“Enqueueing a job via FastAPI Swagger UI.”*

---

## **GET /status/{job_id}**

Check the status of a job.

**Response:**
```json
{
  "job_id": "<uuid>",
  "status": "finished"
}
```

![Screenshot #6](https://raw.githubusercontent.com/Franklindot04/python-background-job-microservice/main/Screenshot%206-%202026-02-15%20at%2009.15.25.png)
*“Checking job status using the /status endpoint.”*

---

## **GET /result/{job_id}**

Retrieve the final output of a completed job.

**Response:**
```json
{
  "job_id": "<uuid>",
  "result": {
    "status": "done",
    "input": {"name": "Franklin"}
  }
}
```
![Screenshot #7](https://raw.githubusercontent.com/Franklindot04/python-background-job-microservice/main/Screenshot%207-2026-02-15%20at%2009.24.46.png)
*“Retrieving job results from Redis.”*

# 🔄 Job Lifecycle (How It Works)

Client sends a job to /enqueue

FastAPI pushes the job into Redis

Redis assigns a job ID

RQ Worker (Terminal 2) picks up the job

Worker executes process_job()

Worker stores the result in Redis

Client checks /status/{job_id}

Client retrieves output via /result/{job_id}

This is the same pattern used by:

Celery

Sidekiq

AWS SQS workers

Background job systems in production

# 🖼 Worker Logs

![Screenshot #5](https://raw.githubusercontent.com/Franklindot04/python-background-job-microservice/main/Screenshot%205-%202026-02-15%20at%2008.53.03.png)
“Worker receiving and processing a job.”

This screenshot proves:

Redis is connected

Worker is alive

Job executed successfully

# 🏁 Final Result

You now have a fully functional microservice with:

Background processing

Job tracking

Job result retrieval

Redis queue

RQ worker

FastAPI API

Clean documentation

Real AWS deployment

This is a portfolio‑quality project that demonstrates real DevOps engineering skills.

# 🚀 Future Improvements

Add Docker + Docker Compose

Add authentication

Add retry logic for failed jobs

Add monitoring (Flower, Prometheus, Grafana)

Add persistent result storage (PostgreSQL)

Deploy with CI/CD pipeline

---
