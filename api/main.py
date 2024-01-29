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

languages_in = ["wixarika","náhuatl", "yorem nokki", "purépecha", "mexicanero"]
languages_out = ["español"]
#data requirements
class Translate(BaseModel):
    text: str 
    source_lang: str 
    target_lang: str 
    #validate petition languages pair
    @validator('source_lang')
    def valid_source_lang(cls, lang):
        if lang not in languages_in:
            raise ValueError("Lenguaje de entrada no disponible")
        return lang

    @validator('target_lang')
    def valid_target_lang(cls, lang):
        if lang not in languages_out:
            raise ValueError("Lenguaje de salida no disponible")
        return lang
 
@app.get('/',  response_class=HTMLResponse)
def home(request: Request):
        """Renders main page"""
        context = {'request': request, 'src_languages': languages_in, 'trg_languages':languages_out}
        return templates.TemplateResponse("home.html", context)

@app.post('/translate')
def json_analisis(args: Translate):
        # Desempacar
        #texto1=args.text
        # Analisis
        source_lang=args.source_lang
        respuesta="adios"
        # Empaquetar respuesta
        return {"result":str(respuesta), "entrada": source_lang}


