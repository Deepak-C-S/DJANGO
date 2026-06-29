from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from myapp.models import *


def empview(request):
    emp=Employee.objects.all()
    d={'employees':emp}
    return render(request,'fake.html',d)
    