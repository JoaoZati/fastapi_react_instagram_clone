# tird party
from fastapi import APIRouter, Depends, status, UploadFile, File
from fastapi.exceptions import HTTPException
from sqlalchemy.orm.session import Session
from typing import List
import string
import random
import shutil

# app
from schemas.posts import PostBase, PostDisplay
from db.database import get_db
from service.posts import create_post_db, get_all_db


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


@router.get("/all", response_model=List[PostDisplay])
def get_all(db: Session = Depends(get_db)):
    return get_all_db(db)


@router.post("/image")
def upload_image(image: UploadFile = File(...)):
    latters = string.ascii_letters
    random_str = "".join(random.choice(latters) for i in range(6))

    image_extension = (
        image.filename.split(".")[1] if len(image.filename.split(".")) >= 2 else ""
    )
    filename = f"_{random_str}.{image_extension}"
    path = f"static/img/{filename}"

    with open(path, "w+b") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {"filename": path}
