from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect,HttpResponse
from django.urls import reverse
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




# def monthly_challenge(request, month):
#     challenge_text = None

#     if month == "jan":
#         challenge_text = "This month is January "
    # elif month == "feb":
    #     challenge_text = "This month is february "
    # elif month == "mar":
    #     challenge_text = "This month is march "
    # elif month == "apr":
    #     challenge_text = "This month is April "
    # elif month == "may":
    #     challenge_text = "This month is May "
    # elif month == "jun":
    #     challenge_text = "This month is June "
    # elif month == "jul":
    #     challenge_text = "This month is July "
    # elif month == "aug":
    #     challenge_text = "This month is August "
    # elif month == "sep":
    #     challenge_text = "This month is September "
    # elif month == "oct":
    #     challenge_text = "This month is October "
    # elif month == "nov":
    #     challenge_text = "This month is November "
    # elif month == "dec":
    #     challenge_text = "This month is December "
    # else:
    #     return HttpResponseNotFound("Incorrect request")
    # return HttpResponse(challenge_text)

monthly_challenges = {
    "jan": "Welcome to the month of January",
    "feb": "Welcome to the month of february",
    "mar": "Welcome to the month of march",
    "apr": "Welcome to the month of apr",
    "may": "Welcome to the month of may",
    "jun": "Welcome to the month of june",
    "jul": "Welcome to the month of july",
    "aug": "Welcome to the month of August",
    "sep": "Welcome to the month of September",
    "oct": "Welcome to the month of october",
    "nov": "Welcome to the month of November",
    "dec": "Welcome to the month of December",
}

def monthly_challenge(request, month):
    try:
        challenge_text= monthly_challenges[month]

        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("Enter correct month code")

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Input")
    
    redirect_month = months[month -1] 
    redirect_path = reverse("month-challenge", args=[redirect_month])

    return HttpResponseRedirect(redirect_path)
