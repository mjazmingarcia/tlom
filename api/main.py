from pydantic import BaseModel, validator
from fastapi import FastAPI
#import model files for do_translation
from models import model1, model2
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
#history list
translations = []
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

#renders main page 
@app.get('/',  response_class=HTMLResponse)
def home(request: Request):
        """Renders main page"""
        context = {'request': request, 'src_languages': languages_in, 'trg_languages':languages_out}
        return templates.TemplateResponse("home.html", context)

@app.post('/translate')  
def do_translation(t: Translate):
    #store translation request in translation list
    translations.append(t)
    #index/ of the added translation req
    t_id = len(translations)-1
    #for find model
    src_lang = t.source_lang
    models = {
        "wixarika": "model1",
        "náhuatl": "model2",
        "yorem nokki": "model3",
        "purépecha": "model4",
        "mexicanero": "model5"
    }
    
    if src_lang in models:
        model = models[src_lang]       
    
    #from the corresponding model file run translation function     
    translation=eval(model).translation_result(t)
    #add translation result to translations list
    my_trans=translations[t_id].dict()
    #my_trans['translation'] = translation
    my_trans.update({"translation": translation})
    translations[t_id] = my_trans
    return {'translation_id':t_id}  
    

@app.get("/words")
def find_quote(t_id:int):
    #get quote to split
    quote = translations[t_id]['text']
    #lista de palabras de la quote
    #quote = 'piity tuunëëk kyukoxëëy poop'
    my_words = quote.split()
    print(my_words)
       
    with open('data/corpus.mir', 'r') as wixcrp:
        for word in my_words:
            flag = False
            for linea in wixcrp:
                linea = linea.rstrip()
                if linea.find(word) == -1: continue
                flag = True
                print(linea)
                    ##just print the first result:
                    ##break
                ##else: print('No se encontró ningún ejemplo de uso')
            if flag==False:
                print('No matched')
            
    
    return 'hey'

@app.get("/history")
def get_history():
    return translations


@app.get("/results")
def get_results():
    return {"translation": 'traducción por añadir'}