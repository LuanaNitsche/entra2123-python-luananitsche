from django.contrib import admin
from django.urls import path
from .views import helloworld, ex002


urlpatterns = [  
    path('', helloworld, name= 'helloworld'),
    path('i', ex002, name= 'index'),
]