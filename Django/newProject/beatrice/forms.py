from django import forms

class Ex001Form(forms.Form):
    #assunto = forms.CharField(label='Assunto', max_length=100)
    idade = forms.IntegerField(label='Idade', required=True)
    texto = forms.CharField(label='Texto', widget=forms.Textarea)    
    #valor = forms.IntegerField(label='Valor', required=True)
    inicio = forms.IntegerField(label='Inicio', required=True)
    fim = forms.IntegerField(label='Fim', required=True)
    
