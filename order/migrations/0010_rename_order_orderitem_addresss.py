# Generated by Django 4.1 on 2022-10-27 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0009_orderitem_order"),
    ]

    operations = [
        migrations.RenameField(
            model_name="orderitem", old_name="order", new_name="addresss",
        ),
    ]