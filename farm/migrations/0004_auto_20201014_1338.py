# Generated by Django 2.2.16 on 2020-10-14 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0003_auto_20201014_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enterpriseselection',
            name='scale',
            field=models.CharField(choices=[(None, '--please select--'), ('Large', 'large'), ('small', 'small')], max_length=100, verbose_name='If yes, at what scale do you do farming?'),
        ),
        migrations.AlterField(
            model_name='enterpriseselection',
            name='sector',
            field=models.CharField(max_length=100, null=True, verbose_name='State your current sector of farming?'),
        ),
    ]