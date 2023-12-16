from typing import Any

from api.permissions import IsAuthor, ReadOnly
from api.serializers.reviews import ReviewSerializer
from cafe.models import Cafe
from django.db.models import Q
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import (
    OpenApiParameter,
    extend_schema,
    extend_schema_view,
)
from rest_framework import serializers, viewsets


@extend_schema(
    tags=["Отзывы"],
    methods=["GET", "POST"],
    description="Пользователь",
)
@extend_schema_view(
    list=extend_schema(
        summary="Получить список отзывов к заведению с id=",
        description="Пользователь",
    ),
    # destroy=extend_schema(
    #     summary="Удалить отзыв",
    #     description="Пользователь",
    # ),
    create=extend_schema(summary="Оставить отзыв"),
    retrieve=extend_schema(
        summary="Один отзыв",
        description="Пользователь",
        parameters=[
            OpenApiParameter(
                name="cafe_id",
                location=OpenApiParameter.PATH,
                type=OpenApiTypes.INT,
            ),
            OpenApiParameter(
                name="id",
                location=OpenApiParameter.PATH,
                type=OpenApiTypes.INT,
            ),
        ],
    ),
    #     partial_update=extend_schema(
    #         summary="Редактировать отзыв",
    #         parameters=[
    #             OpenApiParameter(
    #                 name="cafe_id",
    #                 location=OpenApiParameter.PATH,
    #                 type=OpenApiTypes.INT,
    #             ),
    #             OpenApiParameter(
    #                 name="id",
    #                 location=OpenApiParameter.PATH,
    #                 type=OpenApiTypes.INT,
    #             ),
    #         ],
    #     ),
)
class ReviewViewSet(viewsets.ModelViewSet):
    """
    Вьюсет: Отзывы

    Этот вьюсет обрабатывает операции чтения и создания отзывов для определенного кафе.
    """

    serializer_class = ReviewSerializer
    permission_classes = (IsAuthor | ReadOnly,)
    http_method_names = ["get", "post"]

    @extend_schema(summary="Получает отсортированный список отзывов для кафе")
    def get_queryset(self) -> list[Any]:
        """
        Получает отсортированный список отзывов для кафе.

        :return: Список отзывов, сначала положительные, затем отрицательные, отсортированные по дате публикации.
        :rtype: list
        """
        cafe_id = self.kwargs.get("cafe_id")
        cafe = get_object_or_404(Cafe, id=cafe_id)
        queryset = cafe.review.all().order_by("-pub_date")
        positive_reviews = queryset.filter(score__gte=1)
        negative_reviews = queryset.filter(Q(score__gte=1) & Q(score__lte=5))
        return list(positive_reviews) + list(negative_reviews)

    @extend_schema(summary="Создает новый отзыв для кафе")
    def perform_create(self, serializer: serializers.ModelSerializer) -> HttpResponse:
        """
        Создает новый отзыв для кафе.

        :param serializer: Сериализатор отзыва
        :type serializer: serializers.ModelSerializer
        :return: Ответ HTTP после успешного создания или ошибки, если кафе не найдено.
        :rtype: HttpResponse
        """
        cafe_id = self.kwargs.get("cafe_id")
        try:
            cafe = Cafe.objects.get(id=cafe_id)
        except Cafe.DoesNotExist:
            return HttpResponseNotFound("Кафе с таким ID не найдено в системе.")
        serializer.save(author=self.request.user, cafe=cafe)
