# Generated by Django 4.2 on 2023-09-22 08:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("written_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="topic",
            name="name",
            field=models.CharField(max_length=100),
        ),
    ]
