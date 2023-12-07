from django.db import models
# from django.core.validators import MaxValueValidator, MinValueValidator
from cafe.models import Establishment



class Review(models.Model):
    """Отзывы"""

    establishment = models.ForeignKey(
        Establishment,
        on_delete=models.CASCADE,
        related_name="review",
    )
    # author = models.ForeignKey(
    #     User,
    #     on_delete=models.CASCADE,
    # )
    text = models.TextField(
        verbose_name="Текст отзыва",
        max_length=500,
    )
    created = models.DateTimeField(
        verbose_name="Дата публикации",
        auto_now_add=True,
    )

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        constraints = [
            models.UniqueConstraint(
                fields=["establishment", "author"], name="uniquereview"
            ),
        ]
        ordering = ["-created"]

    def __str__(self):
        return self.text
