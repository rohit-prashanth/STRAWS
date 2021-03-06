# Generated by Django 3.2.6 on 2021-08-23 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strawsapp', '0004_auto_20210823_1244'),
    ]

    operations = [
        migrations.CreateModel(
            name='TablesHistoryDatabase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('mobile_number', models.CharField(max_length=20)),
                ('items', models.TextField()),
                ('total_amount', models.IntegerField()),
                ('payment_mode', models.CharField(choices=[('Cash', 'Cash'), ('UPI', 'UPI'), ('Card Payment', 'Card Payment')], default='Cash', max_length=50)),
            ],
        ),
    ]
