from django.shortcuts import render, HttpResponse
from django import forms
from .forms import NomeForm


def var():
    a = 5
    b = 3.2
    c = 'banana'

#comments
''' comentario
    on
    me'''

def mensagem(request):
    return HttpResponse("OLá mundo!")


def nome(request):
    if request.method == 'POST':
        form = NomeForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            return render(request, 'nome.html', {'nome': nome})
    else:
        form = NomeForm()
    return render(request, 'template.html', {'form': form})


