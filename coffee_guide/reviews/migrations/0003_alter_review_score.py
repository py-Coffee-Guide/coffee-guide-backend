# Generated by Django 4.2.8 on 2023-12-10 15:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reviews", "0002_remove_review_text"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="score",
            field=models.IntegerField(
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
                validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)],
                verbose_name="Оценка",
            ),
        ),
    ]
