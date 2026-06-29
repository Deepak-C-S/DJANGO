import json
from django.shortcuts import render
from .models import Product 
from django.views import View
from django.http import HttpResponse
from django.core.serializers import *
# Create your views here.

class ProductDetails(View):
    def get (self,request,id,*args,**kwargs):
        prod=Product.objects.get(id=id)
        json_data=serialize('json',[prod])
        return HttpResponse(json_data,content_type='application/json')
    
