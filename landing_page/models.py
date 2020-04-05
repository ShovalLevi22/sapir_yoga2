from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.TextField(max_length=10, default='')

    # first_name = models.CharField(max_length=250)
    # last_name = models.CharField(max_length=250)

    # email = models.EmailField(max_length=280)

    def __str__(self):
        return self.user.username
