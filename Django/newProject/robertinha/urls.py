from django.contrib import admin
from django.urls import path
from .views import contato, ex002, index, ex003, ex004, ex005, mercado

app_name = 'robertinha'


urlpatterns = [
    path('ex002', ex002, name= 'ex002'),
    path('contato/', contato, name= 'contato'),
    path('', index, name= 'index'),
    path('pergunta', ex003, name= 'pergunta'),
    path('quest', ex004, name= 'questions'),
    path('ex005', ex005, name='ex005'),
    path('ex006', mercado, name='ex006'),
    
]