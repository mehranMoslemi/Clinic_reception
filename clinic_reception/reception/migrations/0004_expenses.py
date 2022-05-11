# Generated by Django 3.2.5 on 2022-05-11 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0003_auto_20220511_1945'),
    ]

    operations = [
        migrations.CreateModel(
            name='expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='expense name')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='cost')),
                ('quantity', models.IntegerField(verbose_name='quantity')),
                ('date', models.DateField(verbose_name='date')),
            ],
        ),
    ]
