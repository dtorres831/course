from django.shortcuts import render, redirect
import random
import string

# Create your views here.
def index(request):
    # print("*"* 100)
    # count = 0;
    return render(request,"wordgenerator/index.html")

def process(request):
    if request.method == "POST":

        if 'count' in request.session:
            request.session['count']+= 1
        else:
            request.session['count'] = 1


        request.session['randomnum'] = ''.join(random.choice(string.letters[26:] + string.digits) for i in range(14))
        context = {
        'random':random
        }
        print (request.session['randomnum'])
        # print ("*"*100)
        return redirect("/")
