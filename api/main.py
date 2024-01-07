from pydantic import BaseModel, validator
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

languages = ["lang1","lang2", "lang3"]
#data requirements
class Translate(BaseModel):
    text: str 
    source_lang: str 
    target_lang: str 
    #validate petition languages pair
    @validator('source_lang','target_lang')
    def valid_lang(cls, lang):
        if lang not in languages:
            raise ValueError("Lenguaje no disponible")
        return lang
 
@app.get('/',  response_class=HTMLResponse)
def home(request: Request):
        """Renders main page"""
        context = {'request': request, 'languages': languages}
        return templates.TemplateResponse("home.html", context)

@app.post('/translate')
def json_analisis(args: Translate):
        # Desempacar
        #texto1=args.text
        # Analisis
        respuesta="adios"
        # Empaquetar respuesta
        return {"result":str(respuesta)}


