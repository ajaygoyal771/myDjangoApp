from django.http import HttpResponse
from django.shortcuts import render # type: ignore

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
