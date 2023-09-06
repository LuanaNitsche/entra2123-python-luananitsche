from django.shortcuts import render, HttpResponse
from django import forms


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

class name(forms.Form):
    nome = forms.CharField(label = 'Digite seu nome: ', max_length = 100)

# views.py
from django.shortcuts import render


