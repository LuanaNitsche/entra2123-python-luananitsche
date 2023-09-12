from django.shortcuts import render, HttpResponse
from .forms import NomeForm, NumeroForm


def var():
    a = 5
    b = 3.2
    c = 'banana'

def index(request):
    return HttpResponse("Links existentes: /m, /list, /nome, /convert")


def mensagem(request):
    return HttpResponse("Olá Luana!")


def nome(request):
    if request.method == 'POST':
        form = NomeForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            return render(request, 'nome.html', {'nome': nome})
    else:
        form = NomeForm()
    return render(request, 'template.html', {'form': form})


def converter_numero(request):
    if request.method == 'POST':
        form = NumeroForm(request.POST)
        if form.is_valid():
            numero = form.cleaned_data['numero']
            tipo_dado = type(numero).__name__
            return render(request, 'converter_numero.html', {'numero': numero, 'tipo_dado': tipo_dado})
    else:
        form = NumeroForm()
    
    return render(request, 'converter_numero.html', {'form': form})


def lista_nomes(request):
    names = ['luana', 'bia', 'rodrigo', 'fernando', 'cristina']
    tamanho = len(names)
    three = names[2]  # O terceiro elemento tem índice 2 (em Python, a indexação começa em 0)
    
    return render(request, 'lista_nomes.html', {'names': names, 'tamanho': tamanho, 'three': three})
