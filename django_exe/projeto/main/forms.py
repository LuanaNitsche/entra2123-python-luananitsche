from django import forms

class NomeForm(forms.Form):
    nome = forms.CharField(label='Digite seu nome', max_length=100)
