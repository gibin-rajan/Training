from django.db import models

# Create your models here.

# class 92 ref notes


#Should add App name in the setting.py file  like in INSTALLED_APPS

class Student(models.Model):
    first_name= models.CharField(max_length=20)
    last_name= models.CharField(max_length=20)
    age= models.IntegerField()
    email= models.EmailField()   

class Employee(models.Model):
    first_name= models.CharField(max_length=20)
    last_name= models.CharField(max_length=20)
    age= models.IntegerField()
    email= models.EmailField()
    salary=models.IntegerField()   

# py manage.py migrate
# table create
# py manage.py makemigrations
# settings -> Installed_Apps -> Application name
# py manage.py migrate