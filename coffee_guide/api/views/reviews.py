from typing import Any, List, Union

from api.permissions import IsAuthor, ReadOnly
from api.serializers.reviews import ReviewSerializer
from cafe.models import Cafe
from django.db.models import Model, Q, QuerySet
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from rest_framework import serializers, viewsets


class ReviewViewSet(viewsets.ModelViewSet):
    """Вьюсет: Отзывы"""

    serializer_class = ReviewSerializer
    permission_classes = (IsAuthor | ReadOnly,)
    http_method_names = ["get", "post"]

    def get_queryset(self) -> list[Any]:
        """Получает отсортированный список отзывов для кафе."""
        cafe_id = self.kwargs.get("cafe_id")
        cafe = get_object_or_404(Cafe, id=cafe_id)
        queryset = cafe.review.all().order_by("-pub_date")
        positive_reviews = queryset.filter(score__gte=1)
        negative_reviews = queryset.filter(Q(score__gte=1) & Q(score__lte=5))
        return list(positive_reviews) + list(negative_reviews)

    def perform_create(self, serializer: serializers.ModelSerializer) -> HttpResponse:
        """Создает новый отзыв для кафе."""
        cafe_id = self.kwargs.get("cafe_id")
        try:
            cafe = Cafe.objects.get(id=cafe_id)
        except Cafe.DoesNotExist:
            return HttpResponseNotFound("Кафе с таким ID не найдено в системе.")
        serializer.save(author=self.request.user, cafe=cafe)
