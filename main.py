from typing import Annotated

from fastapi import FastAPI, File, Request, Form, UploadFile
from fastapi.templating import Jinja2Templates
from starlette.templating import _TemplateResponse

app = FastAPI()

templates = Jinja2Templates(directory="src/templates")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/upload-file")
async def get_form_upload_trading_ideas(request: Request) -> _TemplateResponse:
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/upload-file")
def read_item(
        file: Annotated[UploadFile, File()],
        file2: Annotated[UploadFile, File()],
        name: Annotated[str, Form()]
):
    print(file)
    print(file2)
    print(name)
    with open("uploaded_audio.wav", "wb") as audio_file:
        audio_file.write(file.file.read())
    return {"status": "File saved successfully"}


@app.post("/uploadfiles")
async def create_upload_files(files: list[UploadFile]):
    uploaded_files = []
    for file in files:
        contents = await file.read()
        with open(file.filename, "wb") as f:
            f.write(contents)
        uploaded_files.append(file.filename)
    return {"filenames": uploaded_files}
