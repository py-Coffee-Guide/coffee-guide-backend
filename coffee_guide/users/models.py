from django.contrib.auth.models import AbstractUser
from django.db import models

from .user_managers import CustomUserManager


class CustomUser(AbstractUser):
    """Модель Пользователя."""

    username = models.CharField(
        "Юзернейм",
        max_length=50,
        unique=True,
        default="Кофейный Сомелье",
        blank=True,
        null=False,
    )
    phone = models.CharField(max_length=11, null=True)
    password = models.CharField(
        "Пароль",
        max_length=50,
        blank=False,
        null=False,
    )
    email = models.EmailField(
        unique=True, max_length=254, verbose_name="email", null=True
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ("username",)

    def __str__(self):
        return f"{self.username}"
