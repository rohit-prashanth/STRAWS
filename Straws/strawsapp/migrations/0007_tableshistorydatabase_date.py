# Generated by Django 3.2.6 on 2021-08-24 14:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('strawsapp', '0006_tableform10_tableform4_tableform5_tableform6_tableform7_tableform8_tableform9'),
    ]

    operations = [
        migrations.AddField(
            model_name='tableshistorydatabase',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
