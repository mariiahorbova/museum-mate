# Generated by Django 4.2.3 on 2023-07-20 15:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gallery", "0002_alter_user_birth_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_author",
            field=models.BooleanField(default=False),
        ),
    ]
