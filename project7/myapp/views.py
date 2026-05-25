from django.shortcuts import render

# Create your views here.
def myview(request):
    name="RAMA"
    place="AYODHYA"
    info={'name':name,'place':place}
    return render(request,'myapp/index.html',info)
