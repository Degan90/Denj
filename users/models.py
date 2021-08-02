from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField( verbose_name='name', max_length=255, unique=True)
    avatar = models.CharField(max_length=500)
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'name'

    def get_username(self):
        return self.name
