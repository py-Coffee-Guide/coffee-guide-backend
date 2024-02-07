import io
import os

# from pathlib import Path

import requests
from django.db import models
from PIL import Image

from coffee_guide.settings import BASE_DIR, MEDIA_ROOT

from users.models import CustomUser


class Cafe(models.Model):
    """Заведение"""

    name = models.CharField(
        verbose_name="Название кофейни",
        max_length=150,
        unique=False,
    )
    description = models.TextField(
        verbose_name="Описание кофейни",
        max_length=1500,
        blank=True,
        null=True,
    )
    address = models.ForeignKey(
        "Address",
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Адрес кофейни",
        related_name="cafe",
    )
    schedules = models.ManyToManyField(
        "Schedule",
        through="ScheduleInCafe",
        verbose_name="Время работы",
        max_length=100,
        related_name="cafes",
    )
    alternatives = models.ManyToManyField(
        "Alternative",
        verbose_name="Дополнительные опции",
        max_length=100,
    )
    tags = models.ManyToManyField(
        "Tag", verbose_name="Доступные опции", max_length=100
    )
    roasters = models.ManyToManyField(
        "Roaster", verbose_name="Обжарщик кофе", max_length=100
    )
    drinks = models.ManyToManyField(
        "Drink",
        through="DrinkInCafe",
        verbose_name="Напиток",
        max_length=100,
        related_name="cafes",
    )
    organization = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Организация",
        related_name="cafes",
    )
    image = models.ImageField(
        blank=True,
        null=True,
        verbose_name="Фото кофейни",
        upload_to="cafe/images"
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "Кофейня"
        verbose_name_plural = "Кофейни"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class Address(models.Model):
    """Адрес кофейни"""

    name = models.CharField(
        verbose_name="Адрес кофейни",
        max_length=150,
    )
    lat = models.FloatField(
        verbose_name="Широта",
        blank=True,
        null=True,
    )
    lon = models.FloatField(
        verbose_name="Долгота",
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"

    def __str__(self):
        return self.name


class Alternative(models.Model):
    """Дополнение"""

    name = models.CharField(
        verbose_name="Дополнение",
        max_length=100,
        unique=True,
    )
    slug = models.SlugField(unique=True, max_length=50, verbose_name="slug")

    class Meta:
        ordering = ("name",)
        verbose_name = "Дополнение"
        verbose_name_plural = "Дополнения"

    def __str__(self):
        return self.name


class Tag(models.Model):
    """Тэг"""

    name = models.CharField(verbose_name="Тэг", max_length=100, unique=True)
    slug = models.SlugField(unique=True, max_length=50, verbose_name="slug")

    class Meta:
        ordering = ("name",)
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"

    def __str__(self):
        return self.name


class Roaster(models.Model):
    """Обжарщик кофе"""

    name = models.CharField(
        verbose_name="Обэарщик кофе", max_length=100, unique=True
    )
    slug = models.SlugField(unique=True, max_length=50, verbose_name="slug")

    class Meta:
        ordering = ("name",)
        verbose_name = "Обжарщик кофе"
        verbose_name_plural = "Обжарщики Кофе"

    def __str__(self):
        return self.name


class Drink(models.Model):
    """Напиток"""

    name = models.CharField(verbose_name="Напиток", max_length=100)
    slug = models.SlugField(unique=True, max_length=50, verbose_name="slug")

    class Meta:
        ordering = ("name",)
        verbose_name = "Напиток"
        verbose_name_plural = "Напитки"

    def __str__(self):
        return self.name


class DrinkInCafe(models.Model):
    """Напиток в заведении"""

    cafe = models.ForeignKey(
        "Cafe",
        on_delete=models.CASCADE,
        null=True,
        related_name="drink",
    )
    drink = models.ForeignKey(
        "Drink",
        on_delete=models.CASCADE,
        null=True,
        related_name="drink",
    )
    cost = models.IntegerField(verbose_name="Стоимость", blank=True, null=True)

    class Meta:
        ordering = ("cafe",)
        verbose_name = "Стоимость напитка в кофейне"
        verbose_name_plural = "Стоимость напитка в кофейне"

    def __str__(self):
        return self.drink.name


class Schedule(models.Model):
    """Дни недели"""

    name = models.CharField(verbose_name="День недели", max_length=100)
    slug = models.SlugField(verbose_name="slug", max_length=50, unique=True)

    class Meta:
        verbose_name: str = "День недели"
        verbose_name_plural: str = "Дни недели"

    def __str__(self) -> str:
        return f"{self.name}"


class ScheduleInCafe(models.Model):
    """Расписание в заведении"""

    schedules = models.ForeignKey(
        "Schedule",
        on_delete=models.CASCADE,
        null=True,
        related_name="schedule_in_cafe",
    )
    cafe = models.ForeignKey(
        "Cafe",
        on_delete=models.CASCADE,
        null=True,
        related_name="schedule_in_cafe",
    )
    start = models.TimeField()
    end = models.TimeField()

    class Meta:
        verbose_name = "Расписание в заведении"
        verbose_name_plural = "Расписание в заведении"

    def __str__(self) -> str:
        return f"{self.start} {self.end}"


# class ImageCafe(models.Model):
#     """Изображение заведения"""

#     cafe = models.ForeignKey(
#         "Cafe",
#         on_delete=models.CASCADE,
#         null=True,
#         related_name="image",
#     )
#     image_file = models.ImageField(upload_to="images", blank=True)
#     image_url = models.CharField(max_length=300, blank=True, null=True,)

#     class Meta:
#         verbose_name = "Фото заведения"
#         verbose_name_plural = "Фото заведений"

#     def __str__(self):
#         return f'Фото кофейни {self.cafe.name}'

#     def save(self, *args, **kwargs):
#         if self.image_url and not self.image_file:
#             response = requests.get(self.image_url, stream=True)
#             print(response.content)
#             img = Image.open(io.BytesIO(response.content))
#             img_name = f"{self.image_url.split('/')[-1]}"
#             img_path = os.path.join(MEDIA_ROOT, img_name)
#             img.save(img_path)
#             self.image_file = os.path.join(img_name)
#         super().save(*args, **kwargs)
