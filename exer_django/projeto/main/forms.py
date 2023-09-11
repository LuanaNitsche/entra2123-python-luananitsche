from django import forms
from django.shortcuts import render

class NomeForm(forms.Form):
    nome = forms.CharField(label='Digite seu nome', max_length=100) 

    ''' Classe CharField possui vários parâmetros, sendo label um deles.
        Label recebe o texto desejado 
        max_length define o tamanho máximo para nome'''
    

class NumeroForm(forms.Form):
    numero = forms.FloatField(label='Digite um número')


# def lista_nomes(request):
#     names = ['luana', 'bia', 'rodrigo', 'fernando', 'cristina']
#     tamanho = len(names)
#     three = names[2]  # O terceiro elemento tem índice 2 (em Python, a indexação começa em 0)
    
#     return render(request, 'lista_nomes.html', {'names': names, 'tamanho': tamanho, 'three': three})