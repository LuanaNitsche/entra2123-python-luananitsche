#beatrice urls.py
from django.urls import path
from beatrice.views import index


app_name = 'beatrice'

urlpatterns = [
    path('', index, name='index_beatrice'),
]