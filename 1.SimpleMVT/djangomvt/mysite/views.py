from django.http.response import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request,'home.html')
    #return HttpResponse("Привіт Команда!!")

def about(request):
    return render(request,'about.html')