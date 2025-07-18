from django.http import HttpResponse
from django.shortcuts import render # type: ignore
import json

def aboutUs(request):
    print(request)
    return HttpResponse("welcome to my first page using Django")


def aboutUsDetail(request, id):
    return HttpResponse("The id is " + str(id))


def homePage(request):
    data = {
        'title': 'My Home page through variable.',
        'string': 'Welcome to myDjangoApp through Variable....!',
        'mmlist': ['Ajay', 'Shubham', 'Poonam', 'Ashok'],
        'details': {
            'Name': 'Ajay',
            'PhoneNumebr': '9958075990'
        },
    }
    return render(request, 'index.html',data)

def userForm(request):
    try:
        print(request)
        n1 = request.GET['val1']
        n2 = request.GET['val2']
        n3 = request.GET['val3']
        print(n1+n2+n3)
    except Exception as e:
        print(e)
        pass
    return render(request, 'userForm.html')