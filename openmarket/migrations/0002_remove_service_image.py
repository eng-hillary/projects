# Generated by Django 2.2.16 on 2020-10-15 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openmarket', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='image',
        ),
    ]
