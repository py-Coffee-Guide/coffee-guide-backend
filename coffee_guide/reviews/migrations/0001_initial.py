# Generated by Django 4.2.8 on 2024-01-10 14:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Review",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "score",
                    models.IntegerField(
                        choices=[
                            (5, "Отлично - 5 звезд"),
                            (4, "Хорошо - 4 звезды"),
                            (3, "Удовлетворительно - 3 звезды"),
                            (2, "Неплохо - 2 звезды"),
                            (1, "Сойдет - 1 звезда"),
                            (1, "Плохо - 1 звезда"),
                            (2, "Неудовлетворительно - 2 звезды"),
                            (3, "Посредственно - 3 звезды"),
                            (4, "Слабо - 4 звезды"),
                            (5, "Ужасно - 5 звезд"),
                        ],
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ],
                        verbose_name="Оценка",
                    ),
                ),
                ("pub_date", models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")),
            ],
            options={
                "verbose_name": "Отзыв",
                "verbose_name_plural": "Отзывы",
                "ordering": ["-pub_date"],
            },
        ),
    ]
