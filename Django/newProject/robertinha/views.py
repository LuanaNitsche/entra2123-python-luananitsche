from django.shortcuts import render, HttpResponse, redirect
from .forms import ContatoForm

# Create your views here.
def index(request):
    context = {
        'minha_string' : 'Olá mundo',
        'meu_inteiro' : 123,
        'meu_booleano' : True,
        'meu_lista' : [1,2,3,4,5],
        'meu_dicionario' : {'a':1, 'b':2, 'c':3},
        'meu_objeto' : {'nome': 'Angelica', 'idade': 23},
        'meu_arquivo' : 'angelica/ex002.html',
        'meu_arquivo_html' : 'angelica/ex002.html',
        'meu_arquivo_css' : 'angelica/ex002.css',
    }
    return render(request, 'robertinha/index.html', context)

def contato(request):  
    # coletar o endereco IP do client (pessoa que acessado esta view)
    ip_address = request.META.get('REMOTE_ADDR')

    if request.method == 'POST':
        metodo = "*POST*"
        form = ContatoForm(request.POST)
        if form.is_valid():
            assunto = form.cleaned_data['assunto']
            texto = form.cleaned_data['texto']
            email = form.cleaned_data['email']
            idade = int(form.cleaned_data['idade'])
            print(assunto, texto, email, qualquer(idade))
        

    else:
        metodo = "*GET*"
        form = ContatoForm()

    context = { 
        'titulo' : 'historia do passos',
        'passo' : 'passo 1',
        'metodo' : metodo,
        'ip_address' : ip_address,
        'form' : form,
    }
    
    return render(request, 'robertinha/contato.html', context)


# def contato2(request):  
#     # coletar o endereco IP do client (pessoa que acessado esta view)
#     ip_address = request.META.get('REMOTE_ADDR')

#     if request.method == 'POST':
#         metodo = "*post*"
#     else:
#         metodo = "*get*"

#     context = { 
#         'titulo' : 'historia do passos',
#         'passo' : 'passo 1',
#         'metodo' : metodo,
#         'ip_address' : ip_address
#     }
#     return render(request, 'robertinha/contato2.html', context)