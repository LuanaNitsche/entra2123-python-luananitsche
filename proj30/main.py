from random_word import RandomWords

word = RandomWords()

while True:
    random = word.get_random_word()
    
    if len(random) >= 8:
        print(random)
        break
    else:
        print("A palavra não encontrada.")

