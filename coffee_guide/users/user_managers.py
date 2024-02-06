from django.contrib.auth.models import BaseUserManager

from coffee_guide.settings import DEFAULT_USER_NAME


class CustomUserManager(BaseUserManager):
    """Менеджер модели пользователя, для регистрации с ИНН."""

    use_in_migrations = True

    def create_user(
        self,
        password,
        email,
        organization_inn,
        username,
        name=DEFAULT_USER_NAME,
        **extra_fields,
    ):
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", True)
        user = self.model(
            username=username,
            password=password,
            organization_inn=organization_inn,
            email=email,
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
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
        user.save(using=self._db)
        return user
