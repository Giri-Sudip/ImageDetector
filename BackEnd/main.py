from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response
from random import randint
from starlette.requests import Request
import uuid
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

db = []

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:8000/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/main")
def main():
    return{"message":"Welcome"}


@app.post("/images/")
async def create_upload_file(file: UploadFile = File(...)):

    file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()  # <-- Important!

    db.append(contents)

    return {"filename": file.filename}


@app.get("/images/")
async def read_random_file():
# get a random file from the image db
 random_index = randint(0, len(db) - 1)
 response = Response(content=db[random_index])
 return response

