from django.contrib import admin
from django.urls import path, include
from .views import helloworld

urlpatterns = [  
    path('', helloworld, name= 'helloworld'),
]