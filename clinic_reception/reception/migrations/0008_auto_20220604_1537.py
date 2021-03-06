# Generated by Django 3.2.5 on 2022-06-04 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0007_auto_20220531_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='RefferalPhysician',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reception.referralphysician', verbose_name='refferal physician'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='services_ctscan',
            field=models.ManyToManyField(blank=True, to='reception.ServiceCtscan'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='services_mri',
            field=models.ManyToManyField(blank=True, related_name='mri_services', to='reception.ServiceMri'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='services_xray',
            field=models.ManyToManyField(blank=True, to='reception.ServiceXray'),
        ),
    ]
