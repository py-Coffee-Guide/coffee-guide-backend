from django.db import models


class Establishment(models.Model):
    """Заведение"""
    name = models.CharField(
        verbose_name="Название заведения",
        max_length=150,
        unique=True,
    )
    address = models.CharField(
        verbose_name="Адрес заведения",
        max_length=100,
    )
    email = models.EmailField(
        verbose_name="Почта",
        max_length=254,
        unique=True,
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
