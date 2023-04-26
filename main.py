# tird party
from fastapi import FastAPI
import uvicorn
from fastapi.staticfiles import StaticFiles

# app
from db.models import Base
from db.database import engine
from auth import authentication
from routes import (
    users,
    posts,
)

app = FastAPI()
app.include_router(authentication.router)
app.include_router(users.router)
app.include_router(posts.router)

Base.metadata.create_all(engine)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def root():
    return {"message": "hello world"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
