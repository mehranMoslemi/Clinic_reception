# Generated by Django 3.2.5 on 2022-06-05 13:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0008_auto_20220604_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='time',
            field=models.TimeField(auto_now_add=True, default=datetime.datetime(2022, 6, 5, 13, 23, 58, 830954, tzinfo=utc), verbose_name='reception time'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date',
            field=models.DateField(verbose_name='reception date'),
        ),
    ]
