from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def view1(request):
    a="THIS IS RESPONCE FROM FIRST APP !"
    return HttpResponse(a)