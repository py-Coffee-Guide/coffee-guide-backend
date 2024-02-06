# Generated by Django 4.2.8 on 2024-02-06 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=150, verbose_name="Адрес кофейни")),
                ("lat", models.FloatField(blank=True, null=True, verbose_name="Широта")),
                ("lon", models.FloatField(blank=True, null=True, verbose_name="Долгота")),
                ("district", models.CharField(blank=True, max_length=100, null=True, verbose_name="Район")),
            ],
            options={
                "verbose_name": "Адрес",
                "verbose_name_plural": "Адреса",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Alternative",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100, unique=True, verbose_name="Дополнение")),
                ("slug", models.SlugField(unique=True, verbose_name="slug")),
            ],
            options={
                "verbose_name": "Дополнение",
                "verbose_name_plural": "Дополнения",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Cafe",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=150, verbose_name="Название кофейни")),
                (
                    "description",
                    models.TextField(blank=True, max_length=1500, null=True, verbose_name="Описание кофейни"),
                ),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="cafe/images", verbose_name="Фото кофейни"),
                ),
                (
                    "address",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cafe",
                        to="cafe.address",
                        verbose_name="Адрес кофейни",
                    ),
                ),
                (
                    "alternatives",
                    models.ManyToManyField(max_length=100, to="cafe.alternative", verbose_name="Дополнительные опции"),
                ),
            ],
            options={
                "verbose_name": "Кофейня",
                "verbose_name_plural": "Кофейни",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Drink",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100, verbose_name="Напиток")),
                ("slug", models.SlugField(unique=True, verbose_name="slug")),
            ],
            options={
                "verbose_name": "Напиток",
                "verbose_name_plural": "Напитки",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Roaster",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100, unique=True, verbose_name="Обэарщик кофе")),
                ("slug", models.SlugField(unique=True, verbose_name="slug")),
            ],
            options={
                "verbose_name": "Обжарщик кофе",
                "verbose_name_plural": "Обжарщики Кофе",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Schedule",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100, verbose_name="День недели")),
                ("slug", models.SlugField(unique=True, verbose_name="slug")),
            ],
            options={
                "verbose_name": "День недели",
                "verbose_name_plural": "Дни недели",
            },
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100, unique=True, verbose_name="Тэг")),
                ("slug", models.SlugField(unique=True, verbose_name="slug")),
            ],
            options={
                "verbose_name": "Тэг",
                "verbose_name_plural": "Тэги",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="ScheduleInCafe",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("start", models.TimeField()),
                ("end", models.TimeField()),
                (
                    "cafe",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="schedule_in_cafe",
                        to="cafe.cafe",
                    ),
                ),
                (
                    "schedules",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="schedule_in_cafe",
                        to="cafe.schedule",
                    ),
                ),
            ],
            options={
                "verbose_name": "Расписание в заведении",
                "verbose_name_plural": "Расписание в заведении",
            },
        ),
        migrations.CreateModel(
            name="DrinkInCafe",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("cost", models.IntegerField(blank=True, null=True, verbose_name="Стоимость")),
                (
                    "cafe",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.CASCADE, related_name="drink", to="cafe.cafe"
                    ),
                ),
                (
                    "drink",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.CASCADE, related_name="drink", to="cafe.drink"
                    ),
                ),
            ],
            options={
                "verbose_name": "Стоимость напитка в кофейне",
                "verbose_name_plural": "Стоимость напитка в кофейне",
                "ordering": ("cafe",),
            },
        ),
        migrations.AddField(
            model_name="cafe",
            name="drinks",
            field=models.ManyToManyField(
                max_length=100,
                related_name="cafes",
                through="cafe.DrinkInCafe",
                to="cafe.drink",
                verbose_name="Напиток",
            ),
        ),
    ]
