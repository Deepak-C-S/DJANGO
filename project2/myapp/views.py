from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def addition(request):
    n1=int(input("enter the number: "))
    n2=int(input("enter the number: "))
    n3=n1+n2
    n4=n1-n2
    n5=n1//n2
    n6=n1*n2
    return HttpResponse(f"Add: {n3} <br> Sub: {n4} <br> Div: {n5} <br> Mul: {n6}")

