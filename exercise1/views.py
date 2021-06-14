from django.http.response import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'exercise1/home.html',{'nombre':'Daniel Alcocer'})

def other(request):
    return HttpResponse('<h1>This is the other page</h1>')