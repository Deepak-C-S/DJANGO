from django.shortcuts import render

# Create your views here.
def demo(request):
    name='Deepak'
    age=22
    d={'name':name,'age':age}
    return render(request,'myapp/demo.html',d)