# Generated by Django 4.1.1 on 2022-10-02 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_post_isactive"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="user_image",
            field=models.ImageField(null=True, upload_to=""),
        ),
    ]