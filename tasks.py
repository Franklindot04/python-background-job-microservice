import time

def process_job(data):
    print(f"Starting job with data: {data}")
    time.sleep(5)  # simulate a slow task
    print("Job completed!")
    return {"status": "done", "input": data}
