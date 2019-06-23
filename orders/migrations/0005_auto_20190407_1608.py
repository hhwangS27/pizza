# Generated by Django 2.0.3 on 2019-04-07 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20190407_1601'),
    ]

    operations = [
        migrations.RenameField(
            model_name='price',
            old_name='kind_pizza',
            new_name='pizza_kind',
        ),
        migrations.RemoveField(
            model_name='topping',
            name='kind_topping',
        ),
        migrations.AddField(
            model_name='topping',
            name='pizza',
            field=models.ManyToManyField(blank=True, related_name='toppings_pizza', to='orders.Price'),
        ),
        migrations.AddField(
            model_name='topping',
            name='price',
            field=models.ManyToManyField(blank=True, related_name='toppings_pice', to='orders.Price'),
        ),
        migrations.AddField(
            model_name='topping',
            name='topping_kind',
            field=models.CharField(default=0, max_length=64),
            preserve_default=False,
        ),
    ]
