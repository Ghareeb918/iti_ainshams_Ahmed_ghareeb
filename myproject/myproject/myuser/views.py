from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("<h1>welcome</h1>")
def login(request):
    return HttpResponse("<h1>Login Page</h1>")
def logout(request):
    return HttpResponse("<h1>Logout Page</h1>")