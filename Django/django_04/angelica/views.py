from django.shortcuts import render

# Create your views here.
def helloworld(request):
    return render(request, 'angelica/hello_world.html')

def ex002(request):
    context = {
        'minha_string' : 'Olá mundo',
        'meu_inteiro' : 123,
        'meu_booleano' : True,
        'meu_lista' : [1,2,3,4,5],
        'meu_dicionario' : {'a':1, 'b':2, 'c':3},
        'meu_objeto' : {'nome': 'Angelica', 'idade': 23},
        'meu_arquivo' : 'angelica/ex002.html',
        'meu_arquivo_html' : 'angelica/ex002.html',
        'meu_arquivo_css' : 'angelica/ex002.css',
    }
    return render(request, 'angelica/ex002.html', context)