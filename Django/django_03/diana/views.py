from django.shortcuts import render, HttpResponse

# Create your views here.

def helloworld(request):
    return HttpResponse('Hello world')




# def index(request):
#     abobra = {
#         'text': 'hello world',
#         'number': 100,
#         'rua': 'rua da praia',
#     }        
#     return render(request, '/diana/index.html', abobra)