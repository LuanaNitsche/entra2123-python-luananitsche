# condicionais if-else

idade = int(input("Digite sua idade: "))
if idade >= 18:
    if idade <= 100:
        print("Você é maior de idade.")
    else:
        print("Idade inválida.")
elif idade >= 0: 
    print("Você é menor de idade.")
else:
    print("Idade inválida.")


x = 21
if idade >= 10:
    if idade <= 20:
        print("Menor que 20")
    else:
        print("Maior que 20")
else:
    print("Menor que 10")

print('Fim')