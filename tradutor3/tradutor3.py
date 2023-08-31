import requests
import input

def translate(text, lang):
    url = "https://translate.yandex.net/api/v1.5/tr.json/translate"
    params = {
        'key': 'trnsl.1.1.20230831T144244Z.c6f503de2167ce05.c5e2111a7ec5b04862675a46fa39747ed509d125',
        'text': text,
        'lang': lang,
    }
    response = requests.get(url, params=params)
    return response.json()['text'][0]

def main():
    # Carregando texto de input.py
    text_to_translate = input.data['text']

    translation_en = translate(text_to_translate, 'en')
    translation_es = translate(text_to_translate, 'es')
    translation_pt = translate(text_to_translate, 'pt')


    translations = {
        "Tradução em Inglês": translation_en,
        "Tradução em Espanhol": translation_es,
        "Tradução em Português": translation_pt

    }

    # Imprimindo as traduções
    i = 0
    while i < len(translations):
        print(list(translations.items())[i])
        i += 1

if __name__ == '__main__':
    main()
