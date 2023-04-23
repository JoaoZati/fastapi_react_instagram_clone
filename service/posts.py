from schemas.posts import PostBase
from sqlalchemy.orm.session import Session
from db.models import Post
from datetime import datetime


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
