from django.contrib import admin
from django.urls import path
from .views import index, contato, contato2

urlpatterns = [
    path('', index, name= 'index.html'),
    path('contato/', contato, name= 'contato'),
    path('c', contato2, name= 'c2')
    
]