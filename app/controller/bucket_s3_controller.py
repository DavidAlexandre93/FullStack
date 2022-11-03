from fastapi import APIRouter, Depends
from app.service.bucket_service import BucketS3
from app.database.connection import AsyncSession, get_session
# from app.model.bucket_request import EmailRequest
# from app.model.bucket_response import EmailResponse

bucket_router = APIRouter(tags=["Bucket_S3"])


@bucket_router.get("/read_file_bucket")
async def read_file_bucket_data():
    return await BucketS3.fileReadBucket()


@bucket_router.post("/save_file_bucket")
async def save_file_bucket_data(db: AsyncSession = Depends(get_session)):
    return await BucketS3.fileSaveData(db=db)
