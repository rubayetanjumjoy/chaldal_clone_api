# Generated by Django 4.1 on 2022-08-29 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="catagory",
            name="icon",
            field=models.CharField(blank=True, max_length=600),
        ),
    ]
