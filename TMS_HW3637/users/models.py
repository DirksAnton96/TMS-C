from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True, null=True, blank=True)
    notify = models.BooleanField(default=True)
        
    class Meta:
        db_table = "users"
        
