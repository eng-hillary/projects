# Generated by Django 2.2.16 on 2020-09-11 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='communityweather',
            old_name='lat',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='communityweather',
            old_name='lon',
            new_name='longitude',
        ),
    ]
