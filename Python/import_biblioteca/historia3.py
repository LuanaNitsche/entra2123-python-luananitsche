import random
import string

def gerar_senha(comprimento, incluir_minusculas=True, incluir_maiusculas=True, incluir_numeros=True, incluir_especiais=True):
    caracteres = ""
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_especiais:
        caracteres += string.punctuation

    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha
