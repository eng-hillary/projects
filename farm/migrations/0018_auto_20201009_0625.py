# Generated by Django 2.2.16 on 2020-10-09 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0017_auto_20201008_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enterprise',
            name='farm',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enterprises', to='farm.Farm'),
        ),
    ]
