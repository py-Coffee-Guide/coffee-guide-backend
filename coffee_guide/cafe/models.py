import io
import requests
import os

from django.db import models
from django.core.exceptions import ValidationError
from pathlib import Path
from PIL import Image

from users.models import CustomUser

from django.core.exceptions import ValidationError
from django.core.files import File
from django.core.validators import RegexValidator
from django.db import models
from users.models import CustomUser

BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


class StopFactor(models.Model):
    """Атрибуты."""
    id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(
        max_length=200, unique=True, verbose_name="Название"
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        # validators=(validate_slug,),
        verbose_name="Уникальный Тег",
    )

    class Meta:
        verbose_name = "Доп. свойство"
        verbose_name_plural = "Доп. свойства"

    def __str__(self):
        return self.name


class Contact(models.Model):
    """Контакты."""

    phone = models.CharField(max_length=11, verbose_name="Номер телефона")
    website = models.URLField(max_length=200, verbose_name="Вебсайт")
    email = models.EmailField(max_length=254, verbose_name="Почта")

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return (f"Номер телефона кофейни - {self.phone}"
                f"E-mail кофейни - {self.email}"
                f"Сайт кофейни - {self.website}")


class Point(models.Model):
    """Координаты"""

    lat = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Ширина")
    lon = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Долгота")

    class Meta:
        verbose_name = "Координаты"
        verbose_name_plural = "Координаты"

    def __str__(self):
        return f"{self.lat}, {self.lon}"


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


class District(models.Model):
    """Район"""

    name = models.CharField(
        verbose_name="Название района",
        max_length=200,
    )
    slug = models.SlugField(
        verbose_name="Ссылка на район",
        max_length=200,
    )

    class Meta:
        verbose_name = "Район"
        verbose_name_plural = "Районы"

    def __str__(self):
        return self.name


class Metro(models.Model):
    """Метро"""

    color = models.CharField(
        verbose_name="Цвет ветки метро",
        max_length=7,
        validators=[
            RegexValidator(
                regex="^#[0-9a-fA-F]{6}$",
                message="Цвет должен быть в формате #123456",
            )
        ],
    )
    comment = models.CharField(
        verbose_name="Название ветки метро",
        max_length=200,
    )
    distance = models.DecimalField(verbose_name="Расстояние до станции", max_digits=6, decimal_places=2)
    name = models.CharField(
        verbose_name="Название станции метро",
        max_length=100,
    )
    slug = models.SlugField(
        verbose_name="Ссылка на метро",
        max_length=200,
        unique=True,
    )

    class Meta:
        verbose_name = "Станция"
        verbose_name_plural = "Станции"

    def __str__(self):
        return self.name


class Schedule(models.Model):
    """Время работы"""
    # Разделить по подобию ингредиентов

    cafe = models.ForeignKey(
        "Cafe",
        on_delete=models.CASCADE,
        null=True,
        related_name="worked",
    )
    day = models.CharField(
        verbose_name="День недели",
        max_length=100,
        # choices=DAY_CHOICES,
    )
    day_off = models.BooleanField(
        verbose_name="Выходной",
        default=False,
    )
    start = models.CharField(
        verbose_name="Начало работы",
        # choices=TIME_CHOICES,
        max_length=145,
        null=True,
        blank=True,
    )
    end = models.CharField(
        verbose_name="Конец работы",
        # choices=TIME_CHOICES,
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
                    {"end": "Укажите корректное время окончания. Оно не может быть меньше времени начала"}
                )

    def __str__(self):
        return self.day


