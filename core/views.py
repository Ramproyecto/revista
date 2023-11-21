from django.shortcuts import render

# Create your views here.

def Home(request):
    context = {
        'ruta_actual': request.path,
    }
    return render(request, "core/home.html", context)

def AboutUs(request):
    context = {
        'ruta_actual': request.path,
    }
    return render(request, "core/about.html", context)

def Frequent(request):
    context = {
        'ruta_actual': request.path,
    }
    return render(request, "core/FAQ.html", context)

def Magazine(request):
    context = {
        'ruta_actual': request.path,
    }
    return render(request, "core/revista.html", context)