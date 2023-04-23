from .database import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    items = relationship("Post", back_populates="user")


class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True, index=True)

    image = Column(Integer, )
    image_url = Column(String)
    image_url_type = Column(String)
    caption = Column(String)
    timestamp = Column(DateTime)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="items")
