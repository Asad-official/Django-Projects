from django.shortcuts import render
from django.shortcuts import HttpResponse,redirect
from .forms import RegisterForm

# Create your views here.
def home(request):
    return render(request,"index.html")
def Register(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login')
    else:
        form=RegisterForm()
        
    return render(request,"register.html",{'form':form})

def login(request):
    return render(request,"login.html")
def logout(request):
    return HttpResponse("Logout")
def delete_task(request,id):
    return HttpResponse("Delete")
