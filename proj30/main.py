from random_word import RandomWords

word = RandomWords() #variavel word recebe classe Randomword

while True:
    random = word.get_random_word() #variavel random recebe variavel word no metodo palavra aleatoria
    
    if len(random) >= 8:
        print(random)
        random = word.get_random_word()
        print(random)
        break
    else:
        print("A palavra não encontrada.")

