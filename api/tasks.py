from models.model1 import translation_result


#find model name corresponding 
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
        raise ValueError('Model not found')    


def search_words(t, corpusname, es_corpus):
    #input quote text word list
    quote = t.text
    words_list = quote.split()
    words_dictionary=dict()
    for index,val in enumerate(words_list):
        # Initialize a flag to track if any lines were found
        flag=False
        with open(corpusname, 'r') as file1, open(es_corpus, 'r') as file2:
            for line_number, (linea, linea2) in enumerate(zip(file1, file2)):
                linea = linea.rstrip()
                linea2=linea2.rstrip()
                if linea.find(words_list[index]) == -1: continue
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
            