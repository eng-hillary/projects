# Generated by Django 3.0.4 on 2020-07-21 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landlord', '0009_auto_20200721_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='picture',
            field=models.ImageField(blank=True, default='home.png', null=True, upload_to='images'),
        ),
    ]
