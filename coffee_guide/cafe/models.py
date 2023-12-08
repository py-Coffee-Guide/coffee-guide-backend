from django.core.exceptions import ValidationError
from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField

# from core.choices import DAY_CHOICES, TIME_CHOICES, CHECK_CHOICES
from users.models import User

from ratings.models import Rating





class City(models.Model):
    """Город"""

    name = models.CharField(
        verbose_name="Название города",
        max_length=200,
    )
    slug = models.SlugField(
        verbose_name="Ссылка на город",
        max_length=200,
    )

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def __str__(self):
        return self.name



class Cafe(models.Model):
    """Заведение"""
    name = models.CharField(
        verbose_name="Название заведения",
        max_length=150,
        unique=True,
    )
    cities = models.ForeignKey(
        City,
        verbose_name="Город",
        related_name="establishments",
        on_delete=models.SET_NULL,
        null=True,
    )
    address = models.CharField(
        verbose_name="Адрес заведения",
        max_length=100,
    )
    average_check = models.CharField(
        verbose_name="Средний чек",
        max_length=120,
        choices=CHECK_CHOICES,
    )
    metro = models.CharField(
        verbose_name=" ",
        max_length=,
        choices=CHECK_CHOICES,
    )
    poster = models.ImageField(
        verbose_name="Постер заведения",
        upload_to="establishment/images/poster",
        blank=True,
        null=True,
        default="",
    )
    latitude = models.FloatField(
        verbose_name="Широта",
        max_length=200,
        blank=True,
        null=True,
    )
    longitude = models.FloatField(
        verbose_name="Долгота",
        max_length=200,
        blank=True,
        null=True,
    )
    email = models.EmailField(
        verbose_name="Почта",
        max_length=254,
        unique=True,
    )
    telephone = PhoneNumberField(
        unique=True,
        verbose_name="Номер телефона",
    )
    rating = models.ForeignKey(
        Rating,
        verbose_name="",
        related_name="",
        on_delete=models.SET_NULL,
        null=True,
    )
    review = models.ForeignKey(
        Reviews,
        verbose_name="",
        related_name="",
        on_delete=models.SET_NULL,
        null=True,
    )
    description = models.TextField(
        verbose_name="Описание заведения",
        max_length=1500,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Заведение"
        verbose_name_plural = "Заведения"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)



class WorkEstablishment(models.Model):
    """Время работы"""

    establishment = models.ForeignKey(
        Cafe,
        on_delete=models.CASCADE,
        null=True,
        related_name="worked",
    )
    day = models.CharField(
        verbose_name="День недели",
        max_length=100,
        choices=DAY_CHOICES,
    )
    day_off = models.BooleanField(
        verbose_name="Выходной",
        default=False,
    )
    start = models.CharField(
        verbose_name="Начало работы",
        choices=TIME_CHOICES,
        max_length=145,
        null=True,
        blank=True,
    )
    end = models.CharField(
        verbose_name="Конец работы",
        choices=TIME_CHOICES,
        max_length=145,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Время работы"
        verbose_name_plural = "Время работы"
        # constraints = [
        #     models.UniqueConstraint(
        #         fields=["day", "establishment"],
        #         name="unique_work",
        #         violation_error_message="Можно добавить только 1 день недели",
        #     ),
        # ]

    def clean(self):
        if self.start and self.end is not None:
            if self.start >= self.end:
                raise ValidationError(
                    {
                        "end": "Укажите корректоное время окончания. Оно не может быть меньше времени начала"
                    }
                )

    def __str__(self):
        return self.day


class ImageEstablishment(models.Model):
    """Несколько изображений"""

    establishment = models.ForeignKey(
        Cafe,
        on_delete=models.CASCADE,
        null=True,
        related_name="images",
    )
    name = models.CharField(
        verbose_name="Описание изображения",
        max_length=100,
    )
    image = models.ImageField(
        verbose_name="Изображение заведения",
        upload_to="establishment/images/est_image",
    )

    class Meta:
        verbose_name = "Изображение заведения"
        verbose_name_plural = "Изображения заведения"

    def __str__(self):
        return self.name


class Favorite(models.Model):
    """Избранное"""

    user = models.ForeignKey(
        User,
        related_name="favorite",
        on_delete=models.CASCADE,
    )
    establishment = models.ForeignKey(
        Cafe,
        related_name="favorite",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Избранное"
        verbose_name_plural = "Избранное"
        ordering = ["id"]
        constraints = [
            models.UniqueConstraint(
                fields=["user", "establishment"], name="uniquefavorit"
            ),
        ]
