from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer


def generate_transformer(t):
    hi_text = "जीवन एक चॉकलेट बॉक्स की तरह है।"
    chinese_text = "生活就像一盒巧克力。"

    model = M2M100ForConditionalGeneration.from_pretrained("seyoungsong/flores101_mm100_175M")
    tokenizer: M2M100Tokenizer = M2M100Tokenizer.from_pretrained("seyoungsong/flores101_mm100_175M")
    # FIX TOKENIZER!
    tokenizer.lang_token_to_id = {t: i for t, i in zip(tokenizer.all_special_tokens, tokenizer.all_special_ids) if i > 5}
    tokenizer.lang_code_to_token = {s.strip("_"): s for s in tokenizer.lang_token_to_id}
    tokenizer.lang_code_to_id = {s.strip("_"): i for s, i in tokenizer.lang_token_to_id.items()}
    tokenizer.id_to_lang_token = {i: s for s, i in tokenizer.lang_token_to_id.items()}
    # translate Chinese to English
    tokenizer.src_lang = "zh"
    encoded_zh = tokenizer(chinese_text, return_tensors="pt")
    generated_tokens = model.generate(**encoded_zh, forced_bos_token_id=tokenizer.get_lang_id("en"))
    resultado=tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    return str(resultado)
# => "Life is like a chocolate box."



def translation_result(t):
    text=t.text
    source_lang=t.source_lang
    target_lang=t.target_lang
    result = f'Traducción  del modelo Flores'
    return str(result)
