from django.contrib import admin
from django.urls import path
from .views import view_pessoa

app_name = 'teste'

urlpatterns = [  
    path('', view_pessoa, name= 'pessoa'),
]