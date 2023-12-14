from django.db import models

# Create your models here.

class User(models.Model):
    class Meta:
        db_table = 'user'
    username = models.CharField(max_length=64, unique=True, primary_key=True)
    password = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.username

# from django.contrib.auth.models import AbstractUser

# class CustomUser(AbstractUser):
#     pass
#     # add additional fields in here

#     def __str__(self):
#         return self.username