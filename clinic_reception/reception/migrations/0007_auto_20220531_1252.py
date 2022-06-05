# Generated by Django 3.2.5 on 2022-05-31 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0006_auto_20220531_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='RefferalPhysician',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='reception.referralphysician', verbose_name='refferal physician'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='services_ctscan',
            field=models.ManyToManyField(null=True, to='reception.ServiceCtscan'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='services_mri',
            field=models.ManyToManyField(null=True, to='reception.ServiceMri'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='services_xray',
            field=models.ManyToManyField(null=True, to='reception.ServiceXray'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='code',
            field=models.PositiveIntegerField(editable=False, unique=True, verbose_name='patient code'),
        ),
    ]
