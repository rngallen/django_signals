# Generated by Django 3.1.6 on 2021-02-04 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
        ('orders', '0002_auto_20210204_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cars',
            field=models.ManyToManyField(related_name='order_cars', to='cars.Car', verbose_name='cars'),
        ),
    ]