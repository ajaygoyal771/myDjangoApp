from django.http import HttpResponse
from django.shortcuts import render

def aboutUs(request):
    print(request)
    return HttpResponse("welcome to my first page using Django")


def aboutUsDetail(request, id):
    return HttpResponse("The id is " + str(id))


def homePage(request):
    return render(request, 'index.html')