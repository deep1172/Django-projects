from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Type first 3 letter of month name in the url and you will get that month name in the web page")
def jan(request):
    return HttpResponse("January")
def feb(request):
    return HttpResponse("february")
def mar(request):
    return HttpResponse("march")
def apr(request):
    return HttpResponse("april")
def may(request):
    return HttpResponse("may")
def jun(request):
    return HttpResponse("june")
def jul(request):
    return HttpResponse("july")
def aug(request):
    return HttpResponse("August")
def sep(request):
    return HttpResponse("September")
def oct(request):
    return HttpResponse("October")
def nov(request):
    return HttpResponse("November")
def dec(request):
    return HttpResponse("December")
