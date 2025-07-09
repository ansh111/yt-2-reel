# Dockerfile
FROM python:3.11

WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y ffmpeg
RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
