from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm
# Create your views here.

def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get('username')
            form.save()
            messages.success(request,f"Your Profile has been created successfully {uname}")
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    context={'form':form}

    return render(request,'users/register.html',context=context)
