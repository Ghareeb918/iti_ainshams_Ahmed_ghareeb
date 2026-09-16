from django.urls import path
from . import views

urlpatterns = [
    path('show/', views.trainee_list, name='trainee_list'),
    path('login/', views.inserttrainee, name='insert_trainee'),
    path('delete/<int:id>/', views.deletetrainee, name='delete_trainee'),
    path('Activity/<int:id>/', views.xorActivity, name='Activity'),
]