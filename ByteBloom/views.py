from django.shortcuts import render #used for html templates render simply meant it is used to return the reponse like the html page how many members are currently viewing that view response
from django.http import HttpResponse  #from http you might get response(raw text)
# Create your views here.
def home(request): #defined function home which receive parameter from http request
    return HttpResponse("Welcome to the ByteBloom Home Page") 