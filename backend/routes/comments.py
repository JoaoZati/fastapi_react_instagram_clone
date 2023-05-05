# tird party
from fastapi import APIRouter, Depends, status, UploadFile, File
from fastapi.exceptions import HTTPException
from sqlalchemy.orm.session import Session

# app
from db.database import get_db
from service.comments import get_all_comment, create_comment
from schemas.comments import CommentBase
from schemas.users import UserAuth

router = APIRouter(
    prefix="/comment", 
    tags=["comment"],
)


@router.get("/all/{post_id}")
def get_all(post_id: int, db: Session = Depends(get_db)):
    return get_all_comment(db, post_id)


@router.post("/create")
def create(
    request: CommentBase,
    db: Session = Depends(get_db),
    current_user: UserAuth = Depends(get_db),
):
    return create_comment(db, request)
