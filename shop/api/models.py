from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    patronymic = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    last_login = None
    is_superuser = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'name',
        'surname',
        'patronymic',
    ]
    objects = CustomUserManager()


class Product(models.Model):
    name = models.CharField(max_length=265)
    description = models.CharField(max_length=265)
    price = models.CharField(max_length=265)
