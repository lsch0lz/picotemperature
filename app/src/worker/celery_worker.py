import os
import time
from datetime import datetime

from celery.app import Celery

redis_url = os.getenv("REDIS_URL", "redis://localhost:6379")

celery_app = Celery('worker', broker=redis_url, backend=redis_url)


@celery_app.task
def dummy_task():
    time.sleep(10)
    folder = "/tmp/celery"
    os.makedirs(folder, exist_ok=True)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(f"{folder}/task-{now}.txt", "w") as f:
        f.write("Celery task executed successfully")
       