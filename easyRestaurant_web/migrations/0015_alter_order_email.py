# Generated by Django 3.2.8 on 2021-12-14 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easyRestaurant_web', '0014_order_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(blank=True, max_length=250),
        ),
    ]
