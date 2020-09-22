# Generated by Django 2.2.16 on 2020-09-21 10:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('openmarket', '0011_auto_20200921_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to=settings.AUTH_USER_MODEL),
        ),
    ]
