from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class UserInfo(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # phone = models.CharField(max_length=10, default='')
    username = models.CharField(max_length=40, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    url_id = models.CharField(max_length=7, default='', blank=True)
    visits_counter = models.IntegerField(default=0)
    unsubscribe = models.BooleanField(default=0)

    def __str__(self):
        return self.username
