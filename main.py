from fastapi import FastAPI, Form
from jobs.pipeline import process_video

from db.sessions import Base, engine
from db.crud import create_task, get_task, get_task_by_url
import uuid
from jobs.video_tasks import process_video_task

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.post("/process-youtube")
def process(youtube_url: str = Form(...)):
    existing  = get_task_by_url(youtube_url)
    if existing:
        return {"task_id": existing.id, "deduplicated": True, "status": existing.status}
    s3_urls = process_video(youtube_url)
    return {"status": "processing", "task_id": s3_urls}

@app.post("/process-youtube-async")
def process(youtube_url: str = Form(...)):
    existing  = get_task_by_url(youtube_url)
    if existing:
        return {"task_id": existing.id, "deduplicated": True, "status": existing.status}
    task_id = process_video_task.delay(youtube_url)
    return {"status": "processing", "task_id": task_id}


@app.get("/status/{task_id}")
def check_status(task_id: str):
    task = get_task(task_id)
    if task:
        return {"task_id": task.id, "status": task.status}
    return {"error": "Task not found"}, 404
