# Generated by Django 4.2.8 on 2024-01-24 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("cafe", "0003_alter_cafe_image_alter_cafe_organization_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cafe",
            name="image",
        ),
        migrations.CreateModel(
            name="ImageCafe",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("image_file", models.ImageField(blank=True, upload_to="images")),
                ("image_url", models.CharField(blank=True, max_length=300, null=True)),
                (
                    "cafe",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.CASCADE, related_name="image", to="cafe.cafe"
                    ),
                ),
            ],
            options={
                "verbose_name": "Фото заведения",
                "verbose_name_plural": "Фото заведений",
            },
        ),
    ]
