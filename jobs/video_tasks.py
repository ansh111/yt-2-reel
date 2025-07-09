from celery_worker import celery_app
from jobs.pipeline import process_video  # your actual video logic

@celery_app.task(name="jobs.video_tasks.process_video_task")
def process_video_task(youtube_url: str, task_id: str):
    process_video(youtube_url, task_id)