from django.shortcuts import render
from beatrice.forms import Ex001Form
import ast


# def qualquera (texto, valor):
#     resultado = texto * valor
#     return resultado

# def qualquerb(texto):
#     lista = ast.literal_eval(texto)
#     print("LISTA")
#     print(lista)
#     return lista[2]

# def qualquer(texto):
#     lista = ast.literal_eval(texto)
#     print("LISTA")
#     ultimo = lista[-2:]
#     return ultimo

def qualquer(texto, inicio, fim):
    lista = ast.literal_eval(texto)
    print("LISTA")
    return lista[inicio:fim]

def index(request):
    return render(request, 'beatrice/index.html')

def ex001(request):
    print("passou aqui 001")
    # coletar o endereco IP do client (pessoa que acessado esta view)
    ip_address = request.META.get('REMOTE_ADDR')
    resultado = '<br>vazio<br>'
    metodo = ""

    if request.method == 'POST':
        print("passou aqui 002")
        metodo = "*POST*"
        form = Ex001Form(request.POST)
        if form.is_valid():   
            print("passou aqui 003")         
            texto = form.cleaned_data['texto']            
            #valor = int(form.cleaned_data['valor'])
            inicio = int(form.cleaned_data['inicio'])
            fim = int(form.cleaned_data['fim'])
            resultado = qualquer(texto, inicio, fim)    
    else:
        print("passou aqui 004")
        metodo = "*GET*"
        form = Ex001Form()



    print("passou aqui 005")
    context = { 
        'titulo' : 'Ex 001',
        'descricao' : 'Digite uma Frase no texto abaixo e digite um nÚMERO no valor abaixo e clique em Enviar',
        'resultado' : resultado,
        'metodo' : metodo,
        'ip_address' : ip_address,
        'form' : form,
        
    }
    print("passou aqui 006")
    return render(request, 'beatrice/ex001.html', context)

