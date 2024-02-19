
def translation_result(t):
    text=t.text
    source_lang=t.source_lang
    target_lang=t.target_lang
    result = f'Traducción del {source_lang} al {target_lang} del texto: {text}'
    return {'translation': result}
