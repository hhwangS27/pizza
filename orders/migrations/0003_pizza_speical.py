# Generated by Django 2.0.3 on 2019-04-07 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20190407_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='speical',
            field=models.BooleanField(default=False),
        ),
    ]
