# Generated by Django 2.2.16 on 2020-10-26 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0014_auto_20201026_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enterpriseselection',
            name='recommendation',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='zone', to='farm.Ecological_Zones'),
        ),
    ]
