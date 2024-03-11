from pydantic import BaseModel, validator
from fastapi import FastAPI, HTTPException
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
from api.const2 import SRC_LANGUAGE2, TGT_LANGUAGE2
from typing import get_args, Union

app = FastAPI(
    title="TLOM API",
    description= DESCRIPTION,
    version="0.0.1",
)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="./templates")

##data requirements schema
#for hf flores
class TranslateFlores(BaseModel):
    text: str = Field(max_length=30, description='El texto no debe tener más de 30 caracteres')
    source_lang: SRC_LANGUAGE2 
    target_lang: TGT_LANGUAGE2
    
#for tlom models
class Translate(BaseModel):
    text: str = Field(max_length=30, description='El texto no debe tener más de 30 caracteres')
    source_lang: SRC_LANGUAGE 
    target_lang: TGT_LANGUAGE
    
#renders main page 
@app.get('/',  response_class=HTMLResponse)
def home(request: Request):
        """Renders TLOM main page."""
        context = {'request': request, 'src_languages': get_args(SRC_LANGUAGE2), 'tgt_languages':get_args(TGT_LANGUAGE2)}
        return templates.TemplateResponse("home.html", context)

@app.post('/translate')
def get_results(t: Union[TranslateFlores, Translate]):
    """
        Translate the text between source and target language.
        
        Depending on the schema, returns certain result. 
        
        The response contains the translation and, if founded, list of examples matching input text words.
        """
    if isinstance(t, Translate):    
        #buscar modelo
        model = tasks.find_model(t)
        #from the corresponding model file run translation function     
        translation=eval(model).translation_result(t)
        #return my_words quotes examples
        examples_dictionary = tasks.search_words(t, 'data/corpus.mir', 'data/corpus.spa')
        my_result = {'srctext': t.text, 'translation' : translation, 'examples': examples_dictionary}
        #return my_result  
    
    elif isinstance(t, TranslateFlores):
        #model2.init_transformer
        flores_translation= model2.generate_transformer(t)
        my_result = {'translation': flores_translation}
    
    else:
        raise HTTPException(status_code=400, detail="Invalid schema type") 
        
    return my_result

@app.post("/words")
def find_examples(t:Translate):
    """
    Find example phrases matching input text words.
    """
    examples_dictionary = tasks.search_words(t, 'data/corpus.mir', 'data/corpus.spa')
    my_result = {'examples': examples_dictionary}
    return my_result
    