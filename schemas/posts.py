from pydantic import BaseModel
from datetime import datetime


class User(BaseModel):
    username: str


class PostBase(BaseModel):
    image: str
    image_url_type: str
    caption: str
    creator_id: int


class PostDisplay(BaseModel):
    image: str
    image_url_type: str
    caption: str
    timestamp: datetime
    user: User

    class Config:
        orm_mode = True
