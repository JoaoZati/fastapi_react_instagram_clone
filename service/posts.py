# third party
from sqlalchemy.orm.session import Session
from datetime import datetime
from fastapi import HTTPException, status

# app
from db.models import Post
from schemas.posts import PostBase
from schemas.users import UserAuth


def create_post_db(db: Session, request: PostBase):
    new_post = Post(
        image_url=request.image_url,
        image_url_type=request.image_url_type,
        caption=request.caption,
        timestamp=datetime.now(),
        user_id=request.creator_id,
    )

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


def get_all_db(db: Session):
    return db.query(Post).all()


def delete_post_db(id: int, db: Session, current_user: UserAuth):
    post = db.query(Post).filter(Post.id == id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {id} not found",
        )

    if post.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Only post creater can delete its own post",
        )

    db.delete(post)
    db.commit()
    return {'message': 'ok'}
