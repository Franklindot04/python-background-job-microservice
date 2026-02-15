from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Microservice is running!"}
from rq import Queue
from redis import Redis
from tasks import process_job

redis_conn = Redis(host="redis")
queue = Queue('default', connection=redis_conn)

@app.post("/enqueue")
def enqueue_job(data: dict):
    job = queue.enqueue(process_job, data)
    return {"job_id": job.get_id()}
from rq.job import Job

@app.get("/status/{job_id}")
def get_status(job_id: str):
    job = Job.fetch(job_id, connection=redis_conn)
    return {"job_id": job_id, "status": job.get_status()}
@app.get("/result/{job_id}")
def get_result(job_id: str):
    try:
        job = Job.fetch(job_id, connection=redis_conn)
        return {"job_id": job_id, "result": job.result}
    except Exception:
        return {"error": "Job not found or expired"}
