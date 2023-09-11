from django.contrib import admin
from django.urls import path, include
from diana.views import helloworld


urlpatterns = [
    path('hello/', helloworld, name= 'helloworld')
    
    #path('index/', index, name = 'index')
]
