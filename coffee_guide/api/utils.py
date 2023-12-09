from rest_framework import status
from django.shortcuts import get_object_or_404

from rest_framework.response import Response

from api.serializers.cafe import CafeUserSerializer


def add_to(self, model, user, pk) -> Response:
    """Добавить рецепт."""
    if model.objects.filter(user=user, cafe__id=pk).exists():
        return Response(
            {"errors": "Рецепт уже добавлен!"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    try:
        cafe = get_object_or_404(model, id=pk)
    except Exception:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    model.objects.create(user=user, cafe=cafe)
    serializer = CafeUserSerializer(cafe)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


def delete_from(self, model, user, pk) -> Response:
    """Удалить рецепт."""
    cafe = get_object_or_404(model, id=pk)
    obj = model.objects.filter(user=user, cafe=cafe)
    if obj.exists():
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(
        {"errors": "Рецепт уже удален!"}, status=status.HTTP_400_BAD_REQUEST
    )
