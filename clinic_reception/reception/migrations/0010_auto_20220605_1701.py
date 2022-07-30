# Generated by Django 3.2.5 on 2022-06-05 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0009_auto_20220605_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='ct_income',
            field=models.FloatField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='mri_income',
            field=models.FloatField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='x_income',
            field=models.FloatField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='time',
            field=models.TimeField(verbose_name='reception time'),
        ),
    ]
