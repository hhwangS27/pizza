# Generated by Django 2.0.3 on 2019-04-07 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20190407_1627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizzaprice',
            name='pizza_kind',
        ),
        migrations.RemoveField(
            model_name='pizzatopping',
            name='pizza',
        ),
        migrations.RemoveField(
            model_name='pizzatopping',
            name='price',
        ),
    ]
