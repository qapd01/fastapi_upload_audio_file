from typing import Annotated

from fastapi import FastAPI, File, Request
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
def read_item(file: Annotated[bytes, File()]):
    print(file)
    with open("uploaded_audio.wav", "wb") as audio_file:
        audio_file.write(file)
    return {"status": "File saved successfully"}
