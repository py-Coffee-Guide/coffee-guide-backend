
from django.contrib.auth import authenticate, login
from django.utils.crypto import get_random_string
from djoser import utils
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import CustomUser
from .serializers import (
    ConfirmationCodeSerializer,
    CustomUserCreateByEmailSerializer,
    CustomUserCreateByPhoneSerializer,
    CustomUserLoginByEmailSerializer,
    CustomUserLoginByPhoneSerializer,
)


class CustomUserViewSet(viewsets.ModelViewSet):
    """Тут пытаюсь реализовать все пользовательские представления."""

    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)

    @action(
        methods=["post"],
    )
    def create_user(self, request, *args, **kwargs):
        """Комментарий."""
        registration_type = request.data.get("registration_type")
        confirmation_code = get_random_string(length=6)
        # с помощью if, по задумке, планировал различать метод регистрации.
        if registration_type == "email":
            serializer = CustomUserCreateByEmailSerializer(data=request.data)
            if serializer.is_valid():
                # если рега по почте, то код активации просто сохраняется в
                # базу без необходимости его вводить.
                user = serializer.save(confirmation_code=confirmation_code)
                # тут что-то пошло не так, я с чего-то решил, что могу
                # отправить стандартное djoser письмо не используя
                # djoser UserViewSet. Не успел доразобраться с этой частью
                # (41-43 строка включительно)
                context = {"user": user, "request": self.request}
                activation_url = utils.get_activation_url(user, context)
                utils.send_activation_email(activation_url, context)

                return Response(
                    {"message": "Ссылка подтверждения отправлена на почту."},
                    status=status.HTTP_201_CREATED,
                )
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        elif registration_type == "phone":
            # Тут рега по телефону, возвращает код пользователю, далее его
            # вводить нужно используя метод confirm_create_user
            serializer = CustomUserCreateByPhoneSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(confirmation_code=confirmation_code)
                return Response(
                    {"confirmation_code": confirmation_code},
                    status=status.HTTP_201_CREATED,
                )
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        else:
            return Response(
                {"error": "Invalid registration type"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    @action(
        methods=["post"],
    )
    def confirm_create_user(self, request, *args, **kwargs):
        """Подтверждение регистрации с использованием confirmation_code."""
        # Пользователь делает ещё один POST запрос с кодом
        serializer = ConfirmationCodeSerializer(data=request.data)
        if serializer.is_valid():
            confirmation_code = serializer.validated_data.get(
                "confirmation_code"
            )
            user = CustomUser.objects.filter(
                confirmation_code=confirmation_code
            ).first()
            if user:
                user.is_active = True
                user.save()
                return Response(
                    {"message": "Успешнпя регистрация!."},
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {"error": "Неверный код подтверждения."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""По сути я планировал авторизацию сделать по такому же принципу - берется
информация из loging_type (login_type = request.data.get("login_type")),
далее блок if email, присваивается CustomUserLoginByEmailSerializer,
получаются данные о пользователе, потом аутентификация (что то типо 
user = authenticate(request, email=email, password=password)) и аналогично
с if phone.
(пример кода)
    def login_user(self, request, *args, **kwargs):
        login_type = request.data.get("login_type"))
        if login_type == "email":
            serializer = CustomUserLoginByEmailSerializer(data=request.data)
            if serializer.is_valid():
                email = serializer.validated_data.get('email', None)
                password = serializer.validated_data.get('password', None)
                user = authenticate(request, email=email, password=password)
            if user is not None:
                login_user(request, user)
                return Response(serializer.data, status=status.HTTP_200_OK)."""

@extend_schema(tags=["Users"], description="Администратор")
@extend_schema_view(
    list=extend_schema(summary="Список пользователей", methods=["GET"]),
    # retrieve=extend_schema(
    #     summary="Детальная информация о пользователе (id=номер телефона)",
    #     methods=["GET"],
    # ),
)
class CustomUserViewSet(UserViewSet):
    """
    Вьюсет для:

    - изменения пароля;
    - изменения username;
    - регистрации нового пользователя;
    """
