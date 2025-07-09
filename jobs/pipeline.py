import uuid
from utils.downloader import download_video
from utils.transcriber import transcribe
from utils.summerizer import get_highlights
from utils.editor import cut_clips
from db.crud import create_task, update_task_status
from utils.storage import upload_clip_to_s3

def process_video(youtube_url: str):
    task_id = str(uuid.uuid4())[:8]
    create_task(task_id, youtube_url)
    try:

        input_path = f"static/{task_id}_input.mp4"
        download_video(youtube_url, output_path=input_path)
        update_task_status(task_id, "transcribing")
        transcript = transcribe(input_path)
        update_task_status(task_id, "summarizing")
        highlights = get_highlights(transcript)
        update_task_status(task_id, "editing")
        clips = cut_clips(input_path, highlights)
        update_task_status(task_id, "done")
        s3_urls  = []
        for i, local_path in enumerate(clips):
             s3_key = f"tasks/{task_id}/clip_{i}.mp4"
             s3_url = upload_clip_to_s3(local_path,s3_key)
             print(f"s3 url {i}: {s3_url} and s3 key: {s3_key}")
             s3_urls.append(s3_url)
        update_task_status(task_id, "done")     
    except Exception as e:
          print(f"exception is :{e}")
          update_task_status(task_id, "failed")

    return s3_urls
