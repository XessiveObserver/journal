# Generated by Django 4.2 on 2023-09-28 13:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("written_app", "0007_topic_slug_alter_topic_id_alter_topicdetail_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="topicdetail",
            name="slug",
            field=models.SlugField(default=1, editable=False, unique=True),
            preserve_default=False,
        ),
    ]
