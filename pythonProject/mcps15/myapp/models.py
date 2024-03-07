from django.db import models

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=20,blank=False)
    password = models.CharField(max_length=20, blank=False)
    class Meta:
        db_table = "login_table"

class Register(models.Model):
    studentname = models.CharField(max_length=20, blank=False)
    yearofstudy= models.CharField(max_length=20, blank=False)
    address = models.CharField(max_length=20, blank=False)
    loginid = models.CharField(max_length=20, blank=False)
    password = models.CharField(max_length=20, blank=False)
    class Meta:
        db_table = 'register'