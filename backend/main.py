# tird party
import os
from fastapi import FastAPI, Request, Response
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


def add_cors_header(request: Request, response: Response) -> None:
    response.headers["Access-Control-Allow-Origin"] = request.headers.get("Origin", "")
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "*"


@app.middleware("http")
async def add_custom_header(request: Request, call_next):
    response = await call_next(request)
    add_cors_header(request, response)
    return response


@app.get("/")
def root():
    return {"message": "hello world"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
