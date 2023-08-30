from random_word import RandomWords
from translate import Translator

word = RandomWords()
translator = Translator(to_lang="pt")

while True:
    random_word = word.get_random_word()
    
    if len(random_word) >= 8:
        traduzida = translator.translate(random_word)
        print("Palavra original em inglês:", random_word)
        print("Palavra traduzida para o português:", traduzida)
        break
    else:
        print("A palavra não atende aos requisitos de comprimento.")