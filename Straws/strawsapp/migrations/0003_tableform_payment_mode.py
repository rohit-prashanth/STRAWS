# Generated by Django 3.2.6 on 2021-08-23 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strawsapp', '0002_tableform'),
    ]

    operations = [
        migrations.AddField(
            model_name='tableform',
            name='payment_mode',
            field=models.CharField(choices=[('Cash', 'Cash'), ('UPI', 'UPI'), ('Card Payment', 'Card Payment')], default='Cash', max_length=50),
        ),
    ]
