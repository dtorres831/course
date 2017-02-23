from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render (request, 'loginandreg/index.html')

def register (request):
    response = User.objects.register(request.POST)

    if not response['Status']:
        for error in response['errors']:
            messages.error(request, error)
            print response['errors']
            # print messages
        return redirect ('/')
    else:
        context ={
            "name": request.POST['first_name']
        }
        return render(request, "loginandreg/success.html", context)
        # return redirect("timedisplay:index")

def login(request):
    response = User.objects.login(request.POST)
    if not response['Status']:
        messages.error(request, response['errors'])
        return redirect('/')
    else:
        # username =User.objects.get(email=request.POST['email'])
        # print username.first_name
        context ={
            "name": response["user"].first_name
        }
        return render(request, "loginandreg/success.html", context)
        # return redirect("timedisplay:index")
