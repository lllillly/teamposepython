from django.shortcuts import render

def renderHome(request) :
    return render(request, "screens/home.html")
