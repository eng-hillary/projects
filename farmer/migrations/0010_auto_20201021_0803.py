# Generated by Django 2.2.16 on 2020-10-21 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0009_auto_20201020_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmerprofile',
            name='credit_access',
            field=models.BooleanField(choices=[(None, '--please select--'), (True, 'Yes'), (False, 'No')], null=True, verbose_name='Have access to credit ?.'),
        ),
    ]