from asyncio import gather, run
from fastapi import Depends
from app.database.connection import AsyncSession, get_session
from app.database.init_db import create_database
from app.service.bucket_service import BucketS3


async def populate(db: AsyncSession = Depends(get_session)):
    await create_database()
    await gather(*[BucketS3.fileSaveData(db=db)])
    tasks = []
    await gather(*tasks)

    run(populate(db=db))
