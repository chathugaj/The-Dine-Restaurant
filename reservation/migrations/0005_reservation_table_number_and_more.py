# Generated by Django 4.2.8 on 2024-01-10 02:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0004_table_alter_reservation_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='table_number',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='reservation.table'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reservation',
            name='reservation_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='time_slot',
            field=models.IntegerField(choices=[(1, '16:00 - 17:30'), (2, '17:30 - 19:00'), (3, '19:00 - 20:30'), (4, '20:30 - 22:00')], default=2),
        ),
    ]
