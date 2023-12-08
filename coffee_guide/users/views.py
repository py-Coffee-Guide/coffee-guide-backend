from djoser.views import UserViewSet
# from rest_framework import mixins, permissions, status, viewsets
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from users.models import CustomUser


class CustomUserViewSet(UserViewSet):
    """Вьюсет для:
    - изменения пароля;
    - изменения username;
    - регистрации нового пользователя;"""

    # def get_queryset(self):
    #     return User.objects.all()

    # def get_serializer_class(self):
    #     if self.action == "set_password":
    #         return SetPasswordSerializer
    #     elif self.action == "set_username":
    #         return SetUsernameSerializer
    #     return CustomUserCreateSerializer

    # def get_serializer(self, *args, **kwargs):
    #     kwargs["context"] = self.get_serializer_context()
    #     return self.get_serializer_class()(*args, **kwargs)

    # @action(
    #     detail=False,
    #     methods=["post"],
    #     permission_classes=(permissions.IsAuthenticated,),
    # )
    # def set_password(self, request):
    #     serializer = self.get_serializer(request.user, data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #     return Response(
    #         {"detail": "Пароль успешно изменен."},
    #         status=status.HTTP_204_NO_CONTENT,
    #     )

    # @action(
    #     detail=False,
    #     methods=["post"],
    #     permission_classes=(permissions.IsAuthenticated,),
    # )
    # def set_username(self, request):
    #     serializer = self.get_serializer(request.user, data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #     return Response(
    #         {"detail": "Username успешно изменен."},
    #         status=status.HTTP_204_NO_CONTENT,
    #     )
