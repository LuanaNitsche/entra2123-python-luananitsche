from django.contrib import admin
from django.urls import path, include
from .views import helloworld, index



urlpatterns = [  
    path('', helloworld, name= 'helloworld'),
    path('i', index, name= 'index'),
]