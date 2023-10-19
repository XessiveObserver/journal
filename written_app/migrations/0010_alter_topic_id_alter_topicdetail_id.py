# Generated by Django 4.2 on 2023-10-11 10:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("written_app", "0009_topic_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="topic",
            name="id",
            field=models.URLField(
                default=uuid.UUID("4e7b9566-60e6-5336-9360-069a3c16a6c4"),
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="topicdetail",
            name="id",
            field=models.URLField(
                default=uuid.UUID("3e5c2108-09da-50fd-800b-e1c7edd4a9c7"),
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]
