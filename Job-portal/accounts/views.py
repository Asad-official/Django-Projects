from django.shortcuts import render ,redirect
from django.contrib.auth import login
from .forms import UserForm
from django.http import HttpResponse

# Create your views here.
def signup_view(request):
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('home')
    else:
            
        form=UserForm()
    return render(request,'accounts/signup.html',{'form':form})