from django.urls import path
from trainee.views import trainee_main,sec_fun
urlpatterns = [
    path('',trainee_main),
    path('sec/',sec_fun),
]