# tird party
from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm.session import Session

# app
from schemas.posts import PostBase, PostDisplay
from db.database import get_db
from service.posts import create_post_db


router = APIRouter(prefix="/post", tags=["post"])

image_url_types = ["absolute", "relative"]


@router.post("", response_model=PostDisplay)
def create(request: PostBase, db: Session = Depends(get_db)):
    if not request.image_url_type in image_url_types:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Parameter image_url_type can only be take values of: {image_url_types}",
        )

    return create_post_db(db, request)
