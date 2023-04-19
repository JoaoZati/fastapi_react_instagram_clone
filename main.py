from fastapi import FastAPI
import uvicorn
from db.models import Base
from db.database import engine

app = FastAPI()
Base.metadata.create_all(engine)


@app.get("/")
def root():
    return {"message": "hello world"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
