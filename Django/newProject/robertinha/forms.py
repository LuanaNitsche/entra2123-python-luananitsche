from django import forms

class ContatoForm(forms.Form):
    assunto = forms.CharField(label='Assuntoxxx', max_length=100)
    texto = forms.CharField(label='Texto', widget=forms.Textarea)
    email = forms.EmailField(label='E-mail', required=False)
    idade = forms.IntegerField(label='Idadexxx', required=True)
    salario = forms.DecimalField(label='Salarioxxx', required=False)    
    enviar = forms.BooleanField(label='Enviarxx', required=False)