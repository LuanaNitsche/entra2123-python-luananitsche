from django.shortcuts import render
from beatrice.forms import Ex001Form

# Create your views here.
def qualquer (texto, valor):
    resultado = texto * valor
    return resultado


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
            valor = int(form.cleaned_data['valor'])
            print(texto, valor)
            resultado = qualquer(texto, valor)    
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