import cod_01 as i                             ##importa o arquivo ipo como 'i' para praticidade

def main():
    frase = input("Digite uma frase: ")
    i.imprimir_caracteres(frase)            ##chama a funcao do arquivo ipo.py com o 'i'

if __name__ == "__main__":                  ##roda a main
    main()
