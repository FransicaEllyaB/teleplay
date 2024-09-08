# Generated by Django 5.1.1 on 2024-09-08 06:16

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Video",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("price", models.IntegerField()),
                ("description", models.TextField()),
                ("release_date", models.DateField(auto_now_add=True)),
                ("duration", models.DurationField()),
                ("rating", models.DecimalField(decimal_places=1, max_digits=2)),
            ],
        ),
    ]
