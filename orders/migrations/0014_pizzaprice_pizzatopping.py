# Generated by Django 2.0.3 on 2019-04-08 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_auto_20190408_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='PizzaPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('pizza_kind', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='orders.Pizza')),
            ],
        ),
        migrations.CreateModel(
            name='PizzaTopping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping_kind', models.CharField(max_length=64)),
                ('pizza', models.ManyToManyField(blank=True, related_name='toppings_pizza', to='orders.Pizza')),
                ('price', models.ManyToManyField(blank=True, related_name='toppings_pice', to='orders.PizzaPrice')),
            ],
        ),
    ]
