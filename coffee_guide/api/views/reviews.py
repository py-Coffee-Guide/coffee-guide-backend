from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from api.permissions import IsAuthor, ReadOnly
from api.serializers.reviews import ReviewSerializer

from cafe.models import Cafe


class ReviewViewSet(viewsets.ModelViewSet):
    """Вьюсет: Отзывы"""

    serializer_class = ReviewSerializer
    permission_classes = (IsAuthor | ReadOnly,)
    http_method_names = ["get", "patch", "delete", "post"]

    def get_queryset(self):
        cafe_id = self.kwargs.get("cafe_id")
        cafe = get_object_or_404(Cafe, id=cafe_id)
        return cafe.review.all()

    def perform_create(self, serializer):
        cafe_id = self.kwargs.get("cafe_id")
        cafe = get_object_or_404(Cafe, id=cafe_id)
        serializer.save(author=self.request.user, cafe=cafe)
