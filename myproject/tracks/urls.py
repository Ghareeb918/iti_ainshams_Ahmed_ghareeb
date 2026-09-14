from django.urls import path
from tracks.views import trackwelcome,sec_fun
urlpatterns = [
    path('',trackwelcome),
    path('sec/',sec_fun),
]