# Generated by Django 4.2.8 on 2024-01-11 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0006_customer_temp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='temp',
        ),
    ]