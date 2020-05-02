from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts=[
    {'author':"ravi",
    'title':'Blog Post1',
     'content':'First Post',
     'date_posted':'27 AUG 2018'
     },
{'author':"Shankar",
    'title':'Blog Post2',
     'content':'Second Post',
     'date_posted':'28 AUG 2018'
     }
]
title='Homepage'
context={'posts':posts,'title':title}

def home(request):

    return render(request,'blog/home.html',context=context)

def about(request):
    return render(request,'blog/home.html')