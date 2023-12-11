from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from cafe.models import Cafe
from users.models import CustomUser

class Review(models.Model):
    """Отзывы"""

    POSITIVE_CHOICES = (
        (5, 'Отлично - 5 звезд'),
        (4, 'Хорошо - 4 звезды'),
        (3, 'Удовлетворительно - 3 звезды'),
        (2, 'Неплохо - 2 звезды'),
        (1, 'Сойдет - 1 звезда'),
    )

    NEGATIVE_CHOICES = (
        (1, 'Плохо - 1 звезда'),
        (2, 'Неудовлетворительно - 2 звезды'),
        (3, 'Посредственно - 3 звезды'),
        (4, 'Слабо - 4 звезды'),
        (5, 'Ужасно - 5 звезд'),
    )

    cafe = models.ForeignKey(
        Cafe,
        on_delete=models.CASCADE,
        related_name="review",
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
    )
    score = models.IntegerField(
        choices=POSITIVE_CHOICES + NEGATIVE_CHOICES,
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
        return f"Review {self.id} by {self.author}"
