from pydantic import BaseModel
from datetime import datetime
from typing import List


class User(BaseModel):
    username: str

    class Config:
        orm_mode = True


class Comment(BaseModel):
    text: str
    username: str
    timestamp: datetime

    class Config:
        orm_mode = True


class PostBase(BaseModel):
    image_url: str
    image_url_type: str
    caption: str
    creator_id: int


class PostDisplay(BaseModel):
    image_url: str
    image_url_type: str
    caption: str
    timestamp: datetime
    user: User
    comments: List[Comment]

    class Config:
        orm_mode = True
