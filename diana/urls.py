from django.contrib import admin
from django.urls import path, include
from diana.views import index


urlpatterns = [
    path('index/', index, name = 'index')
]
