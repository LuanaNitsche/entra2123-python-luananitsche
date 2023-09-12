import sys
import historia3 as h

def main():
    if len(sys.argv) != 2:
        print("Uso: python3 gerador_de_senhas.py <comprimento>")
        return

    comprimento = int(sys.argv[1])

    print("Gerador de Senhas Aleatórias")

    incluir_minusculas = input("Incluir letras minúsculas? (s/n): ").lower() == 's'
    incluir_maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
    incluir_numeros = input("Incluir números? (s/n): ").lower() == 's'
    incluir_especiais = input("Incluir caracteres especiais? (s/n): ").lower() == 's'

    senha = h.gerar_senha(comprimento, incluir_minusculas, incluir_maiusculas, incluir_numeros, incluir_especiais)

    print(f'Sua senha gerada é: {senha}')

if __name__ == "__main__":
    main()
