# Generated by Django 4.2.8 on 2024-01-12 19:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cafe", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="imagecafe",
            name="image_url",
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
