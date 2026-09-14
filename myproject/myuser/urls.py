from django.urls import path
from myuser.views import login,logout,adduser,deleteuser,showusers
urlpatterns = [
    path('login',login),
    path('logout/',logout),
    path('add/',adduser,name='adduser'),
    path('delete/<int:id>',deleteuser, name='deleteuser'),
    path('user/', showusers, name='user'),
]