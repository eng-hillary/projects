# Generated by Django 2.2.16 on 2020-10-16 08:28

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('openmarket', '0002_remove_service_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='driver_contact',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None),
        ),
        migrations.AddField(
            model_name='service',
            name='driver_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
