from django.urls import path
from .views import nome

urlpatterns = [
    path('nome/', nome, name='nome'),
]
