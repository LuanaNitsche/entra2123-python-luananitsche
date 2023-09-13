from django import forms


class ContatoForm(forms.Form):
    assunto = forms.CharField(label='Assunto', max_length=100)
    texto = forms.CharField(label='Texto', widget=forms.Textarea)