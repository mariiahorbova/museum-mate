# Generated by Django 4.2.3 on 2023-07-20 14:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gallery", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="birth_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]