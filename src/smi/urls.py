from django.urls import path
from .views import index,main,news

urlpatterns = [
    path('', main),
    path('index/', index),
    path('news/', news),
    
]