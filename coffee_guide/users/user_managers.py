from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, phone=None, password=None, email=None, username="Кофейный Сомелье"):
        if not phone:
            raise ValueError("The Phone field must be set")
        user = self.model(phone=phone, username=username, password=password)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.model(username=username, password=password)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user
