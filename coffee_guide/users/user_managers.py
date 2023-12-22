from django.contrib.auth.models import BaseUserManager

from coffee_guide.settings import DEFAULT_USER_NAME


class CustomUserManager(BaseUserManager):
    """Менеджер модели пользователя, определяющий
    вид регистрации с дефолтным значением username."""

    use_in_migrations = True

    def register_user_by_email(
        self,
        email,
        password,
        phone=None,
        username=None,
        first_name=DEFAULT_USER_NAME,
        **extra_fields,
    ):
        user = self.model(
            username=username,
            password=password,
            email=email,
            phone=phone,
            first_name=first_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def register_user_by_phone(
        self,
        phone,
        password,
        email=None,
        username=None,
        first_name=DEFAULT_USER_NAME,
        **extra_fields,
    ):
        extra_fields.setdefault("is_active", True)
        user = self.model(
            username=username,
            password=password,
            phone=phone,
            email=email,
            first_name=first_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(
        self,
        password,
        email=None,
        phone=None,
        username=None,
        first_name=DEFAULT_USER_NAME,
        **extra_fields,
    ):
        extra_fields.setdefault("is_superuser", False)

        if not username:
            if not email and not phone:
                raise ValueError("Нужно указать почту или телефон")

        if email:
            email = self.normalize_email(email)

            if not username:
                username = email

            return self.register_user_by_email(
                username=username,
                password=password,
                email=email,
                phone=phone,
                first_name=first_name,
                **extra_fields,
            )

        if phone:
            if not username:
                username = phone

            return self.register_user_by_phone(
                username=username,
                password=password,
                email=email,
                phone=phone,
                first_name=first_name,
                **extra_fields,
            )

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(
                "Суперпользователь должен быть is_superuser=True."
            )

        user = self.create_user(
            username=username, password=password, **extra_fields
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
        # return self.create_user(
        #     username=username,
        #     password=password,
        #     **extra_fields
        # )
