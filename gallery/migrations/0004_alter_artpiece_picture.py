# Generated by Django 4.2.3 on 2023-07-20 20:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gallery", "0003_alter_user_is_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="artpiece",
            name="picture",
            field=models.ImageField(upload_to="pictures"),
        ),
    ]