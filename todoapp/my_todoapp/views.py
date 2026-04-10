from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Home")
def Register(request):
    return HttpResponse("Register")

def login(request):
    return HttpResponse("Login")
def logout(request):
    return HttpResponse("Logout")
def delete_task(request,id):
    return HttpResponse("Delete")
