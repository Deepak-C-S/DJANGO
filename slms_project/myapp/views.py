from django.shortcuts import render
from django.contrib.auth.models import *
from account.models import Profile
# Create your views here.

def register(request):
    if request.method=="POST":
        username=request.POST['username']
        