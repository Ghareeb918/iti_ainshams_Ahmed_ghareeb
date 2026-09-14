from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def trainee_main(request):
    return HttpResponse("<h1>it is empty till now</h1>")
def sec_fun(request):
    return HttpResponse("<h1>sec Func in trainee</h1>")