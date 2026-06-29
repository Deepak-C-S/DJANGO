from django.shortcuts import render,redirect
from django.contrib.auth.models import *
from django.http import HttpResponse
from django.contrib.auth import *

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already exists")

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect(login)

    return render(request, 'register.html')

def loginview(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return HttpResponse("login sucessful")
        return render(request,'login.html')
    