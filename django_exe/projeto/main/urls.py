from django.urls import path
from .views import nome, converter_numero, lista_nomes #importa do arquivo views.py da main, a def nome

urlpatterns = [                         #lista de endereços urls
    path('nome/', nome, name='nome'),   #caminho até a def main
    path('convert/', converter_numero, name='convert_num'),
    path('list/', lista_nomes, name='lista_nomes')

]