class Cafe(models.Model):
    """Заведение"""
    name = models.CharField(
        verbose_name="Название кофейни",
        max_length=150,
        unique=True,
    )
    description = models.TextField(
        verbose_name="Описание кофейни",
        max_length=1500,
        blank=True,
        null=True,
    )
    rating = models.DecimalField(
        verbose_name="Рейтинг 2Gis",
        max_digits=5,
        decimal_places=2,
        null=True,
    )
    address = models.CharField(
        verbose_name="Адрес кофейни",
        max_length=100,
    )
    poster = models.ImageField(
        verbose_name="Постер кофейни",
        upload_to="establishment/images/poster",
        blank=True,
        null=True,
        default="",
    )
    cities = models.ForeignKey(
        City,
        verbose_name="Город",
        related_name="cafe",
        on_delete=models.SET_NULL,
        null=True,
    )
    district = models.ManyToManyField(
        District,
        verbose_name="Район",
        related_name="cafe",
        blank=True,
    )
    point = models.ManyToManyField(
        Point,
        verbose_name="Координаты",
        related_name="cafe",
        blank=True,
    )
    contact = models.ForeignKey(
        Contact,
        verbose_name="Контакты",
        related_name="cafe",
        on_delete=models.SET_NULL,
        null=True,
    )
    stop_factors = models.ManyToManyField(
        StopFactor,
        verbose_name="Доп. свойства",
        related_name="cafes",
        blank=True,
    )
    # schedule = models.ForeignKey(
    #     Schedule,
    #     verbose_name="График работы",
    #     related_name="cafe",
    #     on_delete=models.SET_NULL,
    #     null=True,
    # )
    # review = models.ForeignKey(
    #     Review,
    #     verbose_name="Отзывы",
    #     related_name="cafe",
    #     on_delete=models.SET_NULL,
    #     null=True,
    # )
    # average_check = models.CharField(
    #     verbose_name="Средний чек",
    #     max_length=120,
    #     choices=CHECK_CHOICES,
    # )
    metro = models.ForeignKey(
        Metro,
        verbose_name="Метро",
        related_name="cafe",
        on_delete=models.SET_NULL,
        null=True,
    )
    # latitude = models.FloatField(
    #     verbose_name="Широта",
    #     max_length=200,
    #     blank=True,
    #     null=True,
    # )
    # longitude = models.FloatField(
    #     verbose_name="Долгота",
    #     max_length=200,
    #     blank=True,
    #     null=True,
    # )
    # email = models.EmailField(
    #     verbose_name="Почта",
    #     max_length=254,
    #     unique=True,
    # )
    # telephone = PhoneNumberField(
    #     unique=True,
    #     verbose_name="Номер телефона",
    # )

    class Meta:
        ordering = ('name',)
        verbose_name = "Кофейня"
        verbose_name_plural = "Кофейни"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class ImageCafe(models.Model):
    image_file = models.ImageField(upload_to="images", blank=True)
    image_url = models.URLField(blank=True)

    def save(self, *args, **kwargs):
        if self.image_url and not self.image_file:
            response = requests.get(self.image_url, stream=True)
            img = Image.open(io.BytesIO(response.content))
            img_name = f"{self.image_url.split('/')[-1]}"
            img_path = os.path.join(MEDIA_ROOT, img_name)
            img.save(img_path)
            self.image_file = os.path.join(img_name)
        super().save(*args, **kwargs)


# class ImageEstablishment(models.Model):
#     """Несколько изображений"""

#     establishment = models.ForeignKey(
#         Cafe,
#         on_delete=models.CASCADE,
#         null=True,
#         related_name="images",
#     )
#     name = models.CharField(
#         verbose_name="Описание изображения",
#         max_length=100,
#     )
#     image = models.ImageField(
#         verbose_name="Изображение заведения",
#         upload_to="establishment/images/est_image",
#     )

#     class Meta:
#         verbose_name = "Изображение заведения"
#         verbose_name_plural = "Изображения заведения"

#     def __str__(self):
#         return self.name


class Favorite(models.Model):
    """Избранное"""

    user = models.ForeignKey(
        CustomUser,
        related_name="favorite",
        on_delete=models.CASCADE,
    )
    cafe = models.ForeignKey(
        Cafe,
        related_name="favorite",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Избранное"
        verbose_name_plural = "Избранное"
        ordering = ["id"]
        constraints = [
            models.UniqueConstraint(fields=["user", "cafe"], name="uniquefavorite"),
        ]
