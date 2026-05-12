from django.shortcuts import render
from .forms import *
# Create your views here.

def feedback(request):
    f=Feedback()
    if request.method=="POST":
        f=Feedback(request.POST)
        if f.is_valid():
            name=f.cleaned_data['name']
            rollno=f.cleaned_data['rollno']
            email=f.cleaned_data['email']
            feedback=f.cleaned_data['feedback']
            d={'name':name,'rollno':rollno,'email':email,'feedback':feedback}
            return render(request,'output.html',d)
    d={'Feedback':f}
    return render(request,'forms.html',d)
    