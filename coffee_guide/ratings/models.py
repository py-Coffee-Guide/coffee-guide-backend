from django.db import models
from cafe.models import Establishment


class Rating(models.Model):
    """Рейтинг"""

    establishment = models.ForeignKey(
        Establishment,
        on_delete=models.CASCADE,
        related_name="review",
    )
    # score = models.PositiveSmallIntegerField(
    #     validators=[
    #         MinValueValidator(1, message="Допустимые значние 1-5"),
    #         MaxValueValidator(5, message="Допустимые значние 1-5"),
    #     ],
    # )

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"

    def __str__(self):
        return self.score
