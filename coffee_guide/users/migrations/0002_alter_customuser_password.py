# Generated by Django 4.2.8 on 2023-12-17 19:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="password",
            field=models.CharField(max_length=128, verbose_name="Пароль"),
        ),
    ]
