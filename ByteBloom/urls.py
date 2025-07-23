from django.urls import path #importing url to home page view
from .views import * #for extracting func/classes from current app

urlpatterns = [
    path('',home , name='home'), 
    path('index/', index, name='index'),# API - POSTMAN # maps root https://127.0.0.1/8000 to home view and name is altered here as home
  ]	