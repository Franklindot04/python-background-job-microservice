# Python Background Job Microservice (FastAPI, Redis, Docker)

A small but production-style background job processing system built with **FastAPI**, **Redis**, **RQ**, and **Docker Compose**.

It exposes a simple HTTP API where clients can enqueue jobs, check their status, and retrieve results—while the actual work is processed asynchronously by a background worker.

## 1. Overview

This project is a Dockerized Python microservice system designed to demonstrate real-world DevOps practices.  
It includes an API built with FastAPI, a background worker for asynchronous processing, and Redis as the message broker.  
The goal is to showcase containerization, service orchestration, logging, troubleshooting, and production‑ready architecture.

---

## 2. Architecture

High-level architecture:

```text
Client (Swagger UI / HTTP)
            |
            v
      FastAPI container (bg-api)
            |
            v
      Redis container (redis)
            |
            v
      Worker container (bg-worker)
            |
            v
      Job processed + result stored
```
---
## 3. Why This Project Matters

**Goal:** Demonstrate how a DevOps engineer designs and runs a small, realistic microservice with:

- **FastAPI** as the HTTP API
- **Redis** as a message broker / job queue
- **RQ worker** for background processing
- **Docker & Docker Compose** for containerized orchestration
- **AWS EC2** as the runtime environment

This project is intentionally small in scope but structured like a real-world service: separate components, clear responsibilities, and observable behavior through logs and HTTP endpoints.

---
## 4. Running the Microservice with Docker Compose

This project is fully containerized using **Docker** and **Docker Compose**. 
All components (API, Redis, Worker) start together with a single command.

### 4.1 Start the entire system

```bash
docker compose up --build
```

This will:

- Build the API image
- Build the Worker image
- Start Redis
- Start all containers
- Attach logs from all services into one terminal

You should see output similar to:

```
Attaching to bg-api, bg-worker, redis
redis      | Ready to accept connections
bg-api     | Uvicorn running on http://0.0.0.0:8000
bg-worker  | Listening on default...
```
### 4.2 Stop everything

Press CTRL + C, then run:

```bash
docker compose down
```

#### 4.3 Access the API

Open:

```bash
http://<your-ec2-ip>:8000/docs
```
This gives you the interactive Swagger UI where you can:

- Submit jobs
- Check job status
- Retrieve results

 ### 4.4 Submit a Job (Example)

Send a POST request to:

```bash
curl -X POST "http://<your-ec2-ip>:8000/jobs" \
     -H "Content-Type: application/json" \
     -d '{"text": "hello world"}'
```

You will receive a JSON response containing a job_id.

### 4.5 Check Job Status

Use the job_id you received earlier:

```bash
curl "http://<your-ec2-ip>:8000/jobs/<job_id>"
```
Possible statuses include:

- queued — the worker has not picked it up yet

- in_progress — the worker is processing it

- completed — the result is ready

- failed — something went wrong during processing
---

### 4.6 Retrieve Results

Once the job status is **completed**, fetch the result:

```bash
curl "http://<your-ec2-ip>:8000/jobs/<job_id>/result"
```
If the job succeeded, you will receive the processed output.
If it failed, you will receive an error message.

### 5. Environment Variables

These variables control how your API and worker behave.  
Create a `.env` file in the project root and add:

```bash
REDIS_HOST=redis
REDIS_PORT=6379
API_PORT=8000
```
Make sure the .env file is in the same directory as your docker-compose.yml.

### 6. Project Structure

Your repository should look like this:


``` 
project/
├── api/
│   ├── main.py
│   ├── worker.py
│   └── requirements.txt
├── docker-compose.yml
├── Dockerfile.api
├── Dockerfile.worker
├── .env
└── README.md
```

### 7. Docker Architecture Overview
This is how the services communicate inside Docker:
```
API ---> Redis ---> Worker
 |                     ^
 |_____________________|

```
The API pushes jobs to Redis, and the worker pulls and processes them.

### 8. Stopping the Services

To stop all running containers, press:

CTRL + C

Then remove the containers (but keep the images) with:

```bash
docker-compose down
```

### 9. Viewing Logs

To see the logs for all running services, use:

```bash
docker-compose logs -f
```
To view logs for a specific service (for example, the API), run:

```bash
docker-compose logs -f api
```

### 10. Testing the API

Once the containers are running, you can test the API using:

```bash
curl http://localhost:8000/
```
To send a job to the worker through the API, run:

```bash
curl -X POST http://localhost:8000/process
```

### 11. Troubleshooting

**1. Port already in use (API fails to start)**  

If you see an error about port 8000 being in use, find the process with:

```bash
lsof -i :8000
```
Then stop it:
```bash
kill -9 <PID>
```

**2. Redis connection errors**

Make sure the Redis container is running:

```bash
docker-compose ps
```
You should see a container named redis with status “Up”.

**3. Code changes not applying** 

If you modify Python files but the container doesn’t update:

```bash
docker-compose up --build
```
This forces Docker to rebuild the images.

**4. Worker not processing jobs**
  
Check worker logs:

```bash
docker-compose logs -f worker
```
If it’s running but idle, the API may not be sending jobs correctly.

### 12. Tech Stack

**Backend**
- Python (FastAPI)
- Redis (message broker)
- Worker service (background job processor)

**Containerization**
- Docker
- Docker Compose

**Infrastructure & DevOps**
- Linux environment
- CI/CD‑ready project structure
- Isolated multi‑service architecture

**Networking**
- Internal Docker networks
- Port mapping for API access

### 13. Future Improvements

- Add Docker health checks for API, Redis, and Worker
- Implement retry logic and dead‑letter queues for failed jobs
- Add unit tests and integration tests for API and Worker
- Introduce environment‑specific Compose files (dev / prod)
- Add monitoring (Prometheus + Grafana) for container metrics
- Migrate to a message queue like RabbitMQ or AWS SQS for scaling
- Add CI/CD pipeline to automate builds and deployments

### 14. Project Summary

This project demonstrates a clean, production‑inspired microservice architecture using Docker and Python.  
It includes an API service built with FastAPI, a background worker for asynchronous job processing, and Redis as the message broker.  
All services run in isolated containers using Docker Compose, making the system easy to start, stop, and extend.

The project highlights practical DevOps skills such as containerization, service orchestration, logging, troubleshooting, and environment‑ready structure.  
It serves as a strong foundation for scaling into more advanced distributed systems or integrating CI/CD pipelines.
  
