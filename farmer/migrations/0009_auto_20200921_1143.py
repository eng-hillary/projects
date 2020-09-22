# Generated by Django 2.2.16 on 2020-09-21 11:43

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0008_auto_20200921_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmerprofile',
            name='phone_1',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Phone number 1'),
        ),
        migrations.AlterField(
            model_name='farmerprofile',
            name='phone_2',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Phone number 2'),
        ),
    ]
