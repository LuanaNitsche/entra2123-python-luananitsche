import historia1 as h


def main():
    print("Gerador de Senhas Aleatórias")

    comprimento = int(input("Comprimento da senha desejada: "))

    incluir_minusculas = input("Incluir letras minúsculas? (s/n): ").lower() == 's'
    incluir_maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
    incluir_numeros = input("Incluir números? (s/n): ").lower() == 's'
    incluir_especiais = input("Incluir caracteres especiais? (s/n): ").lower() == 's'

    senha = h.gerar_senha(comprimento, incluir_minusculas, incluir_maiusculas, incluir_numeros, incluir_especiais)

    print(f'Sua senha gerada é: {senha}')

if __name__ == "__main__":
    main()