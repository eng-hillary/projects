# Generated by Django 2.2.16 on 2020-10-13 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openmarket', '0023_auto_20201013_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='inventory_status',
        ),
        migrations.RemoveField(
            model_name='service',
            name='status',
        ),
        migrations.AlterField(
            model_name='service',
            name='certification_status',
            field=models.BooleanField(blank=True, choices=[(None, '--please select--'), (True, 'Yes'), (False, 'No')], null=True, verbose_name='Is the Service Certified'),
        ),
        migrations.AlterField(
            model_name='service',
            name='enterprise',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='location_of_storage_center',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='name_of_storage_center',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='rent',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='size',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='vehicle_capacity',
            field=models.FloatField(blank=True, help_text='capacity of your vehicle in tonnes', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='vehicle_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
