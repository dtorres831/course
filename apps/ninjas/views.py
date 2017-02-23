from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "ninjas/index.html")

def ninjas(request):
    return render(request, "ninjas/ninjas.html")

def soloninjas(request, color):
    context = {
    "color": color
    }
    return render(request, "ninjas/solo.html", context)
