import csv
import requests
import texto

def translate(text, lang):
    url = "https://translate.yandex.net/api/v1.5/tr.json/translate"
    params = {
        'key': 'trnsl.1.1.20230831T144244Z.c6f503de2167ce05.c5e2111a7ec5b04862675a46fa39747ed509d125',
        'text': text,
        'lang': lang,
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        translation = response.json().get('text', [''])[0]
        return translation
    else:
        print(f"Erro na tradução para o idioma {lang}")
        return ""                                                       

def main():
    input_files = ['input_en.txt', 'input_es.txt', 'input_fr.txt']      
    languages = ['en', 'es', 'fr']                                     

    translations = []                                                   

    for i, input_file in enumerate(input_files):  # Corrigido para input_file                      
        with open(input_file, 'r', encoding='utf-8') as file:           
            original_text = file.read()                                 
            for j, lang in enumerate(languages):                        
                if i != j:                                              
                    translated_text = translate(original_text, lang)
                    translations.append([original_text, translated_text, lang])         

    with open('translations.csv', 'w', newline='', encoding='utf-8') as csv_file:       
        csv_writer = csv.writer(csv_file)                                               
        csv_writer.writerow(['original_text', 'translated_text', 'lang'])               
        csv_writer.writerows(translations)                                              

if __name__ == '__main__':
    main()