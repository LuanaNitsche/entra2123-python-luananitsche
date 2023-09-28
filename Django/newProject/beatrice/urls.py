#beatrice urls.py
from django.urls import path
from beatrice.views import  ex001, index


app_name = 'beatrice'

urlpatterns = [
    path('', index, name='index_beatrice'),
    path('ex001', ex001, name='ex001_beatrice'),

]