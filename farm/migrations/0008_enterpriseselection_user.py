# Generated by Django 2.2.16 on 2020-10-15 12:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('farm', '0007_auto_20201015_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='enterpriseselection',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='enterpriseselection', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]