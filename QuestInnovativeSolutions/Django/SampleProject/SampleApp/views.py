import imp
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.


def frst(request):
    return HttpResponse("Welcome  to Django")

def scnd(request):
    return HttpResponse("MVT Pattern")

def thrd(request):
    a='It is an MVT Pattern'
    return HttpResponse("<h2>Django Framework</h2>"+a)

def temp(request):
    return render(request,'frst.html')

def dtl(request):
    a='Helloworld'
    x= [1,2,3,4,5]
    return render(request,'scnd.html',{'data':a, 'new':x})

def temp1(request):
    temp= loader.get_template('frst.html')
    return HttpResponse(temp.render())

