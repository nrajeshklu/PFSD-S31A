from django.db import models

# Create your models here.
class User(models.Model):
    fullname = models.CharField(max_length=20, blank=False)
    email = models.EmailField(max_length=30, blank=False)
    username = models.CharField(max_length=20, blank=False)
    password = models.CharField(max_length=20, blank=False)
    mobileno = models.CharField(max_length=10, blank=False)
    address = models.CharField(max_length=20, blank=False)

    class Meta:
        db_table = "ttm_user_data"