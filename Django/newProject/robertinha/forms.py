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


class QuestionForm(forms.Form):
    def __init__(self, questions, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        
        for key, question in questions.items():
            self.fields[key] = forms.ChoiceField(
                label=question['Q'],
                choices=[
                    ('A', question['A']),
                    ('B', question['B']),
                    ('C', question['C']),
                    ('D', question['D']),
                ],
                widget=forms.RadioSelect(attrs={'class': 'radio-inline'}),
                required=False
            )

# class QuestionForm(forms.Form):
#     respostas = forms.CharField(disabled=False, label='Resposta', required=True, widget=forms.TextInput)
    
class Ex007Form(forms.Form):
    id_produto = forms.CharField(widget=forms.HiddenInput(), required=False)
    nome_produto = forms.CharField()
    qnt_produto = forms.CharField()


