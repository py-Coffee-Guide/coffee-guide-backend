from django.db import models


class Establishment(models.Model):
    """Заведение"""
    pass

    # class Meta:
    #     verbose_name = "Заведение"
    #     verbose_name_plural = "Заведения"
    #
    # def __str__(self):
    #     return self.name

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class Favorite(models.Model):
    """Избранное"""
    pass
