# Generated by Django 4.2.8 on 2024-02-08 21:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("cafe", "0002_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="address",
            name="district",
        ),
    ]