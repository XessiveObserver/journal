# Generated by Django 4.2 on 2023-09-28 12:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("written_app", "0005_alter_topicdetail_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="topic",
            name="id",
            field=models.URLField(
                default=uuid.uuid5, editable=False, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="topicdetail",
            name="id",
            field=models.URLField(
                default=uuid.uuid5, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]
