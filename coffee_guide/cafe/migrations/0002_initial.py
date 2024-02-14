from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("cafe", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
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
        migrations.AddField(
            model_name="cafe",
            name="roasters",
            field=models.ManyToManyField(max_length=100, to="cafe.roaster", verbose_name="Обжарщик кофе"),
        ),
        migrations.AddField(
            model_name="cafe",
            name="schedules",
            field=models.ManyToManyField(
                max_length=100,
                related_name="cafes",
                through="cafe.ScheduleInCafe",
                to="cafe.schedule",
                verbose_name="Время работы",
            ),
        ),
        migrations.AddField(
            model_name="cafe",
            name="tags",
            field=models.ManyToManyField(max_length=100, to="cafe.tag", verbose_name="Доступные опции"),
        ),
    ]
