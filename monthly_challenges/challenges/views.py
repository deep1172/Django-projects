from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect,HttpResponse, response
from django.urls import reverse
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
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\'{month_path}\'> {capitalized_month} </a></li>"

    # response_data="""
    #     <ul>
    #         <li><a href= "/challenges/january">January</a></li>"
    #     </ul>
    # """
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge(request, month):
    try:
        challenge_text= monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    
    except:
        return HttpResponseNotFound("Enter correct month code")

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Input")
    
    redirect_month = months[month -1] 
    redirect_path = reverse("month-challenge", args=[redirect_month])

    return HttpResponseRedirect(redirect_path)
