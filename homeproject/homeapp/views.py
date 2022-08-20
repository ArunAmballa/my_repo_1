from django.shortcuts import render
from homeapp.forms import HomeForm
from homeapp.forms import AgeForm
from homeapp.forms import MarksForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

def Home_view(request):
    form=HomeForm()
    return render(request,'homeapp/home.html',{'form':form})

def Age_view(request):
    name = request.GET['name']
    form=AgeForm()
    response=render(request,'homeapp/age.html',{'form':form,'name':name})
    response.set_cookie('name',name)
    return response

def Marks_view(request):
    age=request.GET['age']
    name=request.COOKIES['name']
    form=MarksForm()
    response=render(request,'homeapp/marks.html',{'form':form,'name':name,'age':age})
    response.set_cookie('age',age)
    return response

def result_view(request):
    marks=request.GET['marks']
    name=request.COOKIES['name']
    age=request.COOKIES['age']
    response=render(request,'homeapp/result.html',{'name':name,'age':age,'marks':marks})
    response.set_cookie('marks',marks)
    return response
