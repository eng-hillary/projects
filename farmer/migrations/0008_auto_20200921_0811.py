# Generated by Django 2.2.16 on 2020-09-21 08:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0007_auto_20200911_1324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farmerprofile',
            name='gender',
        ),
        migrations.AlterField(
            model_name='farmerprofile',
            name='nin',
            field=models.CharField(max_length=50, verbose_name='National Identity Number (NIN)'),
        ),
        migrations.AlterField(
            model_name='farmerprofile',
            name='status',
            field=models.CharField(choices=[(None, '--please select--'), ('active', 'Active'), ('in_active', 'In-Active'), ('rejected', 'Rejected')], default='in_active', max_length=20),
        ),
        migrations.AlterField(
            model_name='farmerprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='farmer', to=settings.AUTH_USER_MODEL),
        ),
    ]
