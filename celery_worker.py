from celery import Celery


celery_app = Celery(
    "worker",
    broker="redis://localhost:6379/0",  # or your Redis URL
    backend="redis://localhost:6379/0",
)

celery_app.autodiscover_tasks(['jobs']) 
import jobs.video_tasks


