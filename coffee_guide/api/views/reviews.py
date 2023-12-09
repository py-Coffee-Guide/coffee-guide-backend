from rest_framework import viewsets
from reviews.models import Review


class ReciewViewSet(viewsets.ModelViewSet):
    """Вьюсет: Городов"""

    queryset = Review.objects.all()
