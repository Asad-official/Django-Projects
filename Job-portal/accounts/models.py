from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    is_employee=models.BooleanField(default=False)
    is_employer=models.BooleanField(default=False)

    phone_number=models.CharField(max_length=15,blank=True,null=True)
    location=models.CharField( max_length=50,blank=True,null=True)

    def __str__(self):
        return self.username