from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def view2(request):
    a="<center><h1 style='color:blue; font-family:times new roman, bold' >THIS IS RESPONCE FROM SECOND APP !</h1></center>"
    return HttpResponse(a)
