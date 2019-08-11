from django.db import models
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

from common.models import BaseModel


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    # identifier = models.CharField(max_length=40, unique=True)
    USERNAME_FIELD = 'username'

    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField(
        unique=True,
        max_length=254,
    )
    # is_active = models.BooleanField(default=True)
    # is_admin = models.BooleanField(default=False)

    objects = UserManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
