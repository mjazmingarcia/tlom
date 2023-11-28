from pydantic import BaseModel
from fastapi import FastAPI
#for templating 
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

__VERSION__ = "0.0.1"
__API_NAME__ = "TLOM API"

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="./templates")
 
@app.get('/')
def home(request: Request):
        """Renders main page"""
        return templates.TemplateResponse("home.html", 
                {'request':request})

