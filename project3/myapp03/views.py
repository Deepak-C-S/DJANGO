from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def view3(request):
    a="THIS IS RESPONCE FROM THIRD APP !"
    return HttpResponse(a)