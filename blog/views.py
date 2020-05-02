from django.shortcuts import render
from django.http import HttpResponse
from . models import Post
# Create your views here.

posts=Post.objects.all()

title='Homepage'
context={'posts':posts,'title':title}

def home(request):

    return render(request,'blog/home.html',context=context)

def about(request):
    return render(request,'blog/about.html')