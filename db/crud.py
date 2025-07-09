
from db.models import Task
from db.sessions import SessionLocal

def create_task(task_id: str, youtube_url: str):
    db = SessionLocal()
    task = Task(id=task_id, youtube_url=youtube_url)
    db.add(task)
    db.commit()
    db.refresh(task)
    db.close()
    return task

def update_task_status(task_id: str, status: str):
    db = SessionLocal()
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        task.status = status
        db.commit()
    db.close()

def get_task(task_id: str):
    db = SessionLocal()
    task = db.query(Task).filter(Task.id == task_id).first()
    db.close()
    return task


def get_task_by_url(youtube_url: str):
    db = SessionLocal()
    task = db.query(Task).filter(Task.youtube_url == youtube_url).first()
    db.close()
    return task

