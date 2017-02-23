from django.shortcuts import render, redirect
from .models import Class, User_Class
from ..loginandreg.models import User
from django.db.models import Count
# Create your views here.
def index(request):
    context = {
        'classes': Class.objects.all()
    }
    # print context
    return render(request, "course/index.html", context)

def blogs(request):
    # print "*"*100
    Class.objects.create(title=request.POST['title'], description=request.POST['description'])
    return redirect('/course/')

def delete(request, id):
    DClass = Class.objects.filter(id=id)
    # print ('QUERY RESULT:', title)

    context = {
        "dclasses": DClass
    }
    # print context
    return render(request, "course/delete.html", context)

def deletecourse(request, id):
    print id
    Class.objects.filter(id=id).delete()
    return redirect('/course/')

def usercourse(request):
    # print User.objects.all()
    # print Class.objects.all()
    # # User_Class.objects.create(title=request.POST['title'],user=request.POST['User'])
    # print User_Class.objects.all()
    if request.method == "POST":
        print request.POST
        selected_user= User.objects.get(id=request.POST['user'])
        selected_course= Class.objects.get(id=request.POST['title'])
        selected_course.users.add(selected_user)
        selected_course.save()
    context ={
        "users" : User.objects.all(),
        "titles": Class.objects.annotate(num=Count("users")),
        # "counts": Class.objects.annotate(num=Count("users"))
        }
    return render(request,"course/course.html",context)
