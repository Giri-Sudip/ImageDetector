# from fastapi import FastAPI, File, UploadFile

# app = FastAPI()



# @app.post("/uploadfile/")
# def create_upload_file(file: UploadFile):

#     return {"filename": file.filename}

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response
from random import randint
import uuid

app = FastAPI()

db = []


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