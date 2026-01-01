from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/download")
async def download_file():
    file_path = "downloads/emotionsml.zip"
    
    if os.path.exists(file_path):
        return FileResponse(
            path=file_path, 
            filename="emotionsml.zip",
            media_type='application/zip'
        )
    return {"error": "El archivo de descarga no existe en la carpeta downloads"}