from pydantic import BaseModel, EmailStr
from typing import List, Optional


class BucketRequest(BaseModel):
    name: Optional[str]
    name: Optional[int]
    name: List[EmailStr]
    name: str

