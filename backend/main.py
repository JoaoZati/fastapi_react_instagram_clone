# tird party
import os
from fastapi import FastAPI
import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

# app
from config import BASE_DIR
from db.models import Base
from db.database import engine
from auth import authentication
from routes import (
    users,
    posts,
    comments,
)



# routes
app = FastAPI()
app.include_router(authentication.router)
app.include_router(users.router)
app.include_router(posts.router)
app.include_router(comments.router)

# configure static files
Base.metadata.create_all(engine)
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

# configure cors
origins = (
    "http://localhost:3000"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


@app.get("/")
def root():
    return {"message": "hello world"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
