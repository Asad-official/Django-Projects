from django.shortcuts import render
from django.shortcuts import HttpResponse,redirect, get_object_or_404
from .forms import RegisterForm, TaskForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Task

# Create your views here.
@login_required
def home(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Assign the logged-in user to the task
            task.save()
            return redirect('home')
    else:
        form = TaskForm()
    tasks=Task.objects.filter(user=request.user).order_by('-created_at')
    context={
        'tasks':tasks ,
        'form':form
    }
    return render(request,"index.html",context)
def Register(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login')
    else:

        form=RegisterForm()

    return render(request,"register.html",{'form':form})

def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            return render(request,"login.html")



        print(username,password)
    return render(request,"login.html")
@login_required
def logout_view(request):
    logout(request)
    return redirect('Login')
def delete_task(request,id):
    # Retrieve the task or return a 404 if it doesn't exist
    task = get_object_or_404(Task, id=id, user=request.user)
    
    if request.method == "POST":
        task.delete()
        return redirect('home')
@login_required
def complete_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    task.completed = True
    task.save()
    return redirect('home') # This reloads index.html with the new data
    
