# tird party
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session

# app
from db.database import get_db
from db.models import User
from auth.hash import verify
from auth.oauth2 import create_access_token

router = APIRouter(
    # prefix="/auth",
    tags=["auth"],
)

HTTP_404_LOGIN_ERROR = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Invalid username or password"
)


# @router.post("")
@router.post("/login")
def login(
    request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.username == request.username).first()
    if not user:
        raise HTTP_404_LOGIN_ERROR
    elif not verify(user.password, request.password):
        raise HTTP_404_LOGIN_ERROR

    access_token = create_access_token(data={"username": user.username})

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_id": user.id,
        "username": user.username,
    }
