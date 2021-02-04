# Generated by Django 3.1.6 on 2021-02-04 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('buyers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('price', models.FloatField(verbose_name='price')),
                ('code', models.CharField(blank=True, max_length=10, verbose_name='code')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_buyer', to='buyers.buyer', verbose_name='buyer')),
            ],
        ),
    ]
