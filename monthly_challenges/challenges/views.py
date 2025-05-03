from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Type first 3 letter of month name in the url and you will get that month name in the web page")
# def jan(request):
#     return HttpResponse("January")
# def feb(request):
#     return HttpResponse("february")
# def mar(request):
#     return HttpResponse("march")
# def apr(request):
#     return HttpResponse("april")
# def may(request):
#     return HttpResponse("may")
# def jun(request):
#     return HttpResponse("june")
# def jul(request):
#     return HttpResponse("july")
# def aug(request):
#     return HttpResponse("August")
# def sep(request):
#     return HttpResponse("September")
# def oct(request):
#     return HttpResponse("October")
# def nov(request):
#     return HttpResponse("November")
# def dec(request):
#     return HttpResponse("December")

def monthly_challenge(request, month):
    challenge_text = None

    if month == "jan":
        challenge_text = "This month is January "
    elif month == "feb":
        challenge_text = "This month is february "
    elif month == "mar":
        challenge_text = "This month is march "
    elif month == "apr":
        challenge_text = "This month is April "
    elif month == "may":
        challenge_text = "This month is May "
    elif month == "jun":
        challenge_text = "This month is June "
    elif month == "jul":
        challenge_text = "This month is July "
    elif month == "aug":
        challenge_text = "This month is August "
    elif month == "sep":
        challenge_text = "This month is September "
    elif month == "oct":
        challenge_text = "This month is October "
    elif month == "nov":
        challenge_text = "This month is November "
    elif month == "dec":
        challenge_text = "This month is December "
    else:
        return HttpResponseNotFound("Incorrect request")
    return HttpResponse(challenge_text)

def monthly_challenge_by_number(request, month):
    return HttpResponse(month)
