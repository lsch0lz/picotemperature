from fastapi import FastAPI
from celery.result import AsyncResult

from app.src.dto.temperature import Temperature
from app.src.worker.celery_worker import celery_app, dummy_task

app = FastAPI()


@app.put("/temperature")
def get_temperature():
    return {"Message": "200 OK"}


@app.get("/start")
def start_task() -> Temperature:
    r = dummy_task.delay()
    return _task_out(result=r)


@app.get("/status")
def get_task_status(task_id: str):
    r = celery_app.AsyncResult(task_id)
    return _task_out(result=r)


def _task_out(result: AsyncResult) -> Temperature:
    return Temperature(id=result.id, status=result.status)
