from redis import Redis
from redis.lock import Lock as RedisLock

from app.src.worker.celery_worker import redis_url


redis_instance = Redis.from_url(redis_url)
lock = RedisLock(redis_instance, name="task_id")

REDIS_TASK_KEY = "current_task"