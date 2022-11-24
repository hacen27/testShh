from django.contrib import render
from django.http import HttpResponse

def menu (request):
    return HttpResponse("Hello MENU"),
def users (request):
    return HttpResponse("Hello MENU"),