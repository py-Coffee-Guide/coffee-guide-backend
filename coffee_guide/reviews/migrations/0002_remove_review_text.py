# Generated by Django 4.2.8 on 2023-12-10 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='text',
        ),
    ]
