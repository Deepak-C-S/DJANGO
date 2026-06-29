from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from myapp.models import Employee
from myapp.forms import EmployeeForm

def display(request):
    e=Employee.objects.all()
    d={'emp':e}
    return render(request,'display.html',d)

def insert_view(request):
    form = EmployeeForm()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/')
    d = {'form': form}
    return render(request, 'insert.html', d)

def update_view(request,id):
    e=Employee.objects.get(id=id)
    if request.method=="POST":
        f=EmployeeForm(request.POST,instance=e)
        if f.is_valid():
            f.save(commit=True)
            return redirect('/')
    f=EmployeeForm(instance=e)
    d={'form':f}
    return render(request,'insert.html',d)

def delete_view(request,id):
    e=Employee.objects.get(id=id)
    e.delete()
    return redirect('/')