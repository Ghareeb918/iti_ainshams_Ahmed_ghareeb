from django.db import models

# Create your models here.
class Trainee(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50,null=False)
    last_name = models.CharField(max_length=50,null=False)
    email =models.EmailField(unique=True)
    password=models.CharField(max_length=100)
    Activity=models.BooleanField(default=True)