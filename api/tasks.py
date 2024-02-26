from models.model1 import translation_result

translations = []
#find model to use
def find_model(t):
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
        return model
    else:
        return None    


#run translation using model
def run_translation(): 
    model = find_model
    translation = model.translation_result
    #store translation in history list
    translations.append(translation.dict())
    return {'model': model, 'result': translation}


def search_words(my_list, corpusname, es_corpus):
    words_dictionary=dict()
    for index,val in enumerate(my_list):
        flag=False
        with open(corpusname, 'r') as file1, open(es_corpus, 'r') as file2:
            for line_number, (linea, linea2) in enumerate(zip(file1, file2)):
                linea = linea.rstrip()
                linea2=linea2.rstrip()
                if linea.find(my_list[index]) == -1: continue
                flag=True
                #create word/value dictionary
                if val not in words_dictionary: words_dictionary[val] = {}
                #words_dictionary[val] = {} if val not in words_dictionary else words_dictionary[val]
                words_dictionary[val].update({linea: linea2})
                #translations[t_id] = my_trans
                #print(words_dictionary)        
        if flag == False:
            print(f'{val} not found')        
    return(words_dictionary)    
            