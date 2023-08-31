import requests
import input  # Importa o arquivo input.py que contém o dicionário data

def translate(text, lang):
    url = "https://translate.yandex.net/api/v1.5/tr.json/translate"
    params = {
        'key': 'sua_chave_aqui',
        'text': text,
        'lang': lang,
    }
    response = requests.get(url, params=params)
    return response.json()['text'][0]

def main():
    text_to_translate = input.data['text']
    target_languages = input.data['langs']

    translations = {}
    for lang in target_languages:
        translation = translate(text_to_translate, lang)
        translations[lang] = translation

    print("Traduções:")
    for lang, translation in translations.items():
        print(f"{lang}: {translation}")

if __name__ == '__main__':
    main()
