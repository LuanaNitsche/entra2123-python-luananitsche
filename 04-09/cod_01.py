import time  ##importa biblioteca time


def imprimir_caracteres(frase): ##funcao para ser chamada no outro arquivo
    for letra in frase:         ## para cada letra da frase, imprime a letra e define 1 segundo de duração de impressao
        print(letra)
        time.sleep(1)