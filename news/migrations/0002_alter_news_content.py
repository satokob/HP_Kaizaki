# Generated by Django 4.2.14 on 2024-09-04 02:23

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="content",
            field=ckeditor.fields.RichTextField(),
        ),
    ]
