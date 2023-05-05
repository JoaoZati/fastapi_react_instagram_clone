# third party
from sqlalchemy.orm.session import Session
from datetime import datetime
# from fastapi import HTTPException, status

# app
from db.models import Comment
from schemas.comments import CommentBase
# from schemas.users import UserAuth


def create_comment(db: Session, request: CommentBase):
    new_comment = Comment(
        text = request.text,
        username = request.username,
        post_id = request.post_id,
        timestamp = datetime.now(),
    )

    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)

    return new_comment


def get_all_comment(db: Session, post_id: int):
    return db.query(Comment).filter(Comment.post_id == post_id).all()
