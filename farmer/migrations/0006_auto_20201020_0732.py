# Generated by Django 2.2.16 on 2020-10-20 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0005_auto_20201019_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmerprofile',
            name='credit_access',
            field=models.BooleanField(choices=[(None, '--please select--'), (True, 'Yes'), (False, 'No')], null=True, verbose_name='Have access to credit ?.'),
        ),
    ]