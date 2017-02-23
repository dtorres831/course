from django.shortcuts import render, HttpResponse
import datetime
# Create your views here.
def index(request):
    time = datetime.datetime.now()
    print datetime
    context = {
    'time': time
    }
    return render(request, 'timedisplay/index.html',context)
