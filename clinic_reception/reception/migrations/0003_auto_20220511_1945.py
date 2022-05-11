# Generated by Django 3.2.5 on 2022-05-11 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0002_invoice_physician_refferalphysician_service'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Service',
            new_name='ServiceCtscan',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='sex',
            new_name='gender',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='services',
        ),
        migrations.AddField(
            model_name='invoice',
            name='services_ctscan',
            field=models.ManyToManyField(to='reception.ServiceCtscan'),
        ),
        migrations.AddField(
            model_name='patient',
            name='middle_name',
            field=models.CharField(default='mehran', max_length=50, verbose_name='middle name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date',
            field=models.DateTimeField(verbose_name='reception date'),
        ),
        migrations.CreateModel(
            name='ServiceXray',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='service name')),
                ('fee', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='service fee')),
                ('physician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reception.physician')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceMri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='service name')),
                ('fee', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='service fee')),
                ('physician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reception.physician')),
            ],
        ),
        migrations.AddField(
            model_name='invoice',
            name='services_mri',
            field=models.ManyToManyField(to='reception.ServiceMri'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='services_xray',
            field=models.ManyToManyField(to='reception.ServiceXray'),
        ),
    ]