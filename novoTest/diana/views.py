from django.shortcuts import render

# Create your views here.


def index(request):
    abobra = {
        'text': 'hello world',
        'number': 100,
        'rua': 'rua da praia',
    }        
    return render(request, 'diana/index.html', abobra)