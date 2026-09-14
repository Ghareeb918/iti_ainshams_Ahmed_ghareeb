from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
users=[]
def home(request):
    return HttpResponse("<h1>welcome</h1>")
def login(request):
    return HttpResponse("<h1>Login Page</h1>")
def logout(request):
    return HttpResponse("<h1>Logout Page</h1>")
def adduser(request):
    if(len(users)>0):
        users.append(users[len(users)-1]+1)
    else:
        users.append(1)
    return HttpResponse(f"<h1>add user {users[len(users)-1]}</h1>")
def deleteuser(request,id):
    if id in users:
        users.remove(id)
        return HttpResponse(f"<h1>{id} removed</h1>")
    else:
        return HttpResponse(f"<h1>{id} not founded</h1>")
def showusers(request):
    return render(request, 'myuser/user.html', {'users': users})