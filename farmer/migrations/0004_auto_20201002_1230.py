# Generated by Django 2.2.16 on 2020-10-02 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0003_auto_20200929_1324'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='farmerprofile',
            options={'permissions': (('can_approve_farmers', 'Can approve farmers'),)},
        ),
    ]
