from django.urls import path
from .views import index,news

urlpatterns = [
    path('', index),
    path('news/', news),
    
]