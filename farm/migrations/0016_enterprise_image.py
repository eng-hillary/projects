# Generated by Django 2.2.16 on 2020-10-08 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0015_auto_20201008_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='enterprise',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]