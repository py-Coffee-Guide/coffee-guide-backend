from django.contrib.auth.models import AbstractUser
from django.db import models

from coffee_guide.settings import DEFAULT_USER_NAME

from cafe.models import Cafe
from .user_managers import CustomUserManager


class CustomUser(AbstractUser):
    """Модель Пользователя."""

    username = models.CharField(
        "Юзернейм",
        unique=True,
        max_length=50,
        blank=True,
        null=False,
    )
    phone = models.CharField(
        "Номер телефона",
        unique=True,
        max_length=11,
        blank=True,
        null=True,
    )
    email = models.EmailField(
        "Почта",
        unique=True,
        max_length=254,
        blank=True,
        null=True,
    )
    first_name = models.CharField(
        "Имя",
        max_length=150,
        default=DEFAULT_USER_NAME,
        blank=True,
        null=False,
    )
    password = models.CharField(
        "Пароль",
        max_length=128,
        blank=False,
        null=False,
    )
    is_verified = models.BooleanField("Проверка верификации", default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    # REQUIRED_FIELDS = ['email', 'phone']

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        unique_together = ("username", "email", "phone")
        ordering = ("username",)

    def __str__(self):
        return f"{self.first_name} ({self.username})"


class Favorite(models.Model):
    """Избранное"""

    user = models.ForeignKey(
        CustomUser,
        related_name="favorite",
        on_delete=models.CASCADE,
    )
    cafe = models.ForeignKey(
        Cafe,
        related_name="favorite",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Избранное"
        verbose_name_plural = "Избранное"
        ordering = ["id"]
        constraints = [
            models.UniqueConstraint(
                fields=["user", "cafe"], name="uniquefavorite"
            ),
        ]
