# Generated by Django 4.2.8 on 2024-01-11 19:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("reviews", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("cafe", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="author",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name="review",
            name="cafe",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="review", to="cafe.cafe"),
        ),
        migrations.AddConstraint(
            model_name="review",
            constraint=models.UniqueConstraint(fields=("cafe", "author"), name="uniquereview"),
        ),
    ]
