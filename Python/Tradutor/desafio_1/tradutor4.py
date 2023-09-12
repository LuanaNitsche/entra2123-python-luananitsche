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
    
    if response.status_code == 200: ##se deu certo a conexão (perfeito)
        translation = response.json().get('text', [''])[0]
        return translation
    else:
        print(f"Erro na tradução para o idioma {lang}")
        return ""

def main():
    try:
        text_to_translate = input.data.get('text', '')
        target_languages = input.data.get('langs', [])

        translations = {}
        for lang in target_languages:
            translation = translate(text_to_translate, lang)
            if translation:
                translations[f"Tradução em {lang}"] = translation

        i = 0
        while i < len(translations):
            print(list(translations.items())[i])
            i += 1
    except Exception as e:
        print(f"Erro: {str(e)}")

if __name__ == '__main__':
    main()
