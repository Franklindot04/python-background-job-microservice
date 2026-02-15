from rq import Worker, Queue
from redis import Redis

redis_conn = Redis(host="redis")
queue = Queue('default', connection=redis_conn)

if __name__ == '__main__':
    worker = Worker([queue])
    worker.work()

