import boto3
import os
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client('s3',
    region_name=os.getenv("AWS_REGION"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
)

def upload_clip_to_s3(local_path: str, s3_key: str) -> str:
    try:
        bucket = os.getenv("S3_BUCKET_NAME")
        s3.upload_file(local_path, bucket, s3_key)
        return f"https://{bucket}.s3.amazonaws.com/{s3_key}"
    except Exception as e:
        print(f"exception:{e}") 
        return ""   
    
