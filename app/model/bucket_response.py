from pydantic import BaseModel


class BucketResponse(BaseModel):
    message: str
