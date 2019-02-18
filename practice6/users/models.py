from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserProfile(AbstractUser):
    class Meta:
        verbose_name = '用户后台总中心'
        verbose_name_plural = '这是什么'