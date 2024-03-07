from django.db import models

# Create your models here.
class User(models.Model):
    fullname = models.CharField(max_length=20, blank=False)
    email = models.EmailField(max_length=30,blank=False)
    username =  models.CharField(max_length=20,blank=False)
    password = models.CharField(max_length=20,blank=False)
    mobileno = models.CharField(max_length=10,blank=False)
    location = models.CharField(max_length=20,blank=False)
    class Meta:
        db_table = "user_table"

class Login(models.Model):
    username = models.CharField(max_length=20,blank=False)
    password = models.CharField(max_length=20, blank=False)
    class Meta:
        db_table = "login_table"

class alogin(models.Model):
    auser = models.CharField(max_length=20, blank=False)
    apassword = models.CharField(max_length=20, blank=False)
    class Meta:
        db_table = 'admin_table'
