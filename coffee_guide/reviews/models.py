from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from cafe.models import Cafe
from users.models import CustomUser


class Review(models.Model):
    """Отзывы"""

    cafe = models.ForeignKey(
        Cafe,
        on_delete=models.CASCADE,
        related_name="review",
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
    )
    text = models.TextField(
        verbose_name="Текст отзыва",
        max_length=500,
    )
    score = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Оценка",
    )
    pub_date = models.DateTimeField(
        verbose_name="Дата публикации",
        auto_now_add=True,
    )

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        constraints = [
            models.UniqueConstraint(
                fields=["cafe", "author"], name="uniquereview"
            ),
        ]
        ordering = ["-pub_date"]

    def __str__(self):
        return self.text
