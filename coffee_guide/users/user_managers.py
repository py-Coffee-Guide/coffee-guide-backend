from django.contrib.auth.models import BaseUserManager
from django.core.mail import send_mail

from api.utils import password_generation
from coffee_guide.settings import DEFAULT_USER_NAME, EMAIL_HOST_USER


class CustomUserManager(BaseUserManager):
    """Менеджер модели пользователя, для регистрации с ИНН."""

    use_in_migrations = True

    def create_user(
        self,
        email,
        organization_inn,
        password=None,
        username=None,
        name=DEFAULT_USER_NAME,
        **extra_fields,
    ):
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", True)
        user = self.model(
            username=organization_inn,
            password=password,
            organization_inn=organization_inn,
            email=email,
            name=name,
        )
        password = password_generation()
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        send_mail(
            "Пароль",
            f"Ваш пароль: {password}",
            EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )
        return user

    def create_superuser(
        self, username, password, organization_inn=None, **extra_fields
    ):
        if organization_inn is None:
            organization_inn = "root"

        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(
                "Суперпользователь должен быть is_superuser=True."
            )

        user = self.create_user(
            username=username,
            password=password,
            organization_inn=organization_inn,
            **extra_fields,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user
