# Generated by Django 5.0 on 2023-12-31 08:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0002_color"),
    ]

    operations = [
        migrations.AddField(
            model_name="person",
            name="Color",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="color",
                to="home.color",
            ),
        ),
    ]
