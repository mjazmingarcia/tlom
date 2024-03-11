from pydantic import BaseModel, validator
from fastapi import FastAPI
#import model files for do_translation
from models import model1, model2
#for tasks functions
from api import tasks
#string validation
from pydantic import Field
#for templating 
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
#constant value
from api.const import SRC_LANGUAGE, TGT_LANGUAGE, DESCRIPTION
from typing import get_args

app = FastAPI(
    title="TLOM API",
    description= DESCRIPTION,
    version="0.0.1",
)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="./templates")

languages_in = ["wixarika","náhuatl", "yorem nokki", "purépecha", "mexicanero"]
languages_out = ["español"]
#data requirements
class Translate(BaseModel):
    text: str = Field(max_length=30, description='El texto no debe tener más de 30 caracteres')
    source_lang: SRC_LANGUAGE 
    target_lang: TGT_LANGUAGE
    
#renders main page 
@app.get('/',  response_class=HTMLResponse)
def home(request: Request):
        """Renders TLOM main page."""
        context = {'request': request, 'src_languages': get_args(SRC_LANGUAGE), 'tgt_languages':get_args(TGT_LANGUAGE)}
        return templates.TemplateResponse("home.html", context)

@app.post('/translate')
def get_results(t: Translate):
    """
    Translate the text between source and target language.

    The response contains the translation and, if founded, list of examples matching input text words.
    """
    #buscar modelo
    model = tasks.find_model(t)
    #from the corresponding model file run translation function     
    translation=eval(model).translation_result(t)
    #return my_words quotes examples
    examples_dictionary = tasks.search_words(t, 'data/corpus.mir', 'data/corpus.spa')
    my_result = {'srctext': t.text, 'translation' : translation, 'examples': examples_dictionary}
    return my_result  
    

@app.post("/words")
def find_examples(t:Translate):
    """
    Find example phrases matching input text words.
    """
    examples_dictionary = tasks.search_words(t, 'data/corpus.mir', 'data/corpus.spa')
    my_result = {'examples': examples_dictionary}
    return my_result
    