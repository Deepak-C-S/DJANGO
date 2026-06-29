from django.http import HttpResponse
from django.shortcuts import render
from myapp.forms import *
from myapp.models import *
# Create your views here.

def formview(request):
    f=StudentForm()
    if request.method=='POST':
        f=StudentForm(request.POST)
        if f.is_valid():
            f.save()
            return HttpResponse('Data added successfully')
    d={'form':f}
    return render(request,'form.html',d)