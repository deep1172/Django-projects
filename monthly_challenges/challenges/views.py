from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def index(request):
    # return HttpResponse(f"""<h1>Click on the month you will be redirected to that month</h1> 
    #                     <ul>
    #                     <li><a href="jan">January</a></li>
    #                     <li><a href="feb">February</a></li>
    #                     <li><a href="mar">March</a></li>
    #                     <li><a href="apr">April</a></li>
    #                     <li><a href="may">May</a></li>
    #                     <li><a href="jun">June</a></li>
    #                     <li><a href="jul">july</a></li>
    #                     <li><a href="aug">August</a></li>
    #                     <li><a href="sep">September</a></li>
    #                     <li><a href="oct">October</a></li>
                      
    #                     <li><a href="nov">November</a></li>
                      
    #                     <li><a href="dec">December</a></li>
                      
    #                     </ul>
    #                      """)




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
