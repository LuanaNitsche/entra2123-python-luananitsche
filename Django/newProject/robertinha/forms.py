from django import forms

class ContatoForm(forms.Form):
    assunto = forms.CharField(label='Assunto', max_length=100)
    texto = forms.CharField(label='Texto', widget=forms.Textarea)
    email = forms.EmailField(label='E-mail', required=False)
    idade = forms.IntegerField(label='Idade', required=True)
    salario = forms.DecimalField(label='Salario', required=False)    
    enviar = forms.BooleanField(label='Enviar', required=False)


class Ex003Form(forms.Form):
    PERGUNTA_CHOICES = [
        ('A', 'Paris'), 
        ('B', 'Brasília'),
        ('C', 'Estocolmo'),
        ('D', 'Nova York')
    ]

    pergunta = forms.CharField(disabled=True, label="Pergunta", required=False)
    resposta = forms.ChoiceField(choices=PERGUNTA_CHOICES, label= "Resposta", required=False)
