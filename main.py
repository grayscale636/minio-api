from fastapi import FastAPI, File, UploadFile
from minio import Minio
from minio.error import S3Error
from dotenv import load_dotenv
import os
import io

load_dotenv()

MINIO_ENDPOINT = os.getenv("MINIO_ENDPOINT")
MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY")
MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY")

app = FastAPI(title="irmnet-api-storage", description="API for uploading files to MinIO", version="1.0")

# configure MinIO client
minio_client = Minio(
    endpoint=MINIO_ENDPOINT,
    access_key=MINIO_ACCESS_KEY,
    secret_key=MINIO_SECRET_KEY,
    secure=False,
)

bucket_name = "mybucket"

# check if bucket exists, if not create it
if not minio_client.bucket_exists(bucket_name):
    minio_client.make_bucket(bucket_name)


@app.post("/upload", tags=["File Handling"])
async def upload_file(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        file_obj = io.BytesIO(contents)

        minio_client.put_object(
            bucket_name,
            file.filename,
            data=file_obj,
            length=len(contents),
            content_type=file.content_type,
        )
        url = minio_client.presigned_get_object(bucket_name, file.filename)

        return {"message": "File uploaded", "filename": file.filename, "file_url": url}
    except S3Error as e:
        return {"error": str(e)}
