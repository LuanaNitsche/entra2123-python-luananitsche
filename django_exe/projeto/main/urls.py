from django.urls import path
from .views import nome, converter_numero, lista_nomes, index, mensagem #importa do arquivo views.py da main, a def nome

urlpatterns = [    
    path('', index, name='index'),                     #lista de endereços urls
    path('m', mensagem, name='mensagem'),
    path('nome/', nome, name='nome'),   #caminho até a def main
    path('convert/', converter_numero, name='convert_num'),
    path('list/', lista_nomes, name='lista_nomes')

]
