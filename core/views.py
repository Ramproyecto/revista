from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request, "core/home.html")

def AboutUs(request):
    return render(request, "core/about.html")