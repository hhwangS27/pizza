# Generated by Django 2.0.3 on 2019-04-12 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0019_order_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='num',
        ),
    ]
