from fastapi import FastAPI, HTTPException
from celery.result import AsyncResult

from app.src.dto.temperature import Temperature
from app.src.worker.celery_worker import celery_app, dummy_task
from app.src.worker.redis_lock import lock, redis_instance, REDIS_TASK_KEY

app = FastAPI()


@app.put("/temperature", response_model=Temperature)
def get_temperature():
    return {"Message": "200 OK"}


@app.get("/start")
def start() -> Temperature:
    try:
        if not lock.acquire(blocking_timeout=4):
            raise HTTPException(status_code=500, detail="Could not acquire lock")

        task_id = redis_instance.get(REDIS_TASK_KEY)
        if task_id is None or celery_app.AsyncResult(task_id).ready():
            # no task was ever run, or the last task finished already
            r = dummy_task.delay()
            redis_instance.set(REDIS_TASK_KEY, r.task_id)
            return _task_out(r)
        else:
            # the last task is still running!
            raise HTTPException(
                status_code=400, detail="A task is already being executed"
            )
    finally:
        lock.release()


@app.get("/status")
def status(task_id: str = None) -> Temperature:
    task_id = task_id or redis_instance.get(REDIS_TASK_KEY)
    if task_id is None:
        raise HTTPException(
            status_code=400, detail=f"Could not determine task {task_id}"
        )
    r = celery_app.AsyncResult(task_id)
    return _task_out(r)


def _task_out(result: AsyncResult) -> Temperature:
    return Temperature(id=result.id, status=result.status)
