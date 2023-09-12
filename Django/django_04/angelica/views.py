from django.shortcuts import render, HttpResponse

# Create your views here.
def helloworld(request):
    return render(request, 'angelica/hello_world.html')

def index(request):
    context = {
        'minha_string' : 'Olá mundo',
        'meu_inteiro' : 123,
        'meu_booleano' : True,
        'meu_lista' : [1,2,3,4,5],
    }
    return render(request, 'angelica/index.html', context)