# Generated by Django 3.2.5 on 2022-05-03 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='first name')),
                ('last_name', models.CharField(max_length=50, verbose_name='last name')),
                ('code', models.PositiveIntegerField(unique=True, verbose_name='patient code')),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'female')], max_length=50, verbose_name='gender')),
                ('date_of_birth', models.DateField(verbose_name='date of birth')),
                ('address', models.CharField(max_length=200, null=True, verbose_name='address')),
                ('post_code', models.CharField(max_length=50, null=True, verbose_name='postal code')),
                ('phone', models.CharField(max_length=50, null=True, verbose_name='phone number')),
            ],
        ),
    ]
