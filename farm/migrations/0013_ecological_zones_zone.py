# Generated by Django 2.2.16 on 2020-10-23 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0012_auto_20201022_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='ecological_zones',
            name='zone',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='district', to='farm.EnterpriseSelection'),
        ),
    ]