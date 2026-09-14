from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def trackwelcome(request):
    return HttpResponse("<h1>welcome</h1>")
def sec_fun(request):
    return HttpResponse("<h1>sec Func</h1>")
