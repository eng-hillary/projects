# Generated by Django 2.2.16 on 2020-09-11 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openmarket', '0002_auto_20200909_0744'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='serviceregistration',
            options={'ordering': ('service_id',)},
        ),
    ]