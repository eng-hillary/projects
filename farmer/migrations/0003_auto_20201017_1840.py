# Generated by Django 2.2.16 on 2020-10-17 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0002_auto_20201017_1453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farmerprofile',
            name='phone_1',
        ),
        migrations.RemoveField(
            model_name='farmerprofile',
            name='phone_2',
        ),
    ]
