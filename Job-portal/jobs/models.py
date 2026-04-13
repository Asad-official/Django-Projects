from django.db import models
from django.conf import settings

# Create your models here.
class Job(models.Model):
    employer=models.ForeignKey(settings.AUTH_USER_MODEL,on_manager_managed=True,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    description=models.TextField()
    location=models.CharField(max_length=100)
    salary=models.CharField(max_length=100,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
