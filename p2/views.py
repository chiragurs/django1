from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("assingment no 1")

def home(request):
    return HttpResponse("<h1>pyspiders basvangudi</h1>")

def html_1(request):
    return render(request,"sample1.html")

def third(request):
    return render(request,"directory/third.html", context={'data':"chirag",'name':"tanu"})

def fourth(request):
    fruits=['apple','mango','banana','kiwi','orange','guava']
    return render(request,"directory/fourth.html",{'fruits':fruits})

def fifth(request):
    return render(request,"directory/fifth.html",{'a':20,'b':30})

