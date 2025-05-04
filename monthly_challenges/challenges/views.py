from django.shortcuts import render
<<<<<<< main
from django.http import HttpResponse
=======
from django.http import HttpResponseNotFound, HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.template.loader import render_to_string
>>>>>>> local
# Create your views here.
def index(request):
<<<<<<< main
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
=======
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
        # response_data = f"<h1>{challenge_text}</h1>"
        # response_data = render_to_string("challenges/challenge.html")
        return render(request, "challenges/challenge.html")
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
>>>>>>> local
