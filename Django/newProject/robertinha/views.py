from django.shortcuts import render, HttpResponse, redirect
from .forms import ContatoForm, Ex003Form


def ex002(request):
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
    return render(request, 'robertinha/ex002.html', context)


def qualquer(valor):
    return valor.upper()


def index(request):
    #return HttpResponse("hello world")
    return render(request, 'robertinha/index.html')

def ex002(request):
    context = {
        'minha_string': 'Olá, Mundo!',
        'meu_inteiro': 123,
        'meu_booleano': True
    }
    return render(request, 'robertinha/ex002.html', context)

def contato(request):  
    # coletar o endereco IP do client (pessoa que acessado esta view)
    ip_address = request.META.get('REMOTE_ADDR')

    if request.method == 'POST':
        metodo = "*POST*"
        form = ContatoForm(request.POST)
        if form.is_valid():
            assunto = form.cleaned_data['assunto']
            assunto = qualquer(assunto) #add 
            texto = form.cleaned_data['texto']
            email = form.cleaned_data['email']
            idade = int(form.cleaned_data['idade'])
            print(assunto, texto, email, idade) #retiramos qualquer(idade)
        

    else:
        metodo = "*GET*"
        initial_data = {                    #Lista que define e coloca dentro das caixas de texto,  
            'assunto': 'Tópico Padrão',         #uma mensagem inicial
            'texto': 'Texto Padrão',
            'email': 'email@exemplo.com',
            'idade': 30,
            
        }
        form = ContatoForm(initial=initial_data) 

    context = { 
        'titulo' : 'historia do passos',
        'passo' : 'passo 1',
        'metodo' : metodo,
        'ip_address' : ip_address,
        'form' : form,
        'resposta' : assunto
    }
    
    return render(request, 'robertinha/contato.html', context)


def index(request):    
    return render(request, 'robertinha/index.html')


def ex003(request):
    ip_adress = request.META.get('REMOTE_ADDR')
    msg = ""

    if request.method == 'POST':
        form = Ex003Form(request.POST, initial={'pergunta': 'Qual é a capital da França?'})
        if form.is_valid():
            resposta = form.cleaned_data['resposta']
            if resposta == 'A': 
                msg = "Parabéns, você acertou!"
            else:
                msg = "Ops, tente novamente."
    else:
        form = Ex003Form(initial={'pergunta': 'Qual é a capital da França?'})
        msg = ""

    context = { 
        'form' : form,
        'msg' : msg,
        
    }


    return render(request, 'robertinha/ex003.html', context)

# def contato2(request):  
#     # coletar o endereco IP do client (pessoa que acessado esta view)
#     ip_address = request.META.get('REMOTE_ADDR')

#     if request.method == 'POST':
#         metodo = "*post*"
#     else:
#         metodo = "*get*"
#         initial_data = {                    #Lista que define e coloca dentro das caixas de texto,  
#             'assunto': 'Tópico Padrão',         #uma mensagem inicial
#             'texto': 'Texto Padrão',
#             'email': 'email@exemplo.com',
#             'idade': 30,
#         }
#         form = ContatoForm(initial=initial_data) 

#     context = { 
#         'titulo' : 'historia do passos',
#         'passo' : 'passo 1',
#         'metodo' : metodo,
#         'ip_address' : ip_address
#     }
#     return render(request, 'robertinha/contato2.html', context)