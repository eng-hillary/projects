# Generated by Django 2.2.16 on 2020-10-06 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0010_auto_20201002_1114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='farm',
            old_name='latitude',
            new_name='lat',
        ),
        migrations.RenameField(
            model_name='farm',
            old_name='longitude',
            new_name='lon',
        ),
    ]
