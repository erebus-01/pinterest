# Generated by Django 4.1.1 on 2022-10-01 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_post"),
    ]

    operations = [
        migrations.AddField(
            model_name="post", name="isActive", field=models.BooleanField(default=True),
        ),
    ]
