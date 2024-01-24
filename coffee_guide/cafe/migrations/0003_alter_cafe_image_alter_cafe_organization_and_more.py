# Generated by Django 4.2.8 on 2024-01-24 14:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("cafe", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cafe",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images", verbose_name="Фото кофейни"),
        ),
        migrations.AlterField(
            model_name="cafe",
            name="organization",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cafes",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Организация",
            ),
        ),
        migrations.DeleteModel(
            name="ImageCafe",
        ),
    ]
