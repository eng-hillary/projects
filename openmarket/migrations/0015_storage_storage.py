# Generated by Django 2.2.16 on 2020-10-12 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('openmarket', '0014_auto_20201001_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='storage',
            name='storage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='openmarket.Service'),
        ),
    ]
