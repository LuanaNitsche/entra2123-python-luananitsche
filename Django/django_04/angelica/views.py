from django.shortcuts import render, HttpResponse

# Create your views here.
def helloworld(request):
    return HttpResponse('Hello world, my brain is melting')