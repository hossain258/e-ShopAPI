from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    username =models.OneToOneField(User,on_delete=models.CASCADE)
    phone =models.CharField(max_length=20,blank=False)
    email=models.EmailField(max_length=200,blank=True)
    address=models.CharField(max_length=300,blank=True)    
    city=models.CharField(max_length=200,blank=True)
    country=models.CharField(max_length=200,blank=True)
    is_varified=models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.user.username
    
