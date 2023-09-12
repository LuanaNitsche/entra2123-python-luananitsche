import requests                                                           ##importa a biblioteca 


def translate(text, lang):                                                ##funcao translate
    url = "https://translate.yandex.net/api/v1.5/tr.json/translate"       ##link yandex
    params = {                                                            ##parametros de cahve, texto e lingua 
        'key': 'trnsl.1.1.20230831T144244Z.c6f503de2167ce05.c5e2111a7ec5b04862675a46fa39747ed509d125',
        'text': text,
        'lang': lang,
    }
    response = requests.get(url, params=params) ##variavel recebe modulo requests com funcao get que recebe parametro params com var params
    return response.json()['text'][0]                                     ##retorna var response com metodo .json

def main():                                                                ##funcao main
    text_to_translate = input("Digite o texto que deseja traduzir: ")      ##texto para ser traduzido
    translation_en = translate(text_to_translate, 'en')                    ##variavel que traduz e armazena texto traduzido em english / spanish / portuguese
    translation_es = translate(text_to_translate, 'es')
    translation_pt = translate(text_to_translate, 'pt')

    print("Tradução em Ingles:", translation_en)                           ##imprime a variavel 
    print("Tradução em Espanhol:", translation_es)
    print("Tradução em Português: ", translation_pt)

if __name__ == '__main__':                                                 ##
    main()