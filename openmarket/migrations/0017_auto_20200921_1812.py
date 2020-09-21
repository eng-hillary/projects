# Generated by Django 2.2.16 on 2020-09-21 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('openmarket', '0016_auto_20200921_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='enterprise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farm.Enterprise'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='major_products',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openmarket.Product'),
        ),
    ]
