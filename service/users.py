from schemas.users import UserBase
from sqlalchemy.orm.session import Session
from db.models import User
from utils import hash_bycrpt


def create_user_db(db: Session, request: UserBase):
    new_user = User(
        username=request.username,
        email=request.email,
        password=hash_bycrpt(request.password),
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
