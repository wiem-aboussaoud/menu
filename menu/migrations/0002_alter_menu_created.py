# Generated by Django 4.1.1 on 2022-09-29 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("menu", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menu",
            name="created",
            field=models.CharField(
                blank=True, default="testing", max_length=12, null=True
            ),
        ),
    ]
