# Docker Compose MinIO FastAPI App

## Prerequisites
- Docker
- Docker Compose

## Setup

1. Copy the environment file:
   ```bash
   cp .env.example .env
   ```

2. Build and run the services:
   ```bash
   docker-compose up --build
   ```

## Services

- **FastAPI App**: http://localhost:8000
  - Upload endpoint: POST /upload
  - Interactive docs: http://localhost:8000/docs

- **MinIO Console**: http://localhost:9001
  - Username: minioadmin
  - Password: minioadmin

- **MinIO API**: http://localhost:9000

## Usage

1. Access FastAPI docs at http://localhost:8000/docs
2. Use the `/upload` endpoint to upload files
3. Access MinIO console at http://localhost:9001 to manage buckets and files

## Development

For development with hot reload, you can run:
```bash
docker-compose up
```

The application code is mounted as a volume, so changes will be reflected automatically.

## Environment Variables

- `MINIO_ENDPOINT`: MinIO server endpoint
- `MINIO_ACCESS_KEY`: MinIO access key
- `MINIO_SECRET_KEY`: MinIO secret key

## Notes

- The `mybucket` bucket is automatically created when the application starts
- Files uploaded through the API will be stored in MinIO
- The application returns presigned URLs for file access
