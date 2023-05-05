from pydantic import BaseModel

class CommentBase(BaseModel):
    username: str
    text: str
    post_id: int
