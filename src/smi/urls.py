from django.urls import path
from .views import index,main

urlpatterns = [
    path('', main),
    path('index/', index),
    
]