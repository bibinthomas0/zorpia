from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from verification.managers import CustomUserManager



class CustomUser(AbstractBaseUser,PermissionsMixin):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    last_login = models.DateTimeField(blank=True, null=True)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=50)
    dob = models.DateField()
    userid = models.IntegerField(unique=True)
    password = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_blocked = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD  = 'email'

    objects = CustomUserManager()
    
    def __str__(self):
        return self.username

class Userdetails(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    phone = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, null=True)
    last_seen = models.DateTimeField()
    commenting = models.BooleanField(default=True)
    posting = models.BooleanField(default=True)
    red_flags = models.PositiveIntegerField()
    userr = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.userr.username