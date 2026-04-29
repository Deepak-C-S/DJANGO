from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def view1(request):
    s="Welcome to Django class"
    return HttpResponse(s)

def view2(request):
    k="Hey I'm Deepak C S"
    return HttpResponse(k)
    
