# tird party
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

# app
from schemas.users import UserDisplay, UserBase
from db.database import get_db
from service.users import create_user_db

router = APIRouter(
    prefix="/user",
    tags=['user']
)


@router.post('', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return create_user_db(db, request)
