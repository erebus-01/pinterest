# Generated by Django 4.1.1 on 2022-09-30 17:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                ("id_user", models.IntegerField()),
                ("story", models.TextField(blank=True)),
                ("firstName", models.CharField(blank=True, max_length=50)),
                ("lastName", models.CharField(blank=True, max_length=50)),
                ("website", models.CharField(blank=True, max_length=20)),
                (
                    "profileimg",
                    models.ImageField(
                        default="blank_profile.png", upload_to="profile_images"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
