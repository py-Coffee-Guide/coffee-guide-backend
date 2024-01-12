import io
import os
# from pathlib import Path

import requests
from django.db import models
from PIL import Image

from coffee_guide.settings import BASE_DIR, MEDIA_ROOT


class Schedule(models.Model):
    """Время работы"""

    # Разделить по подобию ингредиентов

    cafe = models.ForeignKey(
        "Cafe",
        on_delete=models.CASCADE,
        null=True,
        related_name="worked",
    )
    text = models.TextField(
        verbose_name="Время работы",
        max_length=150
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

    # def clean(self):
    #     if self.start and self.end is not None:
    #         if self.start >= self.end:
    #             raise ValidationError(
    #                 {"end": "Укажите корректное время окончания. Оно не может быть меньше времени начала"}
    #             )

    def __str__(self):
        return f"{self.cafe}  {self.text}"


class Filter(models.Model):
    """Фильтр"""
    cafe = models.ForeignKey(
        "Cafe",
        on_delete=models.CASCADE,
        null=True,
        related_name="filter",
    )
    name = models.CharField(
        verbose_name="Фильтр",
        max_length=150,
    )

    class Meta:
        verbose_name = "Фильтр"
        verbose_name_plural = "Фильтр"


class Alternative(models.Model):
    """Альтернатива"""
    cafe = models.ForeignKey(
        "Cafe",
        on_delete=models.CASCADE,
        null=True,
        related_name="alternative",
    )
    name = models.CharField(
        verbose_name="Альтернатива",
        max_length=150
    )

    class Meta:
        verbose_name = "Альтернатива"
        verbose_name_plural = "Альтернатива"


class Roaster(models.Model):
    """Обжарщик кофе"""
    cafe = models.ForeignKey(
        "Cafe",
        on_delete=models.CASCADE,
        null=True,
        related_name="roaster",
    )
    name = models.CharField(
        verbose_name="Обжарщик кофе",
        max_length=150
    )

    class Meta:
        verbose_name = "Обжарщик кофе"
        verbose_name_plural = "Обжарщик кофе"


class Tag(models.Model):
    """Тэг"""
    cafe = models.ForeignKey(
        "Cafe",
        on_delete=models.CASCADE,
        null=True,
        related_name="tag",
    )
    name = models.CharField(
        verbose_name="тэг",
        max_length=150
    )

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэг"


class Drink(models.Model):
    """Напиток"""
    cafe = models.ForeignKey(
        "Cafe",
        on_delete=models.CASCADE,
        null=True,
        related_name="drink",
    )
    name = models.CharField(
        verbose_name="напиток",
        max_length=150
    )

    class Meta:
        verbose_name = "Напиток"
        verbose_name_plural = "Напиток"


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
    district = models.CharField(
        verbose_name="Район",
        max_length=100,
    )
    address = models.CharField(
        verbose_name="Адрес кофейни",
        max_length=100,
    )
    latitude = models.FloatField(
        verbose_name="Широта",
        blank=True,
        null=True,
    )
    longitude = models.FloatField(
        verbose_name="Долгота",
        blank=True,
        null=True,
    )
    poster = models.ImageField(
        verbose_name="Постер кофейни",
        upload_to="establishment/images/poster",
        blank=True,
        null=True,
        default="",
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


class ImageCafe(models.Model):
    cafe = models.ForeignKey(
        Cafe,
        on_delete=models.CASCADE,
        null=True,
        related_name="image",
    )
    image_file = models.ImageField(upload_to="images", blank=True)
    image_url = models.CharField(
        max_length=300,
        blank=True
    )

    def save(self, *args, **kwargs):
        if self.image_url and not self.image_file:
            response = requests.get(self.image_url, stream=True)
            img = Image.open(io.BytesIO(response.content))
            img_name = f"{self.image_url.split('/')[-1]}"
            img_path = os.path.join(MEDIA_ROOT, img_name)
            img.save(img_path)
            self.image_file = os.path.join(img_name)
        super().save(*args, **kwargs)
