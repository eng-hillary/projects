# Generated by Django 2.2.16 on 2020-09-18 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_remove_profile_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='home_address',
            field=models.TextField(blank=True, max_length=30),
        ),
    ]
