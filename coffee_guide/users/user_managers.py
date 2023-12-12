from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    """Менеджер модели пользователя, определяющий
    вид регистрации с дефолтным значением username."""

    def register_user_by_email(
        self, email, password, username="Кофейный Сомелье"
    ):
        user = self.model(username=username, password=password, email=email)
        user.set_password(password)
        user.save()
        return user

    def register_user_by_phone(
        self, phone, password, username="Кофейный Сомелье"
    ):
        user = self.model(username=username, password=password, phone=phone)
        user.set_password(password)
        user.save()
        return user

    def create_user(
        self, email_or_phone, password, username="Кофейный Сомелье"
    ):
        if not email_or_phone:
            raise ValueError("The Phone or Email field must be set")

        elif "@" in email_or_phone:
            email = self.normalize_email(email_or_phone)
            return self.register_user_by_email(
                username=username, password=password, email=email
            )

        else:
            phone = email_or_phone
            return self.register_user_by_phone(
                username=username, password=password, phone=phone
            )
